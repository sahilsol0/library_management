from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Transaction, Book, User
from .forms import IssueBookForm
from book.decorators import user_is_librarian
from django.db.models import Q,Sum
from django.db.models.functions import ExtractDay
from django.utils import timezone

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import PageBreak

# Create your views here.
@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def view_transaction(request):
    query = request.GET.get('search')
    if query:
        all_transactions = Transaction.objects.filter(Q(id__icontains = query))
    else:
        all_transactions = Transaction.objects.all().order_by('-issued_date')
    context = {'alltransactions':all_transactions,}
    return render(request, 'view-transactions.html',context = context)

def download_transaction(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = A4, bottomup=0)

    textobj = c.beginText(2,2)
    textobj.setTextOrigin(inch,inch)
    textobj.setFont("Helvetica",14)

    transactions = Transaction.objects.all()
    books = Book.objects.all()
    lines = ['-----TRANSACTIONS-----'," "]
    lines.append(f"Total books in the library: {books.count()}")
    lines.append(f"Total books issued: {transactions.count()}")
    lines.append(f"Total books returned: {transactions.filter(returned_date__isnull = False).count()}")
    lines.append(f"Total dues: {list(transactions.aggregate(Sum('due')).values())[0]} /-")

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True, filename=f'Transaction-{timezone.now()}.pdf')

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def issue_book(request, id):
    book = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            book.count -= 1
            form.save()
            book.save()
            return redirect("/viewtransactions")
    else:
        form = IssueBookForm(initial={
            'book': book,
        })

    context = {'issuebookform':form,}
    return render(request, 'issue-book.html',context=context)

@user_passes_test(user_is_librarian,login_url='login',redirect_field_name='dashboard')
def return_book(request, id):
    transaction = get_object_or_404(Transaction, id = id)
    if not transaction.returned_date:
        form = IssueBookForm(request.POST or None, instance = transaction)
        if form.is_valid():
            transaction.book.count += 1
            form.save()
            transaction.book.save()
            return redirect("/viewtransactions")
        context = {'returnbookform': form,}
        return render(request, 'return-book.html',context=context)
    else:
        return redirect('viewtransactions')