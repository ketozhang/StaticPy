---
title: Rotating Frame
---

## Notation and Review
Because rotational frame are difficult and often not remembered let's have some quick review:

Angular momentum vector
: The angular momentun vector $\boldsymbol{\omega}$ points towards the direction of rotation (clockwise or counter: CW or CCW). You may also use the direction by right hand rule (direction is towards the thumb as the right hand wraps around the vector either CW or CCW),

    $$ \boldsymbol{\omega} = \omega \hat \omega $$

    * $\omega$ : Magntiude as the speed of rotation
    * $\hat \omega$ : Direction of rotation

    As a function of time, $\boldsymbol{\omega}(t)$ may change on either magnitude $\omega$ and/or direction $\hat \omega$
 
Velocity vector
: The velocity vector if you remember has a magnitude of $v = \omega r$. Because thedirection of the velocity is always perpendicular to the angular velocity vector $\boldsymbol{\omega}$ and the distance away from the axis $\mathbf{r}$ we can easily see that therelationship should be a cross product,

 $$ \mathbf{v} = \boldsymbol\omega \times \mathbf r $$

## Time Derivatives in Rotating Frame

Consider two frames $S$ (rotating frame of angular frequency $\mathbf \Omega$) and rest frame $S_0$ with and arbitrary vector $\mathbf Q$ defined in the $S$ frame with basis stationary in respect to $S$

$$ \mathbf Q = \sum_i{\mathbf Q_i \mathbf e_i} $$

The time derivative of $\mathbf Q$ along the $S$ is simply,

$$ \dot{\mathbf Q} =  \sum_i{\dot{\mathbf Q_i} \mathbf e_i}$$

The time derivative of $\mathbf Q$ along the $S_0$ (denote this as $\dot {\mathbf Q_0}$) is then,

$$ \dot{\mathbf Q}_0=  \sum_i{\dot{Q_i} \mathbf e_i + Q_i \dot{\mathbf e_i}}\\
\dot{\mathbf Q}_0= \dot{\mathbf Q} + \sum{Q_i \dot{\mathbf e_i}}$$

The second term has the time derivative of the basis vector $\dot{\mathbf e_i}$. You may interpret this as a velocity vector along $\hat e_i$ therefore it must be that,

$$
\dot{\mathbf e_i} = \mathbf\Omega \times \mathbf e_i
$$

$$
\dot{\mathbf Q}_0=  \dot{\mathbf Q} + \sum{Q_i (\mathbf\Omega \times \mathbf e_i)}\\
\boxed{\dot{\mathbf Q}_0=  \dot{\mathbf Q} + \mathbf\Omega \times \mathbf Q}
$$

## Newton's Second Law in Rotating Frame

To form Newton's second law we need to define acceleration $\ddot{\mathbf r}_0$ in the rest frame $S_0$. Let's apply the time derivative using the relation of $\dot{\mathbf Q_0}$ above,

$$ \ddot{\mathbf r}_0 = \overbrace{\frac{d}{dt}\underbrace{\left(\dot{\mathbf r} + \mathbf\Omega \times \mathbf r\right)}_{\mathbf Q'}}^{\dot{\mathbf Q}_0'}$$

Notice that the terms inside the parenthesis is just another vector where we want to take the time derivative with respect to $S_0$. We once again apply the relation and take the derivative where $\dot {\mathbf \Omega}_0 = \dot {\mathbf \Omega} = 0$ (constant rotation in both reference frames),

$$
\ddot{\mathbf r}_0 = \ddot {\mathbf r} + 2\mathbf\Omega \times \dot {\mathbf r} + \mathbf\Omega \times \left(\mathbf\Omega \times \mathbf r \right)
$$

We may write Newton's second law in either $S_0$ frame ($\mathbf F_0 = m\ddot{\mathbf r_0}$) or $S$ frame ($\mathbf F = m\ddot{\mathbf r}$). Let's choose the $S$ frame because it will result into a force familiar to Earthlings in the rotating Earth.

$$ \underbrace{m\ddot{\mathbf r}_0}_{\mathbf F_0} = 2m\mathbf\Omega \times \dot {\mathbf r} + \underbrace{m\ddot {\mathbf r}}_{\mathbf F} +  m\mathbf\Omega \times \left(\mathbf\Omega \times \mathbf r \right)$$

Isolating $\mathbf F$ gives,

---

$$ \mathbf F = \mathbf{F_0} + \underbrace{2m\dot {\mathbf r} \times \mathbf \Omega}_{F_\text{cor}} + \underbrace{m(\mathbf \Omega \times \mathbf r) \times \mathbf \Omega}_{F_\text{cf}} \\
\boxed{F_\text{cor} = 2m\dot {\mathbf r} \times \mathbf \Omega}\\
\boxed{F_\text{cf} = m(\mathbf \Omega \times \mathbf r) \times \mathbf \Omega}
$$

* $\mathbf F_\text{cor}$ : The **coriolis force**
* $\mathbf F_\text{cf}$ : The **centrifugal force** notice that we may deduce the equation's magntiude as something very familiar, the centripetal velocity $v_\text{cf}$ as $F_\text{cf} = -mv_\text{cf}\Omega$. This is centrifugal because of the negative sign on the centripetal velocity you're familiar with.
* $\mathbf F$ : The force apprent to observers in the rotating frame $S$, notice that it is no longer simply $\mathbf F = m \mathbf a$ but the extra terms which most people call **ficticious force**
---
