from django.contrib import admin
from .models import TourDate

# Register your models here.


class TourDateAdmin(admin.ModelAdmin):
    model = TourDate
    list_display = ['id', 'title', "date", "city", "venue"]


admin.site.register(TourDate, TourDateAdmin)