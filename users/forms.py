from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                    'required': True,
                    'pattern': '^[0-9]{5}tn[0-9]{3}@utez\\.edu\\.mx$',  # Expresión corregida
                    'title': 'Debe ser un correo institucional (ejemplo: 12345tn678@utez.edu.mx)'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre completo',
                    'required': True,
                    'maxlength': '100',
                    'title': 'Máximo 100 caracteres'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'required': True,
                    'maxlength': '100',
                    'title': 'Máximo 100 caracteres'
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de control',
                    'required': True,
                    'pattern': "^[0-9]{5}tn[0-9]{3}$",
                    'title': 'Debe seguir el formato: 12345tn678'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': '15',
                    'max': '100',
                    'title': 'Debe tener entre 15 y 100 años'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'pattern': '^[0-9]{10}$',
                    'title': 'Debe contener exactamente 10 dígitos'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'pattern': '^(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$',
                    'title': 'Debe tener al menos 8 caracteres, 1 número, 1 mayúscula y 1 carácter especial (@$!%*?&)'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirme su contraseña',
                    'required': True,
                    'title': 'Debe coincidir con la contraseña'
                }
            )
        }
        
class CustomUserLoginForm(AuthenticationForm):
    email = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data

    
class CustomRegisterForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", max_length=150)
    name = forms.CharField(label="Nombre", max_length=100)
    surname = forms.CharField(label="Apellidos", max_length=100)
    control_number = forms.CharField(label="Número de control", max_length=10)
    age = forms.IntegerField(label="Edad")
    tel = forms.CharField(label="Teléfono", max_length=10)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$", email):
            raise forms.ValidationError("Debe ser un correo institucional (ejemplo: 12345tn678@utez.edu.mx)")
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^[0-9]{5}tn[0-9]{3}$", control_number):
            raise forms.ValidationError("Debe seguir el formato: 12345tn678")
        return control_number
    
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 15 or age > 100:
            raise forms.ValidationError("Debe tener entre 15 y 100 años")
        return age
    
    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not re.match(r"^[0-9]{10}$", tel):
            raise forms.ValidationError("Debe contener exactamente 10 dígitos")
        return tel
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not re.match(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$", password1):
            raise forms.ValidationError("Debe tener al menos 8 caracteres, 1 número, 1 mayúscula y 1 carácter especial (@$!%*?&)")
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data
    

