from asgiref.sync import sync_to_async
import plotly.graph_objs as go

@sync_to_async
def generar_grafico_pastel(recuento_vehiculos, meses=None, año=None):
    # Diccionario para convertir números de meses a nombres de meses en español
    meses_nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    # Extraer los nombres de los vehículos y sus recuentos
    placas = list(recuento_vehiculos.keys())
    recuentos = list(recuento_vehiculos.values())

    # Crear la etiqueta del título con meses y año
    if meses and año:
        meses_str = ', '.join(meses_nombres[mes - 1] for mes in sorted(meses))  # Convertir números a nombres y ordenar
        titulo = f'Porcentaje de mantenimientos por vehículo para los meses {meses_str} del año {año}'
    elif meses:
        meses_str = ', '.join(meses_nombres[mes - 1] for mes in sorted(meses))  # Convertir números a nombres y ordenar
        titulo = f'Porcentaje de mantenimientos por vehículo para los meses {meses_str}'
    elif año:
        titulo = f'Porcentaje de mantenimientos por vehículo para el año {año}'
    else:
        titulo = 'Porcentaje de mantenimientos por vehículo'

    # Crear el gráfico de pastel
    fig = go.Figure(data=[go.Pie(
        labels=placas, 
        values=recuentos, 
        hole=0.3,  # Definir el agujero en el pastel
        hoverinfo='label+percent',  # Información adicional en los tooltips
        textinfo='label+percent',  # Mostrar etiquetas y porcentajes en el gráfico
        textposition='inside',  # Posicionar las etiquetas dentro del gráfico
    )])

    # Configurar el diseño del gráfico
    fig.update_layout(
        title=dict(
            text=titulo,
            x=0.5,  # Centrar el título
            xanchor='center',
            font=dict(size=12)  # Tamaño de la fuente del título
        ),
        showlegend=True,
        legend=dict(
            title='Vehículos',
            orientation='h',  # Leyenda horizontal
            x=0.5,
            xanchor='center',
            y=-0.2,  # Posicionar la leyenda debajo del gráfico
        ),
    )

    # Convertir la figura a formato JSON
    fig_json = fig.to_plotly_json()

    return fig_json
