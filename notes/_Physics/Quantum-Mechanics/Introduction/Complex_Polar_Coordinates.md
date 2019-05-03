---
title: Complex Polar Coordinate
---

Complex polar coordinates is easier to deal with and shorter to write than trigonometric cartesian form of the waves. We consider any complex cartesian coordinate can be written in polar coordinates in the form,

$$ a + bi = Ae^{i\theta} $$

Where, 

$$ 
\begin{align}
    e^{i\theta} &= \cos \theta + i\sin \theta \tag{Euler's Formula} \\
    A &= \| a + ib \| = \sqrt{a^2 + b^2} \tag{amplitude or length} \\
    \theta &= \arctan\left(\frac{b}{a}\right) + K, \quad
    \begin{cases}
    K = 0 \quad a>0\\
    K = \pi \quad a<0
    \end{cases}
\end{align}
$$

## Euler's Identities

$$
\begin{align}
    %\label{eq: euler-cos}
    \cos\theta &= \frac{e^{i\theta} + e^{-i\theta}}{2} \\
    %\label{eq: euler-sin}
    \sin\theta &= \frac{e^{i\theta} - e^{-i\theta}}{2i} 
\end{align}
$$

$$
\begin{align}
    e^{i\pi n} = 1 \tag{$n$ is even}\\
    e^{i\pi n} = -1 \tag{$n$ is odd}\\
    e^{i(\frac{\pi}{2} + n\pi)} = i \tag{$n$ is even}\\
    e^{i(\frac{\pi}{2} + n\pi)} = -i \tag{$n$ is odd}\\
\end{align}
$$