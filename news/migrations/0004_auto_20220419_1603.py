# Generated by Django 3.2 on 2022-04-19 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_news_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
        migrations.AddField(
            model_name='news',
            name='offer',
            field=models.BooleanField(default=True, verbose_name='Одобрена'),
        ),
        migrations.AlterField(
            model_name='news',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
        ),
        migrations.CreateModel(
            name='NewsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Лайк', 'Лайк'), ('Дизлайк', 'Дизлайк')], default='Лайк', max_length=10)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Реакция пользователя',
                'verbose_name_plural': 'Реакции пользователей',
            },
        ),
    ]