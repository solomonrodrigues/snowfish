from django.contrib import admin
from .models import BlogPost, Paragraph

# Register your models here.


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ['id', 'title', "timestamp", "has_image", "paragraph_count"]
    inlines = [ParagraphInline]

    def has_image(self, obj):
        return obj.image is not None
    has_image.boolean = True
    has_image.short_description = 'Has Image'

    def paragraph_count(self, obj):
        return obj.paragraphs.count()
    paragraph_count.short_description = 'Number of Paragraphs'


admin.site.register(BlogPost, BlogPostAdmin)
