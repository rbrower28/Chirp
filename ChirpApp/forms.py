from django import forms
from requests import post

from .models import Comment, Post

# Forms go here.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["slug"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "author"]
        labels = {
            "content": ""
        }