from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from org.models import *


def index(request):
    return render(request, 'index.html')


def school(request):
    schoolinfo = SchoolInfo.objects.all()

    province_name = request.GET.get('province_name', '')
    if province_name:
        schoolinfo = schoolinfo.filter(province_name__icontains=province_name)

    type_name = request.GET.get('type_name', '')
    if type_name:
        schoolinfo = schoolinfo.filter(type_name__icontains=type_name)

    school_type = request.GET.get('school_type', '')
    if school_type == '普通本科':
        schoolinfo = schoolinfo.filter(school_type__icontains='6000')
    elif school_type == '独立学院':
        schoolinfo = schoolinfo.filter(school_type__icontains='6001')
    elif school_type == '专科(高职)':
        schoolinfo = schoolinfo.filter(school_type__icontains='6002')
    elif school_type == '中外合作办学':
        schoolinfo = schoolinfo.filter(school_type__icontains='6003')
    elif school_type == '其他':
        schoolinfo = schoolinfo.filter(school_type__icontains='6007')

    college = request.GET.get('college', '')
    if college == '985工程':
        schoolinfo = schoolinfo.filter(f985__icontains='1')
    elif college == '211工程':
        schoolinfo = schoolinfo.filter(f211__icontains='1')
    elif college == '一流大学建设高校':
        schoolinfo = schoolinfo.filter(dual_class__icontains='38001')
    elif college == '一流学科建设高校':
        schoolinfo = schoolinfo.filter(dual_class__icontains='38000')
    elif college == '教育部直属':
        schoolinfo = schoolinfo.filter(department__icontains='1')
    elif college == '中央部委':
        schoolinfo = schoolinfo.filter(central__icontains='1')
    elif college == '自主招生试点':
        schoolinfo = schoolinfo.filter(admissions__icontains='1')

    school_name = request.GET.get('school_name', '')
    if school_name:
        schoolinfo = schoolinfo.filter(school_name__icontains=school_name)

    # 分页
    limit = 20
    paginatior = Paginator(schoolinfo, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'schoolinfo1': loaded,
        'count': schoolinfo.count(),
        'province_name': province_name,
        'type_name': type_name,
        'school_type': school_type,
        'college': college,
        'school_name': school_name,
    }
    return render(request, 'school.html', context)


def specialty(request):
    specialtyinfo = SpecialtyInfo.objects.all()

    level1_name = request.GET.get('level1_name', '')
    if level1_name:
        specialtyinfo = specialtyinfo.filter(level1_name__icontains=level1_name)

    level2_name = request.GET.get('level2_name', '')
    if level2_name:
        specialtyinfo = specialtyinfo.filter(level2_name__icontains=level2_name)

    sp_name = request.GET.get('sp_name', '')
    if sp_name:
        specialtyinfo = specialtyinfo.filter(sp_name__icontains=sp_name)

    # 分页
    limit = 20
    paginatior = Paginator(specialtyinfo, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'specialtyinfo1': loaded,
        'count': specialtyinfo.count(),
        'level1_name': level1_name,
        'level2_name': level2_name,
        'sp_name': sp_name,
    }
    return render(request, 'specialty.html', context)


def lineprovince(request):
    linpro = LinePro.objects.all()

    province = request.GET.get('province', '')
    if province:
        linpro = linpro.filter(province__icontains=province)

    batch = request.GET.get('batch', '')
    if batch:
        linpro = linpro.filter(batch__icontains=batch)

    type = request.GET.get('type', '')
    if type:
        linpro = linpro.filter(type__icontains=type)

    year = request.GET.get('year', '')
    if year:
        linpro = linpro.filter(year__icontains=year)

    # 分页
    limit = 20
    paginatior = Paginator(linpro, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'linpro1': loaded,
        'province': province,
        'batch': batch,
        'type': type,
        'year': year,
    }
    return render(request, 'lineprovince.html', context)


def lineschool(request):
    linsch = LineSchool.objects.all()

    province_name = request.GET.get('province_name', '')
    if province_name:
        linsch = linsch.filter(province_name__icontains=province_name)

    batch = request.GET.get('batch', '')
    if batch:
        linsch = linsch.filter(batch__icontains=batch)

    type = request.GET.get('type', '')
    if type:
        linsch = linsch.filter(type__icontains=type)

    year = request.GET.get('year', '')
    if year:
        linsch = linsch.filter(year__icontains=year)

    type_name = request.GET.get('type_name', '')
    if type_name:
        linsch = linsch.filter(type_name__icontains=type_name)

    college = request.GET.get('college', '')
    if college == '985工程':
        linsch = linsch.filter(f985__icontains='1')
    elif college == '211工程':
        linsch = linsch.filter(f211__icontains='1')
    elif college == '一流大学建设高校':
        linsch = linsch.filter(dual_class__icontains='38001')
    elif college == '一流学科建设高校':
        linsch = linsch.filter(dual_class__icontains='38000')
    elif college == '教育部直属':
        linsch = linsch.filter(department__icontains='1')
    elif college == '中央部委':
        linsch = linsch.filter(central__icontains='1')
    elif college == '自主招生试点':
        linsch = linsch.filter(admissions__icontains='1')

    school_type = request.GET.get('school_type', '')
    if school_type == '普通本科':
        linsch = linsch.filter(school_type__icontains='6000')
    elif school_type == '独立学院':
        linsch = linsch.filter(school_type__icontains='6001')
    elif school_type == '专科(高职)':
        linsch = linsch.filter(school_type__icontains='6002')
    elif school_type == '中外合作办学':
        linsch = linsch.filter(school_type__icontains='6003')
    elif school_type == '其他':
        linsch = linsch.filter(school_type__icontains='6007')

    school_name = request.GET.get('school_name', '')
    if school_name:
        linsch = linsch.filter(school_name__icontains=school_name)

    # 分页
    limit = 20
    paginatior = Paginator(linsch, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'linsch1': loaded,
        'province_name': province_name,
        'batch': batch,
        'type': type,
        'year': year,
        'type_name': type_name,
        'college': college,
        'school_type': school_type,
        'school_name': school_name,
    }
    return render(request, 'lineschool.html', context)


def linespecialty(request):
    linspe = LineSpecialty.objects.all()

    province_name = request.GET.get('province_name', '')
    if province_name:
        linspe = linspe.filter(province_name__icontains=province_name)

    batch = request.GET.get('batch', '')
    if batch:
        linspe = linspe.filter(batch__icontains=batch)

    type = request.GET.get('type', '')
    if type:
        linspe = linspe.filter(type__icontains=type)

    year = request.GET.get('year', '')
    if year:
        linspe = linspe.filter(year__icontains=year)

    type_name = request.GET.get('type_name', '')
    if type_name:
        linspe = linspe.filter(type_name__icontains=type_name)

    college = request.GET.get('college', '')
    if college == '985工程':
        linspe = linspe.filter(f985__icontains='1')
    elif college == '211工程':
        linspe = linspe.filter(f211__icontains='1')
    elif college == '一流大学建设高校':
        linspe = linspe.filter(dual_class__icontains='38001')
    elif college == '一流学科建设高校':
        linspe = linspe.filter(dual_class__icontains='38000')
    elif college == '教育部直属':
        linspe = linspe.filter(department__icontains='1')
    elif college == '中央部委':
        linspe = linspe.filter(central__icontains='1')
    elif college == '自主招生试点':
        linspe = linspe.filter(admissions__icontains='1')

    school_type = request.GET.get('school_type', '')
    if school_type == '普通本科':
        linspe = linspe.filter(school_type__icontains='6000')
    elif school_type == '独立学院':
        linspe = linspe.filter(school_type__icontains='6001')
    elif school_type == '专科(高职)':
        linspe = linspe.filter(school_type__icontains='6002')
    elif school_type == '中外合作办学':
        linspe = linspe.filter(school_type__icontains='6003')
    elif school_type == '其他':
        linspe = linspe.filter(school_type__icontains='6007')

    school_name = request.GET.get('school_name', '')
    if school_name:
        linspe = linspe.filter(school_name__icontains=school_name)

    # 分页
    limit = 20
    paginatior = Paginator(linspe, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'linspe1': loaded,
        'province_name': province_name,
        'batch': batch,
        'type': type,
        'year': year,
        'type_name': type_name,
        'college': college,
        'school_type': school_type,
        'school_name': school_name,
    }
    return render(request, 'linespecialty.html', context)


def forecast(request):
    linsch = LineSchool.objects.all()

    province_name = request.GET.get('province_name', '')
    if province_name:
        linsch = linsch.filter(province_name__icontains=province_name)

    batch = request.GET.get('batch', '')
    if batch:
        linsch = linsch.filter(batch__icontains=batch)

    type = request.GET.get('type', '')
    if type:
        linsch = linsch.filter(type__icontains=type)

    year = request.GET.get('year', '')
    if year:
        linsch = linsch.filter(year__icontains=year)

    type_name = request.GET.get('type_name', '')
    if type_name:
        linsch = linsch.filter(type_name__icontains=type_name)

    college = request.GET.get('college', '')
    if college == '985工程':
        linsch = linsch.filter(f985__icontains='1')
    elif college == '211工程':
        linsch = linsch.filter(f211__icontains='1')
    elif college == '一流大学建设高校':
        linsch = linsch.filter(dual_class__icontains='38001')
    elif college == '一流学科建设高校':
        linsch = linsch.filter(dual_class__icontains='38000')
    elif college == '教育部直属':
        linsch = linsch.filter(department__icontains='1')
    elif college == '中央部委':
        linsch = linsch.filter(central__icontains='1')
    elif college == '自主招生试点':
        linsch = linsch.filter(admissions__icontains='1')

    school_type = request.GET.get('school_type', '')
    if school_type == '普通本科':
        linsch = linsch.filter(school_type__icontains='6000')
    elif school_type == '独立学院':
        linsch = linsch.filter(school_type__icontains='6001')
    elif school_type == '专科(高职)':
        linsch = linsch.filter(school_type__icontains='6002')
    elif school_type == '中外合作办学':
        linsch = linsch.filter(school_type__icontains='6003')
    elif school_type == '其他':
        linsch = linsch.filter(school_type__icontains='6007')

    school_name = request.GET.get('school_name', '')
    if school_name:
        linsch = linsch.filter(school_name__icontains=school_name)

    # 分页
    limit = 20
    paginatior = Paginator(linsch, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'linsch1': loaded,
        'province_name': province_name,
        'batch': batch,
        'type': type,
        'year': year,
        'type_name': type_name,
        'college': college,
        'school_type': school_type,
        'school_name': school_name,
    }
    return render(request, 'forecast.html', context)


def school_detail(request, scid):
    schoolinfo = SchoolInfo.objects.filter(id=scid)
    schoolinfo1 = [i for i in schoolinfo]

    if schoolinfo1[0].school_type == '6000':
        school_type = '本科'
    elif schoolinfo1[0].school_type == '6001':
        school_type = '独立学院'
    elif schoolinfo1[0].school_type == '6002':
        school_type = '专科(高职)'
    elif schoolinfo1[0].school_type == '6003':
        school_type = '中外合作办学'
    else:
        school_type = '其他'

    if schoolinfo1[0].admissions == '1':
        admissions = '自主招生'
    else:
        admissions = ''

    if schoolinfo1[0].central == '1':
        central = '中央部委'
    else:
        central = ''

    if schoolinfo1[0].department == '1':
        department = '教育部直属'
    else:
        department = ''

    if schoolinfo1[0].f211 == '1':
        f211 = '211 工程'
    else:
        f211 = ''

    if schoolinfo1[0].f985 == '1':
        f985 = '985 工程'
    else:
        f985 = ''

    if schoolinfo1[0].dual_class == '38001':
        dual_class = '一流大学建设高校'
    elif schoolinfo1[0].dual_class == '38002':
        dual_class = '一流学科建设高校'
    else:
        dual_class = ''

    context = {
        'schoolinfo1': schoolinfo1[0],
        'scid': scid,
        'school_type': school_type,
        'f211': f211,
        'f985': f985,
        'admissions': admissions,
        'central': central,
        'department': department,
        'dual_class': dual_class,

    }
    return render(request, 'school_detail.html', context)


def specialty_detail(request, spid):
    specialtyinfo = SpecialtyInfo.objects.filter(id=spid)
    specialtyinfo1 = [i for i in specialtyinfo]

    context = {
        'specialtyinfo1': specialtyinfo1[0],
        'spid': spid,
    }
    return render(request, 'specialty_detail.html', context)


def specialty_school(request):
    specialtyinfo = SpecialtyInfo.objects.all()

    # 分页
    limit = 20
    paginatior = Paginator(specialtyinfo, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'specialtyinfo1': loaded,
        'scid': 1,
        'spid': 1,
    }
    return render(request, 'specialty_school.html', context)


def school_compare(request):
    return render(request, 'school_compare.html')


