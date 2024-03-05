from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Add the user to your database here
            return JsonResponse({'message': 'User added successfully'})
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

