from django.shortcuts import render

from gstDocuments.models import Documents
from gstPhotos.models import Photos


def home(request):
    photos = Photos.objects.all()
    documents = Documents.objects.all()

    if name := request.GET.get('search'):
        if request.method == 'GET':
            photos = Photos.objects.filter(name__icontains=name)

    if name := request.GET.get('search'):
        if request.method == 'GET':
            documents = Documents.objects.filter(name__icontains=name)

    context = {
        'documents': documents,
        'photos': photos,
    }
    return render(request, 'home.html', context)
