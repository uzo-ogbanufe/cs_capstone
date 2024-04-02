from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from datetime import datetime

def get_items(request):
    '''
    Retrieve all items from the database and send them to the
    frontend
    '''
    # Connect to the database
    try:
        with connection.cursor() as cursor:
            # Call the procedure to get all of the items
            now = datetime.now()
            cursor.callproc('getAllItems', ['2019-01-01 00:00:00'])

            # Get all of the items from the query
            results = cursor.fetchall()

            # Render the webpage
            return render(request, 'get_items.html', {"items": results})
    
    # If an error occurs, display the error
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

