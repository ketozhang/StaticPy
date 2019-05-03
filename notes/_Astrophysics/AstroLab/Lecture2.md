---
title: Lecture 2
---

## Likelihood Function

Assuming a gaussian error distribution for the data,

$$
P(D \mid \theta) = \prod_{i=1}^n{\frac{1}{\sqrt{2\pi\sigma_i^2}}\exp\left(\frac{-(y_i - \hat y_i)^2}{2\sigma_i^2}\right)}
$$

## Markov Chain Monte Carlo (MCMC)

A method to sample the posterior $P(\theta | D)$.

### MCMC Hasting
1. Begin with starting point $\theta_0$
2. Propose $\theta_{t+1}$ based on sampling a random proposal distribution $J(\theta_{t+1} \mid \theta_t)$.
3. Keep it with a probability proportional to if it improves the posterior ratio else try again:

    $$\frac{P(\theta_{t+1} | D)}{P(\theta_{t} | D)}$$

### Affine Invariant MCMC

Adding multiple samplers (aka **walkers**) we group each walk as a pairs. The next step step for a walker is towards its partner's line of sight. A new partner is assigned at every step.

## Goodness of Fit

* Geweke Score:

    Take the end and begining of the chain and computer the score as,
    $$
    \frac{\bar \theta_e - \bar \theta_b}{\sqrt{\text{Var}[\theta_e]\text{Var}[\theta_b]}}
    $$
* G-R Statistics
* Acceptance Fraction
* Autocorrelation Function
    * Typicall have burn-in period 5 times larger than the ACF convergence number.

## Periodogram

A periodogram can be produced by a fourier transform of some time-series data:

$$
\hat y(f) \equiv \int_{-\infty}^{\infty}y(t)e^{-i2\pi ft}~\mathrm d t
$$

When plotting a periodogram, we often plot the power spectrum over frequency,

$$
\mathcal P(f) \equiv |\hat y(f)|^2
$$

Pratically, an unbounded infinite signal is not possible thus we apply whats called fast fourier transform,

$$
\hat y(f) = \sum_{n=1}^N y(n\Delta t)e^{-i2\pi fn\Delta t}
$$

* $\Delta t$ : Sampling interval.

In irregular sampling interval you get the **Lomb-Scargle Periodogram**. To model data with a single frequency,

$$
\hat y = y_0 + A_f \sin\left(2\pi f\left[t - \phi_f\right]\right)
$$