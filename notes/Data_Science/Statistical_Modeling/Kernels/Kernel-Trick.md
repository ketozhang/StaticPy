---
title: Kernel Trick
---

To explain the kernel trick we will look at the example of the polynomial design function $\Phi(x)$.

Let's define the polynomial kernel function as

$$
k(x, z) = (x^\top z + 1)^p
$$

Note that the kernel function is also the dot product of the design function,

$$
k(x, z) = \Phi(x)^\top  \Phi(z)
$$

The computation for the first kernel function is much faster than the dot product at the second. This is the key to the performance boost in the kernel trick.