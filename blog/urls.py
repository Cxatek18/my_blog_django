from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = "news.views.handling_error_404"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('', include('user.urls')),
    path('', include('my_portfolio.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
