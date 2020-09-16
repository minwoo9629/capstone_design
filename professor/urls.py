from . import views
from django.urls import path

urlpatterns = [
    path('prof', views.prof, name="prof"),
    path('logout', views.logout, name="logout"),
    path('prof/<int:lecture_id>/', views.detail, name="prof_detail"),
    path('prof/<int:lecture_id>/date/', views.detail, name='prof_date'),
    path('setting/<int:lecture_id>/', views.setting, name="lecture_setting"),
    path('prof/<int:lecture_id>/<username>/<date>', views.show_detail, name='show'),
    path('prof/excel/download/<int:lecture_id>', views.download, name="download"),
    path('prof/record/', views.record, name="record")
]