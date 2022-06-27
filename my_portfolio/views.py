# from django.shortcuts import render, redirect
from .models import (
    PortfolioProject,
)
from django.views.generic import (
    ListView,
    DetailView,
)
# Create your views here.


class PortfolioView(ListView):
    model = PortfolioProject
    context_object_name = 'portfolio'
    template_name = 'my_portfolio/my_portfolio.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Мои проекты'
        return context

    def get_queryset(self):
        return PortfolioProject.objects.filter(is_public=True)


class ProjectDetailView(DetailView):
    model = PortfolioProject
    context_object_name = 'project_item'
