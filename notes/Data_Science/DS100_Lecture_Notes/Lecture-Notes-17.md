---
title: Lecture Notes17
---
# Lecture Notes 17

Before we begin, some terms:

Sample
: The data we have

Population
: The general group we study

## Probability
We'll purely be working with discrete data, please take all math here to be discrete so there was be no integrals just summations.

Probability $P$
: The chance that an event occurs

Random Variable $X$
: A variable whose value is determined by a chance event.

## Expected Value
The expected value or expectation value of $X$ is the mean of $X$. For the discrete case, the epected value is given by,

$$\boxed{ \Expected{X} = \sum_{x}{x P(x)}}$$

The expected value has the following properties:

* Expected value of a constant is constant:

$$\Expected{c} = c$$

* The previous property is all you need to understand the following linearity property. For the following take lower case letter to be contant and upper case letter to be random variables.

$$ \Expected{aX+Y+b} = a\Expected{X} + \Expected{Y} + b $$


## Joint Probability
An important property of probability is the **joint probability**.

### Independent Joint Probability

For instance, in a sampling with replacement what is the probability that the first sample $X_1 = x_1$ and $X_2 = x_1$ where $x_1$ is some arbitrary event with probability $P(x_1)$ of being sampled. The answer is becuse the sample is replaced, the two samples are independent. Therefore the joint independent probability is given by,

$$ P(X_1 = x_1, X_2 = x_2) = P(x_1)P(x_2) $$

In general,

$$\boxed{ P(X) = \prod_{x_i\in X}{P(x_i)} }$$

* $X$ : A list of samples $X = \{X_1, X_2,...\}$ each $X_i$ can take the values $\{x_1,x_2,...\}$

### Expectation Value

The expectation value of a joint probability follows linearity such that,

$$ \Expected{aX+bY+c} = \sum_{x \in X}{\sum_{y \in Y}}{P(x,y)(ax+by+c)} $$  

### Conditional Probability

The join property has an identity called the conditional probability which is the probability of an event given that the previous.

It is easy to show this if we only do two samples. For two samples $X$ and $Y$ respectively correspond to the index $x$ and $y$ so the probability is $P(x,y)$ which is also be represented as a **conditional probability**,

$$\boxed{ P(x,y) = P(x \mid y)P(y)\\
P(x,y) = P(y \mid x)P(x) }$$

* As you may have notice it doesn't matter if you swap the $x$ or $y$ for conditional probability.
* $P(x\mid y)$ is phrased as "the probability of x given y".

### Variance

The variance is defined as the average of the data's squared deviation from the mean, here deviation means $\Delta X = X - \Expected{X}$

$$ 
\Var{X} \equiv \Expected{(\Delta X)^2}\\
\boxed{\Var{X} \equiv \Expected{(X - \Expected{X}^2)^2}}
$$

However a more useful identity is the squared term identity,

$$ 
\boxed{\Var{X} = \Expected{X^2} - \Expected{X}^2}
$$

Here are some more properties:

* Variance of a constant is zero
    $$\Var{a} = 0$$
* Variance of a constant factor squares the constant factor
    $$\Var{aX} = a^2\Var{X}$$

* Linearity if Independent
    $$ \Var{X+Y} = \Var{X} + \Var{Y} $$

Another useful quantity that is used a lot more than the variance is called the **standard deviation**, which is just the square root of variance:

$$ \mathbf{SD}[X] = \sqrt{\Var{X}} $$

### Covariance

The covariance describe how two variables vary jointly,

$$
 \Cov{X,Y} = \Expected{\Delta X \Delta Y} \\
\boxed{\Cov{X,Y} \equiv \Expected{(X-\Expected{X})(Y-\Expected{Y})} }
$$

A useful identity is,
$$
\Cov{X,y} = \Expected{XY} - \Expected{X}\Expected{Y}
$$

Some properties:

* By definition covariance of two independent sample is zero

$$ \Cov{X,Y} = 0 \tag{X independent of Y} $$

* Covariance of constants are zero

    $$ \Cov{a, b} = 0 $$

* Covariance of a constant factorc can be factored out,

    $$ \Cov{aX,bY} = ab\Cov{X,Y} $$

Like variance, there is another version of covariance that is used more called **correlation**,

$$\boxed{ \Corr{X,Y} = \frac{\Cov{X,Y}}{\SD{X}\SD{Y}} }$$

## Two Value Example

Let's do an example of a system of two values with probability $p$ and $1-p$,

$$ \Expected{X} = p \\
\Var{X} = p(1-p)
$$

## Statistics with Multiple Samples

This part will be a bit confusing, consider that we take multiple samples labeled $X_i$ indexed with $i$'s. A useful quantity to get from these samples is the average value (**not expected value**) which is also called the **sample mean**,

$$ 
\boxed{\bar{X} \equiv \frac{1}{n}\sum_{i=1}^{n}{X_i}}
$$

For the unbiased and independent samples, we may get statistic quantities from the sample mean,

$$ 
\Expected{\bar X} = \mu\\
\Var{\bar X} = \frac{\sigma^2}{n}\\
\SD{\bar X} = \frac{\sigma^2}{\sqrt{n}}
$$

* $\mu$ : Population mean or the mean of all samples
* $\sigma$ : Standard deviation of all samples
* $ \SD{X} $ : This is also known as the **standard error**, $\SD{X} = \mathbf{SE}(X)$

## Bootstrap Sampling

A bootstrap sample is a method that samples the sample. 

## Average Sample Loss

We will now redefine our loss function to be even more general

$$ \bar{L}(\theta) = \frac{1}{n}\sum_{i=1}^n{\ell(Y_i,f_\theta(X_i))}$$

* $\ell(Y_i,f(X_i))$ : Loss function given some parametric model $f$

## Risk and Expected Loss

Risk is the expected value of the loss function,

$$ R(\theta) =  \Expected{\ell(Y,f_\theta(X))}$$