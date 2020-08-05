from . import views
from django.urls import path

urlpatterns = [
    path('setting/<int:lecture_id>', views.setting, name="setting_lecture"),
]