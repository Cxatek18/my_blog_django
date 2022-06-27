from django import forms
from .models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from captcha.fields import (
    CaptchaField,
)
# from django.contrib.admin.widgets import AdminDateWidget


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'autocomplete': 'off'}),
        help_text='Имя пользователя не должно превыщать 150 символов'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    capcha = CaptchaField(
        label='Капча',
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2'
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'autocomplete': 'off'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    capcha = CaptchaField(
        label='Капча',
    )


class UserBanedForm(forms.ModelForm):
    time_ban = forms.DateTimeField(
        label='Дата',
        widget=forms.widgets.DateInput(attrs={'type': 'data'}),
        input_formats=['%d.%m.%Y %H:%M'],
        help_text='Формат: 12.05.2000 22:50'
    )
    status_ban = forms.BooleanField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = User
        fields = ('time_ban', 'status_ban')
