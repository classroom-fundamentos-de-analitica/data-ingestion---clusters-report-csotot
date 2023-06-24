




"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    cluster = {"text": "cluster", "length": 8}
    cantidad_de_palabras_clave = {"text": "Cantidad de palabras clave", "length": 15}
    porcentaje_de_palabras_clave = {"text": "Porcentaje de palabras clave", "length": 16}
    principales_palabra_clave = {"text": "Principales palabras clave", "length": 79}


    df = pd.read_fwf(
        "clusters_report.txt",
        widths=[cluster["length"], cantidad_de_palabras_clave["length"], porcentaje_de_palabras_clave["length"], principales_palabra_clave["length"]],
        header=[0],
        skiprows=[1, 2, 3]
    )

    df = df.groupby(["Cluster", "Cantidad de", "Porcentaje de"])

    df = df.agg(lambda x: " ".join(x)).reset_index()

    df[principales_palabra_clave["text"]] = df[principales_palabra_clave["text"]].str.replace(r"\s{2,}", " ", regex=True)
    df[principales_palabra_clave["text"]] = df[principales_palabra_clave["text"]].str.replace(".", "", regex=True)

    df["Porcentaje de"] = df["Porcentaje de"].str.slice(0, -2).str.replace(",", ".").astype(float)

    df.columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

    return df

print(ingest_data().principales_palabras_clave.to_list()) 