from django.db import models
import datetime
import django

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100, default = 'author')
    books = models.ManyToManyField('Book', through='BookAuthor')
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
    authors = models.ManyToManyField('Author', through='BookAuthor')
    publisher = models.ManyToManyField(Publisher, related_name='publishers')
    published_year = models.IntegerField(default = 1950)
    ISBN = models.CharField(max_length = 100, null = True,blank = True)
    language = models.CharField(max_length = 100, null = True, blank = True)
    category = models.ManyToManyField(Category, related_name='categories')
    added_date = models.DateField(auto_now=False, auto_now_add=False, default = datetime.date.today())
    count = models.PositiveIntegerField( default = 1)

    def __str__(self):
        return self.title
    
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)