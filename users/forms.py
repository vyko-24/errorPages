from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
import re
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
    
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
                'pattern': r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$",
                'title': 'Ingrese un correo de UTEZ'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True,
                'maxlength': '50'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos',
                'required': True,
                'maxlength': '50'
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Matrícula',
                'required': True,
                'pattern': r'^[0-9]{5}[A-Z]{2}[0-9]{3}$',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'required': True,
                'min': '17',
                'max': '99'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'required': True,
                'pattern': r'^\d{10}$',
                'title': 'Ingrese un número de teléfono válido de 10 dígitos'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
                'minlength': '8',
                'title': 'Debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
                'required': True
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@utez.edu.mx'):
            raise ValidationError("El correo debe ser de UTEZ")
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^\d{5}[A-Z]{2}\d{3}$', control_number):
            raise ValidationError("La matrícula debe tener el formato: 5 dígitos, 2 letras mayúsculas y 3 dígitos")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not re.match(r'^\d{10}$', tel):
            raise ValidationError("El teléfono debe tener exactamente 10 dígitos")
        return tel

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if not re.search(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$', password1):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres, incluir una letra mayúscula, un número y un carácter especial")
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'required': True,
            'pattern': r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$",
            'title': 'Ingrese un correo válido de UTEZ'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True,
            'minlength': '8'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')  
        if not username.endswith('@utez.edu.mx'):
            raise ValidationError("El correo debe ser de la UTEZ")
        return username
    
    def clean_password(self):  # Cambié el nombre de clean_password1 a clean_password
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula")
        if not re.search(r'[0-9]', password):
            raise ValidationError("La contraseña debe contener al menos un número")
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial")
        return password

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Usuario o contraseña incorrectos.")

        return cleaned_data