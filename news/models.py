from django.db import models
from django.urls import reverse
# from user.models import User


class News(models.Model):
    title = models.CharField(
        verbose_name='Название', max_length=255,
        unique=True,
    )
    description = models.CharField(
        verbose_name='Краткое описание', max_length=255,
        unique=True, default='Краткое описание поста',
    )
    content = models.TextField(
        verbose_name='Текст новости',
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
        upload_to='photos/%Y/%m/%d/'
    )
    is_public = models.BooleanField(
        verbose_name='Состояние',
        default=True,
    )
    category = models.ForeignKey(
        'Category', verbose_name='Категория',
        on_delete=models.PROTECT,
    )
    owner = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Автор поста',
        default='1',
        related_name='author'
    )
    liked = models.ManyToManyField(
        'user.User',
        default=None,
        blank=True,
        verbose_name='Лайки',
    )
    offer = models.BooleanField(
        verbose_name='Одобрена',
        default=True,
    )
    favorite_news = models.ManyToManyField(
        'user.User',
        default=None,
        blank=True,
        verbose_name='Добавить в избранное',
        related_name='favorite_news'
    )

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    @property
    def num_likes(self):
        return self.liked.all().count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(
        verbose_name='Название', max_length=120
    )

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class NewsLikes(models.Model):

    LIKE_CHOICES = (
        ('Лайк', 'Лайк'),
        ('Дизлайк', 'Дизлайк')
    )

    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        verbose_name='Новость'
    )
    value = models.CharField(
        choices=LIKE_CHOICES, default='Лайк', max_length=10
    )

    def __str__(self):
        return f'{self.user}: {self.news}'

    class Meta:
        verbose_name = 'Реакция пользователя'
        verbose_name_plural = 'Реакции пользователей'


class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        verbose_name='Новость',
        related_name='comment_news'
    )
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    created_data = models.DateTimeField(
        verbose_name='Создан комментарий', auto_now_add=True
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        blank=True,
    )
    status = models.BooleanField(
        verbose_name='Видимость статьи',
        default=False
    )

    def __str__(self):
        return f'{self.user}: {self.news}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_data']


class FavoriteUserNews(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        verbose_name='Новость',
    )
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f'{self.user}: {self.news}'

    class Meta:
        verbose_name = 'Избранная новость'
        verbose_name_plural = 'Избранные новости'
