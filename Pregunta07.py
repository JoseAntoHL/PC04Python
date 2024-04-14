import requests
import sqlite3

def obtener_precios_dolar(year):
    url = f"https://api.apis.net.pe/v1/tipo-cambio/{year}/dolares"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error al obtener los datos para el año {year}")
        return None

def crear_base_datos():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info
                  (fecha TEXT, compra REAL, venta REAL)''')
    conn.commit()
    conn.close()

def insertar_datos(fecha, compra, venta):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    conn.commit()
    conn.close()

crear_base_datos()
for month in range(1, 13):
    data = obtener_precios_dolar(f"2023-{month:02d}")
    if data:
        for item in data['data']:
            insertar_datos(item['fecha'], item['compra'], item['venta'])

conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM sunat_info")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()