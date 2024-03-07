from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']

        widgets = {
            "username": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300",
                    "placeholder": "username",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300",
                    "placeholder": "youremail@somemail.com",
                }
            ),
            "password1": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300",
                    "placeholder": "enter password",
                }
            ),
            "password2": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300",
                    "placeholder": "confirm password",
                }
            ),
        }


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True,max_length=254)
    class Meta:
        model = User
        fields = ("email")