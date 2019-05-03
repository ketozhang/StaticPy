---
title: Lecture Notes14
---
# Lecture Note 14

* Notation for optimizing the loss function $\ell(\theta)$ is,

$$ \min_\theta{\ell(\theta)} $$

## Gradient Descent

If $\theta$ is a vector (if you loss function has multiple parameters) then we must use the gradient to optimize rather than the derivative of a single coordinate.

$$ \nabla \ell(\boldsymbol\theta) =  \frac{\partial \ell}{\partial \theta_1} + \frac{\partial \ell}{\partial \theta_2} + \ldots \frac{\partial \ell}{\partial \theta_n}$$

In numerical analysis, the **gradient descent** method is:

1. Take the gradient at some point along your curve $\ell(\theta)$. This point is denoted as $\theta^{(0)}$
2. The new point is taken to be the current point $\theta^{(0)}$ minus a constant factor of $\nabla \ell(\theta^{(t)})$

$$\boxed{ \theta^{(t+1)} = \theta^{(t)} - \alpha\nabla \ell(\theta^{(t)}) }$$

Another way of writing this is by the order of approximation notation. I will write this for a general mutlivariable function $f(\mathbf x)$. We say that the $n$-th order approximation for the vector $\mathbf x$ that minimizes $f(\mathbf x)$ is $\mathbf x^{(n)}$ where,

$$\boxed{ \mathbf x^{(n)} =  \mathbf x^{(0)} - a_1 \nabla f(\mathbf x^{(0)}) - a_2 \nabla f(\mathbf x^{(1)}) - \ldots - a_n\nabla f(\mathbf x^{(n-1)})}$$

* $x^{0}$ : Initial guess minimum
* $a_1 \ldots a_n$ : A constant positive optimization parameter that you choose to say how sensitive should the next order approximation be. Often times $a_1 = \ldots a_n$ and this works well numerically sufficiently small value.