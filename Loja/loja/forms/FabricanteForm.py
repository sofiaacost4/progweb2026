from django.forms import ModelForm
from django import forms
from loja.models.Fabricante import Fabricante

class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['Fabricante']
        widgets = {'Fabricante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o nome do fabricante'}),}
        labels = {'Fabricante': 'Fabricante',}
