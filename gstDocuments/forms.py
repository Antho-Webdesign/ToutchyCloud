from django import forms
from .models import Documents


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['nom', 'description', 'type', 'mots_cles', 'tag', 'file_upload', 'preview']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'type': forms.Select(attrs={'class': 'form-select'}),
            'mots_cles': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'tag': forms.Select(attrs={'class': 'form-select'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
            'preview': forms.Select(attrs={'class': 'form-select'}),
        }
