---
title: Random Variable
---

Formally, the **random variable** is defined as a function that maps the outcome space to the real space,

$$
    X : \Omega \to \mathbb R\\
    \big\downarrow \\
    X(\omega_i) = x_i \in \mathbb R
$$

* We can further define as outcome set in real space as $\Omega_X$ which is the result of,

    $$
        \Omega \stackrel{X}{\longrightarrow} \Omega_X\\
        \Omega_X \equiv \set{x: X(\omega \in \Omega)}
    $$

* If an event $A \subseteq \Omega$ occurs in outcomes space then a corresponding event $A' \subseteq \mathbb{R}$ occurs in real space such that,

    $$
        X : A \rightarrow A'\\
        A' = X \in A' = \set{x : x = X(\omega) \in A'}
    $$

## Distribution

The random variable carries the information of the probability distrubtion such that there always exist the probability function for all $x \in \Omega_X$ denoted as:

$$
    P_X(x) \text{ or } P(X=x)
$$

### Equivalence of Two Random Variables

Two random variables $X$ and $Y$ are equivalent only if they represent the same space in the outcome space. However in most cases, $X$ and $Y$ represent two different trials (e.g., first flip and second flip). In this case the two random variables can only be equal in distribution denoted as,

$$
    X \stackrel{d}{=} Y\\
    X \ne Y
$$
