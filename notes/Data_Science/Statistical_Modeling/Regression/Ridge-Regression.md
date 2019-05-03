---
title: Ridge Regression
---

The ridge regression is regression with the $L_2$ regularization,
$$
\mathcal{L} = \sum_{i=1}^n L(y,\hat y) + \lambda|\theta|^2
$$

* $\theta$ : The parameter vector with the bias parameter as zero instead of one $\begin{bmatrix} 0 & \theta_1 & \ldots & \theta_d\end{bmatrix}$ to prevent penalizing the bias term.



For simplicity, here one out we will ignore the bias term.

There are very strong properties of ridge regression that makes this regularization favorable:

1. Guarantees a unique solution because $\mathcal L(\theta)$ is always convex even if $L(\theta)$ is not (for least-square it is).
2. Reduces overfitting by penalizing large parameters.



## Positive Definite Normal Equation

The addition of the $L_2$ regularization guarantees that $\mathcal L(\theta)$ is convex simply because the  matrices in the normal equation are guaranteed to be positive definite.



Let's take for example the least-squares loss,
$$
\mathcal L(\theta) = \sum_{i=1}^n{|y - X\theta|^2  +\lambda|\theta|^2}
$$
The normal equation is given by,
$$
\begin{gather}
(X^\top X + \lambda I)\theta = X^\top y\\
\theta^* = \frac{2|y-X\theta^*|^2}{\lambda} X^\top \left({X\theta^* - y}\right)
\end{gather}
$$

## Relationship to MAP

The addition of the $L_2$ regularization is equivalent of turning an MLE problem to an MAP problem (i.e., by adding a prior).



Once again we use the least-squares loss as an example. The least-squares loss is the log-likelihood function for the Gaussian likelihood. We simply attempt to write the log-posterior problem with this likelihood,
$$
\begin{align}
\theta^* &= \mathop{\arg\min}_\theta \sum_{i=1}^n|y + X\theta|^2 - \lambda |\theta|^2\\
\theta^* &= \mathop{\arg\max}_\theta \left[-\sum_{i=1}^n|y - X\theta|^2 - \lambda |\theta|^2\right]
\end{align}
$$
Thus the prior $P(\theta) \propto \lambda |\theta|^2$.