from django.urls import path

from gstPhotos.views import gallery

urlpatterns = [
    path('gallery/', gallery, name='gallery'),
]
