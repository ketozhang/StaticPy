---
title: Poisson Distribution
---

$$
P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}
$$

* **Expected Value**
    $$\mathbb E[X] = \lambda$$
* **Variance**
    $$\text{Var}[N] = \lambda$$
* **Sums**
    $$\sum{X_i} \sim \text{Poisson}\left(\sum \lambda_i\right)$$

## Limit of the Binomial Distribution

The poisson distribution can be derived by the limit of the binomial distribution. Let $np = \lambda$ where $\lambda$ is set constant. Let $n$ head to infinity and $p$ to zero.

Hence you may interpret the Poisson distribution as the binomial distribution of a rare event in the limit of large number of trials.

$$
\begin{gather*}
    P_k = P(X=k) = {n \choose k}p^k(1-p)^{n-k}\\
    P_0 \approx e^{-\lambda}\\
    \frac{P_k}{P_{k-1}} \approx \frac{\lambda}{k}\\
    P_k = P_0 \prod_{l=1}^k \frac{P_l}{P_{l-1}} \approx e^{-\lambda}\frac{\lambda^k}{k!}
\end{gather*}
$$

## Interval of the Exponential Distribution

Given two poisson that covers seperate interval of its random variable,

$$  $$