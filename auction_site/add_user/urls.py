from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_user, name='add_user'),
]
