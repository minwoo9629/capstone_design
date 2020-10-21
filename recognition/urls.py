from . import views
from django.urls import path, include

urlpatterns = [
    path('recognition', views.recognition, name="recognition"),
]
