---
title: Gaussian Discrimnant Analysis
---

## Multivariate Gaussian

Recall the multivariate gaussian can be represented as in terms of a quadratic function quadratic function $q(x)$ which is called the **quadratic form**,

$$
\begin{gather*}
P(x) = (2 \pi \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2} Q(v)\right]\\
Q(x) = v^\top\Sigma^{-1} v
\end{gather*}
$$

* $v​$ : Deviation vector $X_i-\mu​$
* $X_i​$ : A row of data
* $\mu$ : A vector with each entry as the mean of the feature column.

The quadratic form $q(x)$ describes the shape of the isocontours $q(x) = c$ (for some real scalar $c$). For the Gaussian, the shape is a $\dim(v)$ ellipsoid due to the mapping of a semi-circle function to parabolic function specified by,

$$
|v| \longrightarrow \left\lvert\Sigma^{-1/2} v\right\rvert
$$

### Quadratic Discrimnant Analysis

For each class in $c : \{1,2,3,\ldots,C\}$ there exists a **sample covariance matrix** $\hat\Sigma$,

$$
\hat \Sigma_c = \frac{1}{n_c}\sum_{y_i=c} (X_i - \hat \mu_c)(X_i - \hat \mu_c)^\top
$$

The Bayes optimal rule maximizes $P$ or rather $\log P$ over the class $c$ as its parameter. An equivalent description is to maximize the logistic function,

$$
\hat y = \mathop{\arg\max}_c \bigg[Q_c(x) - Q_d(x)\bigg]
$$

### Linear Discrimnant Analysis

Every class has the same sample covariance matrix which is calculated by the mean of each class's covariance matrix. This is called the **pooled within-class covariance matrix**,

$$
\hat\Sigma = \frac{1}{n}\sum_c\sum_{y_i = c} (X_i - \hat\mu_c)(X_i - \hat\mu_c)^\top
$$

The Bayes optimal rule is equivalently a linear function,

$$
\hat y = \mathop{\arg\max}_c \bigg[(\mu_c-\mu_d)^\top \Sigma^{-1} x - + \log \frac{\pi_c}{\pi_d}\bigg]
$$

## Transformations

* Decorrelating: $XU$
* Sphering: $X\hat\Sigma^{-1/2}​$
* Whitening: Decorrelating + Sphering



## Relations to Principal Component Analysis

$$
P(x) = (2 \pi \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2} v^\top\Sigma^{-1} v\right]~; \qquad v := x-\mu\\
$$

$$
\begin{align*}
q(v) &= v^\top \Sigma^{-1} v \\
&= \underbrace{v^\top Q}_{u^\top} \Lambda^{-1}\underbrace{Q^\top v}_u\\
&= u^\top \Lambda^{-1} u\\
&= \sum_{j=1}^{d} \lambda^{-1} u_j^2\\
&= \sum_{j=1}^{d} \frac{1}{\sigma^2} u_j^2
\end{align*}
$$

$$
\det \Sigma = \prod_{j=1}^d \lambda_j = \prod_{j=1}^d \sigma_j^2 \nonumber
$$

$$
\begin{align*}
P(x) &= \left(2 \pi \prod \sigma_j^2 \right)^{-1/2}\exp\left[-\frac{1}{2} \sum_{j=1}^{d} \frac{1}{\sigma^2} u_j^2\right]\\
&= \prod_{j=1}^d (2\pi \sigma_j^2)^{-1/2}\exp\left[-\frac{u_j^2}{2\sigma^2_j}\right]
\end{align*}\\
u = Q^\top(x-\mu)
$$

