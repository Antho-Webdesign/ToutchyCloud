from django.urls import path
from .views import ContactListView, ContactCreateView, ContactDetailView, ContactUpdateView, ContactDeleteView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('ajouter/', ContactCreateView.as_view(), name='contact_create'),
    path('<slug:slug>/', ContactDetailView.as_view(), name='contact_detail'),
    path('<slug:slug>/modifier/', ContactUpdateView.as_view(), name='contact_update'),
    path('<slug:slug>/supprimer/', ContactDeleteView.as_view(), name='contact_delete'),
]
