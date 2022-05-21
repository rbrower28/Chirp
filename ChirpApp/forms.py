from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post

# Forms go here.

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


FONTS = [
    ('bold', 'bold'),
    ('old', 'old'),
    ('wild', 'wild'),
]

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={"class": "bold", "rows": "4", "maxlength": "200", "placeholder": "I think that..."}))
    font = forms.CharField(label='', widget=forms.RadioSelect(choices=FONTS, attrs={}))

    class Meta:
        model = Post
        fields = ["content", "font"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": "3", "maxlength": "120"}))

    class Meta:
        model = Comment
        exclude = ["post", "author"]
        labels = {
            "content": ""
        }