from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
# from django.http import HttpResponse
from .models import Post


def say_hello(request):
    return render(request, 'index.html', {'name': 'Waleed'})
    # return HttpResponse("Hello you are seeing a test app")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


# class PostView(View):
#     def __init__(self, **kwargs: Any) -> None:
#         super().__init__(**kwargs)
#         self.posts = Post.objects.all()

#     def post_list(self, request):
#         return render(request, 'posts.html', {'posts': self.posts})


# class PostView(ListView):
#     model = Post
#     template_name = 'apptest/posts.html'
#     context_object_name = 'posts'
