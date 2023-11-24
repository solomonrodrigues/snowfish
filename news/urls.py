from django.urls import path

from . import views
from .views import News

urlpatterns = [
    path("", News.as_view(), name="news"),
]
