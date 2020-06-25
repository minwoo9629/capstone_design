from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import urls
router = DefaultRouter()
# router.register('main', views.UserViewSet)
urlpatterns = [
    path('rest', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('stdlect/', views.UserLectureData.as_view()),
    path('attend/', views.AttendData.as_view()),
    path('facial_attend/', views.Facial_AttendData.as_view()),
    path('log/', views.UserLogData.as_view()),
]