from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]

#appending url paths for media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#MEDIA_ROOT is where we send user uploaded content & MEDIA_URL to saccess that content.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#STATIC_ROOT is where all static files will be collected when we run collectstatic command 
#in production & STATIC_URL to access those static files. DEBUG = FALSE