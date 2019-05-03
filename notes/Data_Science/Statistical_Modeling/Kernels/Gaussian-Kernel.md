---
title: Gaussian Kernel
---

The **gaussian kernel** or the **radial basis function kernel** is,

$$
k(x,z) = \exp\left(-\frac{|x-z|^2}{2\sigma^2}\right)
$$

This kernel is used for the design transformation 

$$
\Phi(x) = \exp\left(-\frac{x^2}{2\sigma^2}\right)\left[1, \frac{x}{\sigma \sqrt{1!}}, \frac{x^2}{\sigma^2 \sqrt{2!}} \ldots\right]^\top
$$

This design transformation is an infinite series which is impossible to calculate thus motivating the kernel form.

Some intutition for the gaussian kernel

* Always differentiable
* Behave somewhat like k-nearest neighbor but smoother
* Oscillate less than polynomial kernel
* Can be interpreted as similarity measure which votes how on similar a point $z$ is to a point $x$.
* Sample points vote for the value at $z$ weighted by closeness to the kernel center.