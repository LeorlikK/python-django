# Generated by Django 4.0.6 on 2022-07-19 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopmodel',
            options={'ordering': ['-date_publication'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
