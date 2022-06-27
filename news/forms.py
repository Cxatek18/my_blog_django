from django import forms
from captcha.fields import (
    CaptchaField,
)
from .models import (
    News,
    Comment,
)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'description',
            'content', 'photo', 'is_public', 'offer', 'category',
            'owner',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
            'category': forms.Select(attrs={'class': 'form-control'},),
        }


class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Тема письма',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    connection = forms.CharField(
        label='Как с вами связаться',
        help_text='Ссылка на вашу соцсеть для связи или ваша почта',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    capcha = CaptchaField(
        label='Капча',
    )


class NewsOfferForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'description',
            'content', 'photo', 'offer', 'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
            'category': forms.Select(attrs={'class': 'form-control'},),
            'offer': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
        }


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text', 'status',
        ]

        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
        }
