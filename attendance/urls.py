from . import views
from django.urls import path, include

urlpatterns = [
    path('attend/<str:attend_time>/', views.detail, name="attend_detail"),
]