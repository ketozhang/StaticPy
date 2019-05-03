---
title: Friedmann Robertson Walker Metric
---

The Friedmann Robertson Walker Metric (FRW) describes the metric of the expanding flat universe. It is defined as,

$$\begin{gather}
    g_{\mu\nu} \equiv \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & a^2(t) & 0 & 0 \\ 0 & 0 & a^2(t) & 0 \\ 0 & 0 & 0 & a^2(t) \end{pmatrix}\\
\end{gather}$$

Recall the Minkowski metric as,

$$\begin{gather}
    \eta_{\mu\nu} \equiv \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}\\
\end{gather}$$

We can now see that the Minkowski metric takes $a^2(t) = 1$ (constant scale factor). So as we expect, the Minkowski universe is a flat non-expanding universe where the only curvature exist in the 4-positional vector.

Applying this metric to the describe lengths $ds$ is,

$$
\begin{gather}
    ds^2 = g_{\mu\nu} dx^\mu dx^\nu\\
    \boxed{ds^2 = -dt^2 + a(t)^2\left[dr^2 + S_k(r)^2d\Omega^2\right]}\\
    S_k(t) = \begin{cases}
        R_0\sin\left(\dfrac{r}{R_0}\right) & k=1 \text{ (open)}\\
        r & k=0 \text{ (flat)}\\
        R_0\sinh\left(\dfrac{r}{R_0}\right) & k=-1 \text{ (closed)}
    \end{cases}
\end{gather}
$$

* $k$ : Curvature constant
* $R_0$ : Radius of curvature

## Proper Distance

Considering a universe that follow the FRW metric of some scale factor $a(t)$ that changes over time. The proper distance is the actual distance of the an observed object that emits light. Thus defined as,

$$ d_p(t) = \chi a(t) $$

* $\chi$: comoving distance
* $a(t)$: scale factor


This is given by a photon traveling in a null-space (it's own straight path) where $d\Omega = 0$ and $ds = 0$. Therefore the metric becomes,

$$dt^2 = a(t)^2 dr^2$$

Consider a photon emitted at time $t_e$ and observed at time $t_o$. We can find the proper distance by:

$$
\begin{gather}
    d_p(t) = \int{dr}\\
    \boxed{d_p(t) = \int_{t_e}^{t_o}{\frac{dt}{a(t)}}}
\end{gather}
$$

Additionally the comoving factor can be derived from the definition of proper distance

$$
\begin{gather}
    \chi = \frac{1}{a(t_e)} \int_{t_e}^{t_o}{\frac{dt}{a(t)}}\\
    \boxed{\chi = \left(1 + z\right)\int_{t_e}^{t_o}{\frac{dt}{a(t)}}}
\end{gather}
$$