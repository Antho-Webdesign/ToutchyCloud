from django.urls import path

from gstTasks.views import liste_taches, tache_details

urlpatterns = [
    path('liste-taches/', liste_taches, name='liste_taches'),
    path('tache-details/<slug:slug>/', tache_details, name='tache_details'),


]