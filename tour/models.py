from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib import admin


# Create your models here.


class TourDate(models.Model):
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True, help_text="Optional")
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default='Newcastle')
    country = models.CharField(max_length=100, default='Australia')
    ticket_url = models.URLField(null=True, blank=True, help_text="Optional")
    supports = models.CharField(max_length=200, null=True, blank=True, help_text="Optional")
    description = models.TextField(null=True, blank=True, help_text="Optional")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave empty. This will automatically generate.")

    def __str__(self):
        return f'{self.venue}, {self.date}'

    def save(self, *args, **kwargs):
        # just check if name or location.name has changed
        self.slug = '-'.join((slugify(self.venue), slugify(self.date)))
        super(TourDate, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tour-date", kwargs={"slug": self.slug})

    @admin.display(boolean=True)
    def has_ticket_link(self):
        return bool(self.ticket_url)

    class Meta:
        verbose_name = "Tour Date"
        verbose_name_plural = "Tour Dates"
