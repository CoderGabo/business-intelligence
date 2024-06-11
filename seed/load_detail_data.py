# Importa los modelos de Django
import pandas as pd

def load_detail_data():
    # Lee los datos del archivo Excel
    df = pd.read_excel('seed/DataSet.xlsx', sheet_name='Detalle')

    # Convierte los datos a una lista de diccionarios
    data = df.to_dict(orient='records')

    print(df.head())

    return data