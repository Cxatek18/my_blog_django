from django.urls import path
from .views import (
    AccountDetailView,
    register,
    user_login,
    user_logout,
    UserBanedView,
)

urlpatterns = [
    path('user/register/', register, name='register'),
    path('user/login/', user_login, name='login'),
    path('user/logout/', user_logout, name='logout'),
    path(
        'user/personal_account/<int:pk>',
        AccountDetailView.as_view(), name='personal_account',
    ),
    path(
        'user/personal_account/<int:pk>',
        AccountDetailView.as_view(), name='view_user',
    ),
    path(
        'user/baned_user/<int:pk>',
        UserBanedView.as_view(), name='baned_user',
    ),
]
