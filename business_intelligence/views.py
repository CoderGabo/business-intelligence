from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from .kpi.kpiServiciosTotales.generar_lista_servicios import generar_lista_servicios
from .kpi.kpiServiciosTotales.generar_grafico import generar_grafico

from .kpi.kpiVechiulosMantenimiento.generar_grafica_pastel import generar_grafico_pastel
from .kpi.kpiVechiulosMantenimiento.generar_lista_vehiculos import generar_lista_vehiculos

from .kpi.kpiGananciasTotales.generar_lista_ganacias import generar_lista_ganancias
from .kpi.kpiGananciasTotales.generar_grafico_lineal import generar_grafico_lineal

def index(request):
    return HttpResponse("¡Conexión exitosa!")

async def servicios_barra(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)  # Ejemplo: /kpi/ # Obtener los parámetros de la consulta
    meses = request.GET.getlist('meses', None)
    nombres_servicio = request.GET.getlist('nombres_servicio', None)

    # Convertir parámetros a tipos de datos correctos
    if year:
        year = int(year)
    if meses:
        meses = [int(mes) for mes in meses]
    # Obtener el recuento de servicios utilizados en mantenimientos
    recuento_servicios = await generar_lista_servicios(year, meses, nombres_servicio)

    figura = await generar_grafico(recuento_servicios)
    
    # Crear la respuesta
    response_data = {
        'figura': figura,
    }
    
    return JsonResponse(response_data)
    # return HttpResponse(html_config)

async def servicios_pastel(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)
    meses = request.GET.getlist('meses', None)
    marcas_autos = request.GET.getlist('marca_auto', None)

    # Convertir parámetros a tipos de datos correctos
    if year:
        year = int(year)
    if meses:
        meses = [int(mes) for mes in meses]

    # Obtener el recuento de servicios utilizados en mantenimientos
    recuento_vehiculos = await generar_lista_vehiculos(year,meses,marcas_autos)
    
    figura = await generar_grafico_pastel(recuento_vehiculos, meses, year)

    # Crear la respuesta
    response_data = {
        'figura': figura,
    }

    return JsonResponse(response_data)
    # return HttpResponse(html_config)


async def ganancias_lineal(request):
    # Obtener los parámetros de la consulta
    year = request.GET.get('year', None)
    meses = request.GET.getlist('meses', None)

    # Convertir parámetros a tipos de datos correctos
    if year:
        year = int(year)
    if meses:
       meses = [int(mes) for mes in meses]
    # Obtener el recuento de servicios utilizados en mantenimientos
    ganancias_totales = await generar_lista_ganancias(year, meses)
    
    figura = await generar_grafico_lineal(ganancias_totales)

    # Crear la respuesta
    response_data = {
        'figura': figura,
    }

    return JsonResponse(response_data)
    # return HttpResponse(html_config)