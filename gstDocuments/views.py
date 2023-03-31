from io import BytesIO

from PIL import Image
from pathlib import Path
from django.http import HttpResponse
from django.views import generic
from pdf2image import convert_from_path

from .models import Documents


def pdf_to_image(request, pdf_file, filename):
    print(filename)
    pages = convert_from_path(pdf_file)
    print(pdf_file)
    print(pages)
    for i, page in enumerate(pages):
        img_io = BytesIO()
        page.save(img_io, 'JPEG')
        img_io.seek(0)
        img = Image.open(img_io)
        file_path = Path(filename).with_suffix(f".{i}.jpg")
        print("**********", filename, "**********")
        img.save(file_path)


class DocumentsView(generic.ListView):
    print(pdf_to_image)
    queryset = Documents.objects.all()
    template_name = 'documents/home_documents.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['documents'] = Documents.objects.all()
        return context


class DocumentDetailsView(generic.DetailView):
    model = Documents
    template_name = 'documents/document_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['photo_list'] = Documents.objects.all()
        return context