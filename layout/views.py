from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from tour.models import TourDate
from snowfishapp.models import LatestRelease


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = timezone.now().date()

        # Query the TourDate objects, filter for the next 10 dates after the current date
        upcoming_dates = TourDate.objects.filter(date__gte=current_date).order_by('date')[:10]

        # Pass the upcoming dates to the template context
        context['upcoming_dates'] = upcoming_dates

        context['latest_release'] = LatestRelease.objects.order_by('-release_date').first()

        return context


class About(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'contact.html'


def handle_404(request, exception):
    return render(request, '404.html', status=404)


def handle_500(request):
    return render(request, '500.html', status=404)
