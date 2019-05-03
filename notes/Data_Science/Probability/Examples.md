---
title: Examples
---

## Bootstrap Problem
Consider a population of size $n$ and a boostrap sample of size $N$. The variations of this problem are all either with or without replacement.

1. Without replacement, let the population be consist of males and females such that $n=m+f$. What is the probability of getting $M=k$ males?

    $$ P(M=k) = \frac{}{} $$

2. With replacement, if $N=n$ what is the probability that the bootstrap consist of everyone from the original pouplation.

    There are $n!$ ways to shuffle $n$ unique amount of people. The length of the outcome space is $n^n$,

    $$ P(\text{all unique}) = \frac{n!}{n^n}$$

## Shuffling Problem

Consider a deck of $n=52$ conventional cards shuffled randomly. The variations of this problem are all without replacement.

1. What is the probability that the first card picked is the ace of spades?

    Consider all situation where the ace of spades is on the first card. Permutate the rest and you'll get the number of outcomes that ace of spades is first.

$$
    P(\Omega_1 = A\spadesuit) = \frac{(n-1)!}{n!} = \frac{1}{n}
$$

2. What is the probability that the $k$-th card is the ace of spades?

    The position of the card doesn't matter. We will still use the same strategy before.

    $$
    P(\Omega_k = A\spadesuit) = \frac{(n-1)!}{n!} = \frac{1}{n}
    $$

3. What is the probability that the first $k$-th card is spades?

    There are $N=13$ spades in a deck. There are two ways to solve this problem:

    1. $$P(k) = \frac{N}{n} \cdot \frac{N-1}{n-1} \cdots \frac{N-k+1}{n-k+1} = \frac{N!}{n!}\frac{(n-k)!}{(N-k)!}$$

    2. $$P(k) = \frac{\binom{N}{k}\binom{n-N}{n-k}}{n!}$$

## Min-Max Problem

Consider a six-sided die rolled $n$ times.

1. What is the probability that the minimum roll observed is $m$ ($\min = m$) ?
    Using combinatorics iterating through the event that $k$ of the rolls is exactly $X=m$ while $n-k$ rolls are $X>m$ gives the binomial distribution,

    $$ P(\min = m) = \sum_{k=1}^k {n \choose k} \left(\frac{1}{6}\right)^k\left(\frac{6-m}{6}\right)^{n-k}$$

1. What is the probability that the minimum roll observed $\min$ is at least $m$ ?


    $$ P(\min \ge m) = P\left(\bigcap{i=1}^n X_i \ge m\right) = \left(\frac{6-(m-1)}{6}\right)^n $$

1. What is the expected value of $\min$?
    Use the tail sum formula with part 2

    $$ E[\min] = \sum_{m=1}^6 P(\min \ge m) $$