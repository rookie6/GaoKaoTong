from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from org.models import *


def index(request):
    return render(request, 'index.html')


# def ajax_get(request):
#     schoolinfo = SchoolInfo.objects.all()
#     list = []
#     for i in schoolinfo:
#         list.append([i.school_name, i.province_name])
#     return JsonResponse({'data': list})


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
    return render(request, 'specialty.html')


def specialty_school(request):
    return render(request, 'specialty_school.html')


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
    return render(request, 'lineschool.html')


def linespecialty(request):
    return render(request, 'linespecialty.html')


def forecast(request):
    return render(request, 'forecast.html')


def school_detail(request):
    return render(request, 'school_detail.html')


def specialty_detail(request):
    return render(request, 'specialty_detail.html')


def school_compare(request):
    return render(request, 'school_compare.html')


