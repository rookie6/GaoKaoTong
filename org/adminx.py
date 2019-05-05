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


class SchoolInfoAdmin(object):
    list_display = [
        'school_name',
        'province_name',
        'city_name',
        'county_name',
        'school_type',
        'type_name',
        'school_intro',
        'subject']
    list_per_page = 10
    list_filter = [
        'school_name',
        'province_name',
        'city_name',
        'county_name',
        'school_type',
        'type_name',
        'school_intro',
        'subject']
    search_fields = ['school_name', 'province_name', 'school_intro', 'subject']


class SpecialtyInfoAdmin(object):
    list_display = [
        'sp_name',
        'level1_name',
        'level2_name',
        'level3_name',
        'is_what',
        'do_what',
        'learn_what',
        'content',
        'job']
    list_per_page = 10
    list_filter = [
        'sp_name',
        'level1_name',
        'level2_name',
        'level3_name',
        'limit_year',
        'rate',
        'sel_adv']
    search_fields = ['sp_name']


class LineProAdmin(object):
    list_display = ['province', 'type', 'batch', 'year', 'proscore']
    list_per_page = 10
    list_filter = ['province', 'type', 'batch', 'year', 'proscore']
    search_fields = ['province', 'type', 'batch', 'year', 'proscore']


class LineSchoolAdmin(object):
    list_display = [
        'school_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'average',
        'proscore']
    list_per_page = 10
    list_filter = [
        'school_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'average']
    search_fields = [
        'school_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'proscore']


class LineSpecialtyAdmin(object):
    list_display = [
        'school_name',
        'sp_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'average',
        'proscore']
    list_per_page = 10
    list_filter = [
        'school_name',
        'sp_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'average',
        'proscore']
    search_fields = [
        'school_name',
        'sp_name',
        'local_province_name',
        'type',
        'batch',
        'year',
        'max_score',
        'min_score',
        'average',
        'proscore']


# 注册模型类
xadmin.site.register(SchoolInfo, SchoolInfoAdmin)
xadmin.site.register(SpecialtyInfo, SpecialtyInfoAdmin)
xadmin.site.register(LinePro, LineProAdmin)
xadmin.site.register(LineSchool, LineSchoolAdmin)
xadmin.site.register(LineSpecialty, LineSpecialtyAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
