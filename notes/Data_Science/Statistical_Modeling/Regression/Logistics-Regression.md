---
title: Logistics Regression
---

The **logistic regression** transforms the linear regression problem with the **logistic** or **sigmoid function** $s(z)$ used for posterior distribution estimation and classification[^1].

[^1]: It's unfortunate that it's called logistics regression, but the fact that logistic regression does estimate a posterior distribution is why it's justifiable.

We will motivate this with a binary problem where $Y: \{0,1\}$ notice that the logistic function transforms the linear regression to the interval $[0,1]$.
$$
\begin{gather}
P(X \mid Y=\hat y) = s(\hat y); \qquad \hat y  = X\theta \\
s(z) = \frac{e^z}{1+e^{z}} = \frac{1}{1+e^{-z}}; \qquad s(z) \in [0,1]
\end{gather}
$$
* $\hat y$ : Model

This is purposely done so that we can interpret the logistic regression as a probability of classification given the data $P(X \mid Y)$. From here on out we will choose to classify if $Y=1$.

A more insight into what we're modeling with $\hat y$ is to notice the following identity
$$
\begin{equation}
\log \left[\frac{P(X \mid Y=1)}{1 - P(X\mid Y=1)}\right] = \hat y
\end{equation}
$$
This identity is called **log-odds** or **logit** hence we're fitting some model to the log ratio of probabilities that $Y=1$ compared to $Y=0$.

The objective function to solve for $\theta$ is chosen to be the maximum likelihood (we will discuss why this is equivalent to minimum loss later). The likelihood function is naturally the binomial distribution. We will disregard the leading coefficient because it will be irrelevant in maximization.  The decision rule will be discussion later in the [Decision Rule](#Decision_Rule) section.
$$
\begin{align*}
\log P(X \mid Y=1) &= \sum_{i: y_i = 1} \log P(X_i \mid Y=1~;~\theta) + \sum_{i : y_i = 0} \log \left[1 - P(X_i \mid Y=1~;~\theta)\right]\\
&= \sum_{i=1}^n y_i\log P(X_i \mid Y=1~;~\theta) + (1-y_i) \log \left[1 - P(X_i \mid Y=1~;~\theta)\right]
\end{align*}
$$
We can write this out more compactly by plugging substituting the log-likelihood for each data point with the logistic function where $s_i = s(\hat y)$,
$$
\log P(X \mid Y=1) = \sum_{i=1}^n y_i \log s_i + (1-y_i) \log (1 - s_i)
$$
The objective function is then,
$$
\theta^* = \mathop{\arg\max}_{\theta} \bigg[\log P(X \mid Y=1) \bigg] \label{eq:objective}
$$


The solution to this is discussion in the [Solution](#solution) section.

## Solutions

The gradient for the objective function $\eqref{eq:objective}$  (let's denote it as $\log P$ for brevity is,
$$
\nabla_\theta \log P = -X^\top(y-s) = 0
$$
* $y$ : Vector of labels
* $s$: Vector of the sigmoid for each data point $s = [s_1 \quad s_2 \quad  \ldots \quad  s_n]^\top$

Hence, the normal equation is,
$$
X^\top y = X^\top s
$$
Unfortunately there is no analytical solution that solves for $\theta^*$.  Numerical solutions can be estimated with the methods below:

1. Newton's Method
2. Gradient Descent

The Newton's method is well behaved since the Hessian is easily calculated:
$$
H_\theta(\log P) = X^\top \Omega X
$$
Where $\Omega \in \mathbb R^{d \times d}$ is a diagonal matrix with entries $\omega_i = s_i(1-s_i)$. Using the gradient and the Hessian, Newton's method approximates the next step $\theta(t+1)$ given the current step $\theta(t)$ as,
$$
\begin{gather*}
\theta(t+1) = \theta(t) + \Delta \theta\\
[X^\top \Omega X]\Delta \theta = -X^\top(y-s)
\end{gather*}
$$
Unfortunately the solution is not well behaved if $X^\top X​$ is not always positive definite. However, a ridge regularization discussed in the section [Regularization](#regularization) can guarantee this.

## Decision Rule

The decision rule is simple following the Bayes optimal rule:
$$
\hat Y = \begin{cases}
1 & P(X \mid Y=1) > 0.5\\
0 & \text{otherwise.}
\end{cases}
$$

## Regularization

The most practical regularization is to add the $L_2$ (Ridge) regularization which guarantees that Newton's method is solvable by inversion because the Hessian is positive definite.
$$
\begin{gather*}
H_\theta(\log P) = X^\top \Omega X + 2\lambda I\\
\Delta \theta = -X^\top(y-s)[X^\top \Omega X + 2\lambda I]^{-1}
\end{gather*}
$$


## Multiclass Generalization





## Equivalence to Loss Function





The logistics regression is linear regression with a logistic loss function. We motivate using logistic loss with the example of data that comes from two classes $y: {0,1}$. The probability that we receive $y=0$ along with some data $x$ is $P(y=0 \mid x)$. The probability of the other class is then ​$1 - P(y=0 \mid x)$.
$$
P(X \mid \hat y) = \sum_{i=1}^n  \bigg[ \log P(y_i \mid X_i) + \log\Big(1-P(y_i \mid X_i)\Big) \bigg]
$$

Given $y \in (0,1)$ the logistics function is a discriminant model

The optimization problem is then,

$$
\hat y = \mathop{\arg\min} \sum_{i=1}^n - \left[ y_i \log s_i + (1-y_i)\log(1-s_i)\right]
$$

* $s_i$ : The logistic function for row $i$,

    $$s_i(X_i^\top \theta) = \frac{1}{1+e^{-X_i^T \theta}}$$

    Notice its derivative is,

    $$s_i' = s_i(1-s_i)​


## Properties

* Differs from LDA or QDA by emphasizing the decision boundary
* Less sensitive to outliers
* Robust on non-Gaussians. (LDA is better if data is near Gaussian)
* Unstable to new points for well separated classes.