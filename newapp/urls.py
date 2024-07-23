from django.contrib import admin
from django.urls import path
from newapp.views.dlogin import dlogin
from newapp.views.dlogout import dlogout
from newapp.views.register import register
from newapp.views.change_password import change_password

urlpatterns = [
    path('login/', dlogin, name='dlogin'),
    path('logout/', dlogout, name='dlogout'),
    path('register/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
]
