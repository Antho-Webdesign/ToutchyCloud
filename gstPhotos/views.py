from django.shortcuts import render

from gstPhotos.models import Photos


# Create your views here.
def gallery(request):
    photos = Photos.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'gstPhotos/gallery.html', context)
