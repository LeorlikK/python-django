from django.db import models

# Create your models here.

class News_base(models.Model):
    title = models.CharField('Название', max_length=50, default='No_name')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return f'/news/{self.id}'

# class New_class(models.Model):
#     comments = models.ForeignKey(News_base, on_delete=models.CASCADE)
