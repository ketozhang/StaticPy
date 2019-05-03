---
title: Numerical Integration
---

## Trapezoidal Rule

Recall that the area of a trapezoid is the average length of the two sides multiplied by the width $\Delta x$:

$$ A_\text{trapezoid} = \frac{f(x_1) + f(x_2)}{2}\Delta x$$

The trapezoidal rule approximates the integral of some function $f(x)$ by summing the trapezoidal area of $N-1$ slices. Each slice is made with a straight line boundary from $x_n$ to $x_{n+1}$

$$
\int_{x_n}^{x_{n+1}} f(x)\ \mathrm d x = \frac{f(x_n) + f(x_{n+1})}{2}\Delta x + \mathcal{O}(hf'')\\
\int_{x_1}^{x_N} f(x)\ \mathrm d x = \frac{\Delta x}{N} \left(\frac{1}{2} f(x_1) + f(x_2) + \ldots \frac{1}{2}f(x_N) \right) + \mathcal O\left(\frac{(\Delta x)^3 f''}{N^2}\right)
$$

* The trapezoidal rule is the exact solution for the linear equation $f(x) = mx$

## Simpson's Rule

The Simpson's rule uses parabolic slices instead of linear slices

$$
\int_{x_n}^{x_{n+2}} f(x) \ \mathrm dx = \frac{\Delta x}{3} \Big[f(x_1) + 4f(x_2) + f(x_3)\Big]\\
\int_{x_1}^{x_N} f(x) \mathrm dx = \frac{\Delta x}{3N} \Big[f(x_1) + 4f(x_2) + 2f(x_3) + 4f(x_4) + 2f(x_5) + \ldots + f(x_N)\Big] + \mathcal O\left(\frac{1}{N^4}\right)
$$

* The Simpson's rule is the exact solution for the 3rd degree polynomial $f(x) = ax + bx^2 + cx^3$

## Improper Integrals

1. Integrable Singularity

    If from the interval $a$ to $b$, $f(a) = \infty$

2. Exponential Fall-off

    An integral from $a$ to $\infty$ can be converted into an exponential integral by change of variables:

    $$
        u = e^{-x} \qquad x = -\log u\\
        \int_{a}^{\infty} f(x)\ \mathrm dx = \int_{0}^{e^{-a}} \frac{f(-\log u)}{u}\ du
    $$

