import yfinance as yf


class StockPortfolio:
    """This class represents a stock portfolio that can track holdings and update prices."""

    def __init__(self, filename=None):
        """
        Initializes an empty stock portfolio. Will also give the option to load previous data
        Args:
           filename (str): This gives the option to load a .txt file with old saved data
        """
        print(f"Filename received in __init__: {filename}") # Debugging statement
        self.stocks = {}  # Dictionary to store stock symbols and their quantities
        if filename:
            self.load_portfolio(filename)

    def load_portfolio(self, filename):
        """
        This loads initial stock holdings from .txt file
        Expect format as: 
        symbol quantity [price] # prices are optional
        
        Args: 
            filename (str): The path to the .txt file
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    symbol, quantity, price_str = line.strip().split(',')
                    quantity = int(quantity)
                    price = float(price_str) if price_str else None # handles optional price
                    self.add_stock(symbol, quantity, price) # Add price if provided
                print(f"Successfully loaded portfolio from {filename}")
        except FileNotFoundError:
            print(f"Error: file File '{filename} not found. Starting with empty portfolio.")
        except ValueError:
            print(f"Error parsing portfolio data in '{filename}'. Skipping invalid line.")
            
    def add_stock(self, symbol, quantity, price=None):
        """
        Adds a stock to the portfolio or increases the quantity of an existing stock.

        Args:
            symbol (str): The stock symbol (e.g., AAPL, GOOGL)
            quantity (int): The number of shares to add
        """
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
            if price is not None: # Provides update price if .txt file is loaded
                self.stocks[symbol] = price
        else:
            self.stocks[symbol] = (price, quantity) if price is not None else quantity

    def remove_stock(self, symbol, quantity):
        """
        Removes a stock from the portfolio or reduces the quantity of an existing stock.

        Args:
            symbol (str): The stock symbol
            quantity (int): The number of shares to remove

        Raises:
            ValueError: If the quantity to remove exceeds the available quantity.
        """
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
        """
        Updates the current prices for all stocks in the portfolio using yfinance.

        Prints any errors encountered during price updates.
        """
        for symbol in self.stocks:
            try:
                # Download stock information using yfinance
                stock_info = yf.Ticker(symbol)
                # Get the latest closing price for the day
                latest_price = stock_info.history(period="1d")["Close"][0]
                # Update the stock price in the portfolio
                self.stocks[symbol] = latest_price
                print(f"Successfully updated price for {symbol}: ${latest_price:.2f}")
            except Exception as e:
                print(f"Error updating price for {symbol}: {e}")

    def print_portfolio(self):
        """
        Prints the current state of the portfolio, including symbols, quantities, and total value.
        """
        print("Stock Portfolio:")
        total_value = 0
        for symbol, quantity in self.stocks.items():
            current_price = self.stocks[symbol]
            stock_value = quantity * current_price
            total_value += stock_value
            print(f"{symbol}: {quantity} shares @ ${current_price:.2f} = ${stock_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")
    def save_portfolio(self, filename):
        """
        This will save the current portfolio data to a text file.
        Args: 
            filename (str): This is the path to the .txt file for saving."""
        try:
            with open(filename, 'w') as file:
                for symbol, quantity in self.stocks.items():
                    price = self.stocks.get(symbol, None) #Retrieves price values
                    file.write(f"{symbol},{quantity},{price if price is not None else ''}\n")
            print (f"Successfully saved portfolio data to {filename}")
        except Exception as e:
            print(f"Error saving portfolio data: {e}")
def main():
    choice = input("Do you want to load an existing portfolio (y/n) or create a new one? ")
    filename = None 
    if choice.lower() == 'y':
        filename = input("Which file would you like to open? ")

    portfolio = StockPortfolio(filename)


    # Add initial stocks to the portfolio
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.add_stock("MSFT", 8)

    # Print initial portfolio
    portfolio.print_portfolio()

    # Update prices for all stocks and print success/error messages
    portfolio.update_prices()

    # Print updated portfolio with current prices and total value
    portfolio.print_portfolio()

    # Remove some shares from a stock
    portfolio.remove_stock("AAPL", 3)

    # Print portfolio after removal
    portfolio.print_portfolio()

    # Save portfolio data to a .txt file 
    portfolio.save_portfolio("my_portfolio.txt")


if __name__ == "__main__":
    main()
