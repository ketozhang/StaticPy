---
title: Loss Function
---

The **loss function** is a function that describe the cost, error, or loss resulting from a choice of a model. Mathematically you may interpret this as the function that calculates the deviation of the model from the actual answer/system.

Say for some data $y(x)$ is estimated by a prediction (model) $\theta(x)$, then the loss function $L$ takes in the two functions $L(\theta,y)$ and computes the error.

Still confused? Just go to the next section, this requires examples.

## Motivation
A common way to measure error between some data and model is directly get the residual (subtract the two together). This subtraction may be written as some function (the loss function) as,

$$ L(\theta,y_i) =  |y_i - \theta|$$

We wish to find some model $\theta(x)$ that fits as closely to the data $y(x)$ as possible. The loss function method attempts to do so by minimizing the loss for some parameter $\theta$. We begin by using a single parameter to guess a zeroth order approximation,

$$ y \approx \hat\theta $$

* $\hat \theta$ : Best parameter that minimizes the loss function.

Later on we will attempt to do better by either introducing other parameters (if it exists) or use other expansion like the power series of $\theta$.

## Types of Loss Functions

### Absolute Loss Function
The **absolute loss function** denoted as $\Bbb{L}_1​$ is defined as the **residual** or **difference** the data and model is given by,

$$\boxed{L(\theta,y_i) =  |y_i - \theta|}​$$

* **Pros**
    * Not sensitive to the outlier
* **Cons**
    * Minimum is difficult at $\theta - y_i = 0​$ since the absolute value is not differentiable at the turning point.
* **Minimum of Average $\Bbb L$**
    * The minimum of $\Bbb{L}$ occurs at the **median** of the dataset $y$

### Squared Distance Loss Function

The Euclidean distance or square distance loss function denoted as $\Bbb{L}_2​$ simply computes the distance between the data and the model. It may be written as,

$$\boxed{ L(\theta, y_i) = (y_i-\theta)^2 }$$

* **Pros**
    * Minimum is easy to find since differentiable
* **Cons**
    * Any error ($\abs{y-\theta} > 0​$) is amplified squarely
    * Sensitive to the outlier
* **Minimum of Average $\Bbb L^2$**
    * The minimum of $\Bbb{L}^2​$ occurs at the **mean** of the dataset $y​$

### Huber Loss Function

A popular loss function is the Huber loss that attempts to blend the two loss functions $\Bbb L_1$ and $\Bbb L_2$ by a piecewise function:

$$ L_\alpha(\theta,y_i) = \begin{cases}
    \frac{1}{2}(y-\theta)^2 & \abs{y-\theta} < \alpha\\
    \alpha(\abs{y-\theta} - \frac{\alpha}{2}) & \text{elsewhere}
\end{cases}$$

* $\alpha$ : a parameter that adjust how much of $\Bbb{L}_2$ dominates the loss function. So at $\alpha \ll 1$, the loss function is similar to $\Bbb{L}_1$.

### Discrete Loss Function

A discrete loss function assigns a constant value if some error is made. A very common type of this loss is called the **one-zero loss function** or **binary loss function**.

$$
L(\theta, y_i) =
\begin{cases}
    0, & \hat y = y\\
    1, & \hat y \neq y
\end{cases}
$$

Other discrete loss function can be built to portray for instance great loss for false negative versus small loss for false positives (e.g., medical diagnosis).

## Ensemble Loss Function

Given $n$ sample points and predictions $(y,\hat y )$ we'd like to get a value out of the loss for among every sample point. Take the loss as a vector $L$ and apply some aggregation function $f$ to get the **ensemble loss function**. 
$$
\mathcal L = f(L)
$$

### Risk Function

A common example of the an ensemble loss function is to take the expected value. This is called the **risk function**
$$
R(X,\theta) = \mathbb E[L]
$$
