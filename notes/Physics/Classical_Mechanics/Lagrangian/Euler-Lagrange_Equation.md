---
title: Euler-Lagrange Equation
---

Calculus of variations attempts to solve the shortest path problem problem in a form of the following integral,

$$
\begin{equation}
    S = \int_{x_1}^{x_2}{f\left[y(x),y'(x),x\right] dx}
\end{equation}
$$

Generally,

$$
\begin{align}
    S &= \int_{x_1}^{x_2}{f\left[u_1(v),u_1'(v),u_2(v),u_2'(v)...,v\right] dx}\\
    S &= \int_{x_1}^{x_2}{f\left[\boldsymbol{u}(v),\boldsymbol{u}'(v),v\right] dx}
\end{align}
$$

What we wish to find is $y(x)$ which is a curve that minimizes $S$. 

Any function that satisfies the **Euler-Lagrange equation** (or shortly **Lagrange equations**) can construct the proper $y(x)$. The Lagrange equation is written as,

$$\begin{align}
    \boxed{\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'} = 0}
\end{align}$$

## Proof
The method to find $y(x)$ is weird because we are going to find the wrong answer/curve first. The wrong curve is in some form

$$\begin{align}
    Y'(x) = y(x) + \alpha\eta(x)
\end{align}$$

* $\eta(x)$ : some deviation from the correct curve $y(x)$
* $\alpha$ : a coefficient of the deviation

You can see that the correct answer occurs when $\alpha = 0$. We may also write $S$ as a function with parameter $\alpha$ such that $S(\alpha)$ is minimum at $S(0)$. The condition for a minimum, (more correct, an extrema) is $dS/d\alpha=0$,

$$
\begin{align}
    S(\alpha) &= \int_{x_1}^{x_2}{f(y+\alpha\eta, y'+\alpha\eta',x) \ dx} \\
    \frac{dS}{d\alpha} &= \int_{x_1}^{x_2}{\frac{\partial f}{\partial \alpha} \ dx} \\
    \frac{df}{d\alpha} &= \eta\frac{\partial f}{\partial y} + n'\frac{\partial f}{\partial y'}\nonumber\\
    \frac{dS}{d\alpha} &= \int_{x_1}^{x_2}{\left(\eta\frac{\partial f}{\partial y} + n'\frac{\partial f}{\partial y'}\right) \ dx} = 0\\
\end{align}
$$

For the last line to be true, this must be true by integration by parts,

$$
\begin{align*}
\int_{x_1}^{x_2}{\eta(x)\left(\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'}\right) \ dx} = 0
\end{align*}
$$

Thus it is necessary for any arbitrary $\eta(x) \ne 0$,

$$
\begin{equation}
    \boxed{\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'} = 0}
\end{equation}$$

## Properties
The two properties of the Lagrange equation are theorems that makes solving for the Lagrange equation much simpler,

**Theorem 1: **
: If $f[x(t),x'(t),t]$ is independent on any of its zeroth order derivative parameters $x$ such that,
    
    $$ \frac{\partial f}{\partial x} = 0$$
: then its derivative along say $x'$ is a constant $C$,

    $$ \boxed{\frac{\partial f}{\partial x'} = C} $$
: This theorem applies to all functions that satisfies the Lagrange equations.

**Theorem 2: **
: If $f[x(t),x'(t),t]$ is independent on it's free parameter $t$ such that,

    $$ \frac{df}{dt} = 0 $$

: then the rest of the Lagrange equation follow for some constant $C$,

    $$ \boxed{f - x'\frac{\partial f}{\partial x'} = C} $$

## Example: Shortest Path
The shortest path between two points is,

$$ \begin{align}
    S &= \int_{x_1}^{x_2}{\sqrt{1+(y')^2}\ dx}
\end{align} $$,

Where $f \left(y, y', x\right) = \sqrt{1+(y')^2}$. Let's solve for the Lagrange equation,

$$
\begin{gather}
    \frac{\partial f}{\partial y} = 0, \quad \frac{\partial f}{\partial y'} = \frac{y'}{(1+y'^2)^{1/2}} \nonumber\\
    \frac{y'}{(1+y'^2)^{1/2}} = C\\
\end{gather}
$$ 
For some constant $C$.

$$
\begin{align}
    y'^2 &= C^2(1+(y')^2) \nonumber\\
    y' &= \text{const}
\end{align}
$$

Let's set the constant to be $m$ such that $y' = m$. We can integrate $y'(x)$ to get $y(x)$

{}
hello

$$
\begin{equation}
    \boxed{y(x) = mx + y_0}
\end{equation}
$$

Now you see that the shortest path is a straight line!

## Multivariable
The Lagrange equation solves the integral,

$$
\begin{gather}
    S = \int_{u_1}^{u_2}{f\left[x_1, x_2,...,x_1'(u), x_2'(u),... u\right] \ du} \\
    \frac{\partial f}{\partial x_i} - \frac{d}{du}\frac{\partial f}{\partial x_i'} = 0 \\
\end{gather}
$$