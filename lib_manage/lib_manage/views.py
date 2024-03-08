from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def home_page(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('dashboard')

def about_page(request):
    return render(request, 'about.html')

@login_required(login_url = 'login')
def dashboard_view(request):
    return render(request, 'dashboard.html')