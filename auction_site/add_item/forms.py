from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create validator that checks if a value is non-negative
def non_negative(value):
    if value < 0:
        raise ValidationError(
            _("Value must be positive"),
            params={"value": value},
        )

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)

class ItemForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    title = forms.CharField(label='Title', max_length=64)
    end_date = forms.DateTimeField(label='End Date')
    initial_price = forms.DecimalField(label='Initial Price', max_digits=8, decimal_places=2, validators=[non_negative])
    description = forms.CharField(label='Description', widget=forms.Textarea)
