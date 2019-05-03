---
title: Gaussian Distribution
---

The most prevalent distribution appearing in countless fields is the Gaussian or normal distribution.

$$X \sim N(\mu, \sigma)$$
$$P(X=x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

* **Properties**
    * **Standard Normal Distribution**

        The standard normal distribution is $N(0,1)$ which plays an important role in motivating why we standardize random variables. Say for a Gaussian random variable $X$,

        $$ Y = \frac{X-\mu_X}{\sigma_X} \iff Y \sim N(0,1)$$

    * **Independent Joint Probability (Rotational Invariant)**

        Due to the distribution's property of rotational invariance, the joint property of two iid Gaussian is a Gaussian however you rotate the random variable axes. Even better the Gaussian has the mean and variance of the sums of the two Gaussians.

        $$
        P(X,Y) = \text{N}(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)
        $$

    * **Sum:**

        $$
        P(X+Y) =
        $$

    * **Characteristics Function**:

        $$\tilde p(x) = \exp{\left[-ik\mu -\frac{k^2\sigma^2}{2}\right]} $$

    * **Cumulants and Moments**:
        $$
            \avg{x}_c = \mu ,\quad \avg{x^2}_c = \sigma^2,\quad \avg{x^n}_c = 0, \quad \ldots,\quad  \avg{x^n}_c = 0\\
            \avg{x} = \mu ,\quad \avg{x^2} = \sigma^2 + \mu^2,\quad \avg{x^n} = 3\sigma^2\mu + \mu^3, \quad \ldots
        $$

## Central Limit Theorem

For iid random variables $X_1, X_2, \ldots $ each with the same mean $\mu$ and variance $\sigma^2$. Let $\bar X$ be the sample mean,

$$ \bar X = \frac{1}{n}\sum_i^n{X_i} $$
$$ \text{Var}[\bar X] = \frac{\sigma^2}{n}$$

Let's define the random variable $Z$ to be the standardized sample mean,

$$ Z = \frac{\bar X - \mu}{\frac{\sigma}{\sqrt{n}}} $$

As $n \rightarrow \infty$, this $Z$ tends towards a $N(0,1)$

$$ P(Z \le c) \rightarrow \frac{1}{\sqrt{2\pi}} \int_{-\infty}^c e^{-x^2/2}~\mathrm dx $$

## Multivariate Gaussian
For a vector of random variables $\boldsymbol x$, the multidimensional or multivariate gaussian is given by


$$
\boldsymbol X \sim \mathcal N(\boldsymbol{\mu}, \Sigma)\\
P(x) = (2 \pi \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2}(\boldsymbol x- \boldsymbol \mu)^T \Sigma^{-1} (\boldsymbol x- \boldsymbol \mu)\right]
$$

* $\Sigma$ : The covariance matrix

More compact is to treat $(\boldsymbol x- \boldsymbol \mu)^T \Sigma^{-1} (\boldsymbol x- \boldsymbol \mu)$ as the squared distance of some vector $\Sigma^{-1/2} \boldsymbol \Delta$ where $\boldsymbol\Delta = \boldsymbol{x} - \boldsymbol{\mu}$ which is known as the **deviation vector**. This compact form is given as,

$$
P(\boldsymbol\Delta) = (2 \pi \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2}\left\lvert\Sigma^{-1/2} \boldsymbol \Delta\right\rvert^2\right]
$$

### Covariance Matrix

The covariance matrix $\Sigma$ is a semipositive definite (symmetric) matrix

Diagonal Covariance Matrix
: If the covariance matrix is diagonal then

    $$ P(\boldsymbol{x}) = \prod{P(X_i)} $$