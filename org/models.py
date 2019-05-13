from django.db import models

# Create your models here.


class SchoolInfo(models.Model):
    """
    所有学校的信息
    """
    school_name = models.CharField(max_length=30, verbose_name='学校名称')
    province_name = models.CharField(max_length=30, verbose_name='省份名称')
    city_name = models.CharField(max_length=30, blank=True, verbose_name='城市名称')
    county_name = models.CharField(max_length=30, blank=True, verbose_name='地区名称')
    school_type = models.CharField(max_length=30, blank=True, verbose_name='办学类型')
    type_name = models.CharField(max_length=30, blank=True, verbose_name='院校类型')
    school_intro = models.TextField(blank=True, verbose_name='学校简介')
    subject = models.TextField(blank=True, verbose_name='重点学科')
    admissions = models.CharField(max_length=30, blank=True, verbose_name='自主招生')
    central = models.CharField(max_length=30, blank=True, verbose_name='中央部委')
    department = models.CharField(max_length=30, blank=True, verbose_name='教育部直属')
    f211 = models.CharField(max_length=30, blank=True, verbose_name='211')
    f985 = models.CharField(max_length=30, blank=True, verbose_name='985')
    dual_class = models.CharField(max_length=30, blank=True, verbose_name='双一流')
    dual_class_name = models.CharField(max_length=30, blank=True, verbose_name='双一流名称')

    class Meta:
        verbose_name = "学校信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.pk)


class SpecialtyInfo(models.Model):
    """
    所有专业的信息
    """
    sp_name = models.CharField(max_length=30, blank=True, verbose_name='专业名称')
    level1_name = models.CharField(max_length=30, blank=True, verbose_name='专业层次')
    level2_name = models.CharField(max_length=30, blank=True, verbose_name='专业门类')
    level3_name = models.CharField(max_length=30, blank=True, verbose_name='专业类别')
    limit_year = models.CharField(max_length=30, blank=True, verbose_name='专业学习年份')
    degree = models.CharField(max_length=30, blank=True, verbose_name='授予学士')
    content = models.TextField(blank=True, verbose_name='专业简介')
    job = models.TextField(blank=True, verbose_name='发展')
    is_what = models.TextField(blank=True, verbose_name='是什么')
    do_what = models.TextField(blank=True, verbose_name='干什么')
    learn_what = models.TextField(blank=True, verbose_name='学习什么')
    rate = models.CharField(max_length=30, blank=True, verbose_name='男女比例')
    sel_adv = models.CharField(max_length=30, blank=True, verbose_name='生源选择')

    class Meta:
        verbose_name = '专业信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.pk)


class LinePro(models.Model):
    """
    省分数线信息
    """
    province = models.CharField(max_length=30, verbose_name='省份')
    type = models.CharField(max_length=30, blank=True, verbose_name='文理科')
    batch = models.CharField(max_length=30, blank=True, verbose_name='批次')
    year = models.CharField(max_length=30, blank=True, verbose_name='年份')
    proscore = models.CharField(max_length=30, blank=True, verbose_name='分数')

    class Meta:
        verbose_name = '省份录取分数线'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.pk)


class LineSchool(models.Model):
    """
    学校录取分数线
    """
    school_name = models.CharField(max_length=30, verbose_name='学校名称')
    province_name = models.CharField(max_length=30, verbose_name='省份名称')
    school_type = models.CharField(max_length=30, verbose_name='办学类型')
    type_name = models.CharField(max_length=30, verbose_name='院校类型')
    admissions = models.CharField(max_length=30, blank=True, verbose_name='自主招生')
    central = models.CharField(max_length=30, blank=True, verbose_name='中央部委')
    department = models.CharField(max_length=30, blank=True, verbose_name='教育部直属')
    f211 = models.CharField(max_length=30, blank=True, verbose_name='211')
    f985 = models.CharField(max_length=30, blank=True, verbose_name='985')
    dual_class = models.CharField(max_length=30, blank=True, verbose_name='双一流')
    dual_class_name = models.CharField(max_length=30, blank=True, verbose_name='双一流名称')
    type = models.CharField(max_length=30, blank=True, verbose_name='文理科')
    batch = models.CharField(max_length=30, blank=True, verbose_name='批次')
    local_province_name = models.CharField(max_length=30, blank=True, verbose_name='招生省份')
    year = models.CharField(max_length=30, blank=True, verbose_name='年份')
    max_score = models.CharField(max_length=30, blank=True, verbose_name='最高分')
    min_score = models.CharField(max_length=30, blank=True, verbose_name='最低分')
    average = models.CharField(max_length=30, blank=True, verbose_name='平均分')
    proscore = models.CharField(max_length=30, blank=True, verbose_name='省控线')

    class Meta:
        verbose_name = '学校录取分数线'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.pk)


class LineSpecialty(models.Model):
    """
    专业录取分数线
    """
    sp_name = models.CharField(max_length=30, verbose_name='专业名称')
    school_name = models.CharField(max_length=30, null=True, verbose_name='学校名称')
    level1_name = models.CharField(max_length=30, null=True, verbose_name='专业层次')
    level2_name = models.CharField(max_length=30, null=True, verbose_name='专业门类')
    level3_name = models.CharField(max_length=30, null=True, verbose_name='专业类别')
    province_name = models.CharField(max_length=30, null=True, verbose_name='省份名称')
    school_type = models.CharField(max_length=30, null=True, verbose_name='办学类型')
    type_name = models.CharField(max_length=30, null=True, verbose_name='院校类型')
    admissions = models.CharField(max_length=30, blank=True, null=True, verbose_name='自主招生')
    central = models.CharField(max_length=30, blank=True, null=True, verbose_name='中央部委')
    department = models.CharField(max_length=30, blank=True, null=True, verbose_name='教育部直属')
    f211 = models.CharField(max_length=30, blank=True, null=True, verbose_name='211')
    f985 = models.CharField(max_length=30, blank=True, null=True, verbose_name='985')
    dual_class = models.CharField(max_length=30, blank=True, null=True, verbose_name='双一流')
    dual_class_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='双一流名称')
    type = models.CharField(max_length=30, blank=True, null=True, verbose_name='文理科')
    batch = models.CharField(max_length=30, blank=True, null=True, verbose_name='批次')
    local_province_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='招生省份')
    year = models.CharField(max_length=30, blank=True, null=True, verbose_name='年份')
    max_score = models.CharField(max_length=30, blank=True, null=True, verbose_name='最高分')
    min_score = models.CharField(max_length=30, blank=True, null=True, verbose_name='最低分')
    average = models.CharField(max_length=30, blank=True, null=True, verbose_name='平均分')
    proscore = models.CharField(max_length=30, blank=True, null=True, verbose_name='省控线')

    class Meta:
        verbose_name = '专业录取分数线'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.pk)

