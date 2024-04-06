from django.db import models
from book.models import Book
from django.contrib.auth.models import User
import datetime
from django.db.models.functions import ExtractDay

# Create your models here.
def get_fine(issue_date,returned_date):
        d = (datetime.date(returned_date) - datetime.date(issue_date)).days
        return d

def to_be_returned_by(issued_date):
      pass

class Transaction(models.Model):
    student = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    issued_date = models.DateField(auto_now=False, auto_now_add=False,default = datetime.date(2024,1,1))
    due_date = models.DateField(auto_now=False, auto_now_add=False,default = datetime.date(2024,1,1))
    returned_date = models.DateField(auto_now=False, auto_now_add=False,default= to_be_returned_by(issued_date))
    late_fee = models.IntegerField(null=True)

"""
TODO
make two models borrow and return
borrow
-student id
-staff id
-book id
-issue_date
-due_date

return
-student id
-staff id
-book id
-returned_date
-due_date
-fine

improve this.....👿
"""