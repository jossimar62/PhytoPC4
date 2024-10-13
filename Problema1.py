import requests

# Función para obtener el precio actual de Bitcoin en USD desde la API de CoinDesk
def obtener_precio_bitcoin():
    try:
        # Realizar la solicitud GET a la API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # Convertir la respuesta a JSON
        datos = response.json()
        # Extraer el precio en USD del objeto JSON
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Hubo un problema al conectar con la API de CoinDesk:", e)
        return None

# Solicitar al usuario la cantidad de bitcoins
try:
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

# Obtener el precio actual de Bitcoin
precio_bitcoin = obtener_precio_bitcoin()

# Si la API responde correctamente
if precio_bitcoin is not None:
    # Calcular el costo total en USD
    costo_total = n * precio_bitcoin
    # Mostrar el resultado con formato adecuado
    print(f"El costo actual de {n} Bitcoins es: ${costo_total:,.4f} USD")

