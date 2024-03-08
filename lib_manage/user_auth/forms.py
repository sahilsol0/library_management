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
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "first name",
                }
             ),
             "last_name": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "last name",
                }
             ),
            "username": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "username",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300 text-slate-900",
                    "placeholder": "youremail@somemail.com",
                }
            ),
            "password1": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300 text-slate-900",
                }
            ),
            "password2": TextInput(
                attrs={
                    "class": "border border-solid border-slate-300 text-slate-900",
                }
            ),
        }

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput(attrs={
                "class": "border border-solid border-slate-300 text-slate-900",
                "placeholder": "username",
            }))
    password = forms.CharField(widget = PasswordInput(attrs={
                "class": "border border-solid border-slate-300 text-slate-900",
            }))