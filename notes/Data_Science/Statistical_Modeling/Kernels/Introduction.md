---
title: Introduction
---

Kernels are used like mathematical magic that is able to fit complicated curve with a collection simple functions called a kernel.

The motivation comes from the observation that many learning algorithms:

* have weights that can be written as a linear combination of sample points.
    $$
    \theta =  X^\top a
    $$
* have the property that inner products of the design matrix $\Phi(X)$ can be written without computing $\Phi(X)$ directly.

The change is that instead of solving for the parameters $\theta$, it is now substituted with $a$ (the linear combination coefficients) which is called the **dual parameters**.

The **kernel function** is defined as the calculation involving the in-sample vector $X_i$ and out of sample vector $z$

$$
k(X_i, z)
$$

The kernel matrix is defined as all possible kernel functions for the feature matrix

$$
K = XX^\top; \qquad K_{ij} = k(X_i,X_j)
$$