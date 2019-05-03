---
title: Centrifugal Force
---

<!-- TOC -->

- [Example - Earth's Gravitational Acceleration](#example---earths-gravitational-acceleration)

<!-- /TOC -->

The centrifugal force is the force perpendicular to the direction of motion and points radially outwards along the direction of the rotating arm (perpendicular to the axis of rotation). The **centrifugal force** is defined as,

$$ \boxed{\mathbf F_\text{cf} = m(\mathbf \Omega \times \mathbf r) \times \mathbf \Omega} $$

* $m$ : Mass of the object
* $\mathbf r$ : radial vector away from the origin of the rotating frame
* $\mathbf \Omega$ : Angular frequency of the rotating frame

We may simplify this with cylindrical coordinates for any single-axis rotating frame. Let's $\boldsymbol \rho$ be the projection of the $\mathbf r$ vector onto the axis of rotation $\hat \Omega$

$$ \boldsymbol \rho = \rho \hat\rho \\
\rho \equiv \mathbf r \cdot \hat \Omega = r\sin\theta$$

* $\theta$ : Angle between $\mathbf r$ and $\mathbf \Omega$

By the cross product,

$$\boxed{ F_\text{cf} = m\Omega^2 \rho \hat \rho }$$

## Example - Earth's Gravitational Acceleration

The gravitational acceleration of Earth is affected by the centrifugal force such that the angle away from the radial gravitational force (perpendicular to Earth's surface) is observable (however not the actual magnitude). Recall that the effective gravitational acceleration is,

$$ \mathbf g = \frac{\mathbf F_g}{m} + \frac{ m\Omega^2 \rho \hat \rho}{m} \\
= \mathbf g_0 +  \Omega^2 \rho \hat \rho \\
= \mathbf g_0 +  \Omega^2 R\sin\theta \hat \rho 
$$

* $R$ : radius of the Earth

The angle between $\mathbf g$ and $ \mathbf g_0 $ can be calculated by using the components

$$ 
\boxed{\alpha \approx \frac{g_r}{g_\perp}}\\
g_\perp = \Omega^2 R \sin \theta \cos\theta\\
g_r = \Omega^2 R \sin^2 \theta
$$

The maximum angle occurs at $\theta = 45^\circ$ where $\alpha \approx 0.1^\circ$