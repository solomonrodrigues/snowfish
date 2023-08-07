from django.db import models

# Create your models here.

class NewsPost(models.Model)
	title = models.CharField()
	text = models.TextField()
	timestamp = models.DateTimeField()

	class Meta:
        verbose_name = "News Post"
        verbose_name_plural = "News Posts"
