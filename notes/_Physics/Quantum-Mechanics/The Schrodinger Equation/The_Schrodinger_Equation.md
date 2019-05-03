---
title: The Schrodinger Equation
---

The Schrodinger equation is an equation followed by all of non-relativstic quantum mechanics. It states that for a quantum mechanical system there exist a wavefunction $\Psi(x,t)$ that satisfies the Schrodinger equation given by,

$$ \boxed{i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi} $$

* $\Psi$ : The wavefunction generally written as $\Psi(x,t)$
* $\hat H$ : The Hamiltonian of the system consist of operators that describes the energy of the system.

The Schrodinger equation is often describe as the equivalent of Newton's second law ($F=ma$) for quantum mechanics. Recall that Newton's second law is a partial derivative,

$$ 
\begin{align}
    -\frac{\partial V}{\partial x} &= m\frac{d^2x}{dt^2} \tag{Partial Derivative Form}
\end{align}
$$

## Separation By Variables

The separation by variables may be applied to the Schrodinger Equation to separate into the product of two solutions given by, 

$$\boxed{\Psi(x,t) = \psi(x)\varphi(t), \quad \varphi(t) = e^{\frac{-iEt}{\hbar}}}$$

* $\psi$ : the spacial wavefunction defined as $\psi(x) \equiv \Psi(x)$ 
* $\varphi$ : the temporal wavefunction defined as $\varphi(t) \equiv \Psi(t)$.

If you were to plug in the separated solution into the Schrodinger equation you will get a very important relationship,

$$ \frac{i\hbar }{\varphi}\frac{\partial \varphi}{\partial t} = H\hat \psi = \text{constant} $$

### Derivation
## Time Independent Schrodinger Equation

The **Time Independent Schrodinger Equation (TISE)** is the separated spacial equation of the Schrodinger Equation for the spacial wavefunction $\psi(x)$ given by,

$$ \boxed{\hat H \psi = E\psi} $$

* E : Total energy of the particle.
* The TISE is special equation called the eigenvector $\psi$ and eigenvalue $E$ problem. It states that for some system describe by its Hamiltonian there exist solution(s) (the wavefunction) with energy $E$.
* If there are more than one solution with energy $E$ we consider those solution to be **degenerate**.

## General Solution

Once again we would love to know the solution (a wavefunction) of a system given by some Hamiltonian $\hat H$. We cannot do so without solving for the [Time Independent Schrodinger Equation](#time-independent-schrodinger-equation) which gives us the spacial wavefunction $\psi(x)$. Knowing $\psi(x)$ we can write a general solution,

$$ \Psi(x,t) = \sum{c_n\Psi_n(x,t)} =  \sum{c_n\psi_n(x)\varphi_n(t)}$$
$$ \boxed{\Psi(x,t) = \sum{c_n\psi_ne^{\frac{-iE_nt}{\hbar}}}} $$

## Examples

### Infinite Square Well

### Finite Square Well (Scattering State)

### Finite Square Well (Bounded State) 

### Free Particle

### Potential Step (Scattering State)

### Potential Step (Bound State)

### Delta Potential (Scattering State)

### Delta Potential (Bound State)

