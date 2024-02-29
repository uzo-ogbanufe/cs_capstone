from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import connection

@csrf_exempt  # Temporarily disable CSRF token for testing purposes
@require_http_methods(["GET","POST"])
def add_user(request):
    # Assuming the username is sent as a form data (adjust as needed, e.g., for JSON body)
    username = request.POST.get('username')
    if not username:
        return JsonResponse({"error": "Missing username"}, status=400)

    try:
        with connection.cursor() as cursor:
            # Call the stored procedure
            cursor.callproc('addUser', [username,])
            # If you need to fetch the result, modify accordingly. This example assumes insertion only.

        # Assuming successful insertion without fetching result
        return JsonResponse({"success": True})
    except Exception as e:
        # For debugging purposes; in production, log the error and potentially mask direct error messages
        return JsonResponse({"error": str(e)}, status=500)


"""
Make sure all migrations are applied by running 'python manage.py migrate'.
Start your Django server with 'python manage.py runserver'.
You can now test adding a user by sending a POST request to http://localhost:8000/myapp/add_user/ with a username in the form data.

django-admin startproject yourprojectname
"""