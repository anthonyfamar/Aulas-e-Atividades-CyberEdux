from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('feed', views.feed),
    path('publicate', views.publicate),
    path('artigo/<int:post_id>', views.artigo, name='artigo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)