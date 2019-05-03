## Random Variable

Formally, the **random variable** is defined as a function that maps the outcome space to the real space,

$$
    X : \Omega \to \mathbb R
$$

### Random Variable as a Set

As a set, the random variable the result of mapping the outcome space to the real space $X = \set{x_1, x_2, \ldots, x_n},~~ x_i \in \mathbb{R}$

An event occuring in the outcome space $A \subseteq \Omega$ corresponds to an event occuring in the real space $A' \subseteq X$ (limited to the subspace of $X$) such that,

$$
    X \cup A' = \set{x : x \in A'}\\
    A' = X \cup A'
$$

We can get some intution for these two concepts with the equation for the norm of a probabilistic being 1:

$$
    \sum_{x\in X} P(x) = 1 \tag{2nd Axiom}
$$

### Random Variable as a Function

$$
    X(\omega_i) = x_i \in \mathbb R
$$

If an event $A \subseteq \Omega$ occurs in outcomes space then a corresponding event $A' \subseteq \mathbb{R}$ occurs in real space such that,

$$
    X : A \rightarrow A' \equiv \set{X \in A'} = \set{\omega : X(\omega) \in A'}\\
    A' = X \in A'
$$