from django.urls import path

from . import views
from .views import TourDates

urlpatterns = [
    path("tour/", TourDates.as_view(), name="tour"),
]