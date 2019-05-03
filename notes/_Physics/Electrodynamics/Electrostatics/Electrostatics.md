---
title: Electrostatics
---

## Coulomb's Law

The force that a charge $q_1$ feel from another charge $q_2$ is governed by **Coulomb's law**,

$$
\boldsymbol{F} = \frac{1}{4\pi\epsilon_0}\frac{q_1q_2}{d^2}\boldsymbol{\hat r}
$$

$\epsilon_0$ : permittivity of free space

## Electric Field

The electric field $\boldsymbol{E}$ is a vector field. For a single charge $q$, the electric field produced will be.

$$
\boldsymbol{E} = \frac{1}{4\pi\epsilon_0} \frac{q}{d^2}\boldsymbol{\hat r}
$$

A test charge of charge $q_0$ would feel an electric force if placed on the electric field equal to a scalar factor of its electric charge. That scalar factor is determined by the test charge's position on the electric field thus,

$$
\boldsymbol{F} = q_0 \boldsymbol{E}
$$

### Continuous Form

Often, Coulomb's law is used to calculate the force of a test particle felt by a continuous collection of charges (e.g., a charged sphere). It is much easier to use the continuous form of the electric field for some continuous shape with the characteristic geometry $\mathrm{d}V$ and characteristic charge density $\mathrm{d}\rho$.

Letting the origin be the center of the continuous charge,

$$
\boldsymbol{E} = \frac{1}{4\pi\epsilon_0} \int{\frac{\rho(\boldsymbol r')}{d^2}\boldsymbol{\hat d} \ \mathrm dV} \tag{continuous charge origin}\\
\boldsymbol{d} = \boldsymbol r - \boldsymbol r' \qquad d = \lvert \boldsymbol{d} \rvert
$$

* $\mathrm d V$ : The infinitestimal characteristic geometry (e.g., volume).
* $\boldsymbol{r}$ : Position vector of the test charge
* $\boldsymbol{r'}$ : Position vector of an infinitestimal part of the continuous charge.

Maybe a simpler method is to let the origin be at the test particle and the continuous charges be at a position defined by a position vector $\boldsymbol{r}$:

$$
\boldsymbol{E} = -\frac{1}{4\pi\epsilon_0} \int{\frac{\rho(\boldsymbol r)}{\lvert \boldsymbol r \rvert^2}\boldsymbol{\hat r} \ \mathrm dV} \tag{test charge origin}
$$

* $\boldsymbol{r}$ : Position vector of each charge in the continuous charge collection.
* The negative sign is needed to correct for changing origins.

## Flux

Rather than the electric field, what is also useful to solve for the electric force comes directly from interpretting Coulomb's law with Gauss' law. That is, the flux of the electric field which is the magnitude of the electric field line penetrating perpendicularly through some surface $S$.

$$ \Phi_E \equiv \int_{S} \boldsymbol{E} \cdot \mathrm d \boldsymbol a $$

### Gauss' Law Integral Form

For a electric field source that can be fully contained by a closed surface that closed surface is penetrated by every electric field line produced by the charge enclosed by the surface. Thus the flux can equivalently describe the amount of charge enclosed by the surface. This is **Gauss' Law**,

$$
\oint_{S} \boldsymbol{E} \cdot \mathrm d \boldsymbol a = \frac{Q_\mathrm{enc}}{\epsilon_0}
$$

### Gauss' Law Differential Form

By the divergence theorem we may transform the surface integral to a volume integral,

$$\oint_{S} \boldsymbol{E} \cdot \mathrm d \boldsymbol a = \int_{V} (\nabla \cdot \boldsymbol E) \ \mathrm dV$$

The enclosed charge can also be written as a volume integral with density $\rho$,

$$
\frac{1}{\epsilon_0}Q_\mathrm{enc} = \frac{1}{\epsilon_0}\int_{V} \rho \ \mathrm{d}V
$$

Equating the two integrands above,

$$
\nabla \cdot \boldsymbol{E} = \frac{\rho}{\epsilon_0}
$$

## Curl

The vector problem of the electric field can always be transformed into a much simpler scalar problem. This is proven because the curl of the electric field is always zero. We may use Stoke's theorem to prove this.

The line integral for a line enclosing the charge is always zero due to the nature of a electric field that follows the inverse square law,

$$
\oint \boldsymbol E \cdot \mathrm d \boldsymbol l
$$

Thus by  Stoke's theorem

$$
\nabla \times \boldsymbol{E} = 0
$$

All of this is another way to say that the electric field is a conservative vector field thus the electric fieild is scalar in nature.