from django.urls import path

from . import views
from .views import TourDates, TourDate

urlpatterns = [
    path("tour/", TourDates.as_view(), name="tour"),
    path("tour-date/<slug:slug>", TourDate.as_view(), name="tour-date"),
]