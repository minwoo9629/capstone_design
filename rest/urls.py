from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import urls
router = DefaultRouter()
# router.register('main', views.UserViewSet)
urlpatterns = [
    path('rest', include(router.urls)),
<<<<<<< HEAD
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('stdlect/', views.UserLectureData.as_view()),
    path('attend/', views.AttendData.as_view()),
    path('facial_attend/', views.Facial_AttendData.as_view()),
=======
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('stdlect/', views.UserLectureData.as_view()),
    path('attend/', views.AttendData.as_view()),
    path('facial_attend/', views.Facial_AttendData.as_view()),
    path('lecture/', views.LectureData.as_view()),
    path('final_result/', views.FinalResultData.as_view()),
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
    path('log/', views.UserLogData.as_view()),
]