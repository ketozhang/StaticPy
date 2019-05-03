---
title: Sampling without Replacement
---

## Symmetry

For these problems, we have a symmetry among ordered random variables.

1. The probability of the $i$-th random variable does not matter about order

    $$ P(X_i=x) = \frac{1}{n} $$

2. The probability of the multiple random variable does not care about order

    $$ P(\boldsymbol{X} = \boldsymbol{x}) = \frac{1}{n} \cdot \frac{1}{n-1} \cdots \frac{1}{n-k+1} $$

    * $\boldsymbol X$ : Random variable vector ordered by sequence
    * $\boldsymbol x$ : Outcomes in any order
    * $k$: Length of $\boldsymbol x$

## Hypergeometric Probability

For problem where you only care if there are $k$ number of a desired outcome (without care for order). The subset is length $G$, the outcome space is length $N$, and the number of sampling is $n$ (where $G \le N$). Let the random variable $X$ be the number of the desired subset (of size $G$) in the sample.

 Let $g\le n, g\in \mathbb N$, the hypergeometric series describe this probability,

$$ P(X=g) = \frac{\binom{G}{g} \binom{N-G}{n-g}}{\binom{N}{n}} $$

* This is used very often for simple random samples without replacement.