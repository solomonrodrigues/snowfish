from django.urls import path

from . import views
from .views import TourDatesView, TourDateView

urlpatterns = [
    path("", TourDatesView.as_view(), name="tour"),
    path("date/<slug:slug>/", TourDateView.as_view(), name="tour-date"),
]
