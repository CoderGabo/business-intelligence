from asgiref.sync import sync_to_async
from django.db.models import Count, Func, Value
from django.db.models.functions import Substr
from ...models import ServicioCita

@sync_to_async
def generar_lista_servicios(año=None, meses=None, nombre_servicio=None):
    # Filtrar los datos si se proporciona un nombre de servicio
    queryset = ServicioCita.objects.all()
    if nombre_servicio:
        queryset = queryset.filter(service__name__in=nombre_servicio)

    # Aplicar el filtro de año si se proporciona
    if año is not None:
        año_str = str(año)
        queryset = queryset.filter(appointment__scheduleDate__contains=año_str)
    # Aplicar el filtro de mes si se proporciona
    if meses:
        # Convertir los meses a cadena y agregar los caracteres delimitadores del mes ("/")
        meses_str = [f"{mes:02d}" for mes in meses]
        queryset = queryset.annotate(
            month=Substr('appointment__scheduleDate', 4, 2)  # Extrae el mes (posiciones 4-5)
        ).filter(month__in=meses_str)

    # Realizar la consulta para contar el número de veces que se ha utilizado cada servicio por mes y año
    recuento_servicios_por_mes_y_anio = queryset.annotate(
        year=Substr('appointment__scheduleDate', 7, 4),  # Extrae el año (posiciones 7-10)
        month=Substr('appointment__scheduleDate', 4, 2),  # Extrae el mes (posiciones 4-5)
    ).values('year', 'month', 'service__name').annotate(total=Count('service'))

    # Devolver el resultado como un diccionario anidado donde las claves son los años y meses,
    # y los valores son listas de servicios con sus totales para ese año y mes específicos
    resultados = {}
    for item in recuento_servicios_por_mes_y_anio:
        year = item['year']
        month = item['month']
        service_name = item['service__name']
        total = item['total']
        
        # Crear una clave única para representar el año y mes
        clave = (year, month)
        
        # Si la clave aún no existe en el diccionario, crear una nueva entrada con una lista vacía
        if clave not in resultados:
            resultados[clave] = []
        
        # Agregar el servicio y su total a la lista correspondiente en el diccionario de resultados
        resultados[clave].append({'service_name': service_name, 'total': total})

    return resultados
