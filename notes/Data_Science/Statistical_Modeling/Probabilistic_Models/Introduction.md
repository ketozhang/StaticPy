---
title: Introduction
---

## Bayes Rule

For determining parameters (often used in regression),

$$
P(\theta \mid D) = \frac{P(D\mid\theta)P(\theta)}{P(D)}
$$

For classification determining if some data row $D$ is in some class $y$,

$$
P(Y = y\mid D) = \frac{P(D\mid Y = y)P(Y = y)}{P(D)}
$$

## Risk Function

The risk function is  the expected value of the loss function over all possible solutions from the model $\hat y(\theta)$. This is the marginalization of the loss function over the posterior distribution.

$$
R(\theta, y) = \mathbb{E}[L(\theta,y)] = \int\limits_{\min{y}}^{\max{y}} L(\theta,y)P(\theta \mid x)~\mathrm d y
$$