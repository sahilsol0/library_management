from django import forms
from .models import Transaction
from book.widgets import DatePickerInput

form_style = "bg-color60 w-full text-xl p-2 rounded mb-6 focus:outline-2 outline-color10"
form_style2 = "bg-color60 w-full text-xl p-2 rounded mb-0 focus:outline-2 outline-color10"

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [ 'student' , 'book', 'issued_date', 'due_date', 'returned_date']
        widgets = {
            'student': forms.Select(attrs= {
                'class': form_style,
            }),
            'book': forms.Select(attrs= {
                'class': form_style,
            }),
            'issued_date': DatePickerInput(attrs = {
                'class': form_style,
            }),
            'returned_date': DatePickerInput(attrs = {
                'class': form_style,
            }),
        }