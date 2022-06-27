from django.urls import path
from .views import (
    PortfolioView,
    ProjectDetailView,
)

urlpatterns = [
    path(
        'portfolio/list_project/', PortfolioView.as_view(),  name='portfolio',
    ),
    path(
        'portfolio/<int:pk>/detail/',
        ProjectDetailView.as_view(), name='view_my_project',
    ),
]
