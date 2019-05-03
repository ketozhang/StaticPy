---
title: Vanishing Gradient Problem
---

The vanishing gradient problem is an effect of unit saturation. This occurs when most of the training outputs of the activation function $\hat y$ is close to region of zero gradient.

For instance if $\hat y$ is the sigmoid function, then unit saturation occurs when $\hat y$ is close to 0 or 1.

Being in zero curvature region causes gradient descent to get stuck since the step size becomes too small. Hence appropriately named the **vanishing gradient problem**.

## Solutions

Solutions for mitigating this effect includes:

1. Initialization: Set weights of edges to random with,

    $$
    \begin{gather}
    \mu = 0\\
    \sigma = \frac{1}{\sqrt{n}}
    \end{gather}
    $$
2. Set the target output values to values with high curvature.
3. Change the gradient by some amount such that the parameter are no longer moving towards steepest descent.
4. Use different loss function like cross-entropy.
5. Use a different activation function. A famous replacement for sigmoid is the rectified linear unit (ReLU).