---
title: Spontaneous Emission
---

## Einstein's Coefficients

For the following

* system of particles in a lower state $\psi_a$ state is $N_a$
* a system of particles in an upper state $\psi_b$ state is $N_b$

with the coefficients,

* $A$ : spontaneous emission rate out of $\psi_b$
* $B\rho(\omega_0)$ : stimulated emission rate
* $B_{ab}\rho(\omega_0)$ : rate of particles entering $b$ from $a$
* $B_{ba}\rho(\omega_0)$ : rate of particles leaving $b$ to $a$

Then the number of particles entering the state $\psi_b$ is,

$$ \dot N_b = -N_bA - N_bB_{ba}\rho(\omega_0) + N_aB_{ab}\rho(\rho_0) $$

If the system is in thermal equilibrium then $dN_b/dt = 0$ such that,

$$ B_{ab} = B_{ba} $$

and we can solve for $\rho(\omega_0)$ to find Plancks' law,

$$ \rho(\omega) = \frac{A}{e^{\hbar\omega_0/\tau}B_{ab} - B_{ba}}$$

We see that the spontaneous emission rate can be written in terms of the stimulated emission rate,

$$\begin{align}
\boxed{A = \frac{\omega_0^3 \hbar}{\pi^2c^3}B_{ba}}\\
\boxed{A = \frac{\omega_0^3 q\abs{r_{ba}}^2}{3\pi\epsilon_0\hbar c^3}}
\end{align}$$

This is as far as we can go without going into quantum field theory and electrodynamics. Einstein's coefficient $A$ is a useful equation such that it says spontaneous emission is similar to a system of stimulated emission off by a factor.

## Lifetime and Decay Rate
Consider a system that is out of equilibrium but has a spontaneous emission rate $A$ out of the state $\psi_b$. You may treat $A$ in this case as the decay rate where,

$$\begin{gather}
\frac{dN_b}{dt} = -AN_b\\
N_b(t) = N_b(0)e^{-At}
\end{gather}$$

The period of decay or **lifetime** is then,

$$\begin{equation}
\boxed{\tau = \frac{1}{A}}
\end{equation}$$

Given that there is $n$ states and not just one ($b$) then the decay rate simply adds up,

$$
\begin{gather}
A = \sum_n{A_n}\\
\end{gather}
$$