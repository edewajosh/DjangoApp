from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
  #return HttpResponse('HELLO FROM POSTS')

  posts = Posts.objects.all().order_by('-created_at')[:6]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)

def articles(request):
    posts = Posts.objects.all().order_by('-created_at')
    context = {
        'title' : 'All Articles',
        'posts' : posts
    }
    return render(request, 'posts/articles.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)
