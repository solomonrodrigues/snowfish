from django.contrib import admin
from .models import LatestRelease


@admin.register(LatestRelease)
class LatestReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'status')
    readonly_fields = ('status',)
