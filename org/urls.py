from django.urls import path
from org.views import *


urlpatterns = [
    path('', index, name='index'),
    path('school/', school, name='school'),
    path('school/<scid>/', school_detail, name='school_detail'),
    path('specialty/', specialty, name='specialty'),
    path('specialty/school/', specialty_school, name='specialty_school'),
    path('specialty/<spid>/', specialty_detail, name='specialty_detail'),
    path('lineprovince/', lineprovince, name='lineprovince'),
    path('lineschool/', lineschool, name='lineschool'),
    path('linespecialty/', linespecialty, name='linespecialty'),
    path('forecast/', forecast, name='forecast'),
    path('school_compare/', school_compare, name='school_compare'),
]
