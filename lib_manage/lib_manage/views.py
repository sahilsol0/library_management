from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'home.html')

@login_required(login_url = 'login')
def dashboard_view(request):
    return render(request, 'dashboard.html')