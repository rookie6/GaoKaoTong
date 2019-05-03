import xadmin
from xadmin import views
from org.models import SchoolInfo, SpecialtyInfo, LinePro, LineSchool, LineSpecialty


class BaseSetting(object):
    enable_themes = True  # 定义可切换主题
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '高考通'  # 设置顶部标题
    site_footer = '焦作一米粒有限公司'  # 设置底部标题
    menu_style = "accordion"  # 管理左侧菜单折叠


xadmin.site.register(SchoolInfo)
xadmin.site.register(SpecialtyInfo)
xadmin.site.register(LinePro)
xadmin.site.register(LineSchool)
xadmin.site.register(LineSpecialty)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
