from django.http import JsonResponse
from django.db import connection

def check_database_connection(request):
    try:
        # Intenta ejecutar una consulta simple
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"message": "Database connection is successful"}, status=200)
    except Exception as e:
        return JsonResponse({"message": "Database connection failed", "error": str(e)}, status=500)
