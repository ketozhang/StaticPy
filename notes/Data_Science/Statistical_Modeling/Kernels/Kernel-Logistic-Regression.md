---
title: Kernel Logistic Regression
---

Let's take the logistic regression algorithm with gradient descent. The kernel form for the update rule is

$$
a(t + 1) = a(t) + \alpha (y-s(Ka))
$$

The model is then,

$$
\hat y (z) = s\left(\sum_{i=1}^n a_j k(X_j, z)\right)
$$