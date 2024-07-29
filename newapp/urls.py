from django.contrib import admin
from django.urls import path
from newapp.views.dlogin import dlogin
from newapp.views.dlogout import dlogout
from newapp.views.register import register
from newapp.views.change_password import change_password
from newapp.views.upload import upload
from newapp.views.getRecords import getRecords
from newapp.views.load import load
from newapp.views.setSecurity import setSecurity
from newapp.views.getSecurity import getSecurity
from newapp.views.checkSecurity import checkSecurity
from newapp.views.set_password import set_password

urlpatterns = [
    path('login/', dlogin, name='dlogin'),
    path('logout/', dlogout, name='dlogout'),
    path('register/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
    path('upload/', upload, name='upload'),
    path('getRecords/', getRecords, name='getRecords'),
    path('load/', load, name='load'),
    path('setSecurity/', setSecurity, name='setSecurity'),
    path('getSecurity/', getSecurity, name='getSecurity'),
    path('checkSecurity/', checkSecurity, name='checkSecurity'),
    path('set_password/', set_password, name='set_password'),
]

