from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

@login_required(login_url = 'home')
def dashboard_view(request):
    return render(request, 'dashboard.html')