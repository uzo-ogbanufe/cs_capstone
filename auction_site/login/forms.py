from django import forms


# TODO think of security type users (restrict user from inputting sql)
class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
