---
title: Schmidt Decomposition
---


## Schmidt Decomposition by Density Matrix
The Schmidt decomposition can be seen as a form of the state $\ket{\psi}$ such that density operator of that state is a diagonal matrix. Consider the bipartite state,

$$ \ket{\psi}_{AB} = \sum_{i,\mu}a_{i\mu}\ket{i\mu}$$

Let's work with the density operator $\rho_A$ such that,

$$ \rho_A \equiv \sum_{i,j,\mu}{a_{i\mu}a_{j\mu}^*\ket{i}\bra{j}}  $$

Note that $ \rho_B $ is not necessarily already diagonal but can be diagonalized. Consider the diagonalized matrix of $\rho_A$ to be $\rho_A'$ with eigenvalues $p_i \in \set{p_1,p_2,\ldots,p_n}$ corresponding to the eigenvectors $\ket{i'}$

$$\boxed{ \ket{\psi}_{AB} = \sum_{i}\sqrt{p_i}\ket{i}\otimes\ket{i'} }$$