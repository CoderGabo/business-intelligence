from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ..models import Servicio

@sync_to_async
def get_service_names():
    # Recuperar todos los nombres de servicios de la tabla Service
    service_names = Servicio.objects.values_list('name', flat=True)

    # Convertir el queryset a una lista
    service_names_list = list(service_names)

    return service_names_list

async def get_service_names_view(request):
    # Llamar a la función para recuperar los nombres de servicios
    service_names = await get_service_names()

    # Crear la respuesta JSON con los nombres de servicios
    response_data = {
        'service_names': service_names
    }

    return JsonResponse(response_data)
