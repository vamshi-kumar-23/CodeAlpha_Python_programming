#  Stock Portfolio Tracker 
# Author: Battu Vamshi Kumar

# Step 1: Hardcoded stock prices bro
def track_portfolio():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOG": 140.0,
        "AMZN": 130.0,
        "MSFT": 390.0
    }
    
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    
    # 2. Get user input and convert it to uppercase so it matches the dictionary
    stock_name = input("\nEnter the stock ticker (e.g., AAPL): ").upper()
    
    # 3. Check if the stock exists in our dictionary
    if stock_name in stock_prices:
        try:
            # Get the quantity and convert it to a whole number (integer)
            quantity = int(input(f"How many shares of {stock_name} do you own? "))
            
            # 4. Calculate the total value
            price_per_share = stock_prices[stock_name]
            total_value = quantity * price_per_share
            
            # 5. Display the final result
            print(f"\n--- Portfolio Summary ---")
            print(f"Stock: {stock_name}")
            print(f"Shares: {quantity}")
            print(f"Current Price: ${price_per_share}")
            print(f"Total Investment Value: ${total_value}")
            
        except ValueError:
            # This handles the error if the user types a word instead of a number
            print("Error: Please enter a valid number for the amount of shares.")
    else:
        print("Sorry, that stock is not in our database right now.")

# Run the function
track_portfolio()