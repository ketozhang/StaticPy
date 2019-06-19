---
title: "Probability of an Energy State"
date: 2017-12-05T15:39:52-08:00
draft: true
---
# Probability of an Energy State
Often times the energy of the system becomes very useful to characterize the state of the system (basis for Quantum physics). 

## Boltzmann Factor
The boltzmann factor is the un-normalized probability (aka weight) of a the energy state of a system next to a very large resevoir.

$$\frac{P(\varepsilon_1)}{P(\varepsilon_2)} = \frac{e^{-\varepsilon_1/\tau}}{e^{-\varepsilon_2/\tau}} $$

This makes more sense if we consider normalization function as $Z$

$$P(\varepsilon) = \frac{e^{-\varepsilon/\tau}}{Z}$$
$$P(\varepsilon) \propto e^{-\varepsilon/\tau}$$

* The boltzman factor is the RHS of the second line above.
* To determine the probability of whether a system is in a energy state given all energy states requires the partition function. 

## Partition Function

The **partition function** is the normalization function of the [boltzmann factor](boltzmann-factor).

$$\boxed{Z(\tau, \varepsilon)) \equiv \sum_s{e^{-\varepsilon_s/\tau}}}$$

The subscript $s$ may be confusing and is used to account for degenerate states for instance $\varepsilon_{1/2} = \varepsilon_{-1/2}$ (if spin is considered a state). We will implore the use of the multiplicity function $g(\varepsilon)$ to account for multiplicity and remove $\varepsilon_s$ in favor of $\varepsilon$

$$\boxed{Z(\tau, \varepsilon)) \equiv \sum_\varepsilon{g(\varepsilon)e^{-\varepsilon/\tau}}}$$

## Usage
### Thermal Average Energy
Because we have the probability of an energy state we can get the average energy state.

$$
\begin{gathered}
    \langle{U}\rangle \equiv \sum_s{\varepsilon_s P(\epsilon_s)}\\
    \boxed{\langle{U}\rangle = \frac{\sum \varepsilon_s e^{-\varepsilon_s/\tau}}{Z} = \tau^2 \frac{\partial}{\partial \tau}\left[\log Z\right]}
\end{gathered}
$$

# Probability of Energy and Number State

Now let's consider the system able to transfer particles between another system. We would like to know the probability of finding the system in some energy and number state $P(N,\varepsilon)$

## Gibbs Factor

Like the Boltzmann factor we need to determine how such system is weighted. The system of energy and number state is weighted as,

$$
\begin{gathered}
    P(N,\varepsilon) = \frac{\exp \left(\frac{N\mu - \varepsilon}{\tau}\right)}{Z} \\
    P(N,\varepsilon) \propto \exp \left(\frac{N\mu - \varepsilon}{\tau}\right)
\end{gathered}
$$

$Z$ : Normalization function later to be known as the **Gibbs sum**

Let's write this with a much simpler subsitution 

$$\boxed{\lambda = \exp{(\mu/\tau)}} $$

which is called the **absolute activity**

$$\boxed{P(N,\varepsilon) \propto \lambda^Ne^{-\varepsilon/\tau}}$$

## Gibbs Sum
*Alias: Grand sum*

The Gibbs sum is the normalization function consider all possible energy states and all possible number states.

$$
\begin{gathered}
    Z(\mu,\tau) \equiv \sum_N^\infty{\sum_s{\lambda^Ne^{-\varepsilon_s/\tau}}}\\
    \boxed{Z(\mu,\tau) \equiv \sum_\text{ASN}{\lambda^Ne^{-\varepsilon_s/\tau}}}
\end{gathered}
$$

Like the partition function we may use the multiplicity function to better account for degeneracy.

$$
Z(\tau, \mu) \equiv \sum_{\{N,\;\varepsilon\}}g(\varepsilon)\lambda^Ne^{-\varepsilon/\tau}
$$

## Usage
### Average Number of Particles
Like for the Boltzmann factor $Z(\tau, \varepsilon))$ we have the thermal average energy, the Gibbs sum $Z(\tau, \varepsilon), N)$ we have the average number of particles,

$$ 
\begin{gathered}
    \langle N \rangle = \frac{\sum\limits_\text{ASN}{N\lambda^Ne^{-\varepsilon/\tau}}}{Z(\tau, \varepsilon),N)}\\
    \boxed{\langle N \rangle = \tau \frac{\partial}{\partial \mu} [\log{Z(\tau, \varepsilon),N)}]}\\
    \boxed{\langle N \rangle = \lambda \frac{\partial}{\partial \lambda} [\log{Z(\tau, \varepsilon),N)}]}
\end{gathered}
$$