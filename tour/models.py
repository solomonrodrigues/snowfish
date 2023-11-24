from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class TourDate(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="This will automatically generate.")
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

    def save(self, *args, **kwargs):
        # just check if name or location.name has changed
        self.slug = '-'.join((slugify(self.title), slugify(self.date)))
        super(TourDate, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tour-date", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Tour Date"
        verbose_name_plural = "Tour Dates"
