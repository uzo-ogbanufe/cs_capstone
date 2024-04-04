from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import UserForm, ItemForm
from .models import Item  # Import your item model



# Create your views here.


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Add the item to your database here
            return JsonResponse({'message': 'Item added successfully'})
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def item_detail_view(request, item_id):
    # Get the item or return a 404 if it doesn't exist
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'add_item/templates/item_detail.html', {'item': item})
