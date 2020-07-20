from django import forms
from .models import CVModel


class CVForm(forms.ModelForm):
    class Meta:
        model=CVModel
        fields="__all__"
