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
        queryset = super().get_queryset()
        filter_option = self.request.GET.get('filter', 'upcoming')

        if filter_option == 'past':
            # Show past tour dates
            return queryset.filter(date__lt=timezone.localdate()).order_by(*self.ordering)
        else:
            # Default to showing upcoming tour dates
            return queryset.filter(date__gte=timezone.localdate()).order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add context to show or hide ticket links
        filter_option = self.request.GET.get('filter', 'upcoming')
        context['show_tickets'] = (filter_option != 'past')
        return context


class TourDateView(DetailView):
    model = TourDate
    template_name = 'tour-date.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the tour date is in the future (for single tour date view)
        tour_date = self.object.date
        context['show_tickets'] = tour_date >= timezone.localdate()
        return context
