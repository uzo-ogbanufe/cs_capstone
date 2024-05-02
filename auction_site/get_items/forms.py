from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class BidForm(forms.Form):
    bid_price = forms.DecimalField(label='Bid Price', max_digits=8, decimal_places=2, min_value=0)

    def __init__(self, *args, **kwargs):
        self.min_bid = kwargs.pop('min_bid')
        super(BidForm, self).__init__(*args,**kwargs)
    
    def clean_bid_price(self):
        bid_price = self.cleaned_data['bid_price']
        if bid_price <= self.min_bid:
            raise ValidationError((f'The price must be greater than {self.min_bid:.2f}.'))
        return bid_price
