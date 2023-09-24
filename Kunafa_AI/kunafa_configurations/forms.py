from django import forms
from .models import IPCamera

class IPCameraForm(forms.ModelForm):
    class Meta:
        model=IPCamera
        fields="__all__"