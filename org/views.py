from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def school(request):
    return render(request, 'school.html')


def specialty(request):
    return render(request, 'specialty.html')


def specialty_school(request):
    return render(request, 'specialty_school.html')


def lineprovince(request):
    return render(request, 'lineprovince.html')


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


