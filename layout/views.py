from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the layout index.")


class Home(TemplateView):
    template_name = 'home.html'
