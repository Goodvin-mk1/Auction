from django.urls import path, include
from .views import index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('index.html', index)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)