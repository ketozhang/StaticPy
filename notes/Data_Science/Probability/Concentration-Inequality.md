---
title: Concentration Inequality
---
Bound on random variable deviates from some value.

$$
P(\abs{Y} \ge c) \le \frac{\mathbb E[\abs{Y}^k]}{c^k}
$$

## Chebyshev's Inequality

Suppose $X$ has a finite mean then its deviation from the mean follows,

$$
P(\abs{X-\mathbb E[X]} \ge c) \le \frac{\text{Var}[X]}{c^2}
$$

* This inequality follows from Markov's inequality

In terms of the number of standard deviations ($\sigma$),

$$
P(X - \mathbb E[X] \ge n\sigma) = \frac{1}{n^2}
$$

## Law of Large Numbers

For a sequence of iid random variables $X_1,\ldots,X_n$ let the **sample mean** be defined as,

$$ \bar{X} = \frac{1}{n}\sum{X_i} $$

As $n \rightarrow \infty$, the probability that the sample mean deviates from the population mean $\mu$ absolutely by some positive error $\epsilon$ tends to,

$$ P\left[\abs{\bar{X}- \mu} < \epsilon \right] \rightarrow 1 $$

## Tail Sum Formula

Let $X$ be with range of $\mathbb N$ then,

$$ \mathbb E[X] = \sum_{a=1}^{\infty} P(X \ge a) $$