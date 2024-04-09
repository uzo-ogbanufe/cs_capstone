from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)

class ItemForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    end_date = forms.DateField(label='End Date')
    initial_price = forms.DecimalField(label='Initial Price', max_digits=5, decimal_places=2)
    description = forms.CharField(label='Description', widget=forms.Textarea)
