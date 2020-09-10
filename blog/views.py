from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm


def index(request):
    posts = Post.objects.all()
    paginator=Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render (request,"blog/listPosts.html", {"posts":posts})


def showPost(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request, "blog/showPost.html", {"post":post})