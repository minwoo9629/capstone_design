from . import views
from django.urls import path

urlpatterns = [
    path('prof', views.prof, name="prof"),
    path('logout', views.logout, name="logout"),
<<<<<<< HEAD
    path('prof/<int:lecture_id>/',  views.detail, name="detail"),
=======
    path('prof/<int:lecture_id>/', views.detail, name="prof_detail"),
    path('prof/<int:lecture_id>/date/', views.detail, name='prof_date'),
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
    path('prof/<int:lecture_id>/<username>/<date>', views.show_detail, name='show'),
]