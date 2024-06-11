# Create your views here.
from django.http import JsonResponse

from ..kpi.kpiServiciosTotales.generar_lista_servicios import generar_lista_servicios
from ..kpi.kpiServiciosTotales.generar_grafico import generar_grafico


async def servicios_barra(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)  # Ejemplo: /kpi/ # Obtener los parámetros de la consulta
    meses = request.GET.getlist('months[]', None)
    nombres_servicio = request.GET.getlist('services[]', None)

    # Convertir parámetros a tipos de datos correctos
    if year != '' and year is not None:
        year = int(year)
    if meses:
        meses = [int(mes) for mes in meses if mes.isdigit()]
    # Obtener el recuento de servicios utilizados en mantenimientos
    recuento_servicios = await generar_lista_servicios(year, meses, nombres_servicio)

    figura = await generar_grafico(recuento_servicios)
    
    # Crear la respuesta
    response_data = {
        'figura': figura,
    }
    
    return JsonResponse(response_data)