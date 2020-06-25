from . import views
from django.urls import path, include

urlpatterns = [
    path('attend/<int:lecture_id>/<str:attend_time>/', views.detail, name="attend_detail"),
]