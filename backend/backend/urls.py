from django.urls import path
from .views import add_user
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('add_user'), name='default_redirect'),
    path('add_user/', add_user, name='add_user'),
]
