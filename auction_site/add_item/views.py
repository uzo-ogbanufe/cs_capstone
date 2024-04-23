from django.shortcuts import render, redirect
from .forms import ItemForm
from django.db import connection
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Assuming the session check and database interaction is necessary
            username = request.session.get('username')
            if not username:
                # If username isn't in the session, redirect to login
                # Assuming you have a 'login' named URL
                return redirect('login')

            # Prepare data for database insertion
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['initial_price'] * 100  # Convert to cents
            dateClose = form.cleaned_data['end_date']
            date_of_listing = timezone.now()

            try:
                with connection.cursor() as cursor:
                    # Call the stored procedure and pass validated form data
                    cursor.callproc('addItem', [title, description, username, price, date_of_listing, dateClose])
                    results = cursor.fetchall()
                
                    if results and results[0][0]:
                        # Assuming 'get_items' is a named URL where you want to redirect
                        messages.success(request, 'Item successfully added!')
                        return redirect('get_items')
            except Exception as e:
                # Log the exception for debugging
                # For production, you might want to return a custom error message
                print(f"Error when inserting item: {e}")
                form.add_error(None, 'An unexpected error occurred. Please try again later.')
        # If form is not valid or an exception occurred, re-render the page with the form, which now includes errors
        return render(request, 'add_item.html', {'form': form})

    else:
        # If it's a GET request, render the empty form
        form = ItemForm()
        return render(request, 'add_item.html', {'form': form})
