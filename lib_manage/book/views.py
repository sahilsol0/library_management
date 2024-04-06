from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import CreateBookForm, CreateAuthorForm,CreateCategoryForm,CreatePublisherForm
from django.contrib import messages
from django.http import HttpRequest,HttpResponse
from .models import Book, Author, BookAuthor,Publisher,Category
from .decorators import user_is_librarian
import pandas as pd
import json
from django.db.models import Q
from django.views.generic import ListView


# Create your views here.
@login_required(login_url = 'login')
def view_book_all(request):
    query = request.GET.get('search')
    if query:
        all_books = Book.objects.filter( Q(title__icontains = query) | Q(ISBN__icontains = query) | Q(language__icontains = query) | Q(added_date__icontains = query))
    else:
        all_books = Book.objects.all().order_by("-added_date")
    context = {'allbooks':all_books,}
    return render(request, 'view-books.html',context = context)

@login_required(login_url = 'login')
def view_book(request,id):
    context = {
        "book": Book.objects.get(id = id),
        "author": Author.objects.filter(books = id).values(),
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
    context = {'title': 'Book', 'item':book.title}
    if request.method == 'POST':
        book.delete()
        return redirect("/viewbook/")
    return render(request, 'delete-page.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def update_book(request,id):
    book = get_object_or_404(Book, id = id)
    form = CreateBookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect("/viewbook/"+id)
    context = {'form': form,'title':'Book'}
    return render(request, 'update-page.html',context = context)

#crud for Author model
@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def view_author_all(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CreateAuthorForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'New Author added..')
    else:
        form = CreateAuthorForm()
    all_authors = Author.objects.all()
    context = {'allauthors':all_authors,'addauthorform': form}
    return render(request, 'view-authors.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def delete_author(request,id):
    author = get_object_or_404(Author, id = id)
    context = {'title': 'Author', 'item':author.name}
    if request.method == 'POST':
        author.delete()
        return redirect("/viewauthor/")
    return render(request, 'delete-page.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def update_author(request,id):
    author = get_object_or_404(Author, id = id)
    form = CreateAuthorForm(request.POST or None, instance = author)
    if form.is_valid():
        form.save()
        return redirect("/viewauthor/")
    context = {'form': form,'title':'Author'}
    return render(request, 'update-page.html',context = context)

#crud for Publisher model
@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def view_publisher_all(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CreatePublisherForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Publisher added..')
    else:
        form = CreatePublisherForm()
    all_publishers = Publisher.objects.all()
    context = {'allpublishers': all_publishers,'addpublisherform': form}
    return render(request, 'view-publishers.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def delete_publisher(request,id):
    publisher = get_object_or_404(Publisher, id = id)
    context = {'title': 'Publisher', 'item':publisher.name}
    if request.method == 'POST':
        publisher.delete()
        return redirect("/viewpublisher/")
    return render(request, 'delete-page.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def update_publisher(request,id):
    publisher = get_object_or_404(Publisher, id = id)
    form = CreatePublisherForm(request.POST or None, instance = publisher)
    if form.is_valid():
        form.save()
        return redirect("/viewpublisher/")
    context = {'form': form,'title':'Publisher'}
    return render(request, 'update-page.html',context = context)

#crud for Category model
@login_required(login_url = 'login')
def view_category_all(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Category added..')
    else:
        form = CreateCategoryForm()
    all_categories = Category.objects.all()
    context = {'allcategories':all_categories,'addcategoryform': form}
    return render(request, 'view-categories.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def delete_category(request,id):
    category = get_object_or_404(Category, id = id)
    context = {'title': 'Category', 'item':category.name}
    if request.method == 'POST':
        category.delete()
        return redirect("/viewcategory/")
    return render(request, 'delete-page.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def update_category(request,id):
    category = get_object_or_404(Category, id = id)
    form = CreateCategoryForm(request.POST or None, instance = category)
    if form.is_valid():
        form.save()
        return redirect("/viewcategory/")
    context = {'form': form,'title':'Category'}
    return render(request, 'update-page.html',context = context)

@login_required(login_url = 'login')
def downloads(request):
    df = pd.read_csv("static/downloadbook.csv")
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'books': data }
    return render(request, 'downloads.html', context)
    