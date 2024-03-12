from django.db import models
from book.models import Book
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Transaction(models.Model):
    student_id = models.ForeignKey(User, on_delete = models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete = models.CASCADE)
    issued_date = models.DateField(auto_now=False, auto_now_add=False,default = datetime.date(1999,1,1))
    returned_date = models.DateField(auto_now=False, auto_now_add=False,null = True)
    late_fee = models.IntegerField(default = 0)