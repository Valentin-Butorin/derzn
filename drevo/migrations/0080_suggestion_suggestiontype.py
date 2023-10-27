# Generated by Django 3.2.4 on 2023-10-18 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drevo', '0079_remove_tz_available_suggestion_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionType',
            fields=[
                ('type_name', models.CharField(max_length=255, verbose_name='Название типа')),
                ('weight', models.IntegerField(primary_key=True, serialize=False, verbose_name='Вес для сортировки')),
            ],
            options={
                'verbose_name': 'Вид предложения',
                'verbose_name_plural': 'Виды предложений',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Предложение')),
                ('is_approve', models.BooleanField(blank=True, default=None, null=True, verbose_name='Результат проверки')),
                ('check_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата проверки')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('expert', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checked_suggestions', to=settings.AUTH_USER_MODEL, verbose_name='Эксперт')),
                ('parent_knowlege', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='drevo.znanie', verbose_name='Знание')),
                ('suggestions_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drevo.suggestiontype', verbose_name='Вид предложения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Предложение пользователя',
                'verbose_name_plural': 'Предложения пользователей',
            },
        ),
    ]