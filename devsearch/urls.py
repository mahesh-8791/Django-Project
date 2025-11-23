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