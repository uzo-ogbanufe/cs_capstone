from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from django.shortcuts import redirect
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

def logout(request):
    # Delete the current session
    request.session.flush()
    messages.info(request, 'You have been logged out.')
    # Go back to the login page with an empty form
    return redirect(login)

def login(request):
    '''
    Check if the user exists, and if so log them in and redirect to get_items.
    '''
    # Check if the user is already logged in
    if 'username' in request.session:
        # Redirect to the get_items page if the user is already logged in
        return redirect('get_items')  # Make sure 'get_items' is the name of your URL pattern for get_items view
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            # Check if the user exists
            if userExists(username, request):
                # Log in the user by adding the username to the session
                request.session['username'] = username
                # messages.success(request, 'Successfully logged in')
                # Redirect to the get_items page after login
                return redirect('get_items')  # Make sure 'get_items' is the name of your URL pattern for get_items view
            else:
                # Username does not exist, send an error message
                messages.error(request, 'Username not recognized')

    else:
        form = UserForm()

    # Display the login page with form
    return render(request, 'login.html', {'form': form})