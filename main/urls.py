from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name="main"),
    path('login_check', views.login_check, name="login_check")
]
