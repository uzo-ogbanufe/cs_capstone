from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm
from django.views.decorators.http import require_http_methods
from django.db import connection

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Add the user to your database here
            username = request.POST.get('username')
            if not username:
                return JsonResponse({"error": "Missing username"}, status=400)

            try:
                with connection.cursor() as cursor:
                    # Call the stored procedure
                    cursor.callproc('addUser', [username,])
                    # If you need to fetch the result, modify accordingly. This example assumes insertion only.
                    results = cursor.fetchall()
                # Assuming successful insertion without fetching result
                    if(bool(results[0][0])):
                        return JsonResponse({"success": True})
                    elif(cursor.execute(f"SELECT EXISTS(SELECT * FROM users WHERE username = '{username}')" )):
                        return JsonResponse({"LOGGED IN GOOD JOB": True})
                    else:
                        return JsonResponse({"No way": False})
            except Exception as e:
                # For debugging purposes; in production, log the error and potentially mask direct error messages
                return JsonResponse({"error": str(e)}, status=500)
            
            


            return JsonResponse({'message': 'User added successfully'})
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

