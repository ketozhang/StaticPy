---
title: Planet Formation
menus: astrophysics
---

# Planet Formation
1. [Planet Formation](#planet-formation)
2. [Star Formation](#star-formation)
3. [Protoplanetary Disk](#protoplanetary-disk)
    1. [Infall Stage](#infall-stage)
    2. [Disk Dynamical Evolution](#disk-dynamical-evolution)
    3. [Chemical Evolution](#chemical-evolution)
        1. [Equilibrium Concentration](#equilibrium-concentration)
    4. [Clearing Stage](#clearing-stage)
4. [Solid Bodies Formation](#solid-bodies-formation)
    1. [Planetesimal Formation](#planetesimal-formation)
    2. [Planetesimals Growth](#planetesimals-growth)
    3. [Planetesimal to Planets](#planetesimal-to-planets)

# Star Formation
Star formation will covered [here](star-formation)

# Protoplanetary Disk
The protoplanetary disk forms from the interstellar medium that are leftovers of the star formation. There are three stages of the disk.

1. Infall Stage
2. Disk Dynamical and Chemical Evolution
3. Clearing Stage

## Infall Stage
The first stage, **infall stage**, occurs when molecular cloud core collapse on its own weight (gravitational inward force overpowers all) forming a protostar.

* This stage will occur until all cloud materials are consumed or an external force stops it (i.e., stellar winds). Overall the timescale for this stage is the **free-fall time**.

$$
t_\text{ff} = \left(\frac{3\pi}{32 G\rho} \right)^{1/2}
$$

* Denser area collapse first therefore the collapse is inside out
* Low angular momentum particles would be part of the protostar and it stars spinning.
* High angular momentum particles will not reach the center due to centrifugal force. This forms a disk for the planets to form.
* The kinetic energy of the molecular cloud is distributed into gravitational energy and thermal energy (by the virial theorem). The thermal energy quickly dissipates through radiative cooling.  
The amount of energy per unit mass is given by,

$$
\begin{aligned}
    E_k = E_T =  \frac{GM_\star m}{2d}\\
\end{aligned}
$$

$v_c$ - circular velocity  
$d$ - orbital distance

## Disk Dynamical Evolution
A significant amount of the material fails to reach the protostar thus end up at the disk.
* Angular moment and mass are transported in this stage
    * **Magnetic Torque**:   
        If ionic material are present, angular momentum will disperse to the outer rings due to magnetic field lines. 
        * This effect is called **corotation**:  
          Materials orbiting more rapidly than the star's spin period loses angular momentum thus transferred to slower orbiting portions (outwards since inwards is hotter and faster)
    * **Gravitational Torques**  
      Spiral density waves may form distribute mass until stability limiting the disk mass $M_\text{disk} \le M_\star$. If the protoplanet are large enough, they may excite the density waves at resonant locations to transfer angular momentum outwards.
    * **Viscous Torques**  
      Angular momentum transfer outward due to faster moving molecules at the inner disk colliding with slower moving outer disk.

## Chemical Evolution
Chemical evolution (mainly molecular) is crucial to determining what materials are available for planetesimals to form. 

### Equilibrium Concentration
As the gas in the disk starts to cool, molecules begin to form abundantly between 1200-1300 K (heavier molecule mainly liquid or gas) and below 200 K (lighter molecule mainly gas)

## Clearing Stage
Later on the gas of the protoplanetary disk must be cleared (evident since there very little gas between planets). The two cause is theorize to be:

* UV radiation from nearby stars
* Unstable highly active protostar

# Solid Bodies Formation

## Planetesimal Formation
Small sized solid body, **planetesimals**, are formed from the cooled grains.

* Small solid grains slowly sediment (disperse) out towards the mid-plane of the disk due to the vertical gravitational component of the star.
* mm to cm size grains form at areas further from the mid-plane due to the drop of sedimentation
* cm to km are not well known
* km sized planetesimals grow due to orbiting faster (at Keplerian speed) than the gas (slower because there is a pressure gradient) feeling a drag force.
    * In Keplerian orbit if an object's velocity decreases it would spiral inwards
    * Planetesimals would accrete further by collecting mass as it travels.

## Planetesimals Growth
The planetesimal will grow (accrete) as it accumulate dust

* Planetesimal will be gravitationally bound if the rebound velocity $v_\text{rb}$ with other object is less than the escape velocity $v_\text{rb}<v_e$. The rebound velocity depends on the **collision velocity** ($v_i$) and the **coefficient of restitution** ($\epsilon$),  

$$ 
\begin{aligned}
    v_\text{rb} &= \epsilon v_i\\
    v_i &= \sqrt{v_\infty^2 + v_e^2}\\
    v_e &= \sqrt{\frac{2G(m_1+m_2)}{R_1+R_2}}
\end{aligned}
$$

$v_\infty$ - the velocity where the two masses do not gravitationally effect each other.

* Accretion rate for the planetesimal is comparable to its collision rate given as a mass rate,

$$ 
\begin{aligned}
    \frac{\rm{d} M}{\rm{d} t} &= \rho_s v \pi R^2 \mathcal{F}_g\\
    \mathcal{F}_g &= \left(\frac{b_\text{max}}{a_\text{per}}\right)^2 = 1 + \left(\frac{v_e}{v_\infty}\right)^2
\end{aligned}
$$

$v$ - average relatively velocity between the large (may be called a **planet embryo**) and small planetesimal  
$\rho_s$ - mass density of small body  
$\mathcal{F}_g$ - gravitational enhancement factor  
$b_\text{max}$ - impact parameter (a distance) just when the two bodies are about to hit.  
$a_\text{per}$ - periapse distance

* Gravitational enhancement factor determines the rate of growth such that:  
  $\dot M \propto R^2: v>v_e$  
  $\dot M \propto R^4: v\ll v_e$

* If the planetesimal is much larger than any other planetesimal around it; it may undergo a **runaway growth** where:
    * $\dot M\propto M^{4/3}m^{-2/3}$: If velocity dispersion is governed by planetesimal mass $m$.
    * $\dot M \propto M^{2/3}$: If the massive planetesimal dominate the stirring.

## Planetesimal to Planets
Once the large planetesimal (planet embryo) accumulate enough mass such that there are not much surrounding planetesimals to vary its velocity.

* The timescale for a planet formation is $t\approx 10^8$ such that 2-5 planets are fully formed.