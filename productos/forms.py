from django import forms
from .models import Producto

#Podemos crear un formulario para cada modelo que exista
class productoForm(forms.ModelForm):
    #La clase meta (Metainfo del formulario)
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Producto

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'precio', 'imagen','categoria']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre':forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto'
                }
            ),

            'precio': forms.NumberInput(
                attrs={
                    'class': ' form-control',
                    'placeholder': 'Precio'
                }
            ),

            'imagen': forms.URLInput(
                attrs={
                    'class': ' form-control',
                    'placeholder': 'URL de la magen del producto'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }

        #Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'Url de la imagen',
            'categoria':'Categoria del producto'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {'required': 'El nombre es obligatorio'},
            'precio': {'required': 'El precio no puede estar vacio', 'invalid': 'Ingrese un numero valido'}
        }