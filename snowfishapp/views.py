from django.shortcuts import render
from django.views.generic import TemplateView
from .constants import RELEASES


class MusicView(TemplateView):
    template_name = 'music.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['releases'] = RELEASES
        return context


class PhotosView(TemplateView):
    template_name = 'photos.html'


class VideosView(TemplateView):
    template_name = 'videos.html'
