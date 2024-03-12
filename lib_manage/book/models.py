from django.db import models
import datetime
import django

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100, default = 'author')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100, default = 'category or genre')
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length = 100, default = 'publisher name')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100, default = 'bookname with edition')
    published_date = models.DateField(auto_now=False, auto_now_add=False, default = datetime.date(1990, 10,10))
    added_date = models.DateField(auto_now=False, auto_now_add=False, default = datetime.date.today())
    ISBN = models.CharField(max_length = 100, null = True,blank = True)
    language = models.CharField(max_length = 100, null = True, blank = True)
    count = models.PositiveIntegerField( default = 1)

    def __str__(self):
        return self.title

class BookCategory(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class BookAuthor(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

class BookPublisher(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete = models.CASCADE)