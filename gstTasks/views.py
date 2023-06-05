from django.shortcuts import render
from  .models import CategoryTasks, Tasks

def liste_taches(request):
    categories_taches = CategoryTasks.objects.all()
    taches = Tasks.objects.all()

    context = {
        'taches': taches,
        'categories_taches': categories_taches,
    }
    return render(request, 'tasks/liste_taches.html', context)


def tache_details(request, slug):
    tache = Tasks.objects.get(slug=slug)
    context = {
        'tache': tache,
    }
    return render(request, 'tasks/tache_details.html', context)




