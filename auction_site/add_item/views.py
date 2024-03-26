from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm, ItemForm
from django.views.decorators.http import require_http_methods
from django.db import connection
import datetime
# Create your views here.


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            if not title:
                return JsonResponse({"error": "Missing item"}, status=400)
            

            dateClose = request.POST.get('end_date')
            if not dateClose:
                return JsonResponse({"error": "Missing Closing Date"}, status=400)
            

            price = request.POST.get('initial_price')
            if not price:
                return JsonResponse({"error": "Missing initial price"}, status=400)
            

            description = request.POST.get('description')
            if not description:
                return JsonResponse({"error": "Missing description"}, status=400)


            date_of_listing = '2020-01-01 00:00:00'

            seller_id = 1

            try:
                with connection.cursor() as cursor:
                    # Call the stored procedure
                    cursor.callproc('addItem', [title, dateClose, price, description, seller_id, date_of_listing])
                    # If you need to fetch the result, modify accordingly. This example assumes insertion only.
                    results = cursor.fetchall()
                
                    if(bool(results[0][0])):
                        return JsonResponse({"success": True})
                    else:
                        return JsonResponse({"No way": False})
            except Exception as e:
                # For debugging purposes; in production, log the error and potentially mask direct error messages
                return JsonResponse({"error": str(e)}, status=500)
            
            


            return JsonResponse({'message': 'Item added successfully'})
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


            
            
