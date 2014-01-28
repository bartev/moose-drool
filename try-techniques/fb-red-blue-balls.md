Best distribution of blue and red balls
========================================================

FB interview question
1/16/14

- You have 100 marbles, 1/2 are red, and the other 1/2 are blue.
- Place the balls in 2 bags such that you maximize the probability of picking
a blue ball.
- Assume the probability of picking each bag is the same  
P (blue) = P (blue|bag1)P (bag1) + P (blue|bag2)P (bag2)  
= 1/2 × [P (blue|bag1) + P (blue|bag2)]  

So we want to maximize  
P (blue|bag1) + P (blue|bag2) 

Caution: Don’t assume you have the same number of balls in each bag! define  
b = number of blue balls in bag 1 (5) r = number of red balls in bag 1 (6)  
P (blue|bag1) = b (7) b+r  
P (blue|bag2) = 50 -b (8) (50−b)+(50−r)  
