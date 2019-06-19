---
title: Hilbert Space
---

Axiom 1
: A state is a ray in the Hilbert space. A ray is a general case of a vector that need not to have an origin and need not to be represented by basis vectors.

Axiom 2
: An observable is a self-adjoint Hermitian operator on the Hilbert space.

    * Recall that an operator is defined as a thing that linearly transforming some state $\ket{\psi}$ where linear here means:

        $$ A(a\ket{\psi} + b\ket{\varphi}) = aA\ket{\psi} + bA\ket{\varphi}$$

    * Self-adjoint means that the operator acted upon a braket can be either done by first acting on the bra or firt acting on the ket,

        $$ \bra{\varphi}A\ket{\psi} = A\bra{\varphi}\ket{\psi}$$

    Property: Real Eigenvalues
    : Recall that if,

        $$ A\ket{\psi} = a\ket{\psi} $$

        then we are sure that $a$ is real and $\ket{\psi}$ is a vector that can from the complete basis of the Hilbert space.

    Property: Spectral Representatoin
    : Given $N$ eigenstates denoted by the ket vector $\ket{n}$, we may write the operator as a linear combination of each $n$th eigenstate's projection vector. This is called the **spectral representation** of the operator.

        The projection vector is defined as,

        $$ P_n \equiv \ket{n}\bra{n} $$

        We form the spectral representation,

        $$ A = \sum_{n}^N{a_nP_n} $$

Axiom 3: Unitarity (Dynamics)
: A unitary operator is where its hermitian conjugate equals its inverse,

    $$ \begin{align}
        U^\dagger \equiv (U^*)^T \\
        \boxed{U^{\dagger} = U^{-1}} \tag{Unitary}
    \end{align}$$

    The time evolution is unitary and described by a self adjoin operator called the Hamiltonian. Recall the Schrodinger Equation,

    $$ \frac{\d}{\d t}\ket{\Psi} = -iH\ket{\Psi} \tag{$\hbar = 1$}$$

    For instance we can represent an infinitesimal time step as,

    $$ \ket{\Psi(t + \d t)} = \ket{\Psi(t)} - iH\ket{\Psi(t)} \d t = (1 - iH\d t)\ket{\Psi(t)}$$

    In general this is,

    $$
    \ket{\psi(t)} = U(t-t_0)\ket{\Psi(t_0)} \\
    U(t-t_0) = \exp\left[-i\int{H\d t}\right]
    $$

    The unitary operator preserve orthonomality $\bra{\varphi}\ket{\psi}$ given that the same unitary operator applies to both states (interpret as if the Hamiltonian and time elapsed is the same for the two states),

    $$ \bra{u\varphi}\ket{u\psi} = \bra{\varphi}\ket{\psi} $$