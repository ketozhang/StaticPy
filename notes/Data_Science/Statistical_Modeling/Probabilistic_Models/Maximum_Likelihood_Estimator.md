---
title: Maximum Likelihood Estimator
---

The maximum likelihood estimator (MLE)

## Coin Example

Given a biased coin with probability $p$ to be heads and $1-p$ to be tails. Given $n$ flips we have $X=x$ heads following the binomial distribution which is going to be our likelihood function,

$$
X \sim B(n,p)
$$

$$
P(x \mid p) = {n \choose x} p^x (1-p)^{n-x}
$$

We want the optimal value $p^*$ that maximizes our the probability of our data $x$ (i.e., the number of heads observed). This is the definition of **maximum likelihood**.

$$
p^* = \mathop{\arg\max}_p{P(x \mid p)}
$$

## Gaussian

The parameters of the gaussian likelihood is of course its mean $\mu_c$ and variance $\sigma_c^2$ for each class $c$.

### Gaussian MLE Classifier
The solution for the QDA Gaussian classifier using MLE is,

$$
\hat\mu = \frac{1}{n} \sum_{i=1}^n X_i
$$

$$
\hat \sigma^2 = \frac{1}{dn} \sum_{i=1}^n |x_i - \hat\mu|^2
$$

For LDA Gaussian classifier using MLE,

$$
\hat\mu = \frac{1}{n} \sum_{i=1}^n X_i
$$

$$
\hat \sigma^2 = \frac{1}{dn} \sum_{c}\sum_{i : y_i = c}^n |x_i - \hat\mu_c|^2
$$