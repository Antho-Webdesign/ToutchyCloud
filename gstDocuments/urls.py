from django.urls import path

from gstDocuments.views import DocumentsView

urlpatterns = [
    path('documents-view/', DocumentsView.as_view(), name='gallery-doc-view'),
]
