from django import forms
from .models import Crud

class crudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['nombre','descripcion']

        widgets = {
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Un nombre'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'forms-control',
                    'placeholder':'Una descripción'
                }
            )
        }
        labels = {
            'nombre=':'Un nombre',
            'descripcion':'Una descripción'
        }

        error_messages={
            'nombre':{'required':'el nomre es necesario'},
            'descripcion':{'required':'la descripción es necesaria'}
        }