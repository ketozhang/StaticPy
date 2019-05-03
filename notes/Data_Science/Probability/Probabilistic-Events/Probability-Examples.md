---
title: Probability Scenarios
---

## Degeneracy Problem

The degeneracy or distinct problem ask the question:

<center>***If there are $n$ trials which each trial choose from $N$ possible values, what are the chances that all trials are distinct***</center>

$$
\begin{align*}
    \#(\text{Outcome}) &= N^n\\
    P(\text{distinct}) &= \prod_{i}^n{\frac{N-i}{N}}\\
    P(\mathrm{degeneracy \ge 1}) &= 1 - \prod_{i}^n{\frac{N-i}{N}}
\end{align*}
$$

* Classicaly this is known as the **Birthday Problem**

### Small $N$ and Large $n$

For sufficiently small $N$ and large $n$, the probability can be approximated as,

$$
    P(\text{distinct}) \approx e^{\frac{-n^2}{2N}}
$$

For more accuracy and for any $n$,

$$
    P(\text{distinct}) \approx e^{\frac{(1-n)n}{2N}}
$$

## Derangement Problem

Let $A_1,A_2,\ldots,A_n$ be the set of outcomes such that $i$th position of a sequence is a fixed point (e.g., the $i$th key is use on the $i$th box).

A **derangement** is defined as the set of outcomes such that there are no fixed point. It is much easier to define this with a random variable $X$ which counts the number of fixed point. The derangement is when $X=0$. Let the cardinality of the derangement be $D_n$,

$$ D_n = n! - \abs{\bigcup A_k} $$

$$ \abs{\bigcup A_i} = \sum_{k=1}^n (-1)^{k-1}{n \choose k}(n-k)! $$

$$\boxed{D_n = n! \sum_{k=2}^n \frac{(-1)^k}{k!}}$$