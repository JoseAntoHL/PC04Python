def obtener_precios_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data

def obtener_tipo_cambio_pen(fecha):
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    c.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (fecha,))
    venta_pen = c.fetchone()[0]
    conn.close()
    return venta_pen

def crear_tabla_bitcoin():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                 (fecha TEXT, usd REAL, gbp REAL, eur REAL, pen REAL)''')
    conn.commit()
    conn.close()

def insertar_datos_bitcoin(fecha, usd, gbp, eur, pen):
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    c.execute("INSERT INTO bitcoin (fecha, usd, gbp, eur, pen) VALUES (?, ?, ?, ?, ?)", (fecha, usd, gbp, eur, pen))
    conn.commit()
    conn.close()

crear_tabla_bitcoin()
bitcoin_data = obtener_precios_bitcoin()
fecha = bitcoin_data['time']['updated']
usd = bitcoin_data['bpi']['USD']['rate_float']
gbp = bitcoin_data['bpi']['GBP']['rate_float']
eur = bitcoin_data['bpi']['EUR']['rate_float']
tipo_cambio_pen = obtener_tipo_cambio_pen(fecha.split()[0])
pen = usd * tipo_cambio_pen

insertar_datos_bitcoin(fecha, usd, gbp, eur, pen)

conn = sqlite3.connect('base.db')
c = conn.cursor()
c.execute("SELECT * FROM bitcoin")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
