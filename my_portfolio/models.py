from django.db import models
from django.urls import reverse
# Create your models here.


class PortfolioProject(models.Model):
    title = models.CharField(
        verbose_name='Название', max_length=255,
        unique=True,
    )
    description = models.CharField(
        verbose_name='Описание проекта', max_length=255,
        default='Описание проекта',
    )
    content = models.TextField(
        verbose_name='О проекте',
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Опубликовано', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновелнно', auto_now=True
    )
    photo = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='photos/my_portfolio/%Y/%m/%d/'
    )
    is_public = models.BooleanField(
        verbose_name='Состояние',
        default=True,
    )
    link_project = models.URLField(
        verbose_name='Ссылка на проект',
        max_length=500,
        default='Ссылка на проект'
    )

    def get_absolute_url(self):
        return reverse('view_my_project', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']
