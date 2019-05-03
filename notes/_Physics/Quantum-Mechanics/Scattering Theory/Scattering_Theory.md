---
title: Quantum Scattering Theory
---

<!-- TOC -->

- [Partial Wave Analysis](#partial-wave-analysis)
- [Phase Shifts](#phase-shifts)
- [Cross Sections](#cross-sections)

<!-- /TOC -->

You may want to review some scattering terms in the section [Cross Sections](#cross-sections).

It is not a surprise that in quantum physics we will be using the wavefunction to describe the equivalent position in classical scattering. Afterall we want to know the probability distribution of the scattered particle.

Let's begin by describing the incident particle which has some wavefunction $\psi_{inc}$. We wish for our initial condition to be the same as a free particle moving towards the right so it must be that initially it doesn't see/feel the potential location at $r = 0$. To do this we say that the free particle is moving towards the positive $\hat z$ direction intiially at $r = -\infty$,

$$ \psi_\text{inc}(z) \approx  e^{ikz}$$

We predict that the outgoing particle is a spherical wave with a probability dependent on $\theta$ we define this probability-like function as $f(\theta)$, this is called the **scattering amplitude**.
$$ \psi(r,\theta)_\text{out} \approx  f(\theta) \frac{e^{ikr}}{r}$$

Therefore the wavefunction in the middle of our experiment should include both incoming and outgoing wavefunctions,

$$ \psi \approx A\left(e^{ikz} + f(\theta) \frac{e^{ikr}}{r}\right)$$

The scattering amplitude once again is related to the probability thus related to the number of particle going through the cross section $d \sigma$ it is only natural that the scattering amplitude ,

$$
\d \sigma = \abs{f}^2 d\Omega\\
\boxed{D(\theta) = \frac{d\sigma}{d\Omega} = \abs{f(\theta)}^2}
$$

<!-- Proof
: 
    $$ dP = \abs{\psi_\text{inc}}^2 \d V $$ -->

Now all we need to do is solve for $f(\theta)$; this is not trivial and requires a good amount of assumptions. There are two prevailing methods which are the **partial wave analysis** and the **Born approximation**. I will only cover the first

## Partial Wave Analysis
The partial wave analysis takes the wavefunction at every three separate regions $r \gg 0$, $r \not\gg 0$, and $r = 0$ respectively called the **radiation zone** (or **asymptotic region**), **intermediate region**, and **scattering region**. In every region we assume the following:

* The wavefunction is some form of the Hydrogen wavefunction
* The wavefunction is independent of $\phi$ because there does not exist any particle heading into or out of the page due to incoming wave being purely dependent on $z$
* Because there is no $\phi$ dependence $m = 0$,
    $$ \psi_\text{out}(r,\theta) = R(r)Y_l^0(\phi)$$

Radiation zone
: In the radiation zone the potential is simply the centrifugal term (not zero) which is apparrent only in the radial function. Like usually it is easier to deal with a substitution $u(r) \equiv rR(r)$,

    $$ \frac{\d ^2 u}{\d r^2} - \frac{\ell(\ell + 1)}{r^2}u = -k^2u $$

    The solution is the Bessel functions,

    $$ u(r) = Arj_\ell(kr) + Brn_\ell(kr) $$

    However since we only want solution that's outgoing as a sinusoidal, these are a variant of the Bessel function called the **spherical Hankel functions**:

    $$ h_\ell^{(1)} = j_\ell(kr) + in_\ell(kr), \qquad h_\ell^{(1)} = j_\ell(kr) - in_\ell(kr) $$

    At large $r$, only the $h^{(1)}_\ell(kr)$ exist as a outgoing wave $e^{ikr}/r$ so in conclusion the radial wavefunction is,

    $$ R(r) \sim h_\ell^{(1)}(kr) $$

    In this region, the wavefunction should be,

    $$
    \psi(r,\theta) = A\left(e^{ikz} + \sum_{\ell=0}{c_{l,m}h_\ell^{(1)}}(kr)Y^0_l(\theta)\right) \\
    Y_l^0(\theta) = \sqrt{\frac{2\ell + 1}{4\pi}}P_\ell(\cos \theta)\\
    c_{l,m} Y_l^0(\theta) = i^{\ell + 1}(2\ell + 1)a_\ell P_\ell(\cos\theta)\\
    c_{\ell,0} \equiv i^{\ell+1}k\sqrt{4\pi(2\ell + 1)}\\
    $$

    $$
    \boxed{\psi(r,\theta) = A\left(e^{ikz} + \sum_{\ell=0}{i^{\ell + 1}(2 \ell + 1)a_\ell h_\ell^{(1)}}(kr)P_\ell(\cos\theta)\right)}
    $$

    * $a_\ell$ : Partial wave amplitude which is literally the amplitude of the sinusoidal wave that has the angular momentum number $\ell$.
    * $h_\ell^{(1)} \approx (-i)^{\ell + 1}e^{ikr}/kr$ for large $r$

You can easily extract $f(\theta)$ given this,

$$ f(\theta) = \sum_{\ell = 0}^{\infty}{(2\ell + 1)a_\ell P_\ell(\cos\theta)} $$

Plugging this into $D(\theta)$ and then solving for the total cross section you get,

$$
\boxed{D(\theta) = \abs{\sum_{\ell = 0}^{\infty}{(2\ell + 1)a_\ell P_\ell(\cos\theta)} }^2}\\
\boxed{ \sigma = 4\pi \sum_{\ell = 0}^{\infty}{(2\ell + \ell)\abs{a_\ell}^2} }
$$

Now we need only to solve for $a_\ell$ the partial wave amplitude.

## Phase Shifts

The answer to $a_\ell$ is a phase shift to see why we must rewrite the wavefunction expanding $e^{ikz}$ with **Rayleigh's formula** just so we can represent everything in spherical coordinates,

$$ e^{ikz} = \sum_{\ell = 0}^\infty{i^{\ell}(2\ell + 1)j_\ell(kr)P_\ell(\cos \theta)}$$

$$\psi(r,\theta) = A\sum_{\ell=0}i^{\ell}(2 \ell + 1)\left[j_\ell(kr) + ika_\ell h_\ell^{(1)}\right](kr)P_\ell(\cos\theta)
$$

Why we believe $a_\ell$ is to be purely a phase change is because this scattering (presumably inelastic) has no angular momentum in the $\hat z$ direction (hence $\phi = 0$) therefore it must be that the wavefunction does not change in partial wave amplitude.

For $V=0$ ($\ell = 0$), the wavefunction $\psi_\ell$ is,

$$ \psi_0 = A\frac{2\ell + 1}{2ikr}\left[e^{ikr} + (-1)^{\ell + 1}e^{ikr}\right]P_\ell(\cos\theta)$$

For $V \ne 0$, this is just a phase difference as $r \rightarrow 0$,

$$ \psi^{(\ell)}(r) = A\frac{2\ell + 1}{2ikr}\left[e^{i(kr + 2\delta _\ell)} + (-1)^{\ell + 1}e^{-ikr}\right]P_\ell(\cos\theta)$$

You can match this equation with the previous wavefunction to get,

$$\boxed{ a_\ell = \frac{1}{2ikr}\left(e^{2i\delta_\ell} - 1\right) = \frac{1}{k}e^{i\delta_\ell}\sin(\delta_\ell)}\\
\boxed{D(\theta) = \abs{\sum_{\ell = 0}^{\infty}{\frac{2\ell + 1}{k}e^{i\delta_\ell}\sin(\delta_\ell) P_\ell(\cos\theta)} }^2}\\
\boxed{\sigma = \frac{4\pi}{k^2}\sum_{\ell = 0}^\infty{(2\ell + 1) \sin^2{(\delta_\ell)}}}$$

## Cross Sections

The **differential scattering cross-section** describes the ratio of the incident particle going through an infinitesimal **cross-sectional area** $\d \sigma$ to the outgoing solid angle $\d \Omega$ so,

$$\boxed{ D(\theta) \equiv \frac{\d \sigma}{\d\Omega} }$$

* $\theta$ : Azimuthal parameter interpreted as the angular position, we can easily see that a free particle has a maximum at $\arg\max D(\theta) = 0$ (where $\theta = 0$ is the direction the free particle is moving) not only that $D(\theta) = 0$ for $\theta \ne 0$.

The **total cross-section** is the total area of th incident particle scattered by the target.

$$\boxed{ \sigma \equiv \int{D(\theta)\d \Omega} }$$

Another useful identity is to write this in terms of the impact parameter $b$ (defined as the one-dimensional distance away from the center, often times vertical distance), we can do so because $\d \sigma$ can be written as,

$$\boxed{ \d\sigma = b \d b \d\phi } \\ \downarrow \\ D(\theta) = \frac{b}{\sin\theta}\abs{\frac{\d b}{\d \theta}} $$

In scattering theory, it is preferable to write this in terms of particle luminosity,

$$ \mathcal{L} = \frac{\d N}{\d \sigma \d t} = \frac{\d N}{D(\theta) \d \Omega \d t}$$

It is customary to ignore $dt$ such that $\d N$ may be interpreted as the number of particles per second so set $\d N \rightarrow \d N / \d t$

$$\boxed{ D(\theta) = \frac{1}{\mathcal L} \frac{dN}{d\Omega} }$$

