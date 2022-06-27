from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=120,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=150,
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name='Фото пользователя',
        upload_to='avatars',
        blank=True,
        null=True,
        default='avatars/defalt.jpg',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Является активным'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Является админом'
    )
    is_moderator = models.BooleanField(
        default=False,
        verbose_name='Является модератором'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    time_ban = models.DateTimeField(
        verbose_name='Время блокировки',
        blank=True,
        null=True,
    )
    status_ban = models.BooleanField(
        verbose_name='Статус бана',
        default=False,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse('view_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserBanedIp(models.Model):
    ip_address = models.GenericIPAddressField(
        verbose_name='IP адрес',
    )
    attempts = models.IntegerField(
        'Неудачных попыток', default=0
    )
    time_unblock = models.DateTimeField(
        verbose_name='Время разблокировки', blank=True
    )
    status = models.BooleanField(
        verbose_name='Статус блокировки', default=False
    )

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'Бан по ошибкам авторизации'
        verbose_name_plural = 'Баны по ошибкам авторизации'
