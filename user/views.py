from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from .models import (
    User,
    # UserBanedIp,
)
from .forms import (
    UserRegisterForm,
    UserLoginForm,
    # UserBanedIp,
    UserBanedForm,
)
from django.views.generic import (
    DetailView,
    UpdateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from news.permissions import UserRightsMixin
# import pytz
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегестрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.time_ban is None:
                login(request, user)
                messages.success(request, 'Вы вошли в систему')
                return redirect('home')
            elif user.time_ban < timezone.now():
                login(request, user)
                user.status_ban = False
                user.time_ban = None
                user.save()
                messages.success(request, 'Вы вошли в систему')
                return redirect('home')
            else:
                str_message = f'Извените но вы\
                    забанены до {user.time_ban}'
                messages.error(
                    request, str_message.split('.')[0]
                )
                return render(request, 'user/login.html', {'form': form})
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('login')


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user_info'
    template_name = 'user/personal_account.html'
    raise_exception = True


class UserBanedView(LoginRequiredMixin, UserRightsMixin, UpdateView):
    model = User
    template_name = 'user/baned_user.html'
    form_class = UserBanedForm
    context_object_name = 'user_item'
    success_url = reverse_lazy('home')
    raise_exception = True

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        # request.POST['time_ban'] = timezone.now() + timezone.timedelta(
        #     minutes=2
        # )
        request.POST['status_ban'] = True
        return super(UserBanedView, self).post(request, **kwargs)
