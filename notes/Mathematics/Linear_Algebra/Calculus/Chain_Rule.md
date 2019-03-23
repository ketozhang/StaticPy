---
title: Chain Rule
---

## Scalar-Scalar

We want to take the derivative of a scalar composite function $f​$ with respect to a scalar $x​$.
$$
\begin{align}
f(x) &= f(g(x)) = f \circ g \circ x\\
\frac{\mathrm{d}}{\mathrm{d} x}f(x) &= \frac{\mathrm{d}f}{\mathrm{d} g}\frac{\mathrm{d}g}{\mathrm{d} x}
\end{align}
$$

## Gradient: Scalar-Vector

We want to take the derivative of a scalar composite function with respect to a vector $\vec x$
$$
\begin{align}
f(x) &= f \circ g \circ \vec{x}\\
\frac{\mathrm{d}}{\mathrm{d} \vec x}f(\vec x) &= \frac{\mathrm{d}f}{\mathrm{d} g}\frac{\mathrm{d}g}{\mathrm{d} \vec x}\\
\nabla f(\vec x) &= \left(\frac{\mathrm{d}f}{\mathrm{d} g}\frac{\mathrm{d}g}{\mathrm{d} \vec x}\right)^\top = \nabla g(x) \frac{\mathrm{d}f}{\mathrm{d} g} \label{eq:gradient}
\end{align}
$$
In $\eqref{eq:gradient}​$ the second product term is left transposed because $g​$ can

