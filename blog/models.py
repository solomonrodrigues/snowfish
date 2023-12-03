from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateField()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def has_paragraphs(self):
        return Paragraph.objects.filter(blog_post=self).exists()


class Paragraph(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='paragraphs')
    text = models.TextField()
