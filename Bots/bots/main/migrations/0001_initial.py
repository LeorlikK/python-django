# Generated by Django 4.0.5 on 2022-06-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=250, verbose_name='State')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('position', models.CharField(max_length=250, verbose_name='Position')),
                ('all_res', models.CharField(max_length=250, verbose_name='All_res')),
            ],
            options={
                'verbose_name': 'Бот',
                'verbose_name_plural': 'Боты',
            },
        ),
    ]