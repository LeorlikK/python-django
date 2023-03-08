from django.db import models

# Create your models here.
from django.urls import reverse

class TestJson(models.Model):
    name = models.CharField('Имя', max_length=100)
    number = models.IntegerField('Номер')
    list_json = models.JSONField('Json')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Json'
        verbose_name_plural = 'Json'

class CategoryUhod(models.Model):
    title = models.CharField('Категория', max_length=250, db_index=True)
    slug = models.SlugField('Имя строки', max_length=100, blank=True)

    def __str__(self):
        return self.title

    def sin_sobaki(self):
        return 'Sin sobaki!'

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title',]

class Uhod_base(models.Model):
    publication = models.BooleanField('Опубликовано', null=True, db_index=True)
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField('Имя строки', max_length=100, blank=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    photo = models.ImageField('Фотография', upload_to='photos/%Y/%m/',blank=True)
    date_publication = models.DateTimeField('Дата публикации', auto_now_add=True)
    date_editing = models.DateTimeField('Дата редактирования', auto_now=True)
    category = models.ForeignKey(CategoryUhod, max_length=250, on_delete=models.PROTECT, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_category(self):
        return CategoryUhod.objects.all()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_publication', 'title']