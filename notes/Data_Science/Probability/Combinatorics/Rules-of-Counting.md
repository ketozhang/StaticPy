---
title: Rules of Counting
---

Combinatorics is the study of counting a systems that can be represented as a finite sets.

## Without Replacement

A system without replacement can be counted either with permutation or combination,

1. **First Rule of Counting (Ordered Counting)**
    $$ C(n,k) = \frac{n!}{(n-k)!} $$

2. **Second Rule of Counting (Unordered Counting)**
    $$ P(n,k) = {n\choose k} = \frac{C(n,k)}{k!} $$

## With Replacement
Say there are a set of length $n$ and we wish to create subset of length $k$

### Third Rule of Counting (Ordered)

$$k^n$$

### Fourth Rule of Counting (Unordered)

$${k+n-1 \choose k} = \frac{(k+n-1)!}{k!(n-1)!}$$

#### Example
Let's say you want to invest into $k$ stocks of the $n$ companies. An outcome space can be generated out of the sequence of companies

$$\Omega = \set{\omega \mid \set{C_i}^k}$$

## Derangement

A derangement set $D$ of two sets $A$ and $B$ is,

$$ D = \set{(a,b) : a\in A,~ b\in B,~ a \neq b} $$

The size of the deranged set depends on three characteristics:

1. Are the elements of $D$ distinguishable
2. Are we sampling with or without replacement.
3. Are objects ordered or not.

$$ D_n \equiv \abs{D}$$
$$ D_n = (n-1) \cdot \left(D_{n-1} + D_{n-2}\right) $$

We can solve for this recursion letting $Q_n := D_n - nD_{n-1}$ and noticing $Q_n = -Q_{n-1}$ thus $Q_n = (-1)^{n}$ and then,

$$
\begin{gather*}
    \frac{Q_n}{n!} = \frac{D_n}{n!} - \frac{D_{n-1}}{(n-1)!} = \frac{(-1)^n}{n!}\\
    \frac{D_n}{n!} = \frac{D_{n-1}}{(n-1)!} + \frac{(-1)^n}{n!}\\\\
    \boxed{D_n = n!\sum_{i=0}^{n}\frac{(-1)^{i}}{i!}}\\
    \boxed{\lim_{n\rightarrow \infty} D_n = \frac{n!}{e}}
\end{gather*}
$$

## Useful Identities

$$ {n \choose k + 1} = {n-1 \choose k} + {n-2 \choose k} + \ldots + {k \choose k} $$
