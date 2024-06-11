from asgiref.sync import sync_to_async
import plotly.graph_objs as go

@sync_to_async
def generar_grafico(recuento_servicios_por_mes_y_anio):
    # Crear una lista para almacenar los datos de las barras
    data = []

    # Iterar sobre los años y meses en orden
    for year in range(2022, 2025):
        for month in range(1, 13):
            # Crear la clave para buscar en el diccionario
            clave = (str(year), str(month).zfill(2))

            # Verificar si hay datos para este año y mes
            if clave in recuento_servicios_por_mes_y_anio:
                servicios = recuento_servicios_por_mes_y_anio[clave]

                # Ordenar los servicios alfabéticamente por nombre
                servicios_sorted = sorted(servicios, key=lambda x: x['service_name'])

                # Crear una lista de nombres de servicios y una lista de totales para este año y mes
                nombres_servicios = [servicio['service_name'] for servicio in servicios_sorted]
                totales = [servicio['total'] for servicio in servicios_sorted]

                # Crear las barras para este año y mes
                bars = go.Bar(
                    x=[f"{service_name} ({month}/{year})" for service_name in nombres_servicios],
                    y=totales,
                    name=f'{month}/{year}'
                )

                # Agregar las barras a los datos
                data.append(bars)

    # Crear el diseño del gráfico
    layout = go.Layout(
        title='Recuento de veces que se ha utilizado cada servicio por mes y año',
        xaxis=dict(title='Servicio (Mes/Año)'),
        yaxis=dict(title='Cantidad de veces utilizado'),
        hovermode='closest',
        bargap=0.2,
        plot_bgcolor='#f5f5f5',
        paper_bgcolor='#ffffff'
    )

    # Crear la figura
    fig = go.Figure(data=data, layout=layout)
    fig_json = fig.to_plotly_json()

    return fig_json
