from asgiref.sync import sync_to_async
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from collections import OrderedDict
from ...models import Detail

@sync_to_async
def generar_lista_ganancias(año=None, meses=None):
    # Obtener todos los detalles de los mantenimientos
    detalles = Detail.objects.all()

    # Aplicar filtros opcionales por año y mes
    if año is not None:
        detalles = detalles.filter(maintenance__date__year=año)

    if meses:
        detalles = detalles.filter(maintenance__date__month__in=meses)

    # Agrupar los detalles por año y mes
    detalles_por_mes_y_ano = detalles.annotate(
        year=ExtractYear('maintenance__date'),
        month=ExtractMonth('maintenance__date')
    ).values('year', 'month')

    # Calcular las ganancias por año y mes
    ganancias_por_mes_y_ano = detalles_por_mes_y_ano.annotate(
        total_ganancias=Sum('cost')
    ).values('year', 'month', 'total_ganancias')

    # Devolver los resultados como un diccionario anidado
    resultados = {}
    for item in ganancias_por_mes_y_ano:
        year = int(item['year'])
        month = int(item['month'])
        total_ganancias = item['total_ganancias']
        if year not in resultados:
            resultados[year] = {}
        resultados[year][month] = total_ganancias

    # Ordenar el diccionario por clave (año) en orden descendente
    resultados = OrderedDict(sorted(resultados.items(), reverse=True))

    return resultados
