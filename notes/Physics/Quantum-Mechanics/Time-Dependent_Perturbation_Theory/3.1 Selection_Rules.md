---
title: Selection Rules
---

Recall that every emission rate requires the calculation of the matrix element $\bra{\psi_b}\mathbf{r}\ket{\psi_a}$

The **selection** rule is defined for the Hydrogen wavefunction where certain combinations of $n,l,m$ will result the matrix element to zero. Not only is this convenient for math but it means there are certain transitions that are not allowed.

$$ \bra{n'l'm'}\mathbf{r}\ket{nlm} $$

1. No transition occurs unless $\Delta m = \pm 1$ or $0$
2. No transition occur unless $\Delta l = \pm 1$

Case $\Delta m$ = 0, thus $m = m'$
: The matrix element only survives in $z$

$$ \boxed{\bra{n'l'm'}\mathbf{r}\ket{nlm} = \bra{n'l'm}z\ket{nlm} \hat z}$$

The length square of these matrix element vector is then

$$ \boxed{\bigabs{\bra{n'l'm'}\mathbf{r}\ket{nlm}}^2 = \bigabs{\bra{n'l'm}z\ket{nlm}}^2}$$

Case $\Delta m = \pm 1$ thus $(m'-m)^2 = 1$
: The matrix element only survives in $x$ and $y$ survives such that


$$ \bra{n'l'm\pm 1}\mathbf{r}\ket{nlm} = \bra{n'l'm\pm 1}x\ket{nlm} + \bra{n'l'm \pm 1}y\ket{nlm}\\
\pm \bra{n'l'm\pm 1}x\ket{nlm} = i\bra{n'l'm}y\ket{nlm}\\
\boxed{\bra{n'l'm\pm 1}\mathbf{r}\ket{nlm} = \bra{n'l'm\pm 1}x\ket{nlm}\bigg(\hat x + \mp i \hat y \bigg)}\\
\boxed{\abs{\bra{n'l'm\pm 1}\mathbf{r}\ket{nlm}}^2 = 2\bigabs{\bra{n'l'm\pm 1}x\ket{nlm}}^2}
$$

<!-- TODO: # Proof -->
