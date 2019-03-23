---
title: Error Correcting Code
---

Let a bit sequence be $m_1,m_2,\ldots,m_n$ of $n$ bits.
We will be dealing with two types of errors:

1. **Erasures**: If up to $k$ of the $m_i$ messages gets corrupted and we know exactly which message.
2. **General Errors**: If up to $k$ of the $m_i$ messages get corrupted and we don't know which message.

## Erasures

To insure that if $k$ bits were dropped we would know how to recover the information, we need to send an extra $k$ bits of data through the channel.

1. Let $q > n + k$ be a large prime so all packages are in mod $q$.

2. Let $P(x)$ be the unique polynomial of degree $n-1$ in mod $q$ that goes through the our message as points $(i, m_i)$ such that $P(i) = m_i$ for $1 \le i \le n$

3. Let's send $k$ more messages $P(i) = m_i$ for $n < i \le k$ as insurance.

4. With any $n$ of these $n+k$ messages we can reconstruct $P(i)$ thus we're able to recover the original messages.

## General Errors

We will send $2k$ extra redundant messages.

1. Let $q > n + 2k$ be a large prime.
2. Let $P(i)$ be a unique degree $n-1$ polynomial in mod $q$ that goes through $n+2k$ points of $(i, m_i)$ for $1 \le i \le n + 2k$.
3. If any up to $k$ messages got corrupted we can find a polynomial $Q'(i)$ that goes through $n+k$ recieved points (denoted as $r_i$). We define this polynomial specially as a product of the original polynomial $P(i)$ and the error-locating polynomial $E(i)$ of degree $k$ defined as,

    $$
    \begin{gather*}
        E(i) = (i-e_1)(i-e_2) \ldots (i-e_k)\\
        Q(i) = E(i)P(i)
    \end{gather*}
    $$

    The error-locating polynomial is zero when an corrupted input $i$ is given.

    $$
        P(i)E(i) = r_i E(i)
    $$

    Now $Q(i)$ can be solved because we have $n+k$ points, along with $E(x)$ together.

    $$
    \begin{gather*}
        Q(i) = a_{n+k+1}x^{n+k+1} + \ldots + a_0\\
        E(i) = x^{k} + b_{k-1}x^{x-1} + \ldots + b_0
    \end{gather*}
    $$

    When $b_0$ is solved, the error location is $b_0 \bmod p$. Now we can solve for $P(i)$,

    $$ P(i) = \frac{Q(x)}{E(x)} $$

