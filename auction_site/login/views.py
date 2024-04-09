from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .forms import UserForm

def login(request):
    if request.method == 'POST':  
        form = UserForm(request.POST)  # Get the form data from the POST request
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data.get('username')  # Get the cleaned username data from the form
            if not username:  # Check if username is empty
                messages.error(request, 'Missing username')  # Add an error message if username is missing
            else:
                # Connect to the database if form is valid and username is not empty
                try:
                    with connection.cursor() as cursor:
                        cursor.callproc('checkIfUserExists', [username,])  # Call the checkIfUserExists stored procedure with the username
                        results = cursor.fetchall()  # Fetch the results
                        if bool(results[0][0]):  # Check if the user was added successfully
                            request.session['username'] = username  # Add the username to the session
                            messages.success(request, 'Successfully logged in')  # display a success message
                        else:
                            messages.error(request, 'Username or password not recognized')  # display an error message
                except Exception as e:
                    messages.error(request, str(e))  # Add an error message if an exception occurs
    else:
        form = UserForm() 
    return render(request, 'login.html', {'form': form})  # Render the add_user.html template with the form data
