from django.urls import path
from . import views
from .views import item_detail_view



urlpatterns = [
    path('', views.add_item, name='add_item'),
    path('item/<int:item_id>/', item_detail_view, name='item_detail'),

]
