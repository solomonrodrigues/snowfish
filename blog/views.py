from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

# Create your views here.


class Blog(ListView):
    model = BlogPost
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = self.get_queryset()
        return context
