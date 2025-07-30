import pandas as pd
import numpy as np

# Calculates the returns of each trade
def calculate_returns(data):

    # Initialises the position and return variables
    # Position = 0 means we have no stock (out of the market)
    # Position = 1 means we have a stock (in the market)
    position = 0
    returns = []

    for i in range(len(data)):
        # If a buy signal has occured, saves the buy price and updates the position
        if not np.isnan(data['Buy'].iloc[i]) and position == 0:
            buy_price = data['Buy'].iloc[i]
            position = 1

        # If a sell signal has occured, saves the sell price and updates the position
        elif not np.isnan(data['Sell'].iloc[i]) and position == 1:
            sell_price = data['Sell'].iloc[i]
            position = 0

            # Calculates the return on this trade and adds it to the list
            returns.append((sell_price - buy_price)/buy_price)

    return returns

# Calculates various performance metrics of the strategy
def performance_metrics(returns):

    # Converst the returns list into a pandas series for easier calculations
    returns_series = pd.Series(returns)

    # Calculates the total returns of the strategy
    total_returns = (1 + returns_series).product() - 1

    # Calculates the average returns of the strategy
    avg_returns = returns_series.mean()

    # Calculates the number of trades
    num_trades = len(returns_series)

    # Calculates the Sharpe ratio
    sharpe = returns_series.mean() / returns_series.std()

    print(f"The total returns is: {total_returns}")
    print(f"The average returns is: {avg_returns}")
    print(f"The number of trades is: {num_trades}")
    print(f"The Sharpe ratio is: {sharpe}")
