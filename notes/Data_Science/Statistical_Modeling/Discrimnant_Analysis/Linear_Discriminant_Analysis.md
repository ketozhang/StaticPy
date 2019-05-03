---
title: Linear Discriminant Analysis
---

## Gaussian

Assuming all class have the same variance $\sigma^2$, the Bayes decision boundary for two classes $(A,B)$ goes as,

$$
\hat y(x) = \begin{cases}
A, & \frac{\mu_A - \mu_B}{\sigma^2}x - \frac{|\mu_A|^2 - |\mu_B|^2}{2\sigma^2} + \log(\pi_A) - \log(\pi_B) > 0\\
B & \text{otherwise}
\end{cases}
$$

The posterior probability for any class follows the logistic function.