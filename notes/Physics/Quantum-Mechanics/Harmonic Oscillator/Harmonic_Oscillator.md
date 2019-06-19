---
title: Harmonic Oscillator
---

The Hamiltonian for the harmonic oscillator follows the potential energy of Hooke's law (recall it is negative in magntiude). We consider the system to be similar to a mass $m$ attached to a spring of constant $k$ where we define the natural frequency as $\omega \equiv \sqrt{k/m}$:

$$\begin{equation}
    \boxed{H = \frac{\hat p^2}{2m} + \frac{1}{2}m\omega^2 x^2}
\end{equation}
$$
The eigenstate is the normalized Hermite polynomials. This is rarely used and written out (you'll see why in the ladder operator method) but it is:

$$\begin{gather}
    \boxed{\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^nn!}}H_n\left(\sqrt{\frac{m\omega}{\hbar}}x \right)}\\
    H_n(r) \equiv (-1)^ne^{r^2}\left(\frac{d}{dr}\right)^n e^{-r^2}
\end{gather}$$

Much easier is to write the eigenstates in terms of the [ladder operators](#ladder_operators):

$$
\begin{gather}
    \boxed{\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2}}\\
    \boxed{\psi_n(x) = \frac{1}{n!}(a_+)^n\psi_0(x)}
\end{gather}
$$

The eigenvalues are then,

$$
\begin{equation}
    E_n = \hbar \omega\left(n + \frac{1}{2}\right)
\end{equation}
$$

There are two ways to solve the harmonic oscillator one clever (called the ladder operators) and one brute force. We will only use the clever way in this article becuase it's clever and very useful later on.

## Ladder Operators
The clever way of the harmonic oscillator is a method that will be used almost everywhere to describe not only the harmonic oscillator but also any Hamiltonian that requires the angular momentum operators $J,L,S$. Therefore learning the clever way is most crucial.

We define an operator called the **ladder operator** as:

\begin{equation}
    a_\pm = \frac{1}{\sqrt{2\hbar m \omega}}\left(\mp ip + m \omega x\right)
\end{equation}

We divide $a_\pm$ where $a_+$ is to be called the **raising operator** and $a_-$ is to be called the **lowering operator**. They have a special property that raises and lowers the eigenstate where:

\begin{gather}
    \boxed{a_+\psi_n = \sqrt{n+1}\;\psi_{n+1} \qquad a_-\psi_n = \sqrt{n}\;\psi_{n-1}}\\
\end{gather}

With some work, the Hamiltonian can be written in terms of the ladder operators:

$$\begin{equation}
    H = \hbar\omega(a_\pm a_\mp \pm \frac{1}{2})
\end{equation}$$

The eigenstate to this Hamiltonian is (in terms of the raising operator $a_+$)

$$\begin{gather}
    \boxed{\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2}}\\
    \boxed{\psi_n(x) = \frac{1}{n!}(a_+)^n\psi_0(x)}
\end{gather}$$

The eigenstate above are equivalent to the Hermite polynomials.

### Properties

Conjugates
: The ladder operators are hermitian conjugates of one another:

begin{equation}
    a_\pm^\dagger = a_\mp
\end{equation}

Position
: The position operator can be written in terms of the ladder operators:

$$\begin{equation}
    \boxed{x = \sqrt{\frac{\hbar}{2m\omega}}\left(a_+ + a_-\right)}
\end{equation}$$

Momentum
: The momentum operator can be written in terms of the ladder operators:

$$\begin{equation}
    \boxed{p = i\sqrt{\frac{\hbar m \omega}{2}}\left(a_+ - a_-\right)}
\end{equation}$$


### Motivation
Here we will motivate you why the ladder operators are defined the way it is:

<!-- TODO: Motivate ladder operators Griffiths P.42 -->