---
title: Linear Acceleration
---

We begin studying mechanics on an non intertial frame with cases of linear acceleration. To do so imagine an inertial frame $S_0$ and an accelerating frame $S$. Relative to $S_0$, $S$ is moving at a velocity $\mathbf{V}$ and acceleration $\mathbf{A}$. A ball of mass $m$ is in the $S$ frame, let's explore the forces on the ball.

The ball follow's Newton's second law in the inertial frame thus,

$$ m\ddot{\mathbf{r}} = \mathbf{F} \tag{Newton's 2nd Law - Inertial Frame} $$

Where $\dot{\mathbf{r_0}}$ is defined with the Gaussian transform (vector-addition formula) of the ball's velocity relative to $S$ and the velocity of $S$,

$$ \dot{\mathbf{r}} = \dot{\mathbf{r}} + \mathbf{V} $$

We wish to know Newton's second law for the observer in the accelerating frame $S$. Therefore we need $\ddot{\mathbf{r}}$,

$$ \ddot{\mathbf{r}} = \ddot{\mathbf{r}} - \mathbf{A} $$

$$\begin{equation}
\boxed{m\ddot{\mathbf{r}} = \mathbf{F} - \underbrace{\hphantom{\ \ }m\mathbf{A}\hphantom{\ \ }}_{\mathbf F_\text{inertial}}}\tag{Newton's 2nd Law - Linear Accelerating Frame}
\end{equation}$$

*  $\mathbf{F}_\text{inertial}$ : The non-intertial frame introduces the force called the **inertial force** or infamously the **ficticious force**.