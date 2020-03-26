from django.urls import path,include
from rest_framework.routers import DefaultRouter
from attendance import views

router = DefaultRouter()
router.register('attend', views.AttendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]