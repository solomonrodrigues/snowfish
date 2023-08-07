from django.urls import path

from . import views
from .views import News

urlpatterns = [
    path("news/", News.as_view(), name="news"),
]