from django.urls import path

from . import views
from .views import TourDates, TourDate

urlpatterns = [
    path("", TourDates.as_view(), name="tour"),
    path("date/<slug:slug>", TourDate.as_view(), name="tour-date"),
]
