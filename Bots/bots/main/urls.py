from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.read_1, name='main'),
    #path('<int:pk>', views.BotDetailView.as_view(), name='bot_detail'),
    path('<int:pkk>', views.test_bot, name='bot_detail'),
    path('table-three', views.test_img, name='bot_table_three'),
    path('add_bot', views.add_bot, name='bot_add'),
    path('find', views.test_input, name='bot_test'),
    #path('info/<int:pk>', views.json_test, name='bot_info'),

    path('create', views.add_1, name='bot_create'),
    path('', views.read_1, name='bot_read'),
    path('read/<int:bot_pk>/', views.read_2, name='bot_read_two'),
    path('update', views.update_1, name='bot_update'),
    path('delete', views.delete_1, name='bot_delete'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)