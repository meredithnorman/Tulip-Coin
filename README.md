# Tulip-Coin

This function is my strategy to maximise profits from trading the dynamic Tulip coin (see outline below). <br>
<img width="397" alt="image" src="https://github.com/user-attachments/assets/a74e69dc-a591-4a0c-bd4f-3dd0dea1bf67">
<br>
My function implements the following strategies:
<br> -> It buys when the cost of coins is increasing (slope >0) and the current price is greater than the weighted average. This is a more robust way of hopefully ensuring that the price should continue to increase.
<br> -> It sells when the price is at 35% higher than the bought price - this ensures at least 35% profit is made every sale. This explains why there are some identical asset values in the graph above.
<br> -> After buying, the next action must be selling, this stops the function from consistently buying. 
<br> -> At each buy/sell, 53% of my assets are exchanged. This is chosen as a fairly conservative, but slightly risky percent. Potentially also because 53 is my favourite number :) 

<br> The main down fall of my strategy is the limitation that coins will only be sold if 35% profit is made, so if the coins are purchased when the price is at an all time peak, there may never be an opportunity for the coins to be sold. This function will be pitted against other trading strategies to see who has the most profitable strategy. I am not feeling very confident in my strategy but it has been a fun journey.  

<br> My function was tested using excellent simulation code from: https://github.com/a-s-russo/tulip-coin/blob/main/simulation.py

This yielded the following asset values across 50 simulations:
![mean](https://github.com/user-attachments/assets/0783c3ab-d7b0-416a-9a04-fb7085488709)





