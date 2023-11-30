from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
