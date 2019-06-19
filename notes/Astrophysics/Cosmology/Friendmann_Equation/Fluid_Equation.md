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

## Equation of State
To solve for the fluid equation we need to know $P(\mu)$ which is called the **equation of state**.

### Linear Case
A very famous example of an equation of state is the ideal gas law

$$ P = \frac{N}{V}\tau = w\mu  $$

This will be the one we will use for the simple universe.

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

#### Properties
* This gives the useful proportional relations,

    $$
    \mu_m \propto a^{-3}\\
    \mu_r \propto a^{-4}\\
    \mu_\Lambda = \mu_{\Lambda,0}
    $$
* Notice that the dominating energy density is determined by the size of the universe. For a large universe $a \rightarrow \infty$, the energy with the smallest $w$ survives (cosmological constant).