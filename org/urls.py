from django.urls import path
from org.views import *


urlpatterns = [
    path('', index, name='index'),
    path('school/', school, name='school'),
    path('specialty/', specialty, name='specialty'),
    path('specialty_school/', specialty_school, name='specialty_school'),
    path('lineprovince/', lineprovince, name='lineprovince'),
    path('lineschool/', lineschool, name='lineschool'),
    path('linespecialty/', linespecialty, name='linespecialty'),
    path('forecast/', forecast, name='forecast'),
    path('school_detail/', school_detail, name='school_detail'),
    path('specialty_detail/', specialty_detail, name='specialty_detail'),
    path('school_compare/', school_compare, name='school_compare'),
]

