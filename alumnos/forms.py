from django import forms
from .models import Alumnos

#Podemos crear un formulario para cada modelo que exista
class alumnoForm(forms.ModelForm):
    #La clase meta (Metainfo del formulario)
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Alumnos

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre':forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'apellido':forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }
            ),

            'edad': forms.NumberInput(
                attrs={
                    'class': ' form-control',
                    'placeholder': 'Edad'
                }
            ),
            'matricula':forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Matricula'
                }
            ),
            'correo':forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Correo'
                }
            ),
        }

        #Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre',
            'apellido':'Apellido',
            'edad': 'Edad',
            'matricula':'Matricula',
            'correo': 'Correo'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {'required': 'El nombre es obligatorio'},
            'apellido': {'required': 'El apellido es obligatorio'},
            'edad': {'required': 'La edad es obligatoria', 'invalid': 'Ingrese un numero valido'},
            'matricula': {'required': 'La matricula es obligatorio'},
            'correo': {'required': 'El correo es obligatorio'},
        }