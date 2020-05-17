from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.main, name="main"),
    path('index', views.index, name="index"),
    path('', include('attendance.urls')),
    
]
