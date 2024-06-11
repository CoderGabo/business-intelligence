from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ..models import Vehicle

@sync_to_async
def get_vehicle_brands():
    # Recuperar todas las marcas de vehículos de la tabla Vehicle
    vehicle_brands = Vehicle.objects.values_list('brand', flat=True).distinct()

    # Convertir el queryset a una lista
    vehicle_brands_list = list(vehicle_brands)

    return vehicle_brands_list

async def get_vehicle_brands_view(request):
    # Llamar a la función para recuperar las marcas de vehículos
    vehicle_brands = await get_vehicle_brands()

    # Crear la respuesta JSON con las marcas de vehículos
    response_data = {
        'vehicle_brands': vehicle_brands
    }

    return JsonResponse(response_data)
