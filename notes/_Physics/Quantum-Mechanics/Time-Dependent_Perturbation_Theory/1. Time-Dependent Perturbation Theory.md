---
title: Time-Dependent Perturbation Theory
---

<!-- TOC -->

- [System of Two Eigenvalues](#system-of-two-eigenvalues)
    - [Proof](#proof)
- [Example - Sinusoidal Perturbations](#example---sinusoidal-perturbations)

<!-- /TOC -->

The **Time Dependent Perturbation Theory (TDPT)** solve for the perturbed hamiltonian as a function of time $H'(t)$ such that the full wavefunction $\Psi(x,t)$ (or simply $\Psi(t)$) now has a time-dependent probability coefficient,

$$
\begin{equation}
    \Psi(t) = \sum_k{c_k(t)\psi_k e^{\frac{-iE_k t}{\hbar}}}
\end{equation}
$$

For some given Hamiltonian $H = H^0 + H'$. $\Psi(t)$ should satisfies the TDSE where,

$$ H\Psi = i\hbar \frac{\partial \Psi}{\partial t} $$

Note that the goal of TDPT is to solve for $c_k(t)$ for each wavefunction which determines the probability of measuring the wavefunction at some given time $t$.

## System of Two Eigenvalues
For a system of two eigenvalues $H^0\psi_a = E_a$ and $H^0\psi_b = E_b$, we can write a nice solution for $c_k(t)$ which is,

$$
\begin{gather}
    \boxed{\dot c_a = -\frac{i}{\hbar}\left[c_aH'_{aa} + H'_{ab}e^{i\omega_{ba} t}c_b\right], \qquad \dot c_b = -\frac{i}{\hbar}\left[c_bH'_{bb} + H'_{ba}e^{i\omega_{ba} t}c_a\right]}\\
    H'_{ij} = \bra{\psi_i}H'\ket{\psi_j} \\
    \omega_{ba} \equiv \frac{E_b - E_a}{\hbar}
\end{gather}
$$

* In many cases the diagonal matrices are zero $H_{aa}' = H_{bb}' = 0$

### Proof
Plugging in the wavefunction $\Psi(t)$ into the TDSE we find that,

$$ \begin{equation}
    \boxed{\dot c_a^n = -\frac{i}{\hbar}H'_{ab}e^{i\omega_{ba} t}c_b^{(n-1)}, \qquad \dot c_b^n = -\frac{i}{\hbar}H'_{ba}e^{i\omega_{ba} t}c_a^{(n-1)}}
\end{equation} $$

Unfortunately we cannot simply integrate by time to get $c_a$ or $c_b$ noticing that both formula is dependent on each other. To solve this consider the intial state that the system in definitely in state $\psi_a$ but not $\psi_b$ this means:

$$ c_a(0) = 1 \qquad c_b(0) = 0 $$

We apply this to the zeroth order to find $c_a^0(t)$, $c_b^0(t)$ and then plug that into the first order integrate to find $c_a^1(t)$, $c_b^1(t)$ and so on. This is a recursive process that is generalized like so:

$$ \begin{equation}
    \boxed{\dot c_a^n = -\frac{i}{\hbar}H'_{ab}e^{i\omega_{ba} t}c_b^{(n-1)}, \qquad \dot c_b^n = -\frac{i}{\hbar}H'_{ba}e^{i\omega_{ba} t}c_a^{(n-1)}}
\end{equation} $$

This states that the $n$th order approximation is dependent on the $(n-1)$th order thus a recursive process.

Zeroth Order
: For the zeroth order we consider $\dot c_a(t) = 0$ and $\dot c_b(t) = 0$ therefore the coefficients are constant throughout time,

$$
\begin{equation}
    \boxed{c_a^0(t) = 1 \qquad c_b^0(t) = 0}
\end{equation}
$$

First Order
: For the first order, we plug in the zeroth order coefficient,

$$
\begin{gather}
    \frac{d c_a^1}{dt} = -\frac{i}{h}\left[c_a^0H'_{aa} + H'_{ab}e^{i\omega_{ba} t}c_b^0\right] = 0\\
    \boxed{c_a^1(t) = 1 -\frac{i}{\hbar}\int_0^{t}{H'_{aa}}\d t'}\\
    \frac{d c_b^1}{dt} = -\frac{i}{h}H'_{ba}e^{i\omega_{ba} t}c_a^0 = -\frac{i}{h}H'_{ba}e^{i\omega_{ba} t}\\
    \boxed{c_b^1(t) = \frac{-i}{\hbar}\int_0^{t}{H'_{ba}e^{i\omega_{ba} t'}\d t'}}
\end{gather}
$$

The probability of measuring $\psi_b$ in this case is actually interpretted as the probability of the transition from $\psi_a$ to $\psi_b$,

$$ \boxed{P^1_{a\rightarrow b} = \abs{c_b^1}^2} \tag{First Order}$$

Therefore this generalizes to any initial state $\psi_k$ with $c_k(0)=0$ transitioning to another state $\psi_b$.

## Example - Sinusoidal Perturbations

Consider the perturbed Hamiltonian,

$$
\begin{equation}
    H'(\boldsymbol{r},t) = V(\boldsymbol{r})\cos(\omega_{ba} t)
\end{equation}
$$

Immediately we can see that the perturbed Hamiltonian has a separable characteristic where:

$$
\begin{gather}
    H'_{ba} \equiv V_{ba}\cos(\omega_{ba} t)\\
    V_{ba} \equiv \bra{\psi_a} V \ket{\psi_b}
\end{gather}
$$

Once again we use the initial condition that $c_a(0)=1$ and $c_b(0)=0$ therefore the first order coefficient $c_b(t)$ is,

$$
\begin{gather}
    c_b^1 = \int{H'_{ba}(t)e^{i\omega_{ba} t}dt} = -\frac{V_{ba}}{2\hbar}\left[\frac{e^{i(\omega_{ba} + \omega)t} - 1}{\omega_{ba} + \omega} + \frac{e^{i(\omega_{ba} - \omega)t} - 1}{\omega_{ba} - \omega} \right]
\end{gather}
$$