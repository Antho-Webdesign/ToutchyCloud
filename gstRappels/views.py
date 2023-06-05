from django.shortcuts import render

from gstRappels.models import Rappel


# Create rappel views here.
def liste_rappels(request):
    rappels = Rappel.objects.all()
    context = {
        'rappels': rappels,
    }
    return render(request, 'rappels/liste_rappels.html', context)


def rappel_details(request, slug):
    rappel = Rappel.objects.get(slug=slug)
    context = {
        'rappel': rappel,
    }
    return render(request, 'rappels/rappel_details.html', context)

