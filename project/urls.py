
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app2', include('app2.urls')),
    path('app3', include('app3.urls')),
    path('app4', include('app4.urls')),
    path('tracking', include('tracking.urls')),
    path('news', include('news.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)