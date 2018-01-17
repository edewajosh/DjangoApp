from django.urls import path
from . import views

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('details/<int:id>/', views.details, name='details'),
  path('articles/', views.articles, name='articles'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
