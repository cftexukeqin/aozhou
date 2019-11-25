from django.shortcuts import render
from apps.goods.models import Goods
from django.db.models import Q

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from aozhou import settings
import json
from django.core.serializers import serialize
from django.views.generic import ListView
from aozhou import settings
import json
from django.core.serializers import serialize

from .serializers import GoodsSerializers
from utils import restful
# Create your views here.


def index(request):
    goods_lists = Goods.objects.all()[:20]
    context = {
        'goods_lists':goods_lists
    }
    return render(request,'index.html',context=context)
#
# def index_goods_list(request):
#     page = int(request.GET.get('p',1))
#     category_id = int(request.GET.get('category_id',0))
#
#
#     start = (page-1)*settings.PERPAGE_GOODS_COUNT
#     end = start+settings.PERPAGE_GOODS_COUNT
#
#     start = (page-1)*settings.PERPAGE_GOODS_COUNT
#     end = start+settings.PERPAGE_GOODS_COUNT
#
#     if category_id == 0:
#         goodses = Goods.objects.all()[start:end]
#     else:
#         goodses = Goods.objects.all()[start:end]
#     serializers = GoodsSerializers(goodses,many=True)
#     data = serializers.data
#     return restful.result(data=data)

def goods_list(request):
    goodses = Goods.objects.all()[:40]

    paginator = Paginator(goodses,settings.PERPAGE_GOODS_COUNT)
    p = request.GET.get('page')
    num_pages = paginator.num_pages
    left_has_more = False
    right_has_more = False
    # 分页所需参数
    new_context = {}
    try:

        goodses = paginator.page(p)
        current_page = goodses.number
        if current_page <= settings.AROUND_COUNT + 2:
            left_pages = range(1,current_page)
            print(left_pages)
            print(left_has_more)
            new_context['left_pages'] = left_pages
        else:
            left_has_more = True
            left_pages = range(current_page-settings.AROUND_COUNT,current_page)
            new_context['left_pages'] = left_pages
            new_context['current_page'] = current_page

        if current_page >= num_pages-2-1:
            right_pages = range(current_page+1,num_pages+1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page
        else:
            right_has_more = True
            right_pages = range(current_page+1,current_page+settings.AROUND_COUNT+1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page

    except PageNotAnInteger:
        goodses = paginator.page(1)
    except EmptyPage:
        goodses = paginator.page(paginator.num_pages)

    special_goods = Goods.objects.filter(category__id=18).all()
    # 化妆品
    cosmetics_goods = Goods.objects.filter(category__id=19).all()
    # 奶粉
    milk_goods = Goods.objects.filter(category__id=20).all()
    # 奶粉
    love_goods = Goods.objects.filter(category__id=21).all()
    # 保健产品
    care_goods =Goods.objects.filter(category__id=24).all()

    # 其他
    other_goods = Goods.objects.filter(~Q(category__id__in=[18,19,20,21,24]))

    # 热门商品 销量比较高的
    hot_goodses = Goods.objects.order_by("-sold_num")[:5]

    context = {
        'goodses':goodses,
        'special_goods':special_goods,
        'cosmetics_goods':cosmetics_goods,
        'milk_goods':milk_goods,
        'love_goods':love_goods,
        'care_goods':care_goods,
        'other_goods':other_goods,
        'hot_goodses':hot_goodses,
        'left_has_more':left_has_more,
        'right_has_more':right_has_more,
        'num_pages':num_pages
    }
    context.update(new_context)
    return render(request, 'goods_list.html',context=context)



# class GoodsListView(ListView):
#     model = Goods
#     paginate_by = 10
#     context_object_name = 'goodses'
#     template_name = 'goods_list.html'
#     ordering = 'sold_num'
#     page_kwarg = 'p'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(GoodsListView, self).get_context_data()
#         context['username'] = 'dx'
#         pagination = context['paginator']
#         page = context['page_obj']
#         pagination_data = self.get_content_data(pagination,page)
#         context.update(pagination_data)
#         return context
#     # 获取数据传给前端
#     def get_content_data(self,paginator,page_obj,arroud_count=2):
#         current_page = page_obj.number
#         num_pages = paginator.num_pages
#
#         left_have_more = False
#         right_have_more = False
#
#         if current_page <= arroud_count + 2:
#             left_pages = range(1,current_page)
#         else:
#             left_have_more = True
#             left_pages = range(current_page-arroud_count,current_page)
#
#         if current_page>=num_pages-2-1:
#             right_pages = range(current_page+1,num_pages+1)
#         else:
#             right_have_more = True
#             right_pages = range(current_page+1,current_page+arroud_count+1)
#         context = {
#             'current_page':current_page,
#             'left_pages':left_pages,
#             'right_pages':right_pages,
#             'left_have_more':left_have_more,
#             'right_have_more':right_have_more,
#             'num_pages':num_pages
#         }
#         return context


def goods_detail(request,goods_id):
    goods = Goods.objects.filter(id=goods_id)[0]

    # images = goods.images.all()
    # for image in images:
    #     print(image.image)
    category = goods.category
    hot_goodses = Goods.objects.filter(category=category).order_by("-sold_num")[:5]
    context = {
        'goods':goods,
        'hot_goodses':hot_goodses
    }
    return render(request, 'goods_detail.html',context=context)

# def search(request):
#     kw = request.POST.get("kw")
#     print(kw)
#     goods = Goods.objects.filter(name__contains=kw).all()
#     json_data = serialize('json', goods)  # str
#     json_data = json.loads(json_data)  # 序列化成json对象
#     return restful.result(data=json_data)


def about(request):
    return render(request,'about-us.html')
