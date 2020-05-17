from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('manager.urls')),
    path('',include('student.urls')),
    path('',include('professor.urls')),
    path('',include('rest.urls')),
    path('',include('recognition.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
