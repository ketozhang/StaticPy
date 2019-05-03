---
title: Gradient Descent
---

Gradient descent is a iteratative optimizer that attempts to minimize the problem with only the information of the gradient. Here we will use it to minimize some loss function over the parameter space given by $\theta$. Recall that this gradient for this is,

$$
\nabla \mathcal{L}(\theta) =  \left(\frac{\partial \mathcal{L}}{\partial \theta_1}, \frac{\partial \mathcal{L}}{\partial \theta_2}, \ldots \frac{\partial \mathcal{L}}{\partial \theta_n} \right)
$$

In numerical analysis, the **gradient descent** method is:

1. Take the gradient at some point along your curve $\mathcal{L}(\theta)$. This point is denoted as $\theta^{(0)}$
2. The new point is taken to be the current point $\theta^{(0)}$ minus a constant factor of $\nabla \mathcal{L}(\theta^{(t)})$

$$\boxed{ \theta^{(t+1)} = \theta^{(t)} - \alpha\nabla \mathcal{L}(\theta^{(t)}) }$$

Another way of writing this is by the order of approximation notation. We say that the $n$-th order approximation for the vector $x$ that minimizes $\mathcal L(x)$ is $x^{(n)}$ where,

$$\boxed{ x^{(n)} =  x^{(0)} - \alpha_1 \nabla \mathcal L(x^{(0)}) - \alpha_2 \nabla \mathcal L(x^{(1)}) - \ldots - \alpha_n\nabla \mathcal L(x^{(n-1)})}$$

* $x^{0}$ : Initial guess minimum
* $\alpha_1 \ldots \alpha_n$ : A constant positive optimization parameter that you choose to say how sensitive should the next order approximation be. Often times $\alpha_1 = \ldots \alpha_n$ and this works well numerically sufficiently small value.

---

* Computation time:
    $$\mathcal O(nd)$$
    * $n$ : Number of training points
    * $d$ : Dimensions of training points

## Stocastic Gradient Descent (SGD)

The **stocastic gradient descent (SGD)** is a class of methods of using only a smaller sample of the training points chosen by a random process.

* Computation cost:

    $$ \mathcal O(n'd) $$

    * $n'$ : Number of sample points. This number is often an order or more magnitudes less than $n$.