from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    published_date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length = 100)
    is_available = models.BooleanField(default = True)

