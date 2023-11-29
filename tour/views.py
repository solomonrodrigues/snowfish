from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TourDate

# Create your views here.


class TourDatesView(ListView):
    model = TourDate
    template_name = 'tour-dates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tour_dates'] = self.get_queryset().order_by('-date')
        context['tour_dates'] = [
            {
                'date': '2/12/23',
                'city': 'Newcastle',
                'country': 'AU',
                'venue': 'The Stag and Hunter',
            },
            {
                'date': '13/12/23',
                'city': 'Newcastle',
                'country': 'AU',
                'venue': 'Hamilton Station Hotel',
            },
        ]
        return context


class TourDateView(DetailView):
    model = TourDate
    template_name = 'tour-date.html'
