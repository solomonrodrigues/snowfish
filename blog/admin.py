from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ['id', 'title', "timestamp"]


admin.site.register(BlogPost, BlogPostAdmin)