from asgiref.sync import sync_to_async
import plotly.graph_objs as go

@sync_to_async
def generar_grafico_lineal(ganancias_por_mes_ano):
    # Definir los meses
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # Crear listas para los datos de x (meses) y las series de datos (ganancias por año)
    x = meses
    series_datos = []

    # Ordenar los datos por año
    ganancias_por_mes_ano = dict(sorted(ganancias_por_mes_ano.items()))

    # Calculamos el total de ganancias por año
    total_ganancias_por_año = {año: sum(ganancias.values()) for año, ganancias in ganancias_por_mes_ano.items()}

    # Para cada año, crear una serie de datos
    for año, ganancias in ganancias_por_mes_ano.items():
        # Convertir el diccionario de ganancias a una lista ordenada por mes
        ganancias_mensuales = [ganancias.get(mes, 0) for mes in range(1, 13)]  
        
        # Agregar la serie de datos al gráfico
        series_datos.append(go.Scatter(x=x, y=ganancias_mensuales, mode='lines+markers', name=str(año)))

    # Crear la figura de Plotly
    fig = go.Figure(data=series_datos)

    # Configurar el diseño del gráfico
    fig.update_layout(
        title='Ganancias Totales por Mes y Año',
        xaxis_title='Mes',
        yaxis_title='Ganancias Totales (Bs)',
        xaxis=dict(tickmode='array', tickvals=list(range(12)), ticktext=meses),
        legend=dict(title='Año'),
        hovermode='closest',
        plot_bgcolor='#f5f5f5',
        paper_bgcolor='#ffffff',
        annotations=[
            dict(
                x=1.02,
                y=1,
                xref='paper',
                yref='paper',
                text=f'Año 2022: {total_ganancias_por_año.get(2022, 0)} Bs',
                showarrow=False,
                font=dict(
                    family="Arial",
                    size=11,
                    color="black"
                )
            ),
            dict(
                x=1.02,
                y=0.95,
                xref='paper',
                yref='paper',
                text=f'Año 2023: {total_ganancias_por_año.get(2023, 0)} Bs',
                showarrow=False,
                font=dict(
                    family="Arial",
                    size=11,
                    color="black"
                )
            ),
            dict(
                x=1.02,
                y=0.90,
                xref='paper',
                yref='paper',
                text=f'Año 2024: {total_ganancias_por_año.get(2024, 0)} Bs',
                showarrow=False,
                font=dict(
                    family="Arial",
                    size=11,
                    color="black"
                )
            )
        ]
    )

    # Configurar los ticks del eje Y para que muestren números reales
    fig.update_yaxes(tickformat=',.0f')

    # Agregar texto de hover
    fig.update_traces(hoverinfo='text', hovertemplate='Mes: %{x}<br>Ganancia: %{y:,.0f} Bs')

    # Convertir la figura de Plotly a JSON
    fig_json = fig.to_plotly_json()

    return fig_json
