---
title: Special Relativity
---
> **IMPORTANT: ** From here on out, I will be using natural units where $c=1$. This means that it's important to know that time $t$ has the units of length in [Minkowski space](#spacetime). Please take this moment for a deep breath because you're ready to learn natural units (if you haven't).

## Spacetime
> *Alias: Minkowski Space*

Naturally, one would think that a certain event happen at some fixed time for example an object at time $t_0$ can be at some position $x(t_0)=x_0$ but, it's impossible for the object to be in another position at the same time. In math, one can say that $x(t)$ is a well-defined function such that the vertical line passes for a time vs position graph.

> We ignore the world of quantum mechanics where the position of an object may be in multiple places at the same time determined by some wavefunction. 

This axiom (assumption of our universe) is not true! $x(t)$ is not a well-defined function where we do allow an object to be in two different places at the same time $t_0$. We need to include $t$ in our function such that we define a new concept of position which is a position in **spacetime**. In 3D Euclidean space, this would now be a 4D Euclidean spacetime called the **Minkowski** space. To preserve a position unit the 4th dimension is $ct$ such that,

$$\begin{align}
    x^\mu &= \mathcal{x}^\mu(-ct,x,y,z)\\
    x^\mu &= \begin{pmatrix} t \\ x \\ y \\ z \end{pmatrix}
\end{align}$$

* $x^\mu$ : Minkowski Space function or less confusing the 4-positional vector.
* $t \rightarrow \text{SI} \rightarrow ct$

In a general $N$-space the positional vector $x^\mu$ becomes a $N$-positional vector,

$$
\begin{equation}
    x^\mu = \begin{pmatrix}
        x^0\\ x^1 \\ \vdots \\ x^\mu
    \end{pmatrix}
\end{equation}
$$

> The superscript is not a power but denotes which axis/basis such that say $x^1 = x,\; x^2 = y,\; x^3 = z, \ldots\;$.

The $x^0$ may be confusing for some so one may define cannonical position as $x^i = \{x,y,z,...\}$ such that,

$$
\begin{equation}
    x^\mu \equiv x^\mu(t, x^i)
\end{equation}
$$

## Metric

A bit about metric. Metric is defined to deal with measuring length $S$ (differential: $ds$) given some coordinate system. You should be familiar with the metric for Euclidean surface (flat surface) say for a 2D Euclidean surface in cartesian coordinate should be,

$$
\begin{align}
    S^2 &= x^2 + y^2 \qquad \tag{Pythagorean Theorem}\\
    ds^2 &= dx^2 + dy^2
\end{align}
$$

* $S = \int{ds}$
* Let's use the differential form to be very general. 

The value of $S$ should not be any different in polar coordinate. To preserve $S$ we modify the equation

$$
\begin{equation}
    ds^2 = dr^2 + r^2d\theta^2
\end{equation}
$$

For any general coordinate we may write it as a summation

$$
\begin{align*}
    ds^2 = \sum_{\mu,\nu=1}^{\dim}{g_{\mu\nu}dx^\mu dx^\nu}
\end{align*}
$$

This is often written using Einstein's summation notation which just get rid of the $\sum$. This is useful because it's realizable in matrix form such that $g_{\mu\nu}$ and $dx^\mu dx^\nu$ are matrices,

$$
\begin{gather}
    \boxed{ds^2 = g_{\mu\nu}dx^\mu dx^\nu}\\
    dx^\mu dx^\nu = \begin{pmatrix}
        dx_1^2 & dx_1dx_2 & \ldots\\ dx_2dx_1 & dx_2^2 &\ldots \\ \vdots & \vdots & \ddots
    \end{pmatrix}
\end{gather}
$$

$$
\begin{align}
g_{\mu\nu} = \begin{pmatrix}
    1 & 0\\ 0 & 1
\end{pmatrix} \tag{Cartesian}\\
g_{\mu\nu} = \begin{pmatrix}
    1 & 0\\ 0 & r^2
\end{pmatrix} \tag{Polar}
\end{align}
$$
### Spacetime Interval

The spacetime interval is the length of the 4-positional vector which of course by Pythagorean law 4-dimensional space,

$$\begin{equation}
    ds^2 = -cdt^2 + dx^2 + dy^2 +dz^2
\end{equation}$$

* $ds^2$ : Differential form of the spacetime interval. The square power is part of its definition.

The most important property of the spacetime interval is that length is invariant between any reference frames where $ds' = ds$.

In general in Einstein's notation where $g_{\mu\nu} = \eta_{\mu\nu}$ called the **Minkowski metric**,

$$\begin{gather}
    ds^2 = \eta_{\mu\nu}dx^\mu dx^\nu\\ \nonumber \\
    \eta_{\mu\nu} \equiv \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}\\
\end{gather}$$

### Proper Time

A convention to consider the length or spacetime interval to increase with time is to define the term $\tau$ to be the **proper time**. All it is, is the negative of length in spacetime,

$$
\begin{gather}
    d\tau^2 = -ds^2 \nonumber \\
    \boxed{d\tau^2 = -\eta_{\mu\nu}dx^\mu dx^\nu}
\end{gather}
$$

**Proper time** is implied as the time interval one sees between two events if they were be at rest at their own reference frame (not necessary that the events must be an event of objects at rest). We can easily see this in the definition that if one is at rest then $dx^i = 0$ so,

$$
\begin{align*}
    d\tau^2 &\equiv dt^2 - dx^i\\
    \qquad dx^i &= 0\\
    d\tau &= dt\\
\end{align*}
$$

Notice that if $d\tau$ is maximum when $dx^i=0$. That would mean if the observer was moving then its proper time interval must be shorter than another observer at rest.

## Lorentz Transformation
The Lorentz transformation describes how one can shift from one reference frame to another such that the spacetime interval is invariant. This means there exist a matrix transformation $\Lambda$ that,

$$
\begin{gather}
    dx^\mu \cdot \eta dx^\nu = dx^{\mu'}\cdot \eta dx^{\nu'} = (dx^\mu \Lambda^\mu) \eta (\Lambda^\nu dx^\nu)\\
    \boxed{\eta = \Lambda^\mu \eta \Lambda^\nu}
\end{gather}
$$