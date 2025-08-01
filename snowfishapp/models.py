from django.db import models
from django.utils import timezone


class LatestRelease(models.Model):
    title = models.CharField()
    release_date = models.DateField()
    streaming_link = models.URLField(null=True, blank=True)

    @property
    def status(self):
        if not self.release_date:
            return "undetermined"
        if self.release_date <= timezone.localdate():
            return "released"
        return "unreleased"
