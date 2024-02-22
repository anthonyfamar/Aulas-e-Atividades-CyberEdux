from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('feed', views.feed),
    path('publicate', views.publicate),
    path('artigo/<int:post_id>', views.artigo, name='artigo'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('login', views.login_view),
    path('logout/', views.logout_view),
    path('cadastro', views.cadastro),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)