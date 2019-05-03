---
title: Calculus of Variations
---

## Shortest Path
The length between two points in a plane follows the equation,

$$
\begin{equation}
    ds = \sqrt{dx^2 + dy^2}
\end{equation}
$$

It is simple to convince yourself that,

$$
\begin{equation}
    dy = y'(x)dx
\end{equation}
$$

We are now ready to write the length between two points as a function of $y'(x)$,

$$ \begin{align}
    S &= \int_1^2{ds} = \int_{x_1}^{x_2}{\sqrt{1+y'(x)^2}\ dx}
\end{align} $$
