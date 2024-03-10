from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.forms import PasswordResetForm

form_style = "bg-color60 w-full text-xl p-1 rounded"

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']

        widgets = {
            "username": TextInput(
                attrs={
                    "class": form_style,
                    "placeholder": "johnDoe45",
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class": form_style,
            "placeholder": "John",
        })
        self.fields["last_name"].widget.attrs.update({
            "class": form_style,
            "placeholder": "Doe",
        })
        self.fields["email"].widget.attrs.update({
            "class": form_style,
            "placeholder": "johndoe@anymail.com",
        })
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
           "class": form_style,
        })

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={
        'class': form_style,
        'placeholder': 'registered email',
        'type': 'email',
        'name': 'email',
        }))