# Tulip-Coin

This function is my strategy to maximise profits from trading the dynamic Tulip coin (see outline below). <br> <br>
<img width="397" alt="image" src="https://github.com/user-attachments/assets/a74e69dc-a591-4a0c-bd4f-3dd0dea1bf67">
<br>
<br>
My function implements the following strategies:
<br> -> It buys as many coins as possible in the first 7 minutes as this is when the coins will likely be cheapest. 
<br> -> After 7 minutes, it then sells in the price is over $6 and buys if the price is less than $4, this guarantees at least 50% profit. 
<br> -> In the last 10 minutes I stop buying and sell if the price is over $5.  
<br> -> At each buy I spend 30% of my funds, and in each sell, I sell 20% of the coins. This is fairly conservative and not as risky as @a-s-russo who gives everything 100%.

<br> My function was tested using excellent simulation code which informed some of my parameter choices from: https://github.com/a-s-russo/tulip-coin/blob/main/simulation.py

This yielded the following asset values across 50 simulations:
![9 7mil](https://github.com/user-attachments/assets/0b1a0a81-1bda-4a1b-bba3-e94f53daf778)

<br> <br>
This function was pitted against other trading strategies to see who had the most profitable strategy. Overall my function gave me the second highest profit of around $45,000, only 1.995 million behind @a-s-russo. I was super happy with this and it was great fun using the simulation code to refine my strateegy. Such fun :) 




