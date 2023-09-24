from django import forms
from .models import RemiderModel

class RemindersForm(forms.ModelForm):
    class Meta:
        model=RemiderModel
        fields="__all__"