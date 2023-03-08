from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from glasses import settings
from index import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)