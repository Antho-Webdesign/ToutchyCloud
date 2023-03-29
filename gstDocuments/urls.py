from django.urls import path

from gstDocuments.views import DocumentsView, DocumentDetailsView

urlpatterns = [
    path('documents-view/', DocumentsView.as_view(), name='gallery-doc-view'),
    path('documents-details/<slug:slug>', DocumentDetailsView.as_view(), name='details-doc'),
]
