from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .forms import UserForm

def get_username(request):
    '''
    Gets the username from the form if it exists
    '''
    # Get the username if it exists and check if it exists
    if request.method == 'POST':
        form = UserForm(request.POST)  # Get the form data from the POST request
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data.get('username')  # Get the cleaned username data from the form
            return username
    
    # If username is not valid, return false
    return False

def userExists(username, request):
    '''
    Returns whether the given user exists
    '''
    # Connect to the database if form is valid and username is not empty
    try:
        with connection.cursor() as cursor:
            cursor.callproc('checkIfUserExists', [username,])  # Call the checkIfUserExists stored procedure with the username
            results = cursor.fetchall()  # Fetch the results
            return results[0][0]
    # Catch any errors
    except Exception as e:
        messages.error(request, str(e))  # Add an error message if an exception occurs    

def login(request):
    '''
    Check if the user exists, and if so log them in
    '''
    username = get_username(request)
    if not username:  # Check if username is empty or invalid
        messages.error(request, 'Invalid username')  # Add an error message if username is missing
        form = UserForm() #Default to empty form
    elif userExists(username, request):
        request.session['username'] = username  # Add the username to the session
        messages.success(request, 'Successfully logged in')  # display a success message
        form = UserForm(request.POST)
    else:
        messages.error(request, 'Username or password not recognized')  # display an error message
        form = UserForm(request.POST)
    return render(request, 'login.html', {'form': form})  # Render the add_user.html template with the form data
