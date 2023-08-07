from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsPost

# Create your views here.


class News(ListView):
    model = NewsPost
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_posts'] = self.get_queryset()
        return context
