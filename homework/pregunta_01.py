# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """



    """
    Lee el archivo de envíos, genera gráficos y un dashboard HTML.
    """
    # Crear carpeta de salida
    carpeta_docs = 'docs'
    os.makedirs(carpeta_docs, exist_ok=True)

    # Cargar datos
    datos = pd.read_csv('files/input/shipping-data.csv')

    plt.figure(figsize=(8, 6))
    datos['Warehouse_block'].value_counts().plot(
        kind='bar', color='skyblue'
    )
    plt.title('Cantidad de Envíos por Warehouse')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Cantidad')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(carpeta_docs, 'shipping_per_warehouse.png'))
    plt.close()

    #modo de envío
    plt.figure(figsize=(8, 6))
    datos['Mode_of_Shipment'].value_counts().plot(
        kind='bar', color='lightgreen'
    )
    plt.title('Modo de Envío')
    plt.xlabel('Modo')
    plt.ylabel('Cantidad')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(carpeta_docs, 'mode_of_shipment.png'))
    plt.close()

    plt.figure(figsize=(8, 6))
    datos.groupby('Warehouse_block')['Customer_rating'].mean().plot(
        kind='bar', color='salmon'
    )
    plt.title('Calificación Promedio por Warehouse')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Calificación Promedio')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(carpeta_docs, 'average_customer_rating.png'))
    plt.close()

    plt.figure(figsize=(8, 6))
    datos['Weight_in_gms'].plot(
        kind='hist', bins=20, color='gold', edgecolor='black'
    )
    plt.title('Distribución del Peso de los Productos')
    plt.xlabel('Peso (g)')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(carpeta_docs, 'weight_distribution.png'))
    plt.close()

    html = f"""
    <!DOCTYPE html>
    <html lang=\"es\">
      <head><meta charset=\"UTF-8\"><title>Shipping Dashboard</title></head>
      <body>
        <h1>Shipping Dashboard</h1>
        <figure><h2>Envíos por Warehouse</h2>
          <img src=\"shipping_per_warehouse.png\" alt=\"Shipping per Warehouse\"> 
        </figure>
        <figure><h2>Mode of Shipment</h2>
          <img src=\"mode_of_shipment.png\" alt=\"Mode of Shipment\"> 
        </figure>
        <figure><h2>Average Customer Rating</h2>
          <img src=\"average_customer_rating.png\" alt=\"Average Customer Rating\"> 
        </figure>
        <figure><h2>Weight Distribution</h2>
          <img src=\"weight_distribution.png\" alt=\"Weight Distribution\"> 
        </figure>
      </body>
    </html>
    """
    # save index
    ruta_html = os.path.join(carpeta_docs, 'index.html')
    with open(ruta_html, 'w', encoding='utf-8') as f:
        f.write(html)