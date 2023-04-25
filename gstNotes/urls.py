from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('<str:slug>/', NoteDetailView.as_view(), name='note_detail'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('<slug:slug>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('<slug:slug>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
