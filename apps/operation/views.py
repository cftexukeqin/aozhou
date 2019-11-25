from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required


from apps.goods.models import Goods
from apps.operation.models import UserFav
from utils import restful


@login_required(login_url='/user/login/')
def fav_list(request):
    favs = UserFav.objects.filter(user=request.user).order_by('-add_time').all()
    context = {
        'favs':favs
    }
    return render(request, 'fav/new_Fav.html',context=context)


def userfav(request):
    """
    用户收藏
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        goods_id = request.GET.get('goods_id')
        goods = Goods.objects.filter(id=goods_id).first()
        if UserFav.objects.filter(goods_id=goods_id,user=request.user).exists():
            return restful.paramserror(message="您已收藏该商品！")
        else:
            UserFav.objects.create(user=request.user,goods=goods)
            return restful.ok()
    else:
        return restful.noauth(message="请先登录！")


def del_fav(request):
    fav_id = request.POST.get('id')
    print("********************************")
    print(fav_id)
    fav = UserFav.objects.get(id=fav_id)
    if fav:
        fav.delete()
        return restful.ok()
    else:
        return restful.paramserror("收藏信息有误！")


# def test_fav(request):
#     return render(request,'fav/new_Fav.html')