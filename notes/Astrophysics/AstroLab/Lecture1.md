---
title: Lecture 1
---

## Lab 1

* RR Lyrae (measure distance with luminosity variations)

## Magnitudes & Extinction

The relationship between apparent magnitude and absolute magnitude.

$$
m_\lambda = M_\lambda + 5\log_{10}(d) - 5
$$

If the source goes through some material such as a dust cloud, extinction would happen which may reduce its magnitude and redden the spectra.

$$
m_\lambda = M_\lambda + 5\log_{10}(d) - 5 + A_\lambda
$$

The extinction affects the radiation modeled by an exponential decay.

$$
F_\lambda = F_{\lambda,0} e^{-\tau_\lambda}
$$

$$
\tau_\lambda = \int n\sigma_\lambda\ \mathrm{d}s
$$

* $\tau$ : optical depth
* $n$ : number density
* $\sigma_\lambda$ : wavelength-dependent particle size

We solve for $A_\lambda$ by the difference of the apparent magnitudes (initial then extincted),

$$
\Delta m = -2.5 \log_{10}\left(\frac{F_\lambda}{F_{\lambda,0}}\right) \approx 1.086\tau_\lambda
$$

$$
A_\lambda \equiv \Delta m
$$

The **color excess** or **selective extinction** is the amount of color change (traditionally reddening) due to the extinction which are given by,

$$
E(B-V) = (B-V) - (B-V)_0
$$

The total extinciton is then the extinciton measured in the V-band ($A_V$). This is a normalization value for $R_V$,

$$
R_V = \frac{A_V}{E(B-V)}
$$

## RR Lyrae

RR Lyrae is a variable cepheid that are hydrogen-burning low-mass dying stars.

It is observed that the luminosity and period are positively proportioned $L \approx P$.

$$
\langle{M_V}\rangle = a\log P + b
$$