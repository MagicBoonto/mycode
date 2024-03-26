import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] > quantity:
                self.stocks[symbol] -= quantity
            elif self.stocks[symbol] == quantity:
                del self.stocks[symbol]
            else:
                print("Error: Quantity to remove exceeds the available quantity.")
        else:
            print("Error: Stock symbol not found in the portfolio.")

    def update_prices(self):
        for symbol in self.stocks:
            try:
                stock_info = yf.Ticker(symbol)
                latest_price = stock_info.history(period="1d")["Close"][0]
                self.stocks[symbol] = latest_price
            except Exception as e:
                print(f"Error updating price for {symbol}: {e}")

    def print_portfolio(self):
        print("Stock Portfolio:")
        for symbol, quantity in self.stocks.items():
            print(f"{symbol}: {quantity}")

def main():
    portfolio = StockPortfolio()

    # Add initial stocks to the portfolio
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.add_stock("MSFT", 8)

    # Print initial portfolio
    portfolio.print_portfolio()

    # Update prices
    portfolio.update_prices()

    # Print updated portfolio
    portfolio.print_portfolio()

    # Remove stocks
    portfolio.remove_stock("AAPL", 3)

    # Print portfolio after removal
    portfolio.print_portfolio()

if __name__ == "__main__":
    main()

