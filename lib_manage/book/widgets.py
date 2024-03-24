from django import forms
from django.template import loader
from django.utils.safestring import mark_safe

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class MultipleSelectDropDown():
    template_name = 'dropdown.html'

    def get_context(self, name, value, attrs=None):
        return {'widget': {
            'name': name,
            'value': value,
        }}

    def render(self, name, value, renderer=None, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)