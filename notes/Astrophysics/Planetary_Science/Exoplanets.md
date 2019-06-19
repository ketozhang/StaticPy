---
title: Exoplanets
---

# Observation of Exoplanets
Exoplanets are rarely ever directly observed because they are so far. The two primary difficulties of direct observation are:

* Planets that are much fainter than the host star
* Planets that are much too close to the host star governed by the [Rayleigh Criterion](#rayleigh-criterion)

The following properties of exoplanets are easier to detect:
* More massive planet due to the increase of its host star's wobbling and radial velocity.
* Shorter period planet where its radial velocity varies more.
* Edge on for optimal transit and radial velocity observations.
* Large radius to diminish the bad inclination effects during transit.
* Low density stars (less massive and large radius) to increase wobbling and decrease the inclination effects.

## Pulsar Timing
The first exoplanet to be discovered was discovered by pulsar timing.

First a bit about pulsar. Pulsars are spinning neutron stars that emits radio waves with periodic strength. The period of these waves are very well known and very stable. While stable, any sort of gravitational effect onto the star may cause the superpositions in its waves. This is how the first two exoplanet was found on the same pulsar **PSR 1257+12**

## Doppler Shift and Radial Velocity
With the fundamentals of Kepler's laws and the Doppler shift, planets are found by measuring the star's radial velocity that has an amplitude of $K$. Using this amplitude we may find the planet's mass ($M_p$) with known host star's mass ($M_\star$). The host star's mass ($M_\star$) is guessed with an accuracy of ~10% using the spectral characteristic of the star.

The planet's mass ($M_p$) is then,

$$
\begin{gathered}
    K = \left(\frac{2\pi G}{P}\right)^{\frac{1}{3}}\frac{M_p\sin i}{\left(M_\star + M_p \right)^{2/3}} \frac{1}{\sqrt{1-e^2}}\\
    \frac{1}{\alpha}M_p + M_p^{1/3} = M_\star
\end{gathered}
$$

The second line is a difficult polynomial with a solution of ([Wolfram Alpha](https://www.wolframalpha.com/input/?i=x%2Fa-x%5E(3%2F2)+%3D+y+solve+for+x)).  
However it is much easier to assume $M_\star \gg M_p$

$$M_p = \frac{K{M_\star}^{\frac{2}{3}}\sqrt{1-e^2}}{\sin i}\left(\frac{P}{2\pi G}\right)^{\frac{1}{3}}, \quad M_\star \gg M_p$$

Radial velocity detections are very successful however has two difficult parameters:

* **Eccentricity:** Can be judged from the shape of the radial velocity wave (eccentric orbits has sinusoidal that leans)
* **Inclination:** No information of the radial velocity can be found if the inclination is face-on ($i=90^\circ$). Most of the time inclination are not available giving only a false mass ($M_p\sin i$)

## Wobble Astrometry
While astrometry is a valid method, so far not a single exoplanet has been found using this method. Astrometry of planet detection looks at the wobble of the host star. We know that the star would wobble at an amount of,

$$\Delta \theta \le \frac{M_p}{M_\star}\frac{a}{d}$$
$a$ - semi-major axis between planet and host star  
$d$ - distance away from the Solar System  
$\Delta \theta$ - Radians if $a/d$ are unitless and arcsecs if $a/d$ are in $\rm{pc/AU}$

Note that astrometry is even more accurate than radial velocity because it does not need to worry about inclination therefore the mass measure is the true mass. Once again astrometry fails to discover any so far waiting to be changed in 2020 -- the launch of GAIA space telescope
### Wobble Accuracy - Rayleigh Criterion
**Not the same as the parallax limit**

The Rayleigh criterion sets the limit for how accurate can we measure wobbles (i.e., angles). The angle $\Delta \theta$ one detects must be greater than or equal to,

$$
\begin{aligned}
    \Delta\theta &\ge \Delta\theta_c\\
    \sin(\Delta \theta_c) &= 1.22\frac{\Delta x}{d}\\
    \Delta\theta_c &= 1.22\frac{\Delta x}{d}, \quad \theta_c \ll 1 \text{ rad}
\end{aligned}
$$

$\Delta x$ - the spacial length of the wobble. This is the same amount as $\Delta x = \frac{M_p}{M_\star}a$ ,    
$d$ - distance away from the Solar System

## Transit Photometry
 <div style="text-align:center;height:400px"><img src="Transit-spectroscopy.png"></div>
As a planet transits the host star, a dip in the host star's flux is apparent that looks like a square well. Transits give information about the planet's radius and orbital period. Spectroscopic observations can determine the composition of the planet's atmosphere as well as its albedo indicating existence of cloud.

### Inclination Requirements
The transit method works well if the inclination is quite edge on to line of sight such that

$$\cos i < \frac{R_\star + R_p}{r_\text{min}}$$  

$r_\text{min}$ - distance between the host star and planet when the planet is closest to observer.

The inclination can be measured from the asymmetry of the [Rossiter-McLaughlin Effect](#rossiter-mclaughlin-effect)
### Radius from Transit

* Radius ($R$) - obtained by the dip in the light curve governed by a ratio:
 
$$\frac{\Delta L}{L} = \left(\frac{R_p}{R_\star}\right)^2$$

While not perfect considering any variation of the host star luminosity (e.g., sunspots and limb darkening by the planet)

### Orbital Period from Transit
 May be obtained either by Kepler's equation knowing the mass of the planet and star (via radial velocity measurements) or waiting long enough for the light curve to reach half-period.


 ### Limb Darkening
 One would expect near the edges as the planet crosses the sun. If the planet has an atmosphere, the flux would not be perfectly boxy but curvy. This curvy nature is stronger at shorter wavelength due a greater flux from the Planck function ($\nu \propto E_\gamma \propto F$).

### Occultation - Secondary Eclipse
**Occultation** or **secondary eclipse** occurs when the planet transits behind the star. 

* The secondary eclipse are always square-like and does not have limb darkening since no radiation is penetrating the planet's atmosphere.
* The planet's flux can be measured from the $\Delta F$. If the spectra is measured we can see which wavelength does the planet emit more indicating it composition.
* $\Delta F$ during the secondary eclipse is much less apparent than the primary eclipse since the planet is not as bright as the star

 ### Rossiter-McLaughlin Effect
<div style="text-align:center;height:150px"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Rossiter-McLaughlin_effect.svg/726px-Rossiter-McLaughlin_effect.svg.png"></div>

As the star rotates, the star would emit gas towards the observer (blue-shifted) on side and away from the observer (red-shifted) on the other side. If the planet would to obscure emission, it would seem like the star only emits one side of its gas (either blue-shifted or red-shifted). It's easier to understand if you look at the image above.


 
 ## Gravitational Microlensing
 While very rare, microlensing is a valid way to see planets that are way too far or too small for the other methods to detect. This section will not cover the mechanics but just planet finding. See [Gravitational Lensing](Gravitational_Lensing.md) for more information.

 # Exoplanet Statistics
 ## Star Metallicities
 Because terrestrial planets are made up of majority heavy elements. It makes sense that the greater metalicity a star has, the higher chance the star is to produce a terrestrial planet.

 The star's metallicities does not affect planets with the size greater than or equal to Neptune.