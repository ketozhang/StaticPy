---
title: Introduction
---

Let the chain be a set of random variables with element $X_t$ for the $ith$ step (or link) of the chain.

## Two-State Markov Chain

Consider the initial state be the random variable that can take in the binary value $X_0(\set{a,b}) = \set{0,1}$ with probability $P_a(0), P_b(0)$. Any subsequent steps the probability now depends on the current state. You can imagine a finite state diagram (aka state transition diagram) with transition probability $P_{ij}(t)$ from the current state $i$ to the next state $j$ at iteration $t$. We can form this into a matrix where the column represent all the possible state from to and the row represent all the possible state to transition to.

$$
P =
\begin{bmatrix}
    P_{aa} & P_{ab}\\
    P_{ba} & P_{bb}
\end{bmatrix} =
\begin{bmatrix}
    P_{aa} & 1-P_{aa}\\
    1-P_{bb} & P_{bb}
\end{bmatrix}
$$

## Probability of State

The probability of a state in some iteration $t$ is the state $i_n$,

$$ \mathbb P(X_t = i) = \mathbb P_i(t) = \left[\vec P(0)  P^t\right]_{i} $$
$$\vec P(t) = \vec P(0) P^t$$

* $\vec P(0)$ : Initial state vector
* $P$ : Transition Probability matrix (constant throughout iteration)

## First Step Equation

The average time $\tau = \avg{t}$ it takes for some state in all the possible states ($i \in \Omega$) to end up in some subset of that state ($\Omega_f \subset \Omega$) is given by the **first step equation**:

$$ \tau(f) = 0 \qquad f \in \Omega_f$$
$$ \tau(i) = 1 + \sum_{j \in \Omega} P_{ij}\tau(j) $$

* The problem of average time to reach some state $f$ in Markov chain is called the **Hitting Time** problem.

## Probability of Hitting One Before the Other

Let $\Omega_A$ and $\Omega_B$ be two disjoint subsets of $\Omega$. The probability $\alpha(i)$ that starting at the initial state $i \in \Omega$, we reach a state in $\Omega_A$ before $\Omega_B$ is:

$$
\begin{align*}
    \alpha(a) = 1 \quad &a \in \Omega_A\\
    \alpha(b) = 0 \quad &b \in \Omega_B\\
    \alpha(i) = \sum_{j\in\Omega} P_{ij}\alpha(j) \quad &i \not\in \Omega_A \cup \Omega_B
\end{align*}
$$

## Stationary Distribution

When running the Markov chain we can end up at some state $i$ at some iteration $t$ such that the distribution $P_i(t)$ is stationary meaning it's invariant under the transition probability matrix $P$:

$$
P_i(t) = P_i(t)P
$$

Formally we have the **theorem:**

$P(t_0)$ is invariant if and only if the distribution,

$$
\vec P(t) = \vec P(t_0) \qquad t \ge t_0\\
$$