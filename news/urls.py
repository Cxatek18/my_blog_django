from django.urls import path
# from django.views.decorators.cache import cache_page
from .views import (
    HomeNewsView,
    CategoriesView,
    NewsDeatilView,
    CreateNewsView,
    DeletePostView,
    DeleteListNewsView,
    UpdatePostView,
    AboutMeView,
    contact_me,
    like_news,
    NewsOfferCreate,
    ListNewsOfferView,
    ListCommentsNewsView,
    UpdateCommentView,
    favorite_news_add_remove,
    FavoritesNewsView,
)


urlpatterns = [
    # path('', cache_page(60)(HomeNewsView.as_view()),  name='home',),
    path('', HomeNewsView.as_view(),  name='home',),
    path(
        'category/<int:category_id>',
        CategoriesView.as_view(), name='category',
    ),
    path(
        'news/<int:pk>',
        NewsDeatilView.as_view(), name='view_news',
    ),
    path(
        'news/delete-post/',
        DeleteListNewsView.as_view(), name='list_delete_posts',
    ),
    path(
        'news/<int:pk>/delete',
        DeletePostView.as_view(), name='delete_post',
    ),
    path(
        'news/<int:pk>/update',
        UpdatePostView.as_view(), name='update_post',
    ),
    path(
        'news/create_news/',
        CreateNewsView.as_view(), name='create',
    ),
    path(
        'news/about_me/',
        AboutMeView.as_view(), name='about_me',
    ),
    path(
        'news/contact_with_me/',
        contact_me, name='contact',
    ),
    path(
        'news/like_news/',
        like_news, name='like_news',
    ),
    path(
        'news/offer_news/',
        NewsOfferCreate.as_view(), name='offer_news',
    ),
    path(
        'news/offer_list_news/',
        ListNewsOfferView.as_view(), name='offer_list_news',
    ),
    path(
        'news/list_comment_moder/',
        ListCommentsNewsView.as_view(), name='list_comment_moder',
    ),
    path(
        'news/<int:pk>/update_comment',
        UpdateCommentView.as_view(), name='update_comment',
    ),
    path(
        'news/favorite_news/',
        favorite_news_add_remove, name='favorite_news',
    ),
    path(
        'news/my_favorite_news/',
        FavoritesNewsView.as_view(), name='my_favorite_news',
    )
]
