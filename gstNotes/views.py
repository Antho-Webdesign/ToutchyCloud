from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Note


# Vue qui affiche la liste des notes
class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


# Vue qui affiche les détails d'une note
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


# Vue qui permet de créer une nouvelle note
@method_decorator(login_required, name='dispatch')
class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)


# Vue qui permet de modifier une note existante
@method_decorator(login_required, name='dispatch')
class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note_update.html'
    fields = ['title', 'content', 'category']
    context_object_name = 'note'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'slug': self.object.slug})


# Vue qui permet de supprimer une note existante
@method_decorator(login_required, name='dispatch')
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
    context_object_name = 'note'
