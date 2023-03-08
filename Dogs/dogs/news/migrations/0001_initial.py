# Generated by Django 4.0.5 on 2022-07-01 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryUhod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Uhod_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication', models.BooleanField(db_index=True, null=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('photo', models.ImageField(blank=True, upload_to='photos/Y%/m%/', verbose_name='Фотография')),
                ('date_publication', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('date_editing', models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования')),
                ('category', models.ForeignKey(blank=True, max_length=250, on_delete=django.db.models.deletion.PROTECT, to='news.categoryuhod')),
            ],
            options={
                'verbose_name': 'Уход',
                'verbose_name_plural': 'Уход',
                'ordering': ['title', 'date_publication'],
            },
        ),
    ]