from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10


class ContactCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'contact/contact_form.html'
    fields = ['nom', 'prenom', 'image_prfl', 'email', 'telephone', 'adresse', 'ville', 'pays', 'date_de_naissance',
              'notes']
    success_url = reverse_lazy('contact_list')
    success_message = "Le contact a été créé avec succès."


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'
    context_object_name = 'contact'


class ContactUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Contact
    template_name = 'contact/contact_update.html'
    fields = ['nom', 'prenom', 'image_prfl', 'email', 'telephone', 'adresse', 'ville', 'pays', 'date_de_naissance',
              'notes']
    success_message = "Le contact a été mis à jour avec succès."

    def get_success_url(self):
        return reverse_lazy('contact_detail', kwargs={'slug': self.object.slug})


class ContactDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Contact
    template_name = 'contact/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')
    success_message = "Le contact a été supprimé avec succès."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ContactDeleteView, self).delete(request, *args, **kwargs)
