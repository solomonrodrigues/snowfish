from django.contrib import admin
from .models import TourDate

# Register your models here.


class TourDateAdmin(admin.ModelAdmin):
    model = TourDate
    list_display = ['id', "date", "city", "venue", "has_ticket_link"]
    exclude = ['slug']


admin.site.register(TourDate, TourDateAdmin)
