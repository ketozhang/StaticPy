---
title: "Landau Theory of Phase Transitions"
date: 2017-12-05T15:39:52-08:00
draft: true
---

# Landau Theory of Phase Transitions

The Landau theory gives a systemic formulation of the mean field theory of phase transition applicable to various systems. The basis is to consider a system at constant volume and temperature such that the free energy $F = U - \tau\sigma$  is minimum at equilibrium.

We consider a parameter that causes the the free energy to minimum $\xi_0$. This parameter is the quantity relating to the properties of the system.

$$
\begin{aligned}
    F_L(\xi,\tau) \equiv U(\xi,\tau) - \tau\sigma(\xi,\tau)\\
    F_L(\xi_0,\tau)  = F_{L,\text{min}}, \quad \tau = \text{const.}
\end{aligned}
$$

We assume a great approximation that $F_L(\xi,\tau)$ can be a even power series:

$$\boxed{F_L(\xi,\tau) = g_0(\tau) + \frac{1}{2}g_2(\tau)\xi^2 + ... }$$

* $g_i(\tau)$ : Power series coefficients
* Phase transition occurs if $g_2$ flips its sign at some $\tau_0$ and $g_4>0$.

**Case**: $g_2(\tau)=(\tau-\tau_0)\alpha$ and $g_4 = \text{const}$

Consider only the terms up to $g_4$:

$$ F_L(\xi,\tau) = g_0(\tau) + \frac{1}{2}\alpha(\tau-\tau_0)\xi^2 + \frac{1}{4}g_4\xi^4 $$
$$ \left(\frac{dF_L}{d\xi}\right)_\tau = \alpha(\tau-\tau_0)\xi + \frac{1}{4}g_4\xi^3 = 0$$

The second line has the roots $\xi_1 = 0$ corresponding to $F_{L,min}(\tau>\tau_0)$ and $\xi_2^2 = (\tau_0 - \tau)(\alpha/g_4)$ corresponding to $F_{L,min}(\tau < \tau_0)$

$$
\begin{aligned}
    F(\xi_1) &= g_0(\tau)\\
    F(\xi_2) &= g_0(\tau) - \frac{\alpha^2}{4g_4}(\tau-\tau_0)^2 
\end{aligned}
$$