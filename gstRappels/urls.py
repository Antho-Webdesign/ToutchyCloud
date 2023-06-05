from django.urls import path

from gstRappels.views import liste_rappels, rappel_details

urlpatterns = [
    path('liste-rappels/', liste_rappels, name='liste_rappels'),
    path('rappel-details/<slug:slug>/', rappel_details, name='rappel_details'),
]