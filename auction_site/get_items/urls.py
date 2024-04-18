from django.urls import path
from . import views
from .views import get_items, item_detail  # Import your view function


urlpatterns = [
    path('', views.get_items, name='get_items'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
]
