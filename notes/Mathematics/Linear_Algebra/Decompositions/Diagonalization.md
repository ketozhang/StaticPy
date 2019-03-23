---
title: Diagonalization
---

The diagonalization or eigendecomposition transforms decomposes a square matrix,

$$
A = P\Lambda P^{-1}
$$

* $P$ : The eigenmatrix, a orthogonal matrix with columns as the eigenvectors
* $\Lambda$ : Diagonal matrix with diagonals as eigenvalues corresponding to the chosen eigenvectors in $P$.

## Symmetric Matrices
All symmetric matrix $S$ has an eigendecomposition guaranteed to have $\text{Rank} (S)$ real eigenvalues.

$$
S = U \Lambda U^\dagger
$$

* $U$ : Orthonormal unitary eigenmatrix

### Unitary Eigenmatrix

The unitary eigenmatrix $U$ is a rotational matrix rotating all vectors to the basis of its columns (i.e., rotating to its column space).