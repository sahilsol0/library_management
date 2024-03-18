from django.shortcuts import redirect
from django.contrib.auth.models import User

def user_is_librarian(user):
    if user.groups.filter(name = 'librarian').exists():
        return True
    else:
        return False