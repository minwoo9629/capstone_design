from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import urls
router = DefaultRouter()
# router.register('main', views.UserViewSet)
urlpatterns = [
    path('rest', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('stdlect/', views.UserLectureData.as_view()),
    path('attend/', views.AttendData.as_view()),
    path('lecture/', views.LectureData.as_view()),
]