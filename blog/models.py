from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
