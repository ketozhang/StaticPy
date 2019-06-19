---
title: Energy Density
parent: = Friedmann Equation
---

## Critical Density
The critical (energy) density corresponds to the case where $k = 0$,

$$
\begin{gather}
    \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\mu\\
    \boxed{\mu_c \equiv \frac{3}{8\pi G}H(t)^2}
\end{gather}
$$

## Density Parameter
With the critical density value we motivate the use of normalizing with $\mu_c$ such that we define the **density parameter** as,

$$
\begin{equation}
    \boxed{\Omega(t) \equiv \frac{\mu(t)}{\mu_c(t)}}
\end{equation}
$$

The universe today is about $\Omega(t_0) \approx 1$ as expected since we live in a flat universe.

Using the density parameter, the Friedmann equation becomes,

$$
\begin{equation}
      \left(\frac{\dot a}{a}\right)^2 = \frac{k}{a^2}\left[1 - \Omega(t)\right]^{-1}
\end{equation}
$$

## Radiation Energy Density
The energy density of radiation consist of all relativistic particles. Those include:

Cosmic Microwave Background
: The photon emitted since the early universe with the energy density given by the CMB temperature $T_0$,

$$ \mu_{\text{CMB},0} = \alpha T_0^4 \\
\Omega_{\text{CMB},0} = 5.35 \times 10^{-5}
$$

Neutrino Background
: Theory suggest that there should exist the quasi-relativistic particle, the neutrinos, that fills the sky very similar to the CMB with an energy density:

$$ \mu_v = 3\cdot\frac{7}{8}\left(\frac{4}{11}\right)^{4/3}\mu_\text{CMB} \approx 0.681 \mu_\text{CMB} $$

Starlight
: The starlight (any radiation by massive bodies) is negligible

$$ \frac{\mu_\text{starlight}}{\mu_\text{CMB}} \approx 0.1 $$

In total we only include CMB and neutrino background into the radiation density which is found to be:

$$ 
\Omega_{r,0} = \frac{\mu_\text{CMB,0} + \mu_{v,0}}{\mu_c} \approx 9 \times 10^{-5}
$$
