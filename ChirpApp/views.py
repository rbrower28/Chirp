from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .models import Post
from .forms import CommentForm, LoginForm, PostForm

# Create your views here.


class HomePageView(View):

    def get(self, request):
        posts = Post.objects.all().order_by("-date")

        context = {
            "posts": posts,
            "post_form": PostForm(),
        }
        return render(request, "ChirpApp/index.html", context)

    def post(self, request):
        posts = Post.objects.all().order_by("-date")
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user.get_username()
            post.save()

            return HttpResponseRedirect(reverse("home"))
        
        context = {
            "posts": posts,
            "post_form": post_form,
        }
        return render(request, "ChirpApp/post-detail.html", context)


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("id"),
        }
        return render(request, "ChirpApp/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user.get_username()
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
    template_name = 'ChirpApp/registration/login.html'
    from_class = LoginForm

    # def get_success_url(self):

    #     return super().get_success_url()

    # def post(self, request):
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #     else:
    #         print("oops")
    #         context = {"error": "Invalid username or password"}
    #         return render(request, 'ChirpApp/registration/login.html', context)


# class UserLogout(LogoutView):
#     template_name = 'ChirpApp/temlpates/index.html'
    