---
title: Dipole
---

The dipole is the second term ($n=1$) of the multipole expansion. This is useful when at large $r$ when the total charge at large distance is zero.

$$
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\frac{1}{r^2}\cdot\int{(r'\cos\alpha)\rho(\boldsymbol{r'}) d\mathcal V}\\
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\frac{\boldsymbol{\hat r}}{r^2}\cdot\int{\boldsymbol{r'}\rho(\boldsymbol{r'}) d\mathcal V}
$$

The integral is called the **dipole moment**,

$$
\boxed{\boldsymbol{p} \equiv \int{\boldsymbol{r'} d\mathcal q} = \int{\boldsymbol{r'}\rho(\boldsymbol{r'}) d\mathcal V}}
$$

resulting in the equation of the dipole potential,

$$
\boxed{V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0} \frac{\boldsymbol{p} \cdot \boldsymbol{\hat r}}{r^2}}
$$

## Physical Dipole

The physical dipole is a simplest dipole of two point charges opposite charge with mangitude $q$ and distance vector $\boldsymbol d = \boldsymbol r'_+ - \boldsymbol r'_-$, the dipole moment is given by,

$$
\boxed{\boldsymbol p = q \boldsymbol d}
$$

### Torque

For the dipole, if a uniform electric field was applied a torque may be experience with,

$$
\boxed{\boldsymbol \tau = \boldsymbol{p} \times \boldsymbol{E}}
$$

This behavior often describes what if an electric field is applied to a molecule with some polarity

## Polarization

A polarized object has a quantity called the polarization defined as,

$$
\boxed{\boldsymbol P \equiv \frac{\mathrm d \boldsymbol{p}}{\mathrm d \mathcal V}}
$$

However, the polarization is also a cross-sectional area charge density since $\mathrm d \boldsymbol p  = \boldsymbol r\ \mathrm d q$,

$$
\mathrm d \boldsymbol \sigma = \boldsymbol r \mathrm d \mathcal V\\
\boldsymbol P = \boldsymbol r \frac{\mathrm d q}{\mathrm d \mathcal V} = \frac{\mathrm d q}{d \boldsymbol \sigma}
$$

## Bound Charges

For a distriubtion of dipole we may integrate the potential of the dipole along the infinitestimal geometry. Let's use a 3D object with a 2D surface with infinitestimal $\mathrm d \mathcal V$ and $\mathrm d A$ respectively. Let the object be centered at the origin and the potential point be at distance $d$ away from the origin such that $d \gg r'$ for every point on the distribution. The integral form of the dipole potential is,

$$
\mathrm dV(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0} \frac{\boldsymbol{\hat r} \cdot \mathrm d \boldsymbol{p}}{d^2} \\
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0} \int \frac{\boldsymbol{\hat r} \cdot \boldsymbol{P}(\boldsymbol r')}{d^2} \mathrm d \mathcal V
$$

The potential can be derived into two terms,

$$
\sigma_b \equiv \boldsymbol{P} \cdot \boldsymbol{\hat n}\\
\rho_b \equiv -\nabla \cdot \boldsymbol{P}\\
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\Bigg[\oint_{S} \frac{\sigma_b}{d}\mathrm d A + \int_\mathcal{V}{\frac{\rho_b}{d}\mathrm d \mathcal V}\Bigg]
$$

* $\sigma_b$ : Charge density of the surface
* $\rho_b$ : Charge density of the volume