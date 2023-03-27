from django.shortcuts import render
from django.views import generic

from gstPhotos.models import Photos


# Create your views here.
def gallery(request):
    photos = Photos.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'gstPhotos/gallery.html', context)


class GalleryView(generic.ListView):
    queryset = Photos.objects.all()
    model = Photos
    template_name = 'gstPhotos/gallery.html'
    context_object_name = 'latest_img'

    def get_queryset(self):
        """Return the last five published questions."""
        return Photos.objects.all()


class GalleryDetailView(generic.DetailView):
    model = Photos
    template_name = 'gstPhotos/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['photo_list'] = Photos.objects.all()
        return context
