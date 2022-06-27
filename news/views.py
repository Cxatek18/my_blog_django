from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from .models import (
    News,
    Category,
    NewsLikes,
    Comment,
    FavoriteUserNews,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    TemplateView,
)
from django.views.generic.edit import (
    FormMixin,
)
from .forms import (
    NewsForm,
    ContactForm,
    NewsOfferForm,
    CommentForm,
    UpdateCommentForm,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from .permissions import UserRightsMixin
# Create your views here.


def handling_error_404(request, exception):
    return render(request, 'news/404.html', status=404)


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            content_name = f'{form.cleaned_data["text"]} \
                ||| Для связи: {form.cleaned_data["connection"]}'
            mail = send_mail(
                form.cleaned_data['subject'],
                content_name,
                'gregdev77@gmail.com',
                ['gregdev77@gmail.com'],
                fail_silently=False,
            )
            if mail == 1:
                messages.success(request, 'Письмо успешно отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(request, 'news/contact_with_me.html', {'form': form})


def like_news(request):
    user = request.user
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        news_obj = News.objects.get(id=news_id)

        if user in news_obj.liked.all():
            news_obj.liked.remove(user)
        else:
            news_obj.liked.add(user)

        like, created = NewsLikes.objects.get_or_create(
            user=user, news_id=news_id
        )
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('home')


def favorite_news_add_remove(request):
    user = request.user
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        news_obj = News.objects.get(id=news_id)
        print(request.user.favorite_news.all())

        if user in news_obj.favorite_news.all():
            news_obj.favorite_news.remove(user)
        else:
            news_obj.favorite_news.add(user)

        favorite_news, created = FavoriteUserNews.objects.get_or_create(
            user=user, news_id=news_id
        )

        favorite_news.save()
    return redirect('home')


class HomeNewsView(ListView):
    # model = News - показываем модель из которой берём список
    # аналог строки News.object.all()
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    # extra_context = {'title_head': 'НеГуглиться'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_public=True)


class CategoriesView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    # allow_empty - не разрешаем показ пустых списков
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = Category.objects.get(
                                pk=self.kwargs['category_id']
                            )
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs['category_id'],
            is_public=True,
        )


class NewsDeatilView(FormMixin, DetailView):
    model = News
    context_object_name = 'news_item'
    form_class = CommentForm
    succes_url = 'news/index.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'view_news', kwargs={'pk': self.get_object().id}
        )

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Комментарий создан, ожидайте модерации')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.news = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CreateNewsView(LoginRequiredMixin, UserRightsMixin, CreateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm
    success_url = reverse_lazy('home')
    raise_exception = True


class UpdatePostView(LoginRequiredMixin, UserRightsMixin, UpdateView):
    model = News
    template_name = 'news/update_post.html'
    form_class = NewsForm
    context_object_name = 'news_item'
    success_url = reverse_lazy('home')
    raise_exception = True


class DeletePostView(LoginRequiredMixin, UserRightsMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'news/delete_post.html'
    raise_exception = True


class DeleteListNewsView(LoginRequiredMixin, UserRightsMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/list_delete_post.html'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Удаление постов'
        return context

    def get_queryset(self):
        return News.objects.filter(is_public=True)


class AboutMeView(TemplateView):
    template_name = 'news/about_me.html'
    extra_context = {'title_head': 'Обо мне'}


class NewsOfferCreate(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'news/offer_news.html'
    form_class = NewsOfferForm
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form = NewsOfferForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.offer = False
            instance.owner = self.request.user
            instance.save()
            messages.success(
                request, 'Вы предложили новость к публикации. Спасибо!!!'
            )
        return render(request, 'news/offer_news.html', {'form': form})


class ListNewsOfferView(LoginRequiredMixin, UserRightsMixin, ListView):
    model = News
    context_object_name = 'news_offer'
    template_name = 'news/list_offer_news.html'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Предложеные новости'
        return context

    def get_queryset(self):
        return News.objects.filter(offer=False, is_public=True)


class ListCommentsNewsView(LoginRequiredMixin, UserRightsMixin, ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'news/list_comment_moder.html'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Список комментарии на модерации'
        return context


class UpdateCommentView(LoginRequiredMixin, UserRightsMixin, UpdateView):
    model = Comment
    template_name = 'news/update_comment.html'
    form_class = UpdateCommentForm
    context_object_name = 'comment_item'
    success_url = reverse_lazy('home')
    raise_exception = True


class FavoritesNewsView(LoginRequiredMixin, TemplateView):
    template_name = 'news/favorites_news.html'
    extra_context = {'title_head': 'Избранные новости'}
