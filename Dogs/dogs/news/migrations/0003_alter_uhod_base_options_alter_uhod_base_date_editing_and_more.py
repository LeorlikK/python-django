# Generated by Django 4.0.5 on 2022-07-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_uhod_base_options_categoryuhod_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uhod_base',
            options={'ordering': ['-date_publication', 'title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='uhod_base',
            name='date_editing',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='uhod_base',
            name='date_publication',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='uhod_base',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/', verbose_name='Фотография'),
        ),
    ]