from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import DocumentForm
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


class DocumentCreateView(CreateView):
    model = Documents
    form_class = DocumentForm
    template_name = 'documents/add_document.html'
    success_url = reverse_lazy('document_details')

    def form_valid(self, form):
        document = form.save(commit=False)
        document.slug = slugify(document.nom)
        document.save()
        return redirect(self.success_url)


class DocumentDetailsView(generic.DetailView):
    model = Documents
    template_name = 'documents/document_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['documents'] = Documents.objects.all()
        return context


class DocumentUpdateView(UpdateView):
    model = Documents
    template_name = 'documents/edit_document.html'
    form_class = DocumentForm

    def form_valid(self, form):
        document = form.save(commit=False)
        document.slug = slugify(document.nom)
        document.save()
        print(document.nom)
        return redirect('document_details', pk=document.pk)


class DocumentDeleteView(DeleteView):
    model = Documents
    success_url = reverse_lazy('gallery-doc-view')
    template_name = 'documents/document_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)
