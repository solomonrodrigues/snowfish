from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TourDate

# Create your views here.


class TourDates(ListView):
    model = TourDate
    template_name = 'tour-dates.html'


class TourDate(DetailView):
    model = TourDate
    template_name = 'tour-date.html'