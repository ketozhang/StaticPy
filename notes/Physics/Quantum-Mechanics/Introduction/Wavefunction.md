---
title: Wavefunction
---

Throughout quantum mechanics we use the wavefunction which is comparably used to describe "where a particle is". There are many interpretation of the wavefunction, however, the one most accepted is the [statistical interpretation](#statistical-interpretation). Unfortunately we can't get much further without agreeing that the statistical interpretation is sufficient.

## Statistical and Copenhagen Interpretation

The wavefunction does not actually tell you where a particle is for some given time; instead the **wavefunction** $\Psi(x,t)$ correlates to the probability of the particle being in some position $x$ for some given time $t$. The definition above is definitely abstract and it is considered the **statistical interpretation** of the wavefunction. 

* The most accepted explanation of why we must describe quantum system with probability is that any attempt to observe where the particle is will drastically change the actual position of the particle. In other words, physicist has accepted that it is impossible to measure the exactly position knowing its exact momentum (which is used in the Schrodinger equation). The acceptance of this limitation is called the **Copenhagen interpretation**.

The full mathemateical description of the wavefunction can be written as the probability of the particle being between two points $(a,b)$ is given by,

$$
\begin{equation}
    \boxed{P_{ab} = \int_a^b{|\Psi(x,t)|^2 \;dx}} \label{eq: probability}
\end{equation}
$$

## Probability Density Function

By the Equation $\eqref{eq: probability}$ we see that $|\Psi(x,t)|^2$ is the **probability density function**,

$$
\begin{align}
    \boxed{|\Psi(x,t)|^2 = \frac{dP}{dx}}\label{eq: probability-density}
\end{align}
$$

## Expectation Value

A useful quantity is the mean, average, or expectation value of the wavefunction. The expectation value is the average of some quantity $x$ determined by some probability curve $P(x)$,

$$ \langle x \rangle \equiv \int_{-\infty}^\infty{x\frac{dP}{dx}\; dx}$$
$$ \langle x \rangle \equiv \int_{-\infty}^\infty{x|\Psi|^2\; dx}$$

The definition above is not so general and only applies to parameters and functions. What about operators? When dealing with wavefunctions (which is complex) we often use the Dirac notation. In general let's have an arbitrary hermitian operator[^hermitian] $\hat Q$ in the $x$ basis,

[^hermitian]: the expectation value of hermitian operators are always real. [Proof](Operators.md/#hermitian-operators)

$$ \langle \hat Q \rangle \equiv \langle \Psi | \hat Q \Psi \rangle $$
$$ \langle \hat Q \rangle \equiv \int_0^\infty{\Psi^* \hat Q \Psi\; dx} $$

