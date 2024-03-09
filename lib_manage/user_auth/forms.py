from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']

        widgets = {
             "first_name": TextInput(
                attrs={
                    "id": "First name",
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "first name",
                }
             ),
             "last_name": TextInput(
                attrs={
                    "id": "Last name",
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "last name",
                }
             ),
            "username": TextInput(
                attrs={
                    "id": "Username",
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "username",
                }
            ),
            "email": TextInput(
                attrs={
                    "id": "Email address",
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "youremail@somemail.com",
                }
            ),
            "password1": TextInput(
                attrs={
                    "id": "Password",
                    "class": "border border-solid border-slate-300 text-slate-900",
                }
            ),
            "password2": TextInput(
                attrs={
                    "id": "Password confirmation",
                    "class": "border border-solid border-slate-300 text-slate-900",
                }
            ),
        }

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput(attrs={
                "id": "Username",
                "class": "border border-solid border-slate-300 text-slate-900",
                "placeholder": "username",
            }))
    password = forms.CharField(widget = PasswordInput(attrs={
                "id": "Password",
                "class": "border border-solid border-slate-300 text-slate-900",
            }))