import sqlite3
import requests
from datetime import datetime

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v2/sunat/tipo-cambio?date=2023-05-01"
    response = requests.get(url)
    data = response.json()
    return data

def crear_tabla_sunat():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sunat_info
                 (fecha TEXT, compra REAL, venta REAL)''')
    conn.commit()
    conn.close()

def insertar_datos_sunat(fecha, compra, venta):
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    c.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    conn.commit()
    conn.close()

crear_tabla_sunat()
tipo_cambio_data = obtener_tipo_cambio()
fecha = datetime.now().strftime("%Y-%m-%d")
print(tipo_cambio_data)
compra = tipo_cambio_data['cambio'][0]['compra']
venta = tipo_cambio_data['cambio'][0]['venta']
insertar_datos_sunat(fecha, compra, venta)

conn = sqlite3.connect('base.db')
c = conn.cursor()
c.execute("SELECT * FROM sunat_info")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
