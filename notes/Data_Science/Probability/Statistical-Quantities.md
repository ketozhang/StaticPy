## Expected Value
The expected value or expectation value of $X$ is the mean of $X$. For the discrete case, the epected value is given by,

$$\boxed{ \Expected{X} = \sum_{x}{x P(x)}}$$

The expected value has the following properties:

* Expected value of a constant is constant:

$$\Expected{c} = c$$

* The previous property is all you need to understand the following linearity property. For the following take lower case letter to be contant and upper case letter to be random variables.

$$ \Expected{aX+Y+b} = a\Expected{X} + \Expected{Y} + b $$

## Variance

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

## Covariance

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