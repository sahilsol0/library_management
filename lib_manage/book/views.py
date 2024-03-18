from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import CreateBookForm
from django.contrib import messages
from django.http import HttpRequest,HttpResponse
from .models import Book, Author, BookAuthor
from .decorators import user_is_librarian

# Create your views here.
@login_required(login_url = 'login')
def view_book_all(request):
    all_books = Book.objects.all()
    context = {'allbooks':all_books,}
    return render(request, 'view-books.html',context = context)

@login_required(login_url = 'login')
def view_book(request,id):
    context = {
        "book": Book.objects.get(id = id),
    }
    return render(request, 'detail-view-book.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def add_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request,'New Book added..')
            return redirect("/viewbook")
    else:
        form = CreateBookForm()
    context = {'addbookform': form}
    return render(request, 'add-books.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def delete_book(request,id):
    book = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        book.delete()
        return redirect("/viewbook/")
    return render(request, 'delete-books.html',)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def update_book(request,id):
    book = get_object_or_404(Book, id = id)
    form = CreateBookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect("/viewbook/"+id)
    context = {'updatebookform': form}
    return render(request, 'update-books.html',context = context)
