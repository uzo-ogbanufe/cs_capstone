from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from datetime import datetime

def get_items(request):
    '''
    Retrieve all items from the database and send them to the frontend
    '''
    # Check if the user is logged in, if not, redirect to login page
    if 'username' not in request.session:
        return redirect('login')  # Replace 'login' with your login route's name

    username = request.session['username']  # Get the logged in username

    # Connect to the database
    try:
        with connection.cursor() as cursor:
            # Call the procedure to get all of the items
            now = datetime.now()
            cursor.callproc('getAllItems', [now])

            # Get all of the items from the query
            results = cursor.fetchall()

            # Create a new array so we can format the data
            items = []

            # Format the price
            PRICE_INDEX = 2
            for item in results:
                temp = []
                for attribute in item:
                    temp.append(attribute)
                price = item[PRICE_INDEX] / 100
                temp[PRICE_INDEX] = f"${price:.2f}"
                items.append(temp)

            # Render the webpage, passing the username to the template
            return render(request, 'get_items.html', {"items": items, "username": username})
    
    # If an error occurs, display the error
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
