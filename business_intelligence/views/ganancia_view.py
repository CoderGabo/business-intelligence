from django.http import JsonResponse

from ..kpi.kpiGananciasTotales.generar_lista_ganacias import generar_lista_ganancias
from ..kpi.kpiGananciasTotales.generar_grafico_lineal import generar_grafico_lineal

async def ganancias_lineal(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)
    meses = request.GET.getlist('months[]', None)

    # Convertir parámetros a tipos de datos correctos
    if year:
        year = int(year)
    if meses:
        meses = [int(mes) for mes in meses if mes.isdigit()]
    # Obtener el recuento de servicios utilizados en mantenimientos
    ganancias_totales = await generar_lista_ganancias(year, meses)
    
    figura = await generar_grafico_lineal(ganancias_totales)

    # Crear la respuesta
    response_data = {
        'figura': figura,
    }

    return JsonResponse(response_data)