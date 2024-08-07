import pandas as pd
import numpy as np


def my_strategy(history):
    # Initialize decision variables
    decision = 'hold'
    proportion = 0.0
    if not history.empty:
        current_price = history.iloc[-1]['price_history']
        minutes_remaining = history.iloc[-1]['minutes_remaining']
        proportion=0.0

    # Use the last minute (12) of transactions to calculate the weighted average of prices. 
    # I'm thinking weighted average might be more useful as the most recent prices would be more relevant and there may be heaps of fluctuation
    recent_transactions = history.tail(12)
    weights = np.arange(1, len(recent_transactions) + 1)
    weighted_average_price = np.average(recent_transactions['price_history'], weights=weights)
    
# Calculate the trend using the slope of a linear regression line through the prices
    x = np.arange(len(recent_transactions))
    y = recent_transactions['price_history'].values
    slope, _ = np.polyfit(x, y, 1)

#Static variable to track the most recent sell price
    if not hasattr(my_strategy, "most_recent_buy_price"):
        my_strategy.most_recent_buy_price = 0.0  # Initialise static variable
    if not hasattr(my_strategy, "last_action"):
            my_strategy.last_action = 'sell'  # Initialize static variable to 'sell' to ensure first action is 'buy'

    if minutes_remaining <= 60:
        if my_strategy.last_action == 'sell' and current_price>weighted_average_price and slope>0:  #so pretty much if it is increasing, hopefully these two conditions make it robust.
            decision='buy'
            proportion=0.53
            my_strategy.most_recent_buy_price = current_price
            my_strategy.last_action = 'buy'
        elif current_price>1.35*my_strategy.most_recent_buy_price:    #selling if you have made at least 35% profit
            decision='sell'
            proportion=0.53
            my_strategy.most_recent_buy_price = 0  
            my_strategy.last_action = 'sell'
        else:
            decision = 'hold'
            proportion = 0.0
    return decision, proportion