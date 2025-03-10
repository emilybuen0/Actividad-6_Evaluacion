def cargar_dataset (archivo):
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt

    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv (archivo)
        return (df)
    elif extension == '.xlsx':
         df = pd.read_excel (archivo)
         return (df)
    else : 
        raise ValueError (f"Formato de archivo no soportado: {extension}")

def sustituir_valores_nulos(df):
    for columna in df.columns:
        if df[columna].dtype in ['int64', 'float64']:
            if df.columns.get_loc(columna) % 2 == 0:
                df[columna].fillna(df[columna].mean(), inplace=True)
            else: 
                df[columna].fillna(99, inplace=True)
        else:
            df[columna].fillna("Este_es_un_valor_nulo", inplace=True)
    return df

def cuenta_valores_nulos (df):
    nulos_columnas = df.isnull().sum()
    nulos_totales = df.isnull().sum().sum()

    return("Valores nulos por columna", nulos_columnas,
           "Valores nulos por dataframe", nulos_totales)