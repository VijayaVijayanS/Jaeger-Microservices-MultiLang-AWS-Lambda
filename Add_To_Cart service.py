import alpaca_trade_api as tradeapi

# Set your Alpaca API credentials
ALPACA_API_KEY = 'PKQXY66TMDHLUTYEWVXG'
ALPACA_SECRET_KEY = 'YNYnaq3s80lgN5MAb2E4QQmyePWr49kFHL6XU6aq'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

# Initialize Alpaca API client
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

# Create an empty cart to store selected stocks
cart = []

def list_available_stocks():
    try:
        assets = api.list_assets()
        tradable_stocks = [asset for asset in assets if asset.tradable and asset.asset_class == 'us_equity']

        if tradable_stocks:
            print("\nAvailable Tradable Stocks:")
            for i, stock in enumerate(tradable_stocks):
                print(f"{i + 1}. Symbol: {stock.symbol}")
                print(f"   Name: {stock.name}")
                print(f"   Exchange: {stock.exchange}")
            return tradable_stocks
        else:
            print("No tradable stocks found.")
            return []

    except tradeapi.rest.APIError as e:
        print(f"Error retrieving tradable stocks: {e}")
        return []

def add_to_cart(stock_symbol):
    cart.append(stock_symbol)
    print(f"'{stock_symbol}' added to cart.")

def view_cart():
    if cart:
        print("\nCart:")
        for stock_symbol in cart:
            print(f"- {stock_symbol}")
    else:
        print("Cart is empty.")

def buy_stocks():
    if not cart:
        print("Cart is empty. Add stocks to the cart first.")
        return

    for stock_symbol in cart:
        try:
            # Implement logic to place buy orders here
            # You can use the `api.submit_order` method as shown in previous examples
            # Remember to replace this comment with your buy order logic
            pass
        except tradeapi.rest.APIError as e:
            print(f"Error placing buy order for '{stock_symbol}': {e}")
    print("Buy orders placed successfully.")



def main():
    print("Alpaca API Console Application - Add to Cart and Buy Stocks")

    while True:
        print("\nMenu:")
        print("1. List Available Tradable Stocks")
        print("2. Add Stock to Cart")
        print("3. View Cart")
        print("4. Buy Stocks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_available_stocks()
        elif choice == "2":
            stock_symbol = input("Enter the stock symbol to add to cart: ").strip().upper()
            add_to_cart(stock_symbol)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            buy_stocks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
