from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the layout index.")


class Home(TemplateView):
    template_name = 'home.html'


def handle_404(request, exception):
    return render(request, '404.html', status=404)


def handle_500(request):
    return render(request, '500.html', status=404)
