from django.urls import path

from gstPhotos.views import GalleryView, GalleryDetailView

urlpatterns = [
    path('galleryview/', GalleryView.as_view(), name='gallery-view'),
    path('details-view/<slug:slug>/', GalleryDetailView.as_view(), name='img-details-view'),
]