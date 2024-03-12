from django.contrib import admin
from . models import Book,Category, BookCategory, Author, BookAuthor, Publisher,BookPublisher
# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookCategory)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Publisher)
admin.site.register(BookPublisher)