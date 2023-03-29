from django.urls import path

from gstDocuments.views import DocumentsView, DocumentDetailsView, pdf_to_image

urlpatterns = [
    path('documents-view/', DocumentsView.as_view(), name='gallery-doc-view'),
    path('documents-details/<slug:slug>/', DocumentDetailsView.as_view(), name='details-doc'),
    path('pdf_to_image/<path:pdf_file>/', pdf_to_image, name='pdf_to_image'),
]
