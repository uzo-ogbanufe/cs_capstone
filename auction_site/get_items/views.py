from django.shortcuts import render
from django.http import HttpResponse
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
            cursor.callproc('findAllItems', [now])

            # Get one result from the query
            results = cursor.fetchall()

            return render(request, "hello.html", {"items": results})
    
    # If an error occurs, display the error
    except Exception as e:
        return HttpResponse("<html><body>Error: {e}</body></html>")

