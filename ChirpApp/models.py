from django.db import models

from django.utils.crypto import get_random_string

# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    FontType = models.TextChoices("FontType", "bold old wild")
    font = models.CharField(choices=FontType.choices, max_length=4)
    slug = models.SlugField(unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = get_random_string(5)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} - posted on {self.date} by {self.author}"


class Comment(models.Model):
    content = models.CharField(max_length=120)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - commented on post {self.post.slug} by {self.post.author}"