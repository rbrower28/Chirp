from django.contrib import admin

from .models import User, Post, Comment

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("username",)}

class PostAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_filter = ("author", "date")
    list_display = ("slug", "date", "author")


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)