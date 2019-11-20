from rest_framework import serializers
from .models import Goods,GoodsCategory,GoodsImage


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('id','name','goods_thumbnail','market_price','shop_price')