import cryptocompare as crypto
import requests
import time

#Manera automática
moneda = crypto.get_price('BTC', currency='EUR')
print(moneda)

#Manera bucle
def calculaBTC():

    while True:
        r = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        print(r.json()['data']['rates']['EUR'])
        time.sleep(6)

calculaBTC()