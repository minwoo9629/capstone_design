from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
# router.register('main', views.UserViewSet)

urlpatterns = [
    path('', views.main, name="main"),
    path('index', views.index, name="index"),
    path('rest', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('', include('attendance.urls')),
    path('std/', views.UserList.as_view()),
]
