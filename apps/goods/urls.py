from django.urls import include,path,re_path
from apps.goods import views
app_name = 'goods'

urlpatterns = [
    path('',views.index,name='index'),
    path('lists/',views.goods_list,name='lists'),
    path('goods/<int:goods_id>/',views.goods_detail,name='goods_detail'),
    path('about/',views.about,name='about'),
    # path('search/',views.search,name='search'),
    # path('goods_lists/',views.index_goods_list,name='goods_lists')
    # path('search/',views.search,name='search'),
    # path('goods_lists/',views.index_goods_list,name='goods_lists')
]