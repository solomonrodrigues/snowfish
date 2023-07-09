from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TourDate

# Create your views here.


class TourDates(ListView):
    model = TourDate
    template_name = 'tour-dates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tour_dates'] = self.get_queryset()
        return context


class TourDate(DetailView):
    model = TourDate
    template_name = 'tour-date.html'