from django.urls import path
from . import views
from .views import bid_on_item  # Import your view function


urlpatterns = [
    path('<str:item_id>/', bid_on_item, name='bid_on_item'),
]
