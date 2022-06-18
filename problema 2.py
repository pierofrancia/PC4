'''Bitcoin es una forma de moneda digital, también conocida como
criptomoneda. En lugar de depender de una autoridad central como un
banco, Bitcoin se basa en una red distribuida, también conocida como
cadena de bloques, para registrar transacciones.
En este problema debe generar un programa que realice:
- Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
try:
...
except requests.RequestException:
...
- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.
Nota: El empleo de format string es apropiado para brindar formatos a nuestros datos. Le será
de utilidad el siguiente comando: print(f"${amount:,.4f}")
Recuerde instalar la librería Requests mediante el comando: pip install requests '''

import requests
import json

try:
    api_bitcoin=requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    api_bitcoin=api_bitcoin.json()

    dolar_bitcoin=float(api_bitcoin['price'])

    n=int(input('Ingrese cuantos bitcoins tienes: '))

    dolar_bitcoin=n*dolar_bitcoin
    print(f'Usted tiene: {dolar_bitcoin:,.4f}dolares en Bitcoins')
except ValueError:
    print('Error')
except requests.RequestException:
    print('Error')