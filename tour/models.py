from django.db import models


# Create your models here.


class TourDate(models.Model):
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, default='Australia')
    city = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    ticket_url = models.URLField(null=True, blank=True)
    supports = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "TourDates"
