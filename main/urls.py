from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('main', views.UserViewSet)

urlpatterns = [
    path('', views.main, name="main"),
    path('index', views.index, name="index"),
    path('rest', include(router.urls)),
]
