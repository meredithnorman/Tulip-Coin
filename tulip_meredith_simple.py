def tulip_coin_strategy(history):
    if not history.empty:
        current_price = history.iloc[-1]['price_history']
        minutes_remaining = history.iloc[-1]['minutes_remaining']
        proportion=0.0
    
        if minutes_remaining>=53:       #at the first opportunity you get, buy everything as it is surely the cheapest it will be. Surely there will be a chance to buy in the first 7 minutes.
            decision='buy'
            proportion=1
        
        elif 10<=minutes_remaining<53:
            if current_price>6:
                decision='sell'
                proportion=0.20
            elif current_price<4:
                decision='buy'
                proportion=0.30
            else: 
                decision='hold'
                proportion=1
        
        elif 5<=minutes_remaining<10:
            if current_price>5:
                decision='sell'
                proportion=1
            else: 
                decision='hold'
                proportion=1
    
        elif 0<=minutes_remaining<5:
            if current_price>4:
                decision='sell'
                proportion=1
            else:
                decision='hold'
                proportion=1
    
        return decision, proportion
        
    return 'hold', 1

