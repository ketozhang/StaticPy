---
title: Capacitor
---

## Capacitance

Capacitance is defined as the constant of proportionality between charge and electric potential.

$$
C \equiv \frac{q}{V}
$$

* $q$ : Charge of the positive terminal
* $V$ : The electric potential required to move a charge from the negative terminal to the positive terminal.

Despite the capacitance is defined with dependence on $q$ and $V$, when describing the capacitance of a specific capacitor this is false as any change in $q$ also changes $V$ so that $C$ stays constant. The capacitance is purely dependent on the geometry of the capacitor.

## Infinite Sheet

An infinite plate of an electric field uniformly distributed with electric density $\rho$ produces a electric field of $\boldsymbol{E}$ pointinng normal to the surface on both sides of the slate. Using the Gaussian pill box for area $A$ at a negligible height the enclosed charge is,

$$
Q_\mathrm{enc} = \sigma A
$$

The surface integral of the electric field is,

$$
\oint \boldsymbol{E} \cdot \mathrm d \boldsymbol A = 2\boldsymbol{E}A
$$

Thus by Gauss's law,

$$
\boxed{E = \frac{\sigma}{2\epsilon_0}}
$$

## Infinite Twin Plate Capacitor

Consider two plate of metal similar to the [infinite sheet](#infinite-sheet) however with a definite area $A$. Fill on plate with purely positive charge $q=Q$ and the other plate purely negative charges $q=-Q$. We only pay attention to the electric field between the positive plate and the negative plate thus the LHS of Gauss's law is half that of the infinite sheet,

$$
\oint \boldsymbol{E} \cdot \mathrm d \boldsymbol{A} = EA = \frac{Q}{\epsilon_0}\\
E = \frac{Q}{A}
$$

Let the area be much greater than the separation of the two plates $A \gg d$ such that the charge are uniformally distributed along the plate with charge density $\sigma = Q/A$. Thus the electric field is twice that of the infinite sheet.

$$
E = \frac{\sigma}{\epsilon_0}
$$

Because the electric field is constant along the uniform sheet, the electric potential is just

$$
V  = \frac{\sigma}{\epsilon_0}d\\
\boxed{C = \frac{Q}{V} = \frac{A\epsilon_0}{d}}
$$