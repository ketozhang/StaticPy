---
title: Non-linear Classificaton
---

## Parabolic Transformations

This section is for kernel that follow parabolic functions (i.e., shapes that are conic or in general quadric).

### Ellipsoid and Hyperboloid

The polynomial draws a ellipsoid or hyperboloid plane in $\mathbb R^d$.

If the principle axis of the plane are aligned with the coorindate axis then the polynomial is without the cross-terms where $\Phi: \mathbb R^d \rightarrow \mathbb R^{2d}$,

$$
\Phi(X_i) = \begin{bmatrix}
    X_i^{2}\\
    X_i
\end{bmatrix}
$$

If the planes aren't axis-aligned then ($\Phi : \mathbb R^d \rightarrow \mathbb R^\frac{d^2 + 3d}{2}$),

$$
\Phi(X_i) = \begin{bmatrix}
    X_i^{2}\\
    X_iX_{j\neq i}\\
    X_i
\end{bmatrix}
$$
