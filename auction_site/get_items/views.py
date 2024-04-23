from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from datetime import datetime

def get_items(request):
    if 'username' not in request.session:
        return redirect('login')  # Assuming 'login' is the route name for your login page

    username = request.session['username']

    try:
        with connection.cursor() as cursor:
            now = datetime.now()
            cursor.callproc('getAllItems', [now])
            results = cursor.fetchall()
            items = []

            for item in results:
                temp = list(item)  # Convert tuple to list to be able to modify it
                PRICE_INDEX = 3  # Ensure this index points to 'current_price'

                # Convert current_price to int before division if it's coming as a string
                price = int(temp[PRICE_INDEX]) / 100
                temp[PRICE_INDEX] = f"${price:.2f}"
                items.append(temp)

            return render(request, 'get_items.html', {"items": items, "username": username})
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



def item_detail(request, item_id):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('getItemDetails', [item_id])
            item_details = cursor.fetchone()
            
            # Check if item_details is not None
            if item_details:
                # Format the price if it's in cents
                price_index = 3  # Adjust the index based on the actual order of columns in your SELECT statement
                item_details = list(item_details)  # Convert tuple to list to be able to modify it
                price = item_details[price_index] / 100
                item_details[price_index] = f"${price:.2f}"
                # Pass the details to the template as a dictionary
                context = {'item': dict(zip(['id', 'title', 'seller', 'price', 'listing_date', 'closing_date', 'description'], item_details))}
            else:
                context = {'error': 'Item not found'}
            
            return render(request, 'item_detail.html', context)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

