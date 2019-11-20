import xadmin
from .models import GoodsCategory,Goods,GoodsImage


class GoodsAdmin:
    #显示的列
    list_display = ['name','category','click_num','fav_num','market_price','shop_price','goods_desc','goods_rank','is_hot','is_new','add_time']
    #可以搜索的字段
    search_fields = ['name', ]
    #列表页可以直接编辑的
    list_editable = ["is_hot",'market_price','shop_price']
    #过滤器
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category"]
    #富文本编辑器
    style_fields = {"goods_desc": "ueditor"}

    # 在添加商品的时候可以添加商品图片
    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]



class GoodsCategoryAdmin(object):
    list_display = ["name","is_tab","desc","add_time"]
    list_filter = ["name",'add_time','is_tab']
    # 列表页可以直接编辑的
    list_editable = ["name", 'desc', 'is_tab']
    search_fields = ['name', ]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)

