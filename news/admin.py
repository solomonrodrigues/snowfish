from django.contrib import admin
from .models import NewsPost

# Register your models here.


class NewsPostAdmin(admin.ModelAdmin):
    model = NewsPost
    list_display = ['id', 'title', "timestamp"]


admin.site.register(NewsPost, NewsPostAdmin)