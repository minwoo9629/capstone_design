from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name="main"),
    path('', include('attendance.urls')),
]
