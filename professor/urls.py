from . import views
from django.urls import path

urlpatterns = [
    path('prof', views.prof, name="prof"),
    path('logout', views.logout, name="logout"),
]