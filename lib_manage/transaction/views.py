from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpRequest,HttpResponse
from .models import Transaction, Book
from .forms import IssueBookForm
from book.decorators import user_is_librarian
from django.db.models import Q
from django.db.models.functions import ExtractDay

# Create your views here.
@login_required(login_url='login')
def view_transaction(request):
    query = request.GET.get('search')
    if query:
        all_transactions = Transaction.objects.filter(Q(id__icontains = query) | Q(returned_date__icontains = query))
    else:
        all_transactions = Transaction.objects.all().order_by('-due')
    context = {'alltransactions':all_transactions,}
    return render(request, 'view-transactions.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def issue_book(request, id):
    book = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            print('save')
            form.save()
            return redirect("/viewtransactions")
        else:
            print('book not available')
    else:
        form = IssueBookForm(initial={
            'book': book,
        })

    context = {'issuebookform':form,}
    return render(request, 'issue-book.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def return_book(request, id):
    transaction = get_object_or_404(Transaction, id = id)
    form = IssueBookForm(request.POST or None, instance = transaction)
    if form.is_valid():
        form.save()
        return redirect("/viewtransactions")
    context = {'returnbookform': form,}
    return render(request, 'return-book.html',context=context)