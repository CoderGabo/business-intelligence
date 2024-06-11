from asgiref.sync import sync_to_async
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from ...models import Mantenimiento, Vehicle

@sync_to_async
def generar_lista_vehiculos(year=None, meses=None, marcas_autos=None):
    # Filtrar los mantenimientos según los parámetros proporcionados
    mantenimientos = Mantenimiento.objects.all()

    if year:
        mantenimientos = mantenimientos.filter(date__year=year)
    
    if marcas_autos:
        vehiculos = Vehicle.objects.filter(brand__in=marcas_autos)
        vins_vehiculos = vehiculos.values_list('vin', flat=True)
        mantenimientos = mantenimientos.filter(vehicle__vin__in=vins_vehiculos)

    if meses:
        mantenimientos = mantenimientos.annotate(month=ExtractMonth('date')).filter(month__in=meses)

    # Contar el número de mantenimientos por marca de vehículo
    recuento_mantenimientos_por_marca = mantenimientos.values('vehicle__brand').annotate(total=Count('vehicle'))

    # Calcular el total de mantenimientos
    total_mantenimientos = mantenimientos.count()

    # Calcular el porcentaje de mantenimientos por marca
    porcentaje_por_marca = {item['vehicle__brand']: (item['total'] / total_mantenimientos) * 100 for item in recuento_mantenimientos_por_marca}

    return porcentaje_por_marca
