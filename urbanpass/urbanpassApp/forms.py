from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Rol

ID_ROL_CHOICES = (
    ('', 'Selecciona el rol'),
    (1, 'Cliente'),
    (2, 'Promotor'),
    (3, 'Colaborador'),
)

class UserRegisterForm(forms.ModelForm):
    id_rol = forms.ChoiceField(choices=ID_ROL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='ID Rol')
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'telefono', 'contrasena', 'id_rol']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Email',
            'telefono': 'Telefono',
            'contrasena': 'Contrasena',
            'id_rol': 'ID Rol',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_id_rol(self):
        id_rol = self.cleaned_data.get('id_rol')
        if id_rol:
            return Rol.objects.get(pk=id_rol)
        return None
