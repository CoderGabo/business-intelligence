from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.db.models.functions import ExtractYear

from ..models import Mantenimiento


@sync_to_async
def get_maintenance_years():
    # Obtener los años de los registros en el campo 'date' de la tabla Maintenance
    maintenance_years = Mantenimiento.objects.annotate(year=ExtractYear('date')).values_list('year', flat=True).distinct().order_by('year')

    # Convertir el queryset a una lista
    maintenance_years_list = list(maintenance_years)

    return maintenance_years_list

async def get_maintenance_years_view(request):
    # Llamar a la función para obtener los años de los registros en la tabla Maintenance
    maintenance_years = await get_maintenance_years()

    # Crear la respuesta JSON con los años de los registros en la tabla Maintenance
    response_data = {
        'maintenance_years': maintenance_years
    }

    return JsonResponse(response_data)
