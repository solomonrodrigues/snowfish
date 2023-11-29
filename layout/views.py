from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the layout index.")


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings_name'] = settings.SETTINGS_NAME
        context['base_used'] = settings.BASE_USED
        context['development_used'] = settings.DEVELOPMENT_USED
        context['production_used'] = settings.PRODUCTION_USED
        return context

