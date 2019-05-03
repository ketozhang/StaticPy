---
title: N-Body Problem
parent: Lagrangian
---

## Two Body Problem
The two body problem is one at which two particles interacting at vector position $\boldsymbol{r_1}$ and $\boldsymbol{r_2}$ away from some arbitrary origin. The insignificance of this origin is what makes this problem difficult. The interaction of the two particle is some potential energy (e.g., gravitational potential, electrical potential) that has a distance dependent. The distance between the two particle is $r = \abs{\boldsymbol{r_1}-\boldsymbol{r_2}}$ thus their Lagrangian is,

$$
\begin{align}
    \mathcal{L} = \frac{1}{2}m_1\boldsymbol{\dot r_1}^2 + \frac{1}{2}m_2\boldsymbol{\dot r_2}^2 - U(r)
\end{align}
$$

With the natural choice of $\boldsymbol{r_1}$ and $\boldsymbol{r_2}$ as generalized coordinates.

### Center of Mass - Generalized Coordinates
Often times we use the the **center of mass (CM)** as the frame of reference. The CM is at vector position $\boldsymbol{R}$ you may recall the formula,

$$
\begin{gather}
    \boldsymbol{R} = \frac{m_1\boldsymbol{r_2}+m_2\boldsymbol{r_2}}{M}\\
    \boldsymbol{r_1} = \boldsymbol{R} + \frac{m_2}{M}\boldsymbol{r}\qquad \boldsymbol{r_2} = \boldsymbol{R} - \frac{m_1}{M}\boldsymbol{r}
\end{gather}
$$

* $M$ : Total mass $M \equiv m_1 + m_2$
* $\boldsymbol{r}$ : Particle's distance vector of length $r$ as discussed before.

Why we do so is because if the system is isolated then $\dot R$ is constant, then CM does not accelerate thus it's a rest frame. Let's rewrite the Lagrangian with these generalized coordinate,

$$
\begin{gather}
    T = \frac{1}{2}M\dot R^2 + \frac{1}{2}\mu\dot r^2\\
    \mu = \frac{m_1m_2}{M}
\end{gather}
$$

$$
\begin{gather}
    \boxed{\mathcal{L} = \frac{1}{2}M\dot R^2 + \left[\frac{1}{2}\mu\boldsymbol{\dot r}^2 - U(\boldsymbol{r})\right]}\\
    \mathcal{L} = \mathcal{L_{cm}} + \mathcal{L_{rel}}
\end{gather}
$$

* $\mu$ : Reduced mass
* $\mathcal{L_{cm}}$ : Lagrangian of the CM
* $\mathcal{L_{rel}}$ : Lagrangian of the relative distance.

The Lagrange equation gives the equation of motion for $R$ and $\boldsymbol{r}$.

$$
\begin{gather}
    M\ddot R = 0\\
    \boxed{\dot R = \text{const}}\\
\end{gather}
$$

$$
\begin{gather}
    \boxed{\mu\ddot r = -\nabla U(\boldsymbol{r})}
\end{gather}
$$

The last line infers what we expect $F_r = -\nabla U(\boldsymbol{r})$

### Center of Mass - Rest Frame
We never actually used the center of mass as a frame yet since we didn't set $\dot R = 0$, doing so and rewriting everything relative to the CM frame. In this frame, we imagine two masses $m_1$ and $m_2$ orbitting a central rest mass $\mu$ from their respective distances $\boldsymbol{r_1}$ and $\boldsymbol{r}_2$.

$$
\begin{gather}
    \boldsymbol{r_1} = \frac{m_2}{M}\boldsymbol{r} = \frac{\mu}{m_1}\boldsymbol{r} \\ \boldsymbol{r_2} = -\frac{m_1}{M}\boldsymbol{r} = -\frac{\mu}{m_2}\boldsymbol{r}\\
    \frac{\boldsymbol{ r_1}}{\boldsymbol{ r_2}} = \frac{m_2}{m_1}
\end{gather}
$$
The main purpose for this center of mass frame is to separately find the relationship between $r_1$ to $\mu$ and $r_2$ to $\mu$ separately.

## Center of Mass - Single Mass Frame
What is amazing about this problem is that we can further simplify the problem to be a mass $\mu$ rotating around the CM at length $\boldsymbol{r}$. The reason so is because the angular momentum is the same for system of two orbiting masses of $m_1$ and $m_2$ than with one orbiting mass of $\mu$,

$$ L = \boldsymbol{r}_1 \times \boldsymbol{p}_1 + \boldsymbol{r}_2 \times \boldsymbol{p}_2 = \boldsymbol{r} \times \mu \boldsymbol{\dot r}$$

The Lagrangian for the one orbiting mass $\mu$ is now done in polar coordiantes since the $r$ is the distance from origin where $\boldsymbol{r} = \boldsymbol{r}(r,\phi)$,

$$
\begin{equation}
    \mathcal{L} = \frac{1}{2}\mu(\dot r^2 + r^2\dot{\phi^2}) - U(r)
\end{equation}
$$

The Lagrangian is independent of $\phi$ so angular momentum along $\phi$ is conserve. We can represent this by applying the Lagrange equation to get a $\phi$ equation,

$$
\begin{align}
    \mu r^2 \dot \phi = L_z\\
    \phi(r,t) = \frac{L_z}{\mu r^2}t + \phi_0 
\end{align}
$$

* $L_z$ : A constant angular momentum along $z$ which is equivalent to the angular momentum along $\phi$
* It's important to notice that $\phi$ is dependent on $r$ not only $t$. We definitely wish to find $\phi(t)$ or $\phi(r)$ but first we need the radial equation. 


The $r$ equation (**radial equation**) is then,

$$
\begin{gather}
    \boxed{\mu \ddot r = \mu r\dot \phi - \frac{dU}{dr}}
\end{gather}
$$

### One-Dimensional Reduction
Notice that the radial equation is a sum of two potentials where $F_r = \mu \ddot r$ 

$$
\begin{gather}
    F_r = -\frac{d}{dr}\left[U_\text{cf}(r) + U(r)\right]\\
    U_\text{cf}(r) = \int {\mu r\dot\phi\; dr}\\
\end{gather}
$$

For $U_\text{cf}(r)$, we may replace $\dot \phi$ with $\dot \phi= \frac{L_z}{\mu r^2}$

$$
\begin{gather}
    F_\text{cf} = \mu r \left(\frac{L_z}{\mu r^2}\right)^2 = \frac{L_z^2}{\mu r^3}\\
    U_\text{cf}(r) = -\int{F_\text{cf}\; dr} = \frac{L_z^2}{2\mu r^2}
\end{gather}
$$

The new radial equation is then,

$$
\begin{gather}
    F_r = -\frac{d}{dr}\left[U(r) + U_\text{cf}(r)\right] = -\frac{d}{dr}U_\text{eff}(r)\\
    U_\text{eff}(r) = U(r) + U_\text{cf}(r)
\end{gather}
$$

This is what we meant by the problem can be simplified to a single dimension of a single parameter $r$ (distance away from CM). Initially the only potential was gravitational potential (for the orbital problem) but because we are in the rotating frame, there exist a fictitious force $F_\text{cf}$ which the subscript really means the **centrifugal force**.