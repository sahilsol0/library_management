from django import forms
from .models import Book,Author,Publisher,Category
from .widgets import DatePickerInput, MultipleSelectDropDown

form_style = "bg-color60 w-full text-xl p-2 rounded mb-6 focus:outline-2 outline-color10"
form_style2 = "bg-color60 w-full text-xl p-2 rounded mb-0 focus:outline-2 outline-color10"

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': form_style,
            }),
            'authors': forms.SelectMultiple(attrs= {
                'class': form_style,
            }),
            'publisher': forms.SelectMultiple(attrs = {
                'class': form_style,
            }),
            'published_year': forms.NumberInput(attrs = {
                'class': form_style,
            }),
            'ISBN': forms.TextInput(attrs = {
                'class': form_style,
            }),
            'language': forms.TextInput(attrs = {
                'class': form_style,
            }),
            'category': forms.SelectMultiple(attrs = {
                'class': form_style,
            }),
            'added_date': DatePickerInput(attrs = {
                'class': form_style,
            }),
            'shelf_no': forms.NumberInput(attrs = {
                'class': form_style,
            }),
            'count': forms.NumberInput(attrs = {
                'class': form_style,
            }),
        }

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': form_style2,
            })
        }

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': form_style2,
            })
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': form_style2,
            })
        }
