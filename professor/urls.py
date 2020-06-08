from . import views
from django.urls import path

urlpatterns = [
    path('prof', views.prof, name="prof"),
    path('logout', views.logout, name="logout"),
    # path('prof/<int:lecture_id>/', views.detail, name="detail"),
]