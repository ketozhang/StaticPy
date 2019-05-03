---
title: The Lagrangian
---

Lagrange found that there exist a principle of variation for all of physics that follows Newton's second law called the **principle of least action**. The principle states that the universe likes to take the last action $S$ along some path dependent on time described by the **Lagrangian** $\mathcal{L}$. 

This description sets up the shortest path (action) problem where,

$$
\begin{align}
    S = \int_{t_1}^{t_2}{\mathcal{L}\; dt}
\end{align}
$$

We define the Lagrangian as the difference between kinetic $K$ and potential energy $U$ (for reason and it's difficult to interpret),

$$
\begin{gather}
    \boxed{\mathcal{L} \equiv K - U}\\
    \mathcal{L} \equiv \frac{1}{2}m\boldsymbol{\dot r}^2 - U(\boldsymbol{r}) \nonumber
\end{gather}
$$

The Lagrangian is define to follow the Lagrange equation you will soon realize it's because the Lagrange equation is a direct relationship to Newton's laws.

We take a specific case where the Lagrangian is made up of conservative non-constraint forces (like gravity) and any constraint force (forces normal to the particle's motion), Recall that the Lagrange equation for states that if $\mathcal{L}$ is a function of $r$ we may write,

$$
    \frac{\partial \mathcal{L}}{\partial r} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot r} = 0
$$

In general, one may decompose $\boldsymbol{r}$ into $n$ Lagrange equations for $n$ parameters (excluding the free parameter $t$). This is only valid for system considered to be holonomic systems.

## Lagrangian and Newtonian Mechanics

By the definition of the Lagrangian, we may compose some components of Newtonian mechanics,

$$
\begin{align*}
    \frac{\partial \mathcal{L}}{\partial \boldsymbol{r}} &= -\nabla U = \boldsymbol{F}\\
    \frac{\partial \mathcal{L}}{\partial \boldsymbol{\dot r}} &= m\boldsymbol{\dot r} = \boldsymbol{P}
\end{align*}
$$

Therefore,

$$\begin{gather}
    \boxed{\boldsymbol{F} = \frac{\partial \mathcal{L}}{\partial \boldsymbol{r}}}\\
    \boxed{\boldsymbol{P} = \frac{\partial \mathcal{L}}{\partial \boldsymbol{\dot r}} }
\end{gather}$$

You can see that the Lagrange equation satisfies for the Lagrangian because,

$$
\begin{gather*}
    \boldsymbol{F} = \frac{d}{dt}\boldsymbol{P}\\
    \frac{\partial \mathcal{L}}{\partial \boldsymbol{r}} = \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \boldsymbol{\dot r}}
\end{gather*}
$$

We may also do this for the rotational counterpart say in polar coordinates $\boldsymbol{r} = \boldsymbol{r}(r,\phi)$,

$$
\begin{align}
    \boxed{\boldsymbol{\tau} = \frac{\partial \mathcal{L}}{\partial \phi}}\\
    \boxed{\boldsymbol{L} = \frac{\partial \mathcal{L}}{\partial \boldsymbol{\dot \phi}}}
\end{align}
$$

## Lagrangian in a Constrained System
A system in constraint is one at which constraint forces come into play (normal force, tension force, etc). While defined so, we prefer to considered a constraint system where we write a relationship between each generalized coordinate

**Example:** 
: For example the x and y position of a ladder leaning against the wall has the constraint that the ladder is some length $l$. It is obvious that the constraint is by Pythogorean theorem,
: 

    $$
    \begin{align}
        x^2 + y^2 = l^2 =\text{const}
    \end{align}$$

: We see that there is a relationship between $x$ and $y$