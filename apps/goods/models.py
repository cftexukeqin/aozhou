from django.db import models
from django.utils.timezone import now as now_func
from DjangoUeditor.models import UEditorField

class GoodsCategory(models.Model):
    """
    商品类别
    """
    name = models.CharField("类别名称",max_length=30)
    desc = models.TextField("分类描述", default="", help_text="分类描述")
    # 是否导航
    is_tab = models.BooleanField("是否导航", default=False, help_text="是否导航")
    add_time = models.DateTimeField("添加时间", auto_now_add=True)

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
    商品信息
    """
    name = models.CharField("分类名称",max_length=50,help_text="类名")
    category = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,verbose_name="商品类目")
    click_num = models.IntegerField("点击率",default=0)
    fav_num = models.IntegerField("收藏数",default=0)
    goods_num = models.IntegerField("库存数",default=999)
    sold_num = models.IntegerField("销量",default=0)
    market_price = models.FloatField("市场价",default=0)
    shop_price = models.FloatField("销售价",default=0)
    # goods_desc = models.TextField("商品详情",default="")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    goods_rank = models.IntegerField("商品等级",default=5,null=True,blank=True)

    goods_thumbnail = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")

    is_hot = models.BooleanField("是否热卖",default=False)
    is_new = models.BooleanField("是否新品",default=False)

    add_time = models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品",related_name="images")
    image = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    add_time = models.DateTimeField("添加时间", auto_now_add=True)

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name