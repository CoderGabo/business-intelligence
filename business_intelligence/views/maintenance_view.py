from django.http import JsonResponse

from ..kpi.kpiVechiulosMantenimiento.generar_grafica_pastel import generar_grafico_pastel
from ..kpi.kpiVechiulosMantenimiento.generar_lista_vehiculos import generar_lista_vehiculos

async def maintenance_pastel(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)
    meses = request.GET.getlist('months[]', None)
    marcas_autos = request.GET.getlist('brands[]', None)

    # Convertir parámetros a tipos de datos correctos
    if year:
        year = int(year)
    if meses:
        meses = [int(mes) for mes in meses if mes.isdigit()]

    # Obtener el recuento de servicios utilizados en mantenimientos
    recuento_vehiculos = await generar_lista_vehiculos(year,meses,marcas_autos)
    
    figura = await generar_grafico_pastel(recuento_vehiculos, meses, year)

    # Crear la respuesta
    response_data = {
        'figura': figura,
    }

    return JsonResponse(response_data)