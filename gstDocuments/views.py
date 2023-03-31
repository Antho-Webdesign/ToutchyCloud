from django.views import generic
from django.views.generic import ListView

from .models import Documents


class DocumentsView(ListView):
    queryset = Documents.objects.all()
    template_name = 'documents/home_documents.html'
    context_object_name = 'documents_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        return context


class DocumentDetailsView(generic.DetailView):
    model = Documents
    template_name = 'documents/document_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['documents'] = Documents.objects.all()
        return context
