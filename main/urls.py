from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name="main"),
    path('detail/<int:lecture_id>/', views.detail, name="detail"),
]
