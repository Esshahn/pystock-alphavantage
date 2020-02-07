# pystocks-vanguard

Small class that retrieves stock prices via the Alpha Vantage API.

## Installation

No dependencies.

## Usage

The data is retrieved via the Alpha Vantage API: https://www.alphavantage.co/

You need an API key, it's free and you'll get it without email address confirmation: https://www.alphavantage.co/support/#api-key

Note that the API is limited to 5 requests per minute and 500 requests per day. If you get errors, too many requests might be the reason.

### Examples

````
from stocks import Stocks

apikey = "your api key"

stocks = Stocks(apikey)
res = stocks.price("AAPL")

print(f'{res["name"]} is at {res["currency"]}{res["price"]}')
````

The output of the print function would be:

`AAPL is at EUR288.34` 

In this case, we request the stock price for the symbol "AAPL" (which stands for Apple). The result `res` contains a dict with `name` (which is the same as the input symbol given), `currency`, which is per default `EUR` and the `price`, which is a float.

If you want the stock price in a different currency, you have two options:

`stocks.set_currency("USD")` - changes the default currency to `USD`

This is useful if you always want every result to be in the specified currency.

Alternatively you can add the currency directly in the price request:

`res = stocks.price("AAPL","JPY")` - which requests the stock price in `JPY` (Japanese YEN).

Finally, you can convert prices between currencies manually:

````
price_in_USD = 100
price_in_EUR = stocks.convert_currency(price_in_USD, "USD", "EUR")
````

## History

* 0.0.1
** Initial commit
 





