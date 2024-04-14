import requests
import sqlite3

# Función para obtener el precio de compra y venta del bitcoin en diferentes monedas
def obtener_precios_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['bpi']
    else:
        print("Error al obtener los datos del bitcoin")
        return None

# Función para obtener el tipo de cambio de PEN desde SUNAT
def obtener_tipo_cambio_pen(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio/{fecha}/dolares/pen"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['venta']
    else:
        print(f"Error al obtener el tipo de cambio de PEN para la fecha {fecha}")
        return None

# Crear la tabla bitcoin en la base de datos
def crear_tabla_bitcoin():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                  (fecha TEXT, usd REAL, gbp REAL, eur REAL, pen REAL)''')
    conn.commit()
    conn.close()

# Insertar los datos en la tabla bitcoin
def insertar_datos(fecha, usd, gbp, eur, pen):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bitcoin (fecha, usd, gbp, eur, pen) VALUES (?, ?, ?, ?, ?)", (fecha, usd, gbp, eur, pen))
    conn.commit()
    conn.close()

# Obtener los precios del bitcoin y guardarlos en la base de datos
crear_tabla_bitcoin()
bitcoin_data = obtener_precios_bitcoin()
if bitcoin_data and 'bpi' in bitcoin_data:
    fecha = bitcoin_data.get('time', {}).get('updated', 'Fecha desconocida')
    if 'USD' in bitcoin_data['bpi']:
        usd = bitcoin_data['bpi']['USD']['rate_float']
        gbp = bitcoin_data['bpi']['GBP']['rate_float']
        eur = bitcoin_data['bpi']['EUR']['rate_float']
        tipo_cambio_pen = obtener_tipo_cambio_pen(fecha.split()[0])
        pen = usd * tipo_cambio_pen
        insertar_datos(fecha, usd, gbp, eur, pen)



# Consultar la base de datos para calcular el precio de comprar 10 bitcoins en PEN y EUR
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM bitcoin")
row = cursor.fetchone()
if row:
    precio_10_bitcoins_pen = row[4] * 10
    precio_10_bitcoins_eur = row[3] * 10
    print(f"Precio de comprar 10 bitcoins en PEN: {precio_10_bitcoins_pen}")
    print(f"Precio de comprar 10 bitcoins en EUR: {precio_10_bitcoins_eur}")
conn.close()
