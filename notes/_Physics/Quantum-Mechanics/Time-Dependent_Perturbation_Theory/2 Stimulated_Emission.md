---
title: Stimulated Emission
---

## Coherent Electromagnetic Waves

The interaction of an electron with a photon can be described by the atomic interaction with an electromagnetic wave.

Consider the simple case that we shine a light polarized light source along the $z$ direction such that the wavelength is greater than the atomic size $\lambda \gg \lambda_{dB}$. We can them simplify this electromagnetic wave as,

$$ \begin{gather}
    \boldsymbol{E} = E_0\cos(\omega t)\hat z\\
    V = \int{\boldsymbol{E}\; d\boldsymbol{r}} = -qE_0z\cos(\omega t)
\end{gather} $$

The perturbed Hamiltonian is then,

$$
\begin{gather}
    H' = -qE_0 z \cos(\omega t)\\
    H'_{ba} = -qE_0\cos(\omega t)z_{ab}\\
    z_{ab} \equiv \bra{\psi_a}z\ket{\psi_b}
\end{gather}
$$

Notice that $z_{ab}$ is always integrate to zero since $z|\psi|^2$ is always odd. Of course, this only applies to wavefunctions that can be considered even or odd with $z$. 

The probability of transition between $a$ to $b$ for the case that $\omega \gg \omega_0$ (true for our light source) is,

$$ \begin{gather}
    P_{a\rightarrow b}(t) = \left(\frac{qE_0}{\hbar}|z_{ab}|\right)^2\frac{\sin^2\left(\frac{\Delta \omega t}{2}\right)}{\Delta \omega^2}\\
    \Delta \omega \equiv \omega - \omega_0
\end{gather} $$

Now for an astonishing fact, the probability going the other way $P_{b\rightarrow a}(t)$ is the exact same! Notice all you need to do is flip the sign of $\omega_0$ to get the opposite transition.

$$ \begin{equation}
    \boxed{P_{a\rightarrow b}(t) = P_{b\rightarrow a}(t)}
\end{equation} $$

If $E_a < E_b$ then $a \rightarrow b$ is called **absorption** and $b\rightarrow a$ is called **stimulated emission**. This is amazing because you wouldn't expect $\psi_b$ to go to a lower energy level if an electromagnetic is contributed. Naturally you may have heard of an atom emitting light without any perturbation. This is called instead **spontaneous emission**.

## Incoherent Electromagnetic Waves
The incoherent perturbation is best described by its energy density $\mu$ which is composed of all frequencies. Recall that the energy density of the electromagnetic wave is,

$$ \mu = \frac{\epsilon_0}{2}E_0^2 $$

* $E_0$ : electrical field amplitude

We may rewrite the monochromic stimualted emission as

$$
\begin{equation}
    P_{b\rightarrow a}(t) = \frac{2q\mu}{\epsilon_0 \hbar^2}\abs{z_{ba}}^2\frac{\sin^2\left(\frac{\Delta \omega t}{2}\right)}{\Delta \omega^2}
\end{equation}
$$

To consider the full range of frequency we integrate over $\omega$. Recall,

$$ d\mu = \rho(\omega)\; d\omega $$

$$\begin{equation}
\boxed{P_{b\rightarrow a}(t) = \frac{2q}{\epsilon_0 \hbar^2}\abs{z_{ba}}^2\int_{-\infty}^{\infty}{\rho(\omega)\frac{\sin^2\left(\frac{(\Delta \omega) t}{2}\right)}{(\Delta \omega)^2}\; d\omega}}
\end{equation}$$

We may assume that energy density dominates at resonant frequency $\omega = \omega_0$ so $\rho(\omega) = \rho(\omega_0)$. Substituting $x \equiv (\Delta \omega)t/2$ we can extend the integral to $x=\pm\infty$ and find that,

$$\begin{equation}
    \boxed{P_{b\rightarrow a}(t) \simeq \frac{\pi q \abs{z_{ba}}^2}{\epsilon_0\hbar^2} \rho(\omega_0)t}
\end{equation}$$

## Isotropic Electromagnetic Waves
Let's now introduced unpolarized light, actually light coming from every direction isotropically. The equation no long has the electromagnetic wave coming from the $\hat z$ direction but now everywhere $\abs{z_{ba}} \rightarrow \abs{r_{ba}}$.

The isotropic light will be polarized along $\hat n$ thus we project $\abs{r_{ba}}$ to $\hat n$ and take the average value as the factor of the effective electric field.,

$$ \abs{r_{ba} \cdot \hat n}^2 = \int{\frac{1}{4\pi} \cos^2\theta\sin\theta \; d\theta\; d\phi} = \frac{1}{3}\abs{r_{ba}}^2 $$

$$\begin{equation}
    \boxed{P_{b\rightarrow a}(t) \simeq \frac{\pi q \abs{r_{ba}}^2}{3\epsilon_0\hbar^2} \rho(\omega_0)t}
\end{equation}$$

## Transition Rate
The transition rate has a good approximation considering statistically large numbers of photons (attempts to transition). In this approximation the transition rate is the rate of success,

$$
\begin{equation}
R_{b\rightarrow a} \equiv \frac{dP_{b\rightarrow a}}{dt}
\end{equation}
$$

## Fermi's Golden Rule
The most simplest way to memorize all of these is **Fermi's golden rule**. The rule states that the transitional probability given the energy density of state $\rho$ given by such integral,

$$ R_{i \rightarrow f} = \frac{2\rho}{\hbar}\abs{H'_{fi}}^2\int_{-\infty}^{\infty} \frac{\sin \omega t}{\omega} \d \omega$$

This is simply equal to,

$$\boxed{ R_{i \rightarrow f}  = \frac{2\pi}{\hbar}\abs{H_{fi}}^2\rho}$$