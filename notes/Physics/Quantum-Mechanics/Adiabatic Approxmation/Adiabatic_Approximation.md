---
title: Adiabatic Approximation
---

The adiabatic approximation considers a time dependent Hamiltonian $H(t)$ that preserves the **adibataic theorem**

Adiabatic Theorem
: If the initial Hamiltonian $H^{i}$ the system is in the $n$th eigenstate $\psi^{i}_n$ then later on at some time $t>0$ the Hamiltonian becomes $H^{f}$ such that the **eigenstate is still** on the $n$th but of the current Hamiltonian $\psi^{f}_n$.

    While the adabatic process does not require a small perturbation what is required is a **slow change** in the time-dependent Hamiltonian $H(t)$

Given a system that abides the adiabatic theorem thus the adiabatic approximation, the total wavefunction is,

$$
    \boxed{\Psi(t) = \sum_n{c_n(0)\psi_n(t)}e^{i\left[ \theta_n(t) + \gamma_n(t) \right]}}\\
    \boxed{\gamma_n(t) \equiv i\int_0^t{\braket{\psi_n(t')}{\dot\psi_n(t')}\d t'}}\\
$$

* $\theta_n(t)$ is called the **dynamic phase**
* $\gamma_n(t)$ is called the **geometric phase**

Proof
: For a time-dependent Hamiltonian $H(t)$, the eigenfunction and eigenvalue changes with time

    $$H(t)\psi_n(t) = E_n(t)\psi_n(t)$$
 
    In general the total wavefunction $\Psi(t)$ is a linear combination of each eigenstate however this time the $E_n(t)$ is no longer constant over time,

    $$
    \boxed{\Psi(t) = \sum_n{c_n(t)\psi_n(t)e^{i\theta_n(t)}}}\\
    \boxed{\theta_n(t) \equiv -\frac{1}{\hbar}\int_0^t{E_n(t')\d t}}
    $$

    Plugging $\Psi(t)$ into the TDSE and applying $\bra{\psi_m}$ gives,

    $$
    \dot c_m(t) = -\sum_n{c_n\braket{\psi_m}{\dot \psi_n}}e^{\theta_n - \theta_m}
    $$

    Differentiating the TISE you would find that

    $$
    \braket{\psi_m}{\dot\psi_n} = \frac{\bra{\psi_m}\dot H\ket{\psi_n}}{E_n - E_m}
    $$

    Plugging this into $\dot c_m(t)$ gives,

    $$
    \boxed{\dot c_m(t) = - c_m\braket{\psi_m}{\dot \psi_m} - \sum_{n\ne m}c_n \frac{\bra{\psi_m}\dot H\ket{\psi_n}}{E_n - E_m}\exp\left[\frac{-i}{\hbar}\int_0^t{E_n(t') - E_m(t')\d t'}\right]}
    $$

    This is the exact solution to the Time Dependent Hamiltonian problem (not an estimate like the TD Perturbation Theory).

    Now let's apply the adibatic approximation. $\dot H$ is very small because the Hamiltonian changes slowly thus the whole second term droped in $\dot c_m(t)$

    $$ 
        \dot c_m(t) = - c_m\braket{\psi_m}{\dot \psi_m}
    $$

    The solution to this differential equation is of course,

    $$
    \boxed{c_m(t) = c_m(0)e^{i\gamma_m(t)}}\\
    \boxed{\gamma_m(t) \equiv i\int_0^t{\braket{\psi_m(t')}{\dot\psi_m(t')}\d t'}}\\
    \boxed{\Psi_n(t) = \psi_n(t)e^{i\left[ \theta_n(t) + \gamma_n(t) \right]}}
    $$

    * Please note that the dot notation is a partial time derivative $\dot \psi_m(t) = \partial \psi_m / \partial t$

## Berry's Phase

Previously we've seen the time dependent Hamiltonian that changes over time has the geometric phase:

$$ \gamma_n(t) \equiv i\int_0^t{\braket{\psi_n(t')}{\dot\psi_n(t')}\d t'} $$

Now let's consider some parameter that changes over time which changes the Hamiltonian (like the size of the width in the infinite square well). Let's denote this parameter as $R(t)$ therefore the Hamiltonian is $H(R(t))$. We can write the geometric phase as an integrate along $R$,

$$
\frac{\partial \psi}{\partial t} = \frac{\partial \psi_n}{\partial R}\frac{dR}{dt}\\
\gamma_n(R) = i\int_{R_i}^{R_f}{\braket{\psi_n(R)}{\psi_n'(R)}\d R}
$$

This is as expected and not very interesting since if $R_f=  R_i$, the integral goes to zero $\gamma_n=0$

Now consider multiple parameters such that $\mathbf{R} = \mathbf{R_1} + \mathbf{R_2} + \dots \mathbf{R_N}$ then,

$$
\boxed{\gamma_n(R) = i\int_{\mathbf R_i}^{\mathbf R_f}{\braket{\psi_n}{\nabla_{\mathbf R}\psi_n}\d \mathbf R}}
$$

Say after some time $T$ the Hamiltonian return to it's original form therefore travel around the closed loop around $\mathbf R$,

$$ 
\boxed{\gamma_n(T) = i \oint{\braket{\psi_n}{\nabla_{\mathbf R}\psi_n}\d \mathbf R}}
$$

From Stoke's theorem we may write this as a surface integral,

$$ 
\boxed{\gamma_n(T) = i \int{\nabla_{\mathbf R} \times \braket{\psi_n}{\nabla_{\mathbf R}\psi_n}\d \mathbf a}}
$$

### Aharonov-Bohm Effect

Consider an electron splitting dodging the solenoid magnetic field. Let's center the coordinate system at the solenoid such that,

$$ 
\mathbf B(r) = \begin{cases}
    B_0 \hat z & r < a\\
    0 & r > a
\end{cases}
$$

The Aharonov-Bohm effect states there a geometric phase will occur to the wavefunction ofthe electron even if the electron does not travel through a nonzero magnetic field. The vector potential of the magnetic field is given by,

$$ 
\mathbf B = \nabla \times \mathbf A \\
\mathbf A = \frac{\Phi}{2\pi r}\hat\phi \qquad (r>a)
$$

Clearly at regions where the magnetic field is zero ($r > a$ in this experiment), $\nabla \times \mathbf A = 0$. However this **does not mean** $\mathbf A = 0$. The TDSE is given as,

$$ \left[ \frac{1}{2m}\left(\frac{h}{i}\nabla - q\mathbf A \right)^2 + V \right]\Psi = i\hbar \frac{\partial \Psi}{\partial t}  $$

This has the solutions,

$$ 
\Psi = e^{ig}\Psi'\\
g(\mathbf r) \equiv \frac{q}{\hbar}\int_{\mathcal{O}}^{\mathbf r}{\mathbf A(\mathbf r')\cdot \d \mathbf r'} = \pm \frac{q\Phi}{2\hbar}
$$