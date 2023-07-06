from django.shortcuts import render
from django.views.generic import ListView
from .models import TourDate

# Create your views here.


class TourDates(ListView):
    model = TourDate
    template_name = 'tour-dates.html'