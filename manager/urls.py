from . import views
from django.urls import path

urlpatterns = [
    path('manager', views.manager, name="manager"),
    path('logout', views.logout, name="logout"),
]