from django.shortcuts import render
from django.urls import path


from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"), #/
    path("<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"), #/12345
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout")
]
