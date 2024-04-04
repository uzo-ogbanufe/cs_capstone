from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_items, name='get_items'),
]
