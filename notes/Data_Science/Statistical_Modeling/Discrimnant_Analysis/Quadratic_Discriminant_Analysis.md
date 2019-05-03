---
title: Quadratic Discriminant Analysis
---



## Gaussian

Let the multivariate gaussian be,

$$
P(x \mid \mu, \sigma) = \left(2 \pi \sigma^2 \right)^{d/2} \exp\left(-\frac{|x-\mu|^2}{2\sigma^2}\right)
$$

Let the $N$ classes be represented as $c \in \{1,2,\ldots,N\}​$ such that each class has the following statistics:

* $\mu_c$ : Mean of the class
* $\sigma_c$ : Standard deviation of the class
* $\pi_c$ : Prior of the class

The optimization problem can be simplified using logarithm to preserve maximization of the Bayes decision,

$$
\begin{align*}
    \hat y(x) &= \mathop{\arg\max}_c \log\left( (2\pi)^{d/2} P(x \mid \mu, \sigma) \pi_c \right) \\
    &= \mathop{\arg\max}_c \frac{|x-\mu_c|^2}{2\sigma_c^2} - d\log{\sigma_c} + \log{\pi_c}
\end{align*}
$$

## General Quadratic Function

For some quadratic function $Q(x)$, the Bayes decision rule is given by,

$$
\hat y(x) = \mathop{\arg\max}_c Q_c(x)
$$

The Bayes decision rule for the quadratic discriminant always product a posterior distribution that is a **logistic function**. We can easily see this by considering only two classes $(A,B)$.

$$
\hat y(x) = \begin{cases}
A & Q_A(x) - Q_B(x) > 0 \\
B & \text{otherwise}
\end{cases}
$$

$$
\begin{align*}
    P(Y \mid X) &= \frac{e^{Q_A(x)}}{e^{Q_A(x)} + e^{Q_B(x)}}\\
    &= \frac{1}{1 + e^{Q_A(x) - Q_B(x)}}
\end{align*}
$$