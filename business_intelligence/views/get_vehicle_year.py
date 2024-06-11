from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ..models import Vehicle

@sync_to_async
def get_vehicle_years():
    # Recuperar todas las marcas de vehículos de la tabla Vehicle
    vehicle_years = Vehicle.objects.values_list('year', flat=True).distinct().order_by('year')

    # Convertir el queryset a una lista
    vehicle_years_list = list(vehicle_years)

    return vehicle_years_list

async def get_vehicle_years_view(request):
    # Llamar a la función para recuperar las marcas de vehículos
    vehicle_years = await get_vehicle_years()

    # Crear la respuesta JSON con las marcas de vehículos
    response_data = {
        'vehicle_years': vehicle_years
    }

    return JsonResponse(response_data)
