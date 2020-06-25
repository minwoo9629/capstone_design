from . import views
from django.urls import path

urlpatterns = [
    path('prof', views.prof, name="prof"),
    path('logout', views.logout, name="logout"),
    path('prof/<int:lecture_id>/', views.detail, name="prof_detail"),
    path('prof/<int:lecture_id>/date/', views.detail, name='prof_date'),
    path('prof/<int:lecture_id>/<username>/<date>', views.show_detail, name='show'),
]