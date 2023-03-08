from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import  views
from .views import UhodList, UhodDetail, CategoryList, TestSearch, ApiJson, BotApiView

urlpatterns = [
    path('', views.test_input, name='news'),
    path('create', views.ApiJson.as_view(), name='create'),
    path('read', views.ApiJson.as_view(), name='read'),
    path('update/<slug:slug>/', views.json_update, name='update'),
    path('delete', views.json_delete, name='delete'),
    path('', views.TestSearch.as_view(), name='news'),
    #path('', UhodList.as_view(), name='news'),
    path('/<int:pk>/', CategoryList.as_view(), name='news_category'),
    path('news/<int:pk>/', UhodDetail.as_view(), name='news_detail'),
    #re_path
    #path('<slug:bot_command>/', BotApiView.as_view()),
    path('<slug:bot_command>/', views.json_update),
]



# urlpatterns = [
#     path('', views.test1, name='news'),
#     path('<str:slug>/', views.test2, name='category'),
#     path('detail/<int:pk>', views.test3, name='news_detail'),
# ]
