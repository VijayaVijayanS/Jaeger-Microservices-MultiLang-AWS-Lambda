import alpaca_trade_api as tradeapi

# Replace with your Alpaca API key and secret

API_KEY = "PKQXY66TMDHLUTYEWVXG"

API_SECRET = "YNYnaq3s80lgN5MAb2E4QQmyePWr49kFHL6XU6aq"

api = tradeapi.REST(API_KEY, API_SECRET, base_url="https://paper-api.alpaca.markets")


def sell_stock(symbol, qty):
    try:

        api.submit_order(

            symbol=symbol,

            qty=qty,

            side="sell",

            type="market",

            time_in_force="gtc"

        )

        print(f"Sold {qty} shares of {symbol}")

    except tradeapi.rest.APIError as e:

        print(f"Failed to sell: {e}")


def main():
    symbol = input("Enter stock symbol to sell: ").upper()

    qty = int(input("Enter quantity to sell: "))

    sell_stock(symbol, qty)


if __name__ == "__main__":
    main()
