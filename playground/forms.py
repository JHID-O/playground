from django import forms
from .models import PlaygroundModel

class PlaygroundModelForm(forms.ModelForm):
    class Meta:
        model = PlaygroundModel
        fields = '__all__'