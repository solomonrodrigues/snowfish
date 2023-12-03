from django.views.generic import ListView, DetailView
from .models import TourDate
from django.utils import timezone

# Create your views here.


class TourDatesView(ListView):
    model = TourDate
    template_name = 'tour-dates.html'
    context_object_name = 'tour_dates'
    ordering = ['date']

    def get_queryset(self):
        # Filter out dates that are before today
        return super().get_queryset().filter(date__gte=timezone.now().date()).order_by(*self.ordering)


class TourDateView(DetailView):
    model = TourDate
    template_name = 'tour-date.html'
