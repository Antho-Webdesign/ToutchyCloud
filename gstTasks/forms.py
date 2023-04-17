from django import forms

from toutchycloud_settings.settings import AUTH_USER_MODEL
from .models import Task, Customer


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Titre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    due_date = forms.DateField(
        label='Date d\'échéance',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    priority = forms.IntegerField(
        label='Priorité',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    status = forms.CharField(
        label='Statut',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    assigned_to = forms.ModelChoiceField(
        label='Assigné à',
        queryset=Customer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = "__all__"
