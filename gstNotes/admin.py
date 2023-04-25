from django.contrib import admin

from gstNotes.models import Note, Category

admin.site.register(Category)
admin.site.register(Note)