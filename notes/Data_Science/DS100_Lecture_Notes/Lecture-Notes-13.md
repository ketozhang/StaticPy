---
title: Lecture Notes13
---
# Lecture Notes 13 - Modeling Estimation

## Model
Model is an **idealized** representation of a system

### Defining the Model
To start out with creating a model, one can make a hypothesis. These hypothesis may be based on **prior knowledge**.

### Define the Loss

**Loss function**
: A function that characterize the cost, error, or loss resulting from a particular chioce of model or model parameters.

#### Square Loss
A very popular loss function is the ${L^2}$ ('el two') loss which is a quadratic loss function.

$$ L(\theta,y) = (y-\theta)^2 $$

* $y$ : data
* $\theta$ : predicted value
* Pros: If good fit, no loss
* Cons: If bad fit, very bad loss

#### Absolute Loss
The $L^1$ loss is the linear loss function,

$$ L(\theta,y) = \lvert{y-\theta}\rvert $$

* Pros: If good fit, no loss
* Cons: If bad fit, some loss

#### Huber Loss
The Huber's Loss function smooths out the non-differentiable part of the absolute loss as a tradeoff between the pros and cons square and absolute loss.

$$ L_\alpha(\theta,y) = \begin{cases} \frac{1}{2}(y-\theta)^2 \\ \alpha\left(\lvert{y-\theta}\rvert - \alpha/2\right) \end{cases} $$

* $\alpha$: Sensitivity parameters for outliers.

#### Average Loss
The amount of loss for each data point may be calculated the unweighted average,

$$ L(\theta, \mathcal{D}) = \frac{1}{n}\sum_{i=1}^{n}{L(\theta, y_i)}$$

#### Loss Optimization
The loss function is optimizeable in parameter $\theta$. $\theta_\text{min}$ may exist in the critical points where $L'(\theta) = 0$. I will assume you know calculus and skip the notes on calculus optimization.

The minmum for the square loss function is the mean of the data:
$$ \hat{\theta} = \frac{1}{n}\sum_{i=1}^n{y_i}$$

For the average absolute loss the minimum is the median of the data:

$$ \hat{\theta} = \text{median}(y) $$

For the Huber function there is no analytical solution, it is the roots of the equation:

$$ \sum_{\theta \ge y_i + \alpha}{\alpha} - \sum_{\theta \le y_i - \alpha}{\alpha} - \sum_{\lvert{\theta - y_i}\rvert < \alpha}{(y_i-\theta)} = 0$$