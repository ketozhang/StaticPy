---
title: Cross Entropy
---

The cross entropy is a loss function for data that are naturally in the probability space. To explain **entropy**, we need the quantity called **surprise** which is the quanitty that can be interpreted as the surprise one feels if an event occurs if that even has probability $P(Y=c)$:

$$
-\log_2 P(Y=c)\\
|\log_2 P(Y=c)|
$$

The entropy is the average of surprise of the outcome space $C$.

$$
H(S) = - \sum_{c \in C} P(Y=c) \log_2 P(Y=c)
$$

However, the average surprise being entropy is probably not a great interpretation. Let's look at some edge cases for the entropy:

* All points are same class $c$ : $H(S) = 0$
* Half points are in class $c=1$ and the other $c=0$ : $H(S) = 1$
* All $n$ points are different classes: $H(S) = \log_2 n$

Hence the entropy can be interpreted as the bitsize needed to represent the possible classes.