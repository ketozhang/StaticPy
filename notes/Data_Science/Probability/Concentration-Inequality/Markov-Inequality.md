---
title: Markov's Inequality
---

## First Moment Markov's Inequality

Markov's inequality at its simplest deals with the mean or first moment of the distribution. Suppose $X \ge 0$ and $\abs{\mathbb E[X]} < \infty$, for any constant $c$,

$$
P(X \ge c) \le \frac{\mathbb E[X]}{c}
$$

Proof
: Consider the following lemma:

    $$
    \begin{gather*}
        X \ge c I \set{X \ge c}
        \mathbb E[X] \ge c \mathbb E[I \set{X \ge c}]\\
        \mathbb E[X] \ge c P(X \ge c)\\\\
        P(X \ge c) \le \frac{\mathbb E[X]}{c}
    \end{gather*}
    $$

## Markov's Inequality - Monotonically Increasing Function

To generalize the simple Markov's inequality, we allow the first moment to be of any monotonically increasing function $\varphi(X)$,

$$
P(X \ge c) \le \frac{\mathbb E[\varphi(X)]}{\varphi(c)}
$$

### General Moment Markov Inequality

Any $k$-th moment is also a monotonically increasing function thus w e can generalize the moment to any $k$,

$$
P(X \ge c) \le \frac{\mathbb E[X^k]}{c^k}
$$