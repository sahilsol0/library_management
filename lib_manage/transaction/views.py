from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpRequest,HttpResponse
from .models import Transaction
from .forms import IssueBookForm
from book.decorators import user_is_librarian
from django.db.models import Q
from django.db.models.functions import ExtractDay

# Create your views here.
@login_required(login_url='login')
def view_transaction(request):
    all_transactions = Transaction.objects.all()
    context = {'alltransactions':all_transactions,}
    return render(request, 'view-transactions.html',context = context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            Transaction.late_fee = ExtractDay(Transaction.issued_date,Transaction.returned_date)
            return redirect("/viewtransactions")
    else:
        form = IssueBookForm()

    context = {'issuebookform':form}
    return render(request, 'issue-book.html',context=context)