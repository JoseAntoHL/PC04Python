import requests
from datetime import datetime

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()
bitcoin_price_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))

fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("bitcoin_prices.txt", "a") as file:
    file.write(f"{fecha_actual},{bitcoin_price_usd}\n")

print("Datos de precio de Bitcoin almacenados en bitcoin_prices.txt")
