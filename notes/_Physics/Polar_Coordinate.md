---
title: Polar Coordinates
layout: page
---

## 2D Polar Coordinate

The two-dimensional polar coordinate uses the two parameter vectors $\boldsymbol{r}$ and angle vector $\boldsymbol{\phi}$. It is simply defined by unit vectors,

$$
\boldsymbol{r} = r\boldsymbol{\hat r}
$$

$$ \boldsymbol{\phi} = \phi\boldsymbol{\hat \phi} $$

### Cartesian to Polar

We make the transformation given $x, y$ by,

$$
\begin{align}
    \begin{pmatrix}
        x = r \cos \phi\\
        y = r \sin \phi
    \end{pmatrix}
    \longleftrightarrow
    \begin{pmatrix}
        r = \sqrt{x^2 + y^2}\\
        \phi = \arctan (y/x)
    \end{pmatrix}
\end{align}
$$

* This transformation is not mathematically general since we use $\arctan$. More properly use $\arctan2$

### Velocity

There is an unfamiliar property for the rate of change in polar coordinates compared to cartesian coordinates. Most prominent is velocity, $\boldsymbol{\dot r}$ which is,

$$ \boldsymbol{\dot r} = \frac{dr}{dt} \boldsymbol{\hat r} + r\frac{d\boldsymbol{\hat r}}{dt} $$

Which may be simplified to,

$$\begin{align}
    \boldsymbol{v} \equiv \boldsymbol{\dot r}\\
    v_r \equiv \dot r \quad v_\phi &\equiv r \dot \phi
\end{align}$$

$$\boxed{\boldsymbol{v} \equiv v_r \boldsymbol{\hat r} + v_\phi  \boldsymbol{\hat \phi}} $$


#### Derivation

Naively one may assume $d\boldsymbol{\hat r}/dt = 0$ however this is not the case because $\boldsymbol{\hat r}$ is allowed to change directions over time[^directions]. Let's take for granted and assume $d\boldsymbol{\hat r}/dt = \dot \phi \boldsymbol{\hat \phi}$

$$ \begin{align}
    \boldsymbol{\dot r} &= \frac{dr}{dt} \boldsymbol{\hat r} + r\frac{d \phi}{dt}\boldsymbol{\hat \phi} \\
    \boldsymbol{\dot r} &= \dot r \boldsymbol{\hat r} + r \dot \phi \boldsymbol{\hat \phi}
\end{align}
$$

More familiar uses the identity,

$$\begin{align}
    \boldsymbol{v} \equiv \boldsymbol{\dot r}\\
    v_r \equiv \dot r \quad v_\phi &\equiv r \dot \phi
\end{align}$$

$$\boxed{\boldsymbol{v} \equiv v_r \boldsymbol{\hat r} + v_\phi  \boldsymbol{\hat \phi}} $$

[^directions]: When learning vectors in cartesian coordinates we take for granted that $d\boldsymbol{\hat x}/dt = 0$ which is definitely true since $\boldsymbol{\hat x}$ never changes directions.

### Acceleration

The second time derivative or acceleration is defined as,

$$ \boldsymbol{a} \equiv \boldsymbol{\ddot r} = \boldsymbol{\dot v} $$

Knowing $d \boldsymbol{\hat \phi}/dt$ gives us acceleration as,

$$ \frac{d\boldsymbol{\hat\phi}}{dt} = -\frac{d\phi}{dt}\boldsymbol{\hat r} $$

$$ \boldsymbol{a} = (\ddot r - r\phi^2)\boldsymbol{\hat r} + (r \ddot \phi + 2\dot r \dot \phi)\boldsymbol{\hat \phi} $$

Given that $\dot r = 0$ thus $\ddot r = 0$ gives us a somewhat more familiar form of acceleration,

$$ a = -r\dot \phi^2 \boldsymbol{\hat r} + r\ddot \phi \boldsymbol{\hat \phi} $$

$$ a_\text{c} \equiv r\dot \phi^2 = r\omega^2, \qquad  a_\perp \equiv r\ddot \phi = r\alpha$$

$$ a = a_c \boldsymbol{\hat r} + a_\perp \boldsymbol{\hat \phi} $$

* $\alpha$ : angular acceleration
* $a_c$ : centripetal acceleration
* $a_\perp$ : tangential acceleration

