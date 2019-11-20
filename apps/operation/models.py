from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from apps.goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")

    add_time = models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

