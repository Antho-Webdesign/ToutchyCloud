from django.views import generic

from .models import Documents


class DocumentsView(generic.ListView):
    queryset = Documents.objects.all()
    template_name = 'documents/home_documents.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['documents'] = Documents.objects.all()
        return context
