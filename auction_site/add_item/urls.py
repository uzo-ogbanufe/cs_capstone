from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_item, name='add_item'),
    
]
