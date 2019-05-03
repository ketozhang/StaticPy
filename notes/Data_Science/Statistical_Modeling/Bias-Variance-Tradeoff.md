---
title: Bias Variance Tradeoff
---

Bias
: Error due in the hypothesis or model to fit the data.

Varaince
: Error due to fitting random noise in the data.

## Bias Variance Decomposition

$$
y = y^* + \epsilon
$$

$$
\begin{align*}
    E\big[ L(y, \hat y) \big] &= E\big[ (y - \hat y)^2 \big]\\
    &= \left(E\big[ \hat y \big]  - y^*\right)^2 + \text{Var}\big[ \hat y  \big] + \text{Var}\big[ y \big]
\end{align*}
$$

* Bias
* Variance
* Irreducible Error