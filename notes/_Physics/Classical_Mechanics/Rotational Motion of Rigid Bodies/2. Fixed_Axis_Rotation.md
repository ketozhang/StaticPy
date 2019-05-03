---
title: Rotation about a Fixed Axis
---

<!-- TOC -->

- [Angular Momentum](#angular-momentum)
- [Kinetic Energy](#kinetic-energy)

<!-- /TOC -->

We will observe the rotation of a system of rigid bodies on a fixed axis ($\dot{\mathbf R} = 0$). 

## Angular Momentum

The angular momentum of the system is only the spin angular momentum so let $\mathbf L = \mathbf S$

$$ \mathbf L = \sum{\mathbf r_\alpha \times m_\alpha \mathbf v_\alpha} $$

* $\mathbf r_\alpha$ : Position vector relative to the CM
* $\mathbf v_\alpha$ : Velocity vector relative to the CM such that $\mathbf v_\alpha \equiv \dot {\mathbf r_\alpha}$

Since the rigid bodies rotating it is best to use angular frequency in stead of velocity,

$$ \mathbf v_\alpha = \boldsymbol{\omega}_\alpha \times \mathbf r_\alpha \\
v_\alpha = \rho_\alpha \omega\\
\rho_\alpha \equiv \sqrt{x_\alpha^2 + y_\alpha^2}\\
\mathbf{L} = \sum{m_\alpha \mathbf r_\alpha \times \left(\boldsymbol{\omega}_\alpha \times \mathbf r_\alpha\right)} \\
= \sum{m_\alpha \left[\boldsymbol{\mathbf \omega}_\alpha (\mathbf r_\alpha \cdot \mathbf r_\alpha) + \mathbf{r}_\alpha(\mathbf{r}_\alpha \cdot \boldsymbol \omega_\alpha)\right]}  \\
\boxed{\mathbf{L} = \sum{m_\alpha \rho^2\boldsymbol{\mathbf \omega}_\alpha}  }\\
\mathbf{L} = \sum{m_\alpha \left(-x_\alpha z_\alpha,  y_\alpha z_\alpha, x_\alpha^2 + y_\alpha^2 \right)}  \omega \\
\boxed{\mathbf{L} = \sum{\left(-m_\alpha x_\alpha z_\alpha, m_\alpha y_\alpha z_\alpha,I_z\right)\omega}}\\
\boxed{I_z = \sum{m_\alpha \rho_\alpha^2}}
$$

## Kinetic Energy

The kinetic energy is,comprised only of the rotational` kinetic energy so,

$$
T = \frac{1}{2}\sum{m_\alpha v_\alpha^2} = \frac{1}{2}\sum{m_\alpha^2\rho_\alpha^2 \omega^2}\\
\boxed{T = \frac{1}{2}I_z\omega^2}
$$