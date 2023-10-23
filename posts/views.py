from django.shortcuts import render
from .models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all()
    return(render(request, 'index.html', {'posts':posts}))

def post(request, slug):
    posts = Posts.objects.get(slug = slug)
    return(render(request, 'post.html', {'posts': posts}))

def posts(request):
    posts = Posts.objects.all()
    return(render(request, 'posts.html', {'posts':posts}))