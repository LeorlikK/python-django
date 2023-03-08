from django.db import models

# Create your models here.
from django.db.models import CharField, SlugField
from django.urls import reverse_lazy


class ShopModel(models.Model):
    publication = models.BooleanField(verbose_name='Опубликовано', null=True, db_index=True)
    model = models.CharField(verbose_name='Модель', max_length=250, blank=True)
    name = models.CharField(verbose_name='Название', max_length=250)
    slug = models.SlugField(verbose_name='URL', max_length=250)
    short_text = models.CharField(verbose_name='Краткое описание', help_text='2 строки, разделенные "/"', max_length=250, blank=True)
    full_text = models.TextField(verbose_name='Описание', blank=True)
    price = models.FloatField(verbose_name='Цена', blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='images/%Y/%m/', blank=True)
    date_publication = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    date_editing = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse_lazy('bot_detail', kwargs={'pkk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-date_publication', ]