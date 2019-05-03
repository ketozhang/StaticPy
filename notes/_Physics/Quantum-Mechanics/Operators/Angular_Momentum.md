---
title: Angular Momentum
parent: Operator
---

The angular momentum in quantum mechanics can be seen as an operator defined as,

$$\begin{equation}
    \hat{L} \equiv \hat r \times \hat p
\end{equation}$$
$$
\begin{align}
    \hat L_x &= y\hat p_z - z\hat p_y\\
    \hat L_y &= z\hat p_x - x\hat p_z\\
    \hat L_z &= x\hat p_y - y\hat p_x
\end{align}
$$

However this definition is quite useless since we do not want to deal with cross products with operators. Instead it is preferred to use either the components or the square of $\hat L$,

$$
\begin{equation}
    \hat L^2 \equiv \hat L_x^2 + \hat L_y^2 + \hat L_z^2
\end{equation}
$$

<center style="color:red; font-weight:bold"> From here-on out, there is no need to write the hat notation so $L \equiv \hat L$. </center>

## Motivation
To motivate the use of the angular momentum operator, we need to write it in spherical coordinates,

$$
\begin{align}
    L &\equiv \frac{\hbar}{i}\left( \hat \phi \frac{\partial}{\partial\theta} - \hat\theta \frac{1}{\sin\theta}\frac{\partial}{\partial\phi} \right)\\
    L_z &= \frac{h}{i}\frac{\partial}{\partial\phi}\\
    L^2 &= -\hbar^2\left[ \frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial}{\partial \theta}\right) - \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2} \right]\\
\end{align}
$$

With this definition of $L$, we can write the TISE in spherical coordinates; specifically we can write the kinetic energy $\hat K$ as,

$$
\begin{equation}
    \hat K = \frac{1}{2mr^2}\left[-\hbar^2 \frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + L^2\right]
\end{equation}
$$

> Will be required in the hydrogen TISE.

## Commutation
The commutation relation between each component of $L$ and $L^2$,

1. The component of $L$ does not commute with eachother
    
    $$
    \begin{gather}
        [L_x,L_y] = i\hbar L_z\\
        [L_y,L_z] = i\hbar L_x\\
        [L_z,L_x] = i\hbar L_y\\
    \end{gather}
    $$

2. $L$ and all of its components commute with $L^2$

    $$
    \begin{gather}
        [L^2,L] = 0\\
        [L^2,L_j] = 0
    \end{gather}
    $$

    * $j = \{x,y,z\}$ 

## Ladder Operators
The ladder operator is defined very similar to the harmonic oscillator,

$$
\begin{equation}
    L_\pm \equiv L_x + iL_y
\end{equation}
$$

## Eigenvalue
From the commutation rules, we know that it's futile to find an eigenvalue or eigenstate of any two $L_j$ component of $L$. Instead we choose one to be our favorite; by convention, that is $L_z$ (for no good reason, maybe because $z$ needs more love since $x$ and $y$ always steals the spotlight).

If we choose $L_z$ we are limited to the eigenstate of $L_z$ which luckily must also be an eigenstate of $L^2$ by commutation **but not** eigenstates of $L_x$ or $L_y$ as we discussed before.

For the eigenstate of $L_z$ and $L^2$ we denote as $\psi = \ket{\ell, m}$ (will be explained), we found the eigenvalues to be:

$$
\begin{gather}
    \boxed{L_z\ket{\ell, m_\ell} = \hbar m_\ell \ket{\ell, m}}\\
    \boxed{L^2\ket{\ell, m_\ell} = \hbar^2 \ell \ket{\ell, m}}
\end{gather}
$$

* $\ell$ : half-step integers known as the angular momentum (azimuthal) quantum number
    * In the hydrogen equation, $\ell$ is limited by $n$ where $\ell = \{0, \ldots,n-1\}$ and is a special case that only $\ell$ as whole integers must exist.
* $m_\ell$ : whole integers known as the associated angular momentum (azimuthal) number
    * At all cases, $m_\ell = \{-\ell, -\ell + 1, \ldots, \ell - 1, \ell\}$
    * Often may be written with $m$ if not written with the associated spin number $m_s$.

The motivation of using $\ell$ and $m_\ell$ is that there exist more than one eigenstate of $L_z$ and $L^2$. Knowing one eigenstate $\ket{\ell, m_{\ell}}$ will allow you to know all of the eigenstate by applying the ladder operators. In other words,

**Eigenstates of $L_z$ and $L^2$ are the Ladder Operated Eigenstates:**

$$ 
\begin{gather}
    L_-...L_-\ket{l, m_\ell}\\
    \vdots\\
    L_-\ket{l, m_\ell}\\
    \ket{l, m_\ell}\\
    L_+\ket{l, m_\ell}\\
    \vdots\\
    L_+...L_+\ket{l, m_\ell}
\end{gather}
$$

Each of these eigenstates are associated with (not all unique) eigenvalues depending on $\ell$ and $m_\ell$ quantum numbers.

### Proof

