--- 
title: Degenerate Perturbation Theory
---

For the perturbed Hamiltonian $H = H^0 + H'$. If the eigenstates of $H^0$ are degenerate then there is a case where non-degenerate perturbation theory does not apply.

Recall the definition of degenerate states which the eigenstate and its linear combination both share the same eigenvalue $E^0$.

$$ H^0\psi^0_n = E^0\psi_n^0 $$
$$ H^0\sum_n{c_n\psi_n^0} = E^0\sum_n{c_n\psi_n^0} $$

## Two-Fold Degenerate State

![**Figure: ** As the strength of the perturbation increases, the more the eigenvalue diverges corresponding to $\psi_a$ and $\psi_b$ originally degenerate wavefunction.](https://i.gyazo.com/633cd15b571e86168a702aa6ff8dbb70.png)

We begin first with $2$-fold degeneracy and later expand onto $N$-fold. In this $2$-fold degeneracy there exist two degenerate wavefunctions $\psi_a$ and $\psi_b$ which shares the eigenvalue $E^0 \equiv E_a^0 = E_b^0$

We claimed that there exist a case where non-degenerate perturbation theory does not apply. Let's first look at the non-applicable case which is of course called the degenerate perturbation theory.

In the degenerate perturbation theory we have an issue that we do not know whether if the first order correction is either:

$$
\begin{gather}
    \langle H' \rangle_{aa} \quad\text{or}\quad \langle H' \rangle_{bb}\\
\end{gather}
$$ 

* $H'_{aa}$, $H'_{bb}$ : Where $H'_{ij} \equiv \langle{\psi_i|H'|\psi_j}\rangle$

### Proof

Let's first deal with two degenerate states $\psi_a^0$ and $\psi_b^0$ with energy $E^0$. We wish to make corrections to the eigenvalue $E$ and eigenfunction $\psi$ where,

$$\begin{align}
    \psi^0 = \alpha\psi_a^0 + \beta\psi_b^0 \label{eq: wavefunction}
\end{align}$$
$$H^0\psi^0 = E^0$$

Such that the perturbed TISE is the same as before,

$$ \begin{gather*}
    (H^0+H')\psi = E\psi
\end{gather*} $$

$$\begin{align*}
    E \equiv E^0 + \lambda E^1 + ...,\qquad \psi \equiv \psi^0 + \lambda \psi^1 + ...
\end{align*}$$

### First Order Corrections

The first order equation is,

$$ H^0\psi^1 + H'\psi^0 = E^0\psi^1 + E^1 \psi^0 $$

We will first correct the eigenvalue $E^1$ by applying $\langle \psi^0_a |$

$$ \langle \psi^0_a |H^0\psi^1 \rangle + \langle \psi^0_a |H'\psi^0\rangle = E^0\langle \psi^0_a |\psi^1\rangle + E^1 \langle \psi^0_a |\psi^0\rangle $$

This simplifies noticing that the first term on each side cancels out $E^0\langle \psi^0_a |\psi^1\rangle$ and we may also introduce Equation \eqref{eq: wavefunction},

$$\alpha\langle \psi^0_a |H'\psi_a^0\rangle + \beta\langle \psi^0_a |H'\psi_b^0\rangle = \alpha E^1$$

To simplify, we'll change notation,

$$ \langle H' \rangle_{ij} \equiv  \langle \psi^0_i |H'\psi_j^0\rangle $$

$$ \begin{equation}
    \boxed{\alpha \langle H' \rangle _{aa} + \beta \langle H' \rangle_{ab} = \alpha E^1}
    \label{eq: e1}
\end{equation} $$

Equation \eqref{eq: e1} is an interesting equation because it is a linear combination we'll soon appreciate. What is really important is that if $\avg{H'}_{ab}=0$ then we get the nondegenerate perturbation theory.

1. Take the inner product with $\psi_b^0$ to get another linear combination

$$ \begin{equation}
\boxed{\alpha \langle H' \rangle _{ba} + \beta \langle H' \rangle_{bb} = \beta E^1}
\label{eq: e2}
\end{equation} $$

2. Multiply by $\langle H'\rangle_{ab}$

3. <mark> Eliminate $\beta W_{ab}$ </mark> 

$$ \alpha \left[\langle H'\rangle_{ab}\langle H'\rangle_{ba} - (E^1 - \langle H'\rangle_{aa})(E^1-\langle H'\rangle_{bb})\right] = 0$$

Given that $\alpha \neq 0$[^alpha], this is a quadratic equation,

[^alpha]: When $\alpha = 0$ that means the unperturbed wavefunction is $\psi_b$.

$$ E^1_\pm = \frac{1}{2}\left[\langle H'\rangle_{aa} + \langle H'\rangle_{bb} \pm \sqrt{\left(\langle H'\rangle_{aa} - \langle H'\rangle_{bb}\right)^2 + 4 |\langle H'\rangle_{ab}|^2} \right] $$

What's interesting is when $\langle H' \rangle_{ab} = 0$ then,

$$ E^1_+ =  \langle H' \rangle_{aa}, \qquad E^1_- = \langle H' \rangle_{bb}$$

This is the same result as the nondegenerate perturbation theory. The next subsection will show the cases where $\avg{H'}_{ab}=0$.

#### Theorem - Nondegenerate and Degenerate Equivalence

Degenerate perturbation theory equates to the same corrections as nondegenerate perturbation theory if an operator $A$ such that it commutes with both $H^0$ and $H'$ and also satisfies the following condition,

If, 
$$\begin{align*}
    [A, H^0] &= [A, H'] = 0\\
    A\psi_a^0 &= \lambda_a\psi_a^0\\
    A\psi_b^0 &= \lambda_b\psi_b^0\\
    \lambda_a &\neq \lambda_b
\end{align*} $$

then nondegenerate applies to degenerate case or in other words,

$$ \langle H' \rangle_{ab} = 0$$

## N-Fold Degeneracy

The generalization of $N$-fold degeneracy is to use an $N\times N$ matrix. Let's write Equation \eqref{eq: e1} and Equation \eqref{eq: e2} aligned,

$$\begin{align*}
    \alpha \langle H' \rangle _{aa} + \beta \langle H' \rangle_{ab} &= \alpha E^1\\
    \alpha \langle H' \rangle _{ba} + \beta \langle H' \rangle_{bb} &= \beta E^1
\end{align*}$$

$$ \begin{pmatrix}
    \langle H' \rangle _{aa} & \langle H' \rangle _{ab}\\
    \langle H' \rangle _{ba} & \langle H' \rangle _{bb}
\end{pmatrix} 
\begin{pmatrix}
    \alpha \\ \beta
\end{pmatrix} = E^1 \begin{pmatrix}
    \alpha \\ \beta
\end{pmatrix}
$$

### Example
> TODO: Provide 1 matrix example one for degenerate and one non-degenerate theory.

