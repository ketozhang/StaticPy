---
title: Sampling Probability
---

A sampling probability is often one at which follows these sampling rules. For $N$ individuals we wish gather the individuals into $n$ subsets:

1. Each sample cannot be picked more than once (no replacement)
2. Order does not matter

The probability of a given subset following these two rules being chosen can be solved two ways:

## Brute Force - Number of Configurations

The brute force methods requires the knowledge of all possible configurations. This is the method that is often first taught in statistics and following our rules it sounds like we have to use **combination** (order does not matter). Recall the combination is defined as the number of configuration of group one can make with $n$ things and each group has $k$ things. Combination also simply quoted as the "$n$ choose $k$" function which is,

$$\boxed{ \begin{pmatrix}
    n \\ k
\end{pmatrix} = \frac{n!}{k!(n-k)!}}$$

---

Example
: The population of the data is $N=10$, if you were to group the population into pairs ($k=2$) how many groups can you make?

$$ \begin{pmatrix}
    N \\ k
\end{pmatrix} = \begin{pmatrix}
    10 \\ 2
\end{pmatrix} = \frac{10!}{2!8!} = \frac{9\cdot 10}{2}  = \boxed{45 \text{ pairs}}$$

---

Back to the sampling problem. Here the number of things are subsets and the the groups are the sample. We wish to ask what is the probability of the sample contain a certain subset. Let's call this particular subset $A$,

$$P(A) = \frac{\text{Samples with A}}{\text{Total Posible Samples}}$$ 

---

Example
: The sample are once again in pairs, but now my subsets are marked from $A$ to $Z$ ($n=26$), what is the probability of choosing $A$ as part of my sample?


$$ C_\text{pairs} = \begin{pmatrix}
    n \\ 2
\end{pmatrix} = \frac{n!}{2!(n-2)!}$$

$$ C_A = \begin{pmatrix}
    n-1 \\ 1
\end{pmatrix} = n-1 \tag{Pairs with A}$$

$$
P(A) = \frac{C_A}{C_\text{Pairs}} = \frac{2!(n-2)!(n-1)}{n!}
$$

## Probability by Recursion

You may also find the probability by multiplying

$$ \mathcal{P}(A) = P(A) \cdot P(\neg A) $$