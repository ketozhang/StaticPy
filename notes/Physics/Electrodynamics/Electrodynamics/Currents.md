---
title: Currents
---

Current $\bvec I$ is the charge per unit time flowing through some wire. The SI unit is coulombs-per-second $(\mathrm{C\cdot s^{-1}})$ or **amperes** ($\mathrm A$),

$$
\bvec I \equiv \frac{\mathrm d q}{\mathrm d t} \bvec{\hat l}
$$

## Line Current

Speaking of a wire with a line charge $\lambda$ moving through the wire at velocity $\mathbf v$, the current is given as a vector,

$$
\bvec{I} = \lambda \bvec{v}
$$

The magnetic force can be represented by the current via,

$$
\bvec F = \int{\left(\bvec I \times \bvec{B}\right) \mathrm d l} = - I \int{\bvec{B} \times \mathrm d \bvec l }
$$

Notice that the current always point along the wire (since the charge is confined to moving along the wire) thus $\mathrm{dir} \ \bvec{I} = \bvec {\hat l}$

## Surface Current

The current of a strip is given by a **surface current density** $\bvec K$ which is the current per unit width given by,

$$
\boxed{\bvec K \equiv \frac{\mathrm d \bvec I}{\mathrm d w}}
$$

Equivalently, given a surface charge density, the surface current density is also,

$$
\bvec K = \sigma \bvec v
$$

## Volume Current

The current of an object like a cylinder is given by a **volume current density** $\bvec J$ defined as,

$$
\boxed{\bvec J \equiv \frac{\mathrm d \bvec I}{\mathrm d A}}
$$

Where $\mathrm d A$ is the cross-sectional area.

### Continunity Equation

By conservation of charges, the current inside the volume must equal to the amount of charge flowing out of the surface per second. One may derive the differential relationship called the **continunity equation**,

$$
\boxed{\nabla \cdot \bvec J = -\frac{\partial p}{\partial t}}
$$