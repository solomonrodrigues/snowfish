from django.shortcuts import render
from django.views.generic import TemplateView

class MusicView(TemplateView):
    template_name = 'music.html'

class PhotosView(TemplateView):
    template_name = 'photos.html'

class VideosView(TemplateView):
    template_name = 'videos.html'


