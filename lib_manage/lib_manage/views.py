from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from transaction.models import Transaction
from book.models import Book
from django.contrib.auth.models import User

def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'home.html')

def about_page(request):
    return render(request, 'about.html')

@login_required(login_url = 'login')
def dashboard_view(request):
    context = {
        'issuedbooks':Transaction.objects.filter(student=request.user),
    }
    if request.user.groups.all()[0].name == 'librarian':
        context = {
            'issuedbooks':Transaction.objects.filter(student=request.user),
            'alltransactions': Transaction.objects.all().count(),
            'allbooks': Book.objects.all().count(),
            'allusers': User.objects.all().count(),
        }

    return render(request, 'dashboard.html',context=context)