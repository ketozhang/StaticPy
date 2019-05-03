---
title: Lecture Notes18
---
# Lecture 18 - The Bias Variane Tradeoff and Regularization

## Linear Model for Non-Linear Data

Say we wish to model a general function $f(x)$ which is not always linear, a linear fit to $f(x)$ can be generally approximated like so:

$$ f_\theta(\phi(x)) = \phi(x)^T \theta = \sum_{j=1}^{k}{\phi(x)_j \theta_j}  $$

* $\phi(x)$ : A vector of functions.
    * If you're familiar with linear algebra, this is similar to a set of basis vectors but not the same.
* $\theta$ : The model's parameter that weighs each vector hence it's common to call this the weight coefficient.

Bias
: The **bias** is the expected deviation between the predicted value and the true value.

    Depends on:

    * choice of model function $f(\theta)$
    * learning procedure

Observation Variance
: Observation variance is the variability of the random noise in the process we are trying to model. It is usually impossible to get rid of all observation variance. Sources of observation variance comes from:

    * measurement variability
    * stochasticity
    * missing information

Estimated Model Variance
: **Estimated model variance** is the variability in the predicted value accros different training datasets

    * Sensitive to variation in the training data
    * Poor generalization
    * Overfitting

## Example: Analysis of Squared Error

Let's say we wish to model our data $y$ that has some noise. We will absorb this noise into an error value $\epsilon$ such that the true function that describe the system is denoted as $h(x)$ therefore the data is,

$$ y =h(x) + \epsilon $$

Expected Loss
: Before we compute the expected loss notice that the $\Expected{y} = \Expected{h(x)}$ since $\Expected{\epsilon} = 0$ due to the error being a random variable.

$$
\begin{align*}
\Expected{(y-f_{\hat\theta})^2} &= \Expected{(y- h(x) + h(x) - f_{\hat\theta})^2}\\
&= \Expected{(y-h(x))^2} + \Expected{(h(x)-f_{\hat\theta})^2} +  2\Expected{(y-h(x))(h(x)-f_{\hat\theta})}\\
\Expected{(y-f_{\hat\theta})^2} &= \underbrace{\Expected{(h(x)-f_{\hat\theta})^2}}_\text{Obs. Variance} + (\underbrace{h(x)-\Expected{f_{\hat\theta}^2}}_\text{Bias})^2 + \underbrace{\Expected{(\Expected{f_{\hat\theta}} - f_{\hat\theta})^2}}_\text{Model Variance}
\end{align*}
$$

## Regularization

Regularization is to add a parameter $\lambda$ to control them modeling complexity through the regularization function $R(\theta)$. This is used in determining the model parameter.

$$\hat \theta \equiv \arg \min \frac{1}{n}\sum_i^n{\ell(y_i,f_\theta(x_i))} + \lambda \mathbf{R}(\theta)$$

Example of regularization include the same exact function as the loss functions $\Bbb{L^1}$ (Ridge regularization) and $\Bbb{L^2}$ (LASSO regularization).

The point is to simply introduce another function that further optimizes the model parameter.