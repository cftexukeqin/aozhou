import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aozhou.settings')

import django
django.setup()

from apps.goods.models import Goods,GoodsCategory,GoodsImage

from db_tools.data.goods import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail['goods_name']
    goods.goods_desc = goods_detail['goods_desc']
    goods.shop_price = float(int(goods_detail['shop_price'].replace("￥","").replace("元","")))
    # goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] else ""
    goods.market_price = float(int(goods_detail['market_price'].replace("￥","").replace("元","")))
    goods.goods_thumbnail = goods_detail['goods_image'][0] if goods_detail['goods_image'] else ""

    category_name = goods_detail['goods_category']
    category = GoodsCategory.objects.filter(name=category_name)
    goods.category = category[0]
    goods.save()

    for goods_image in goods_detail['goods_image']:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()
print("测试数据库商品信息写入成功!")