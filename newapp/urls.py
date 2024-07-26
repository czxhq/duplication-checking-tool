from django.contrib import admin
from django.urls import path
from newapp.views.dlogin import dlogin
from newapp.views.dlogout import dlogout
from newapp.views.register import register
from newapp.views.change_password import change_password
from newapp.views.upload import upload
from newapp.views.getRecords import getRecords
from newapp.views.load import load

urlpatterns = [
    path('login/', dlogin, name='dlogin'),
    path('logout/', dlogout, name='dlogout'),
    path('register/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
    path('upload/', upload, name='upload'),
    path('getRecords/', getRecords, name='getRecords'),
    path('load/', load, name='load'),
]
