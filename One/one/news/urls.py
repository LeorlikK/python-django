from django.urls import path
from . import views

# app_name = 'arcticles'
urlpatterns = [
    path('', views.all_news, name='all_news'),
    path('<int:pk>/', views.all_news2, name='all_news_two'),
    path('create', views.create_news, name='create_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='reed_once_news'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    #
    path('get', views.get, name='get'),
    path('find', views.find_news, name='find_news'),

]