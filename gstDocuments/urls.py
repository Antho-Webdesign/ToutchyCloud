from django.urls import path

from gstDocuments.views import DocumentsView, DocumentDetailsView, DocumentUpdateView, DocumentDeleteView

urlpatterns = [
    path('documents-view/', DocumentsView.as_view(), name='gallery-doc-view'),
    path('documents-details/<slug:slug>/', DocumentDetailsView.as_view(), name='details-doc'),
    path('documents/<int:pk>/edit/', DocumentUpdateView.as_view(), name='document_edit'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),
    # path('pdf_to_image/', pdf_to_image, name='pdf_to_image'),
]
