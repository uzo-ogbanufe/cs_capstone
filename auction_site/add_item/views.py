from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm, ItemForm


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
