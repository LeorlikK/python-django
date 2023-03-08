from django.db import models
# Create your models here.
from django.urls import reverse_lazy

class Test_input_base(models.Model):
    text_input = models.CharField('Text input', max_length=250)


class Table_base(models.Model):
    state = models.CharField('State', max_length=250) # verbose_name='Статус'
    name = models.CharField('Name', max_length=250)
    position = models.CharField('Position' ,max_length=250)
    all_res = models.CharField('All_res' ,max_length=250)

    a1 = models.BooleanField('a1', null=True)
    a2 = models.DateTimeField('a2', auto_now_add=True)

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse_lazy('bot_detail', kwargs={'pkk': self.pk})

    def __str__(self):
        return f'{self.name}, {self.id}'

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'
        ordering = ['-a1', '-a2']

class Category(models.Model):
    title = models.CharField(max_length=250, db_index=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

""" Сложные поля с фалами:
    FileField = models.FileField(upload_to='uploads/%Y/%m/%d/')
    ImageField = model.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    JSONField = model.JSONField
    """

class Table_base_two(models.Model):
    state = models.CharField('State', max_length=250)
    name = models.CharField('Name', max_length=250)
    position = models.CharField('Position' ,max_length=250)
    all_res = models.CharField('All_res' ,max_length=250)

    aaa = models.BooleanField('aaa', null=True)
    bbb = models.DateTimeField('bbb', auto_now_add=True)
    ccc = models.DateTimeField('ccc', auto_now=True)
    ddd = models.DateTimeField('ddd', blank=True)
    iii = models.DecimalField('iii', blank=True, max_digits=5, decimal_places=2)
    fff = models.EmailField('fff', max_length=254)
    ggg = models.IntegerField('ggg')
    hhh = models.TextField('hhh', max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'БотДВА'
        verbose_name_plural = 'БотыДВА'

class Table_base_three(models.Model):
    name = models.CharField(max_length=250, default=True)
    eee = models.ImageField(upload_to='photo/%Y/%m/%d/') # height_field=True, width_field=True) #blank=True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'БотТРИ'
        verbose_name_plural = 'БотыТРИ'