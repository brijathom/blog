from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("entry_title", "entry_text")

        widgets = {
            "entry_title": forms.TextInput(attrs={"class": "form-control", 'autofocus': 'autofocus'}),
            "entry_text": forms.Textarea(attrs={"class": "form-control"}),
        }
