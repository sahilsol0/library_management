from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from datetime import timedelta,date,datetime
from django.db.models.functions import ExtractDay

# Create your models here.
def dueDate(issue_date):
  valid_days = 15
  due_date = issue_date + timedelta(days=valid_days)
  return due_date

def dues(due_date, return_date):
  fine_per_day = 2 #after the due date,returning book a fine calculated 1 rupee each day after the due date untill return
  due = 0
  if return_date >= due_date:
    due = (return_date - due_date).days * fine_per_day
  return due


class Transaction(models.Model):
  student = models.ForeignKey(User, on_delete = models.CASCADE)
  book = models.ForeignKey(Book, on_delete = models.CASCADE)
  issued_date = models.DateField(auto_now=False, auto_now_add=False,default = datetime.now())
  due_date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
  returned_date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
  due = models.IntegerField(null=True,blank=True)

  def save(self,*args, **kwargs):
    self.due_date = dueDate(self.issued_date)
    if self.returned_date:
      self.due = dues(self.due_date, self.returned_date)
    else:
      self.due = 0
    super(Transaction,self).save(*args, **kwargs)