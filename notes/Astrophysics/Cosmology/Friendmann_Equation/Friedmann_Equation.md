---
title: Friedmann Equation
---

<!-- TOC -->

- [Hubble's Constant](#hubbles-constant)
- [Non-Relativistic Form](#non-relativistic-form)
    - [Proof](#proof)
- [Density Parameter Form](#density-parameter-form)
- [Fluid Equation](#fluid-equation)
    - [Proof - Newtonian](#proof---newtonian)
- [Acceleration Equation](#acceleration-equation)
- [Equation of State](#equation-of-state)
- [Cosmological Constant - Incorrect Version](#cosmological-constant---incorrect-version)
- [Cosmological Constant - Vacuum Energy](#cosmological-constant---vacuum-energy)

<!-- /TOC -->

The Friedmann equation applies the Friedmann metric,

$$ ds^2 = -dt^2 + a(t)^2\left[dr^2 + S_k(r)^2d\Omega^2\right] $$

to Einstein's field equation,

$$ G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} $$

The resultant is an equation that describes how the Hubble parameter varies over time $H^2(t)$. You may interpret this as how the universe expands over time. The Friedmann equation is an implicit function of time more explicitly it depends on the energy density $\rho$ of the universe. 

Often times, we use the definition of the Hubble's parameter,

$$ H(t) \equiv \frac{\dot a}{a} $$

Mass Density Form
: 

$$
\begin{equation}
    \left(\frac{\dot a}{a}\right)^2 = -\frac{4\pi G}{3}\left(\rho + \frac{3\rho}{c^2}\right) + \frac{\Lambda c^2}{3}
\end{equation}
$$

Energy Density Form
: 
$$
\begin{equation}
    \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3c^2}\mu - \frac{\kappa c^2}{R_0^2a^2}
\end{equation}
$$

Natural Unit Form
: 
$$
\begin{equation}
    \boxed{\left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\mu - \frac{k}{a^2}}
\end{equation}
$$

* $\mu$ : Energy density of the universe
* $k$ : Curvature constant where $k\equiv \kappa/R_0^2$

We will be using the natural unit form since it's natural. 

## Hubble's Constant
Immediately one can infer the Hubble's constant from the Friedmann equation setting $t = t_0$ which is today.

$$
\begin{gather}
    \left(\frac{\dot a_0}{a_0}\right)^2 = H_0^2\\
    H_0^2 = \frac{8\pi G}{3}\mu_0 - \frac{k}{a^2}
\end{gather}
$$

## Non-Relativistic Form
The Friedmann equation can be thought of as an expanding finite sphere of mass density $\rho(t)$

$$
\begin{equation}
    \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\rho(t) + \frac{2C}{r_s^2}\frac{1}{a(t)^2}
\end{equation}
$$

* $C$ : Constant that affects the expansion rate
* $r_s$ co-moving radius

### Proof


## Density Parameter Form

$$
\begin{equation}
    \left(\frac{\dot a }{a}\right)^2 = H_0^2 \left[\frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^4} + \Omega_{\Lambda,0} + \frac{1-\Omega_0}{a^2}\right]
\end{equation}
$$


## Fluid Equation
The fluid equation is the equation of motion for the energy density $\rho$ as a function of time. It is given by an adiabatic expansion of the universe.,

$$
\begin{gather}
    \boxed{\dot\mu + 3\frac{\dot a}{a}(\mu + P) = 0}\\
    \dot\mu = -3\frac{\dot a}{a}(\mu + P)\\
    \boxed{\dot \mu \frac{a}{\dot a} = -3(\mu + P)}
\end{gather}
$$

### Proof - Newtonian
You may prove exactly, the fluid equation for the adiabatic expansion of a sphere with total internal energy $E = V(t)\mu(t)$ where $V(t)$ is,

$$
\boxed{V(t) = \frac{4\pi}{3}r_s^3a(t)^3}
$$

## Acceleration Equation
Knowing the Friedmann equation and fluid equation we can take the derivative to get,

$$
\begin{equation}
    \boxed{\frac{\ddot a}{a} = -\frac{4\pi G}{3c^2}\left(\mu + 3P\right)}
\end{equation}
$$

The condition of acceleration is to make $\mu + 3P < 0$ so $P < -\frac{1}{3}\mu$. Unfortunately we do not know how $P$ relates to $\mu$ which both share the same units.


## Equation of State
We assume that pressure $P$ and energy density $\mu$ are linearly proportional such that,

$$ \begin{equation}
    P = w\mu\\
    w = \begin{cases}
        0 & \text{matter}\\
        1/3 & \text{radiation}\\
        -1 & \text{dark energy}
    \end{cases}
\end{equation} $$

* $w$ : A constant relating to the type of energy. Notice that from the acceleration equation, the universe accelerates for $w < -1/3$ so it motivates that the unknown energy (dark energy) is negative. Why we use exactly $w = -1$ for dark energy is explained in the [cosmological constant](#cosmological_constant)

For a universe of several energy components, $\mu$ is a weighted sum of those energies,

$$
P = \sum_i w_i\mu_i
$$

Now let's apply each type of energy density to the fluid equation:

$$ 
\begin{gather*}
    \dot \mu_i + 3 \frac{\dot a}{a}\left(\mu_i + P_i\right) = 0\\
    \frac{d\mu_i}{\mu_i} = -3(1+w_i)\frac{da}{a}\\
\end{gather*} 
$$

$$
\begin{equation}
    \boxed{\mu_i(a) = \mu_{i,0}a^{-3(1+w_i)}}
\end{equation}
$$

This gives the useful proportional relations,

$$
\mu_m \propto a^{-3}\\
\mu_r \propto a^{-4}\\
\mu_\Lambda = \mu_{\Lambda,0}
$$

## Cosmological Constant - Incorrect Version
The cosmological constant $\Lambda$ started out as a correction to Einstein's field equation for a universe full of matter and radiation. In Einstein's years, scientist did not believe that the universe was either expanding or contracting thus conclude that a universe of matter and radiation must be a stable universe. Unfortunately, Einstein equation does not agree so Einstein added the cosmological constant such that the Friedmann equation changes to:

$$
\begin{equation}
    \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\mu - \frac{k}{a^2} + \frac{\lambda}{3}
\end{equation}
$$

The acceleration equation is then,

$$
\begin{equation}
    \frac{\ddot a}{a} = -\frac{4\pi G}{3}\left(\mu + 3P \right) + \frac{\Lambda}{3}
\end{equation}
$$

Notice that at a stable universe where $\ddot a(t) = 0$, when $P = 0\cdot\mu + \frac{1}{3}\mu$ and

$$
\begin{equation}
    \boxed{\Lambda \equiv 4\pi G \mu}\\
    \boxed{\mu_\Lambda \equiv \frac{1}{8\pi G}\Lambda}
\end{equation}
$$

* $\mu_\Lambda$ : Cosmological constant component of energy density (note: $\mu \ne \mu_\Lambda$), independent of time.

Let's plug in $\Lambda$ into the Friedmann equation for a static universe $\dot a = 0$ and $a = 1$,

$$
\begin{gather}
    \frac{2\Lambda}{3} - \frac{k}{a^2} + \frac{\Lambda}{3}\\
    \boxed{k = \Lambda}
\end{gather}
$$

Since $\Lambda > 0$, this indicates that the curvature $k > 0$ therefore a open but static universe. This sounds incorrect and it is; in the next section we will explore the more acceptable use of the cosmological constant. 

Motivation on the Incorrectness
: 
Consider even a slight increase in $\Lambda$ then $\dot a > 0$ which causes $\mu_m \rightarrow 0$ and by the Friedmann equation this feedbacks to $\dot a \rightarrow 0$ even more. We got a non-linear expanding universe

## Cosmological Constant - Vacuum Energy
The most accepted "correct" way to interpret the cosmological constant is as vacuum energy. Yes, vacuum has energy which many may first have been introduced as the Heinsenberg uncertainty principle,

$$ \begin{equation}
    \Delta E \Delta t \le h
\end{equation} $$