# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# import re

# class UserForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=64)

# class ItemForm(forms.Form):
#     # username = forms.CharField(label='Username', max_length=64)
#     title = forms.CharField(label='Title', max_length=64)
#     end_date = forms.DateTimeField(label='End Date')
#     initial_price = forms.DecimalField(label='Initial Price', max_digits=8, decimal_places=2, min_value=0)
#     description = forms.CharField(label='Description', widget=forms.Textarea)

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

class ItemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=64)
    end_date = forms.DateTimeField(label='End Date')
    initial_price = forms.DecimalField(label='Initial Price', max_digits=8, decimal_places=2, min_value=0)
    description = forms.CharField(label='Description', max_length=5000, widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        # Allow only alphanumeric characters and spaces in the title
        if not re.match(r'^[a-zA-Z0-9 \-]+$', title):
            raise ValidationError('Invalid characters in title. Only letters, numbers, and spaces are allowed.')
        return title

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        # Check that the end date is not in the past
        if end_date < timezone.now():
            raise ValidationError(('End date cannot be in the past. Please enter a future date.'))
        return end_date
    
    def clean_initial_price(self):
        initial_price = self.cleaned_data['initial_price']
        if initial_price <= 0:
            raise ValidationError(('The price must be greater than zero.'))
        return initial_price
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if not re.match(r'^[a-zA-Z0-9\s.,?!:;"\'()-]+$', description):
            raise ValidationError('Invalid characters in description. Please use English characters and common punctuation.')  
        return description
