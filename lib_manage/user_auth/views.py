from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from .decorators import authenticated_user
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.models import Group,User
from django.db.models. signals import post_save
from django.dispatch import receiver

def profile(request):
    return render(request, 'profile.html')

@authenticated_user
def user_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.all()[1]
            user.groups.add(group)
            messages.success(request,'Account created successfully!!')
            return redirect("login")
    else:
        form = CreateUserForm()

    context = {'registerform': form}
    return render(request, 'register.html',context = context)

@authenticated_user
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user  = authenticate(request,username=username,password =password)

            if user is not None:
                login(request,user)
                messages.success(request,'logging in...')
                return redirect('dashboard')
            else:
                messages.info(request,'Invalid login details')
    context = {'loginform':form}
    return render(request, 'login.html',context = context)

def user_logout(request):
    logout(request)
    messages.success(request,'logging out!!')
    return redirect('home')

# @receiver(post_save, sender=User)
# def add_to_group(sender, instance, created, ** kwargs):
#     if created:
#         pass