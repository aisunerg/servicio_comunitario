from django import forms
from .models import AuthUser




class LoginForm(forms.Form):

    email = forms.EmailField(label="Correo Electronico")
    password = forms.CharField(widget=forms.PasswordInput())
    # forms.PasswordInput

    # class Meta:
    #     model = AuthUser
    #     fields = ['email', 'password']
    #     widgets = {
    #         'email': forms.EmailField(attrs={'placeholder' : 'Escribe tu correo'}),
    #         'password': forms.PasswordInput(attrs={'placeholder' : 'Escribe tu correo'})
    #     }