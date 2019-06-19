---
title: Center of Mass
---

<!-- TOC -->

- [External Force - Point Particle Property](#external-force---point-particle-property)
- [Total Angular Momentum](#total-angular-momentum)
    - [Proof](#proof)
    - [Relationship with Torque](#relationship-with-torque)
    - [Proof](#proof-1)
- [Total Kinetic Energy](#total-kinetic-energy)
    - [Proof](#proof-2)
- [Total Potential Energy](#total-potential-energy)

<!-- /TOC -->

The center of mass $\mathbf R$ is defined as the position given by the mass weighted average in math that is for $N$ particles,

$$ \boxed{\mathbf{R} = \frac{1}{M}\sum_{\alpha = 1}^{N}{m_\alpha \mathbf r_\alpha}} $$

The following section we will look at the properties of the center of mass.

## External Force - Point Particle Property

The center of mass is often very useful because we can always justify almost any rigid body as point particles. This is due to,

$$ \mathbf{P} = \sum_\alpha{m_\alpha \dot{\mathbf r}} = M\mathbf{\dot R} \\
\boxed{\mathbf F_\text{ext} = \dot{\mathbf P} = M\ddot{\mathbf{R}}}
$$

Of course we're assuming the mass does not change over time (part of rigid body definition).

## Total Angular Momentum

The total angular momentum $\mathbf J$ is composed of the angular momentun of the CM (orbital angular momentum $\mathbf L$) and the angular momentum of each rigid body particle relative to the CM (spin angular momentum $\mathbf S$).

$$
\boxed{\mathbf J = \underbrace{\vphantom{\sum}\mathbf R \times \mathbf P}_{\mathbf L} + \underbrace{\sum\mathbf {r}'_\alpha \times m_\alpha \dot{\mathbf r}_\alpha'}_{\mathbf S}}
$$

* $\mathbf r_\alpha'$ : Position vector describing the distance away from the center of mass

    $$ \mathbf r_\alpha' \equiv \mathbf{\mathbf r_\alpha - \mathbf R} $$

### Proof
This is easily proven knowing that the total angular momentum is define as the angular momentum of each particle relative to some origin,

$$
\mathbf{J} \equiv \mathbf{r_\alpha} \times \mathbf{p_\alpha} = \mathbf{r_\alpha} \times m_\alpha\dot{\mathbf{r}}_\alpha
$$

In terms of the distance away from the origin we can replace $\mathbf{r_\alpha}$ with,

$$ \mathbf r_\alpha' \equiv \mathbf{\mathbf r_\alpha - \mathbf R} $$

Doing so and crossing out zeroes gives,

$$ \mathbf J = \underbrace{\vphantom{\sum}\mathbf R \times \mathbf P}_{\mathbf L} + \underbrace{\sum\mathbf {r}'_\alpha \times m_\alpha \dot{\mathbf r}_\alpha'}_{\mathbf S} $$

### Relationship with Torque

Let's define the total torque applied to the system about the origin as $\boldsymbol \tau$,

$$ \boldsymbol\tau = \dot {\mathbf J}  $$

As you've guessed it, the total torque is composed of the torque acted upon the CM $\boldsymbol{\tau}_{CM}$ and the torque acted upon each particle relative to the CM $\boldsymbol{\tau}_\text{rot}$,

$$\boxed{ \boldsymbol{\tau} = \dot{\mathbf L} + \dot{\mathbf S} = \underbrace{\vphantom{\sum}\boldsymbol{R} \times \mathbf{F}_\text{ext}}_{\boldsymbol{\tau}_{CM}} + \underbrace{\sum{\mathbf{r}'_\alpha \times \mathbf F_\alpha^\text{ext}}}_{\boldsymbol\tau_\text{rot}} }$$

### Proof

## Total Kinetic Energy
Similar to the angular momentum, the total kinetic energy is made up of the CM's kinetic energy and the kinetic energy (only rotational) of each rigid body relative to the CM,

$$ \boxed{K \equiv \underbrace{\frac{1}{2}M\dot{\mathbf R}^2}_{K_\text{CM}} + \underbrace{\frac{1}{2}\sum m_\alpha {\dot{\mathbf{r}}_\alpha'}^2}_{K_\text{rot}}}
$$

* $\mathbf R$ : For the total kinetic energy, it is not necessary that $\mathbf R$ be a located at the center of mass. You may choose any point of reference and preferably one that does not move since if $\dot{\mathbf R } = 0$,

    $$ K = \frac{1}{2}\sum m_\alpha {\dot{\mathbf{r}}_\alpha'}^2 \tag{$\dot{\mathbf R} = 0$} $$

### Proof

## Total Potential Energy

The total potential energy is just the external potential energy of the CM. We can do so because we consider the internal potential as a zeropoint (there should be no differential potential energy for a system of rigid bodies).

$$\boxed{ U = U_\text{ext} }$$