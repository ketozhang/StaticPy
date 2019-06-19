---
title: Non-Degenerate Perturbation Theory
---

Given a easily solvable solution to the Schrodinger equation denoted as,

$$ H^0 \psi_n^0 = E_n^0 \psi_n^0$$

* $H^0$ : simple solvable Hamiltonian
* $\psi_n^0$ : general solution to the simple Hamiltonian assuming there are $n$ solutions.
* $E_n^0$ : general energy eigenvalue to the simple Hamiltonian assuming there are $n$ energy eigenvalues.

We would like to perturb the Hamiltonian very slightly transforming the Hamiltonian into,

$$ H = H^0 + \lambda H' \tag{Perturbed Hamiltonian} $$

* $H'$ : perturbation that contributes to the Hamiltonian
* $\lambda$ : strength of the perturbation, it's arbitrary and assume to be very small.

**Perturbation theory** states that the solution to the perturbed hamiltonian is in the form of a geometric series,

$$ 
\begin{align}
    \psi_n &= \psi_n^0 + \lambda\psi_n^1 + ...\lambda^k\psi_n^j\\
    E_n &= E_n^0 + \lambda E_n^1 + ... \lambda^k E_n^j
\end{align} 
$$

* $\psi_n^j$ : the $j$-th order correction to the eigenfunction
* $E_n^j$ : the $j$-th order correction to the eigenvalue
* $\lambda_n^k$ : The $k$-th power

While it is a confusing notation, $j$-th **index does not mean power** only $k$-th does.

We may now rewrite the TISE for the perturbed hamiltonian. This simplifies to,

$$ \begin{align}
    \boxed{
    H^0\psi_n^0 + \lambda(H^0\psi_n^1+H'\psi_n^0) + \lambda^2(H^0\psi_n^2 + H'\psi_n^1) + ... \\
    = E_n^0\psi_n^0 + \lambda(E_n^0\psi_n^1 + E_n^1\psi_n^0) + \lambda^2(E_n^0\psi_n^2 + E_n^1\psi_n^1 + E_n^2\psi_n^0 )}
    \label{eq: perturbed-tise}
\end{align}$$

## First Order Perturbation
For very small perturbations where $\lambda \ll 1$ we may approximate first order by considering terms in the Equation \eqref{eq: perturbed-tise} with $\lambda^1$,

$$
\begin{align}
    \boxed{H^0\psi_n^1+H'\psi_n^0 = E_n^0\psi_n^1 + E_n^1\psi_n^0}
    \label{eq: first-order}
\end{align}
$$

The first order correction to the eigenvalue and eigenfunction are the following,

$$
\begin{align}
     \boxed{E_n^1 = \langle H' \rangle }
     \label{eq: first-order-eigenvalue}
\end{align}
$$

$$
\begin{equation}
    \boxed{\psi_n^1 = \sum_{m \neq n}{\frac{\langle \psi_m^0 |H'|\psi_n^0\rangle}{E^0_n - E_m^0} \psi_m^0}} 
    \label{eq: first-order-eigenfunction}
\end{equation}
$$

Equation \eqref{eq: first-order-eigenfunction} is valid only if the system is non-degenerate hence the name of the theory.

### Correction to Eigenvalue

We wish to find $E_n^1$ by applying $\langle \psi_n^0 |$,

$$ 
\begin{align}
    \langle \psi^0_n| H^0\psi_n^1 \rangle+ \langle \psi^0_n | H'\psi_n^0 \rangle &= E_n^0\langle \psi^0_n  |\psi_n^1 \rangle + E_n^1\langle \psi^0_n  |\psi_n^0\rangle\\
    E_n^0 \langle \psi_n^0 | \psi_n^1 \rangle + \langle \psi^0_n | H'\psi_n^0 \rangle &= E_n^0\langle \psi^0_n  |\psi_n^1 \rangle + E_n^1  \\
\end{align}
$$

$$ E_n^1 = \langle \psi_n^0 | H' | \psi_n^0 \rangle $$

We find that the first order correction of the eigenvalue $E_n^1$ is the expectation value of $H'$ for the unperturbed eigenfunction $\psi_n^0$,

$$
\begin{align}
     \boxed{E_n^1 = \langle H' \rangle }
     \tag{1st Order Eigenfunction Correction}
\end{align}
$$

### Correction to Eigenfunction

We wish to find the first order correction to the wavefunction $\psi_n^1$. To do so let's rewrite Equation \eqref{eq: first-order} as an inhomogeneous differential equation,

$$
\begin{align}
    (H^0 - E^0_n)\psi_n^1 = -(H'-E_n^1)\psi_n^0
    \label{eq: first-order-2}
\end{align}
$$

Recall that the $\psi_n^1$ is a wavefunction that can definitely be built by a linear combination of the complete set of the unperturbed wavefunctions $\psi_n^0$. We will use the subscript $m$ to preventing you from assuming $n=m$,

$$ \psi_n^1 = \sum_{m}{c_m^{(n)}\psi_m^0} $$

The solution to finding $\psi_n^1$ is to find what each weight $c_m^{(n)}$ corresponds to,

Let's plug this back into Equation \eqref{eq: first-order-2},

$$
\begin{equation}
    (H^0 - E^0_n)\sum_{m}{c_m^{(n)}\psi_m^0} = -(H'-E_n^1)\psi_n^0
\end{equation}
$$

Notice that the term in the sum where $n=m$ goes to zero since $(H^0 - E_n^0)\psi_n^0 = 0$ so we can ignore the term $m=n$. Also notice that we do know the eigenvalue for every application of the hamiltonian on $\psi_m^0$ to be $E_m^0$.,

$$
\begin{equation}
    \sum_{m\neq n}{c_m^{(n)}(E_m^0 - E^0_n)\psi_m^0} = -(H'-E_n^1)\psi_n^0
\end{equation}
$$

You're able to isolate $c_m^{(n)}$ if we were to apply $\langle \psi_l^0 |$ where $l\neq n$, and notice that $\langle \psi_l^0 | \psi_m^0\rangle$ only exist if $m=l$

$$
\begin{align*}
    \sum_{m\neq n}{c_m^{(n)}(E_m^0 - E^0_n)\langle \psi_l^0 |\psi_m^0}\rangle &= -\langle \psi_m^0 |(H'-E_n^1)|\psi_n^0\rangle\\
    c_l^{(n)}(E_l^0 - E^0_n) &= -\langle \psi_l^0 |H'|\psi_n^0\rangle\\
\end{align*}
$$

$$c_l^{(n)} = \frac{\langle \psi_l^0 |H'|\psi_n^0\rangle}{E^0_n - E_l^0}$$

Let's switch the index $l$ back to $m$ since we won't be needing anymore confusion,

$$
\begin{equation}
    c_m^{(n)} = \frac{\langle \psi_m^0 |H'|\psi_n^0\rangle}{E^0_n - E_m^0}
    \label{eq: weight}
\end{equation}
$$

Thus the first order correction to the eigenfunction $\psi_n^1$ is ,

$$
\begin{equation}
    \boxed{\psi_n^1 = \sum_{m \neq m}{\frac{\langle \psi_m^0 |H'|\psi_n^0\rangle}{E^0_n - E_m^0} \psi_m^0}}
    \tag{1st Order Eigenfunction Correction}
\end{equation}
$$

## Second Order Perturbation
Similar to first order, we will only consider terms with $\lambda^2$ in the Equation \eqref{eq: perturbed-tise},

$$ 
\begin{align}
    \boxed{H^0\psi_n^2 + H'\psi_n^1 = E_n^0\psi_n^2 + E_n^1\psi_n^1 + E_n^2\psi_n^0}
\end{align} 
$$

### Correction to Eigenvalue
### Correction to Eigenfunction

