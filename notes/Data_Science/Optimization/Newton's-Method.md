---
title: Newton's Method
---

The Newton's method is an optimization method requiring the curvature of the interested optimization problem $L(\theta)$.

Starting at an initial step $\theta(t=0)$:

1. Approximate a quadratic function at the current step.
2. Jump to the unique critical point.
3. Repeat 1-2 until satisfied.

## Taylor Expansion

The quadratic function comes from the second term of the Taylor series,

$$
\nabla L(\theta) = \nabla L(\theta)\big\rvert_{\theta(t)} + \mathcal H (L(\theta))\big\rvert_{\theta(t)}\Delta \theta + \mathcal O(|\Delta \theta |^2)
$$

Where $\mathcal H$ is the Hessian operator.

The critical point lies where $\nabla L(\theta) = 0$ so we can solve for $\Delta\theta$,

$$
\Delta \theta = -\left[H(L(\theta))\big\rvert_{\theta(t)}\right]^{-1}\nabla L(\theta)\big\rvert_{\theta(t)}
$$