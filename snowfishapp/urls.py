from django.urls import path
from .views import MusicView, PhotosView, VideosView

urlpatterns = [
    path('music/', MusicView.as_view(), name='music'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('videos/', VideosView.as_view(), name='videos'),
]
