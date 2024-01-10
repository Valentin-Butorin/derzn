# Generated by Django 3.2.4 on 2024-01-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0106_auto_20231223_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='var',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='var',
            name='structure',
            field=models.IntegerField(choices=[(0, 'Переменная'), (1, 'Массив'), (2, 'Справочник'), (3, 'Итератор'), (4, 'Условие')], default=0, verbose_name='Структура'),
        ),
    ]
