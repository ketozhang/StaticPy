---
title: Einstein's Field Equation
---

Einstein's general relativity proposed the idea that the energy density and pressure of the universe is directly related to spacetime curvature. 

If the universe was purely made of up mass thus only gravity matters, the field equation (equation for how a free particle moves in some space) for the universe will be the Poisson equation:

$$ \begin{equation}
    \nabla^2 \Phi = 4\pi G\rho
\end{equation} $$

* $\Phi$ : Gravitational potential
* $\rho$: mass density

However general relativity tells us that not only mass in general contribute to the spacetime curvature but also radiation, dark energy, universe's curvature, and any types of energy energy. Thus we need a field equation that describe all of these which is called the **Einstein's Field Equation**:

$$ \begin{equation}
    \boxed{G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}}
\end{equation} $$

* $G_{\mu\nu}$ : The **Einstein tensor**, a $4\times 4$ symmetric matrix that describes the curvature of space at every location $t,x,y,z$.
* $T_{\mu\nu}$: The **stress-energy tensor** (or **stress tensor**), another symmetric $4\times 4$ matrix. The RHS is a matrix that depends on $P$ and $\rho$ which of course has the parameters $x,y,z,t$.

A $4\times 4$ symmetric matrix has 4 diagonals and 3+2+1 = 6 independent entries. Therefore there is 10 independent differential equation to solve for. While there does exist a very complicated solution, most of the time Einstein's field equation is used within special cases. The following sections list some special cases

Friedmann equation
: In a a homogenous and isotropic system then there is dependence of $\rho$ and $P$ along $x,y,z$ therefore the Einstein's field equation is only time dependent.

    See [Friedmann equation](Friedmann_Equation.md)