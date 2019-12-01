import xadmin
from .models import UserFav


class UserFavAdmin(object):
    list_display = ["user","goods","add_time"]
    list_filter = ["user",'goods','add_time']
    # 列表页可以直接编辑的
    list_editable = ["user", 'goods', 'add_time']
    search_fields = ['user', ]


xadmin.site.register(UserFav, UserFavAdmin)
