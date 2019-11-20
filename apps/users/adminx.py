import xadmin
from xadmin import views


class BaseSetting(object):
    # 添加主题
    enable_themes = True
    user_bootswatch = True


class GlobalSettings:
    # 全局配置
    site_title = "佳佳的后台"
    site_footer = ""
    menu_style = "accordion"



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)