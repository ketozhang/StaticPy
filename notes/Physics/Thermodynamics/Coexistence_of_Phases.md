---
title: "Coexistence of Phases"
---

# Coexistence of Phases

Consider a substance in isothermal such that we are able to vary its volume and pressure. We may graph this in a curve called the **isotherm**. 

Let's focus on liquid and gas phase (all of this applies between solid-gas and solid-liquid as well). At a certain isotherm the two liquid and gas phase may coexist if:

* the isotherm lies below a **critical temperature** $\tau_c$ such that
* the two phases are in thermal, diffusive, and pressure equilibrium
    
    $$\tau_l=\tau_g, \quad \mu_l=\mu_g, \quad P_l = P_g$$

* note that the the substance will in a certain phase if that phase's chemical potential is the lowest:
    * Gas: $\mu_g < \mu_l$
    * Liquid: $\mu_l < \mu_g$ and $\mu_l < \mu_s$
    * Solid: $\mu_s < \mu_l$

# Coexistence Curve and Clausius-Claperyon Relation
*Alias: Vapor Pressure Curve, Vapor Pressure Equation*

The coexistence curve is a pressure-temperature curve along which two phases may exist (coexist). For the case of liquid and gas, the coexistence curve has the slope given by the Clausius-Claperyon Relation:

$$\boxed{\frac{dP}{d\tau} = \frac{L}{\tau \Delta \nu}}$$

* $L$ : Latent heat of vaporization
* $\Delta \nu$ : The change in volume if a single particle would change from liquid to gas

## Derivation
The coexistence curve follows the following differential equation:

$$ \frac{dP}{d\tau} = \frac{\frac{\partial \mu_l}{\partial \tau} - \frac{\partial \mu_g}{\partial \tau}}{\frac{\partial \mu_g}{\partial P} - \frac{\partial \mu_l}{\partial P}} $$

We can represent this better using the definition of the differentials of the Gibbs free energy

$$
\begin{gathered}
    \frac{1}{N}\left(\frac{dG}{dP}\right)_{N,\tau} = \left(\frac{d\mu}{dP}\right)_{\tau} = \frac{V}{N} \equiv \nu\\
    \frac{1}{N}\left(\frac{dG}{d\tau}\right)_{N,P} = \left(\frac{d\mu}{d\tau}\right)_{P} = \frac{\sigma}{N} \equiv s\\
    \boxed{\frac{dP}{d\tau} = \frac{s_g-s_l}{\nu_g-\nu_l} = \frac{\Delta s}{\Delta\nu}}
\end{gathered}
$$

While confusing we'll use:

* $\nu$ which relates to the volume per particle. $\Delta\nu$ is the change in volume if we were to transfer one particle from one phase to another
* $s$ the entropy per particle. This changes the differential equation to a state equation. $\Delta s$ is the change in entropy if we were to transfer one particle from one phase to another

 We may use the **[latent heat of vaporization](#latent-heat-of-vaporization)** to simplify the vapor pressure equation.

$$ L \equiv \frac{dQ_{l\rightarrow g}}{N} = \frac{\tau(\sigma_g - \sigma_l)}{N}$$
$$L \equiv \tau(s_g - s_l)$$

Replacing this definition to $dP/d\tau$ above gives the **Clausius-Claperyon equation**,

$$ \boxed{\frac{dP}{d\tau} = \frac{L}{\tau \Delta \nu}} $$

## Clausius-Claperyon of the Ideal Gas 
The Clausius-Claperyon relation has a useful form in the ideal gas such that 

* $\Delta \nu \approx v_g = V_g/N_g$ since gas takes up more volume by many orders $v_g / v_l \approx 10^3$
* Ideal gas law is followed so that $\Delta v \approx V_g/N_g = \tau/P$

The vapor pressure equation them becomes,

$$
\begin{gathered}
    \frac{dP}{d\tau} = \frac{L}{\tau^2}P \\
    \boxed{\frac{d}{d\tau}\log{P} = \frac{L}{\tau^2}}
\end{gathered} 
$$

### Coexistence Curve of the Ideal Gas
If we assume that $L=L_0$ does not depend on temperature then we can easily integrate the Clausius-Claperyon equation to the coexistence curve.

$$ 
\begin{gathered}
    \int{\frac{dP}{P}} = L_0 \int{\frac{1}{\tau^2} d\tau} \\
    \boxed{P(\tau) = P_0e^{-L_0/\tau}}
\end{gathered}
$$

# Latent Heat of Vaporization
The amount of heat transfered a single particle of liquid to gas is called the **latnet heat of vaporization**.

$$L \equiv \frac{dQ}{N}$$