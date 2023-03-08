from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.input_user, name='input'),
    path('logout', views.logout_user, name='logout'),
    path('registration', views.registration_user, name='registration'),
]9