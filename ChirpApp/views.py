from distutils.log import Log
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView 
from django.contrib import messages

from .models import Post
from .forms import CommentForm

# Create your views here.


class HomePageView(ListView):
    template_name = "ChirpApp/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:10]
        return data


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, "ChirpApp/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, "ChirpApp/post-detail.html", context)


# def user_login(request):
#     return render(request, 'ChirpApp/authentication/login.html', {})


class UserLogin(LoginView):
    template_name = 'registration/login.html'
