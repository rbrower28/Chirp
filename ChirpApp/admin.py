from django.contrib import admin

from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_filter = ("author", "date")
    list_display = ("slug", "date", "author")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)