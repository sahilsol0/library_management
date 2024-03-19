from django import forms
from .models import Book,Author,Publisher,Category

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
