---
title: Lecture Notes20
---
# Lecture Notes 20

## Derivation of the Normal Equation

THe normal equation is no longer bonus material. Consider the system we want to model with data $Y$ and the model denoted as $\hat Y$ which is represented as,

$$ \hat Y = \Phi\hat \theta $$

* This means that $\hat Y$ lives vector space span by $\Phi$ (in other words columns space of $\Phi$).
* $Y$ does not necessarily have to live in the column space of $\Phi$ however there exist a component of of $Y$ that does which is exactly what we meant by the model $\hat Y$.
* There residual/error is the distance away $Y$ is from the column space of $\Phi$ which we want to minimize (distance always refers to squared loss).

Recall that the distance vector from $Y$ to some point on the column space $\Phi \theta$ is $Y - \Phi\theta$ for some parameter $\theta$. The shortest distance (minmize squared loss) is a vector perpendicular/orthogonal to the column space so,

$$ \Phi^T(Y - \Phi\hat\theta) = 0 \tag{othogonality} \\
    \boxed{\hat\theta = (\Phi^T\Phi)^{-1} - \Phi^TY}
$$

## Bias-Variance Tradeoff

Let's get ack to the bias-variance tradeoff. We need some terms:

Training data
: The data used by the model

Test data
: The data used to test the model. We'd use test data to see if model is a good fit for the general case

The bias-variance tradeoff explains that the more your model matches your training data (decreasing bias, increasing complexity) the less likely your model will match your test data (increasing variance) vice versa.

## Train-Test Split

We ask the question if you have a finite amount of data how much should be invested into training and how much should be invested to testing?

* In practice usually train = 90% and test = 10%.
    * very bad for stock predictions (way too time dependent)
* Larger training set $\rightarrow$ more complex models
* Larger test set $\rightarrow$ better estimate of generalization error

## Generalization and Testing Model

1. Split data into training and test sets
2. Use only the trianing data when designing, trianing, and tuning the model
    * Never look at the test data
    * If you look at the test data, you must try cross validation
3. Commit to your final model and train once more using only the training data
4. Test the final model using the test data.
    * If it sucks, go back to step #2
5. Train on all available data

### Cross Validation

Cross validation is like bootstraping where we take multiple sets of training data and test data instead of one. Say there are $N$ sets then $N$ models are generated, you may test all $N$ models to all available data to see which one is the best.

## Regularization
Regularization once again is the process to weigh the features. We wish to minimize the loss function so there must be some features that increases the loss function too much therefore we regularize that feature to be lower.

$$ \hat \theta = \hat \theta_0 + \lambda R(\theta) $$

* $\hat \theta_0$ : Unregularized $\theta$ parameter

For the regularization parameter $\lambda$ we wish to have,

$$ \text{Complexity}(f_\theta) \le \lambda $$

Unfortunately complexity isn't easy to computer. We may take this definition that complexity is the sum of the set of our model that contributes something $\Bbb{I[\theta_j \ne \theta]}$. The quantity that we sum accross is also confusing.

$$
\text{Complexity} f(\theta) \equiv \sum_{j=1}^{d}{\Bbb{I[\theta_j \ne \theta]}}
$$