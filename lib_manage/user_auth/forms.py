from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput

form_style = "bg-color60 w-full text-xl p-1 rounded"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']

        widgets = {
             "first_name": TextInput(
                attrs={
                    "id": "First name",
                    "class": form_style,
                    "placeholder": "first name",
                }
             ),
             "last_name": TextInput(
                attrs={
                    "id": "Last name",
                    "class": form_style,
                    "placeholder": "last name",
                }
             ),
            "username": TextInput(
                attrs={
                    "id": "Username",
                    "class": form_style,
                    "placeholder": "username",
                }
            ),
            "email": TextInput(
                attrs={
                    "id": "Email address",
                    "class": form_style,
                    "placeholder": "youremail@somemail.com",
                }
            ),
            "password1": TextInput(
                attrs={
                    "id": "Password",
                }
            ),
            "password2": TextInput(
                attrs={
                    "id": "Password confirmation",
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            "class": form_style,
        })
        self.fields["password2"].widget.attrs.update({
           "class": form_style,
        })
    
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput(attrs={
                "id": "Username",
                "class": form_style,
                "placeholder": "username",
            }))
    password = forms.CharField(widget = PasswordInput(attrs={
                "id": "Password",
                "class": form_style,
            }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
           "class": form_style,
        })