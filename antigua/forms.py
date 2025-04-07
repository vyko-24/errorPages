from django import forms
from .models import Antigua

class AntiguoForm(forms.ModelForm):
    class Meta:
        model = Antigua
        fields=['nombre','descripcion']

        widgets = {
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre'
                }
            ),
            'descipcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Descripción'
                }
            ),
        }

        labels={
            'nombre':'Nombre',
            'descripcion':'Descripción'
        }

        error_mesagges={
            'nombre':{'required','El nombre es obligatorio'},
            'descripcion':{'required','La descripción es obligatoria'}
        }