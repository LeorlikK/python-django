from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_biography, name='all_biography'),
    path('yennefer', views.yennefer_biography, name='yennefer_biography'),
    path('triss', views.triss_biography, name='triss_biography')
]