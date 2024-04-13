import requests

try:
    n = float(input("Ingrese la cantidad de bitcoins: "))

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    bitcoin_precio_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    total_costo_usd = n * bitcoin_precio_usd

    print(f"El costo total de {n} bitcoins en USD es: ${total_costo_usd:,.4f}")

except requests.RequestException:
    print("Error al conectarse")
except ValueError:
    print("Valor no valido")
