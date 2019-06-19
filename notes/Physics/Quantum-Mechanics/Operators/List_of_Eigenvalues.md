---
title: List of Eigenvalues 
---

Quite commonly, without practice, you may forget the eigenvalues of some operator applied to your wavefunction.

## Hydrogen

Hamiltonian
: $$ \hat H = \frac{-\hbar^2}{2m}\hat\nabla^2 - \frac{e^2}{4\pi\epsilon_0}\frac{1}{r} $$
$$
\begin{align}
    E_n &= -\frac{m_e}{2\hbar^2}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2\frac{1}{n^2} \\
    &= \frac{m\alpha^2 c^2}{2}\frac{1}{n^2}\\
    &\approx \frac{13.6 \text{ eV}}{n^2}
\end{align}
$$

Angular Momentum Operator
: $$\hat L_z = \frac{\hbar}{i}\frac{\partial}{\partial \phi}$$

$$
\begin{align}
    L_z(m) = \hbar m 
\end{align}
$$

: $$\hat L^2 = \hat L_x^2 + \hat L_y^2 + \hat L_z^2$$

$$ \begin{align}
    L^2(\ell) = \hbar^2\ell(\ell + 1)
\end{align} $$

## Harmonic Oscillator
Each dimension of the harmonic oscillator is separable therefore we only have to write one dimension. The full solution is of course the product of each dimension's solutions.

For $r = \{x, y, z, ... x_N\}$ and $n = \{n_x, n_y, n_z, ...n_{x_N}\}$ where $N = \dim \hat H$

Hamiltonian
: $$ \hat H = -\frac{\hbar^2}{2m}\hat\nabla^2 + \frac{1}{2}m\sum_{i}{x_i^2}$$

$$ \begin{equation}
    E_{n} =\hbar\omega\left(n + \frac{1}{2}\right)\\
    E_{(n_x, n_y, n_z, ...n_{x_N})} = \prod_{n}\hbar\omega\left(n + \frac{1}{2}\right)
\end{equation} $$
