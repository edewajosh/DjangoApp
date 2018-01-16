from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', include('posts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
