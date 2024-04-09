from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm
from django.db import connection
from django.contrib import messages

def add_user(request):
    if request.method == 'POST':  
        form = UserForm(request.POST)  # Get the form data from the POST request
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data.get('username')  # Get the cleaned username data from the form
            if not username:  # Check if username is empty
                messages.error(request, 'Missing username')  # Add an error message if username is missing
            else:
                try:
                    with connection.cursor() as cursor:
                        cursor.callproc('addUser', [username,])  # Call the addUser stored procedure with the username
                        results = cursor.fetchall()  # Fetch the results
                        if bool(results[0][0]):  # Check if the user was added successfully
                            messages.success(request, 'User added successfully')  # display a success message for user
                        else:
                            messages.error(request, 'Username has been taken, please try again')  # display an error message
                except Exception as e:
                    messages.error(request, str(e))  # Add an error message if an exception occurs
    else:
        form = UserForm() 
    return render(request, 'add_user.html', {'form': form})  # Render the add_user.html template with the form data
