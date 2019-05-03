---
title: Kernel Ridge Regression
---

Take some cenetered data $X, y$ such that we can confidently write the normal equation for ridge regression as:

$$
(X^\top X + \lambda I) \theta = X^\top y
$$

Now to write $\theta$ in terms of the linear combination of $X$,

$$
\begin{gather*}
\theta = \frac{1}{\lambda}(X^\top y - X^\top X \theta) = X^\top a\\
a = \frac{1}{\lambda}(y-X\theta)
\end{gather*}
$$

Now to remove the $\theta$ dependency,

$$
a = (XX^\top + \lambda I)^{-1}y
$$

Replacing $\theta$ in the ridge regression loss function,

$$
\mathcal L = |XX^\top a - y|^2 + \lambda |X^\top a|^2
$$

Another property is when solving for a out of sample point $z$,

$$
\hat y(z) = w^\top z = a^\top X z = \sum_{i=1}^n a_i(X_i^\top z)
$$

Here motivates the kernel function,

$$
k(X_i, z) = X_i^\top z
$$

thus also the kernel matrix $K$. Now we can summarize the optimization solution (i.e., the normal equation) and the model

$$
\begin{gather}
(K + \lambda I) a = y\\
\hat y (z) = \sum_{i=1}^n a_i k(X_i,z)
\end{gather}
$$

## Performance

The dual (or kernel) form of ridge regression has the performance:

$$
\mathcal O (n^3 + n^2 d)
$$

compared with the primal form which has the performance:

$\mathcal O(d^3 + d^2 n)$

So whenever $d > n$ , the kernel form is best used. Furthermore any increase in $d$ due to the design transformation is ignored with kernels.