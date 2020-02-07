import urllib.request
import json


class Stocks():
    """ takes the API key of Alpha Vantage as input """

    def __init__(self, apikey):
        self.apikey = apikey
        self.set_currency()

    
    def set_currency(self, currency="EUR"):
        self.currency = currency


    def price(self, name, *args):

        if args:
            currency = args[0]
        else:
            currency = self.currency

        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + \
            name+"&apikey="+self.apikey

        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())

        last_date = list(data["Time Series (Daily)"].keys())[0]
        price = float(data["Time Series (Daily)"][last_date]["4. close"])

        if currency is not "USD":
            price = self.convert_currency(price,"USD",currency)

        return({'price':price, 'currency':currency, 'name':name})


    def convert_currency(self, price, from_currency, to_currency):
        
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + \
            from_currency+"&to_currency="+to_currency+"&apikey="+self.apikey

        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())

        rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return (price * rate)

