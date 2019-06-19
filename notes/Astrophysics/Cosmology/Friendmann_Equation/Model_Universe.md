---
title: Model Universe
parent: Friedmann Equation
---

<!-- TOC -->

- [Derivation](#derivation)
- [Empty Universe - Curvature Only](#empty-universe---curvature-only)
- [Flat Universe - No Curvature](#flat-universe---no-curvature)
- [Single Component Universe](#single-component-universe)
    - [Matter or Radiation Dominated Universe](#matter-or-radiation-dominated-universe)
    - [Cosmological Constant Dominated Universe](#cosmological-constant-dominated-universe)
- [Multiple Component Universe](#multiple-component-universe)
    - [Two-Component Equilibrium](#two-component-equilibrium)
    - [Matter + Curvature](#matter--curvature)
    - [Matter + Cosmological Constant](#matter--cosmological-constant)
    - [Matter + Curvature + Cosmological Constant](#matter--curvature--cosmological-constant)
    - [Radiation + Matter](#radiation--matter)

<!-- /TOC -->

With the Friedmann equation, one can play around with the different types of universe by playing around with the either the energy density parameters or the curvature constant. The Friedmann equation that is easiest to deal with is to write the Friedmann equation in terms of density parameter:

$$
\begin{equation}
    H^2 = H_0^2\Omega\\
    \boxed{\left(\frac{\dot a}{a}\right)^2 = H_0^2\left[\frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0} + \frac{(1-\Omega_0)}{a}\right]}
\end{equation}
$$

## Derivation

We define the total density parameter to be $\Omega$,

$$
\begin{gather}
    \mu = \sum_i{\frac{\mu_{i,0}}{a^{3(1+w)}}}\\
    \boxed{\Omega \equiv \frac{\mu}{\mu_c}}\\
    \mu_c = \frac{3}{8\pi G}H(t)^2
\end{gather}
$$

The Friedmann equation can be isolated from the curvature term,

$$ 
\begin{gather}
    H^2(t) - \frac{8\pi G}{3}\mu = -\frac{k}{a^2}\\
    \boxed{H^2(t) \left[1 - \Omega(t) \right]= -\frac{k}{a^2}}
\end{gather}
$$

Let's introduce the Hubble's constant by setting $t = t_0$ and $a(t_0)=1$,

$$
\begin{gather}
    H_0^2 \left[1 - \Omega_0 \right]= -k\\
    \boxed{k = H_0^2 \left[\Omega_0 - 1\right]}
\end{gather}
$$

Plugging in $k$ to the Friedmann equation would give,

$$
\begin{gather}
    \boxed{\left(\frac{\dot a}{a}\right)^2 = H_0^2\left[\frac{\mu}{\mu_{c,0}} + \frac{(1-\Omega_0)}{a}\right]}\\
    \boxed{\left(\frac{\dot a}{a}\right)^2 = H_0^2\left[\frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0} + \frac{(1-\Omega_0)}{a}\right]}
\end{gather}
$$


## Empty Universe - Curvature Only
In the empty universe, all energy densities are set to zero $\Omega = 0$ and the curvature constant only exist. This is one of the rare times we will use the full definition of $k = \kappa c^2/R_0^2$. The Friedmann equation goes as (remember to set $c = 1$),

$$ H^2 = \frac{k}{a^2} = \frac{\kappa}{R_0^2a^2} $$

$$ \begin{equation}
    \dot a = \sqrt{- \frac{\kappa}{R_0^2}}
\end{equation} $$

There exist only two solutions, when $\kappa = 0$ or $\kappa = -1$ ($\kappa = 1$ gives an imaginary solution so let's ignore this.).

$$ \begin{gather}
    \boxed{a = \begin{cases}
        1 & k=0\\
        t/t_0 & k=-1
    \end{cases}}\\
    \boxed{t_0 \equiv \frac{1}{R_0} = \frac{1}{H_0}}
\end{gather} $$

This is the case where **Hubble's time** $H_0^{-1}$ is the age of the universe $t_0$!

## Flat Universe - No Curvature
A flat universe is one at which the curvature constant $k = 0$. The Friedmann equation is then:

$$ \begin{equation}
    H^2 = \frac{8\pi G}{3}\mu
\end{equation} $$

This is a fun universe to play around with because we can get all the extreme cases and outcomes many exciting theories such as the Big Bang, Big Crunch, Big Freeze, etc. However to make this easier it is easier to write the Friedmann equation in terms of the density parameters:

$$ \Omega \equiv \sum_i{\Omega_i} = \sum_i{\frac{\Omega_{i,0}}{a^{3\left(1 + w_i\right)}}}$$

In the flat universe, we define $\Omega_0 = 1$ such that the curvature is $1 - \Omega_0 = 0$ (not necesarrily at all time but some period where $t_0$ is part of).

$$
\begin{gather}
    H^2 = H_0^2\Omega\\
    \left(\frac{\dot a}{a}\right)^2 = H_0^2\left[\frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0}\right]
\end{gather}
$$

* Remaining energy density parameter of unknown particles. We set this to zero for the benchmark model.

Before we begin dwelling into this universe, we begin with the next few sections seeing how each individual components and subsets of these components affect the universe.

## Single Component Universe

The single component universe is a flat universe (we've already covered empty universe universe in the previous section which is a curvature-only) with either matter, radiation, or cosmological constant.

The Friedmann equation for the single component universe is,

$$ 
H(t) = H_0 \sqrt{\frac{\Omega}{a^{3(w+1)}}} \qquad \Omega = 1\\
\dot a = H_0a^{-(1+3w)/2}
$$

### Matter or Radiation Dominated Universe
In the matter or radiation dominated universe, the $w \ne 1$ therefore the differential equation goes as the power law.

$$ H_0 t =  \int{a^{b/2} \d a} \qquad b = 1+3w$$

The scale factor and redshift is then,

$$ 
\boxed{a(t) = \left(\frac{t}{t_0}\right)^{2/3(w+1)}}\\
\boxed{1 + z = \left(\frac{t_0}{t_e}\right)^{2/3(w+1)}}\\
\boxed{t_0 \equiv \frac{2}{3(1+w)}H_0^{-1}}\\
$$

* $t_0$ : This can be interpretted as the age of the universe when the universe was single component dominated
* $t_e$ : The age of the universe when the observed light was emitted. Of course $t_e = t_0$ when $z=0$ by definition.
    
    $$\boxed{ t_e = t_0\left(1 + z\right)^{-3(w+1)/2} }$$

### Cosmological Constant Dominated Universe

<!-- TODO: -->

## Multiple Component Universe


### Two-Component Equilibrium
$$
\frac{\Omega_{i,0}}{\Omega_{j,0}} = a^{(w_i+1)/(w_j+1)}\\
\boxed{a_{ij} = \left(\frac{\Omega_{i,0}}{\Omega_{j,0}}\right)^{(w_j+1)/(w_i+1)}}
$$

### Matter + Curvature

The Friedmann equation for matter and curvature dominated universe is,

$$\boxed{ H(t)^2 = H_0^2\left[\frac{\Omega_0}{a^3} + \frac{1-\Omega_0}{a^2} \right] }$$

* $\Omega_0$ : Energy density at $t_0$, in this universe $\Omega_0 = \Omega_{m,0}$.

* There exist a scale factor when the univere is stationary $H(t)=0$,

    $$
    a_\max = \frac{\Omega_0}{\Omega_0 - 1}, \qquad H_0 > 0\\
    a_\min = \frac{\Omega_0}{\Omega_0 - 1}, \qquad H_0 < 0
    $$

Let's take a look at what happen when $\Omega_0$ is great, less than, or equal to $1$.

|    Density     |   Curvature   |                 Fate                 |
| -------------- | ------------- | ------------------------------------ |
| $\Omega_0 < 1$ | $\kappa =-1$  | Big Chill ($\alpha \propto t$)       |
| $\Omega_0 = 1$ | $\kappa = 0$  | Big Chill ($\alpha \propto t^{2/3}$) |
| $\Omega_0 > 1$ | $\kappa = +1$ | Big Crunch                           |


* If $\Omega_0 > 1$ 
    * then $k = 1$ and the extrema scale factor is positive $a>0$. 
    * that means there exist an extrema for both cases of initially expanding or contracting universe. 
    * for the initially expanding universe $H_0 > 0$ an extrema will be reached at some time where $a(t_\max) = a_\max$ and then begin to contract $H(t) < 0$ for $t > t_\max$. 
    * so say a universe that began with a Big Bang will eventually contract itself into its hot dense "ball" of matter. This contraction is known as the **Big Crunch** 
* If $\Omega_0 = 1$
    * this is the matter dominated universe
    * then $k = 0$ and the extrema scale factor goes to infinity $a \rightarrow \infty$ at the rate $\alpha \propto t^{2/3}$
    * this means that the universe will continue to expand or contract infinitely
    * for the initially expading universe, it will keep expanding and eventually freeze (space between matter is much greater than interaction lengthscale) thus expansion is known as the **Big Chill**.
* If $\Omega_0 < 1$
    * then $k = -1$ and the extrema scale factor goes to infinity $a \rightarrow \infty$ at the rate $\alpha \propto t^{2/3}$
    * The extrema does not exist except at $\Omega_0 = 0$ since we do not allow $a < 0$
    * This is another case of the big chill since $H(t)$ is always positive thus the universe expands at a rate of $a \propto t$

Let's solve for $a(t)$,

Case $\Omega_0 \ne 1$
: 

$$ H_0 t = \int{ \frac{da}{\sqrt{\Omega_0/a + (1-\Omega_0)}} } $$

The solution to this is the cycloid,

$$ 
a(\theta) \equiv \frac{1}{2}\frac{\Omega_0}{\Omega_0 - 1}\left(1 - \cos\theta\right)\\
\boxed{t(\theta) = \frac{1}{2H_0}\frac{\Omega_0}{\left(\Omega_0 - 1\right)^{3/2}}(\theta - \sin\theta)}
$$

* $\theta$ : Ranges from the beginning of the universe $\theta=0$ to the Big Crunch $\theta = 2\pi$

### Matter + Cosmological Constant

### Matter + Curvature + Cosmological Constant

### Radiation + Matter