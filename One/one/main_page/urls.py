from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('biography', views.biography, name='biography')
]