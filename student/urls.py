from . import views
from django.urls import path

urlpatterns = [
    path('student', views.student, name="student"),
    path('logout', views.logout, name="logout"),
]