---
title: Kernel Perceptron
---

Recall the perceptron update rule while there exist an $y_i$ that's misclassified:

$$
\theta(t+1) = \theta(t) + \alpha y_i \Phi(X_i)
$$

The kernel form only deals with a single parameter rather than the whole feature space,

$$
a_i(t+1) = a_i(t) + \epsilon y_i
$$

Notice that

$$
\Phi(X_i)^\top \theta = (\Phi(X)w)_i = (Ka)_i
$$

So,

$$
\hat y(z) = \theta^\top \Phi(z) = a^\top \Phi(X)\Phi(z) = \sum_{i=1}^n a_i k(X_i,z)
$$