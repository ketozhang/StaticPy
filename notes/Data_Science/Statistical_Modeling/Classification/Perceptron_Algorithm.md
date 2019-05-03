---
title: Percepton Algorithm
---

The perceptron algorithm is the most simplest form of what now called the neural network. The algorithm can be used to classify a binary class. The goal is to find some weights $\theta$ that satisfies the following:
$$
y = \begin{cases} 1 & X_i^\top \theta \ge 0\\ -1 & X_i^\top \theta \le 0 \end{cases}
$$
This is equivalent to finding a hyperplane that linearly separates the data points. However a strict constraint is that the hyperplane is centered at the origin[^bias].

[^bias]: This constraint can be removed by adding a bias term $\theta_0$ along with transforming the design matrix with ones.

We define a loss function as,

$$
L(y_i, \theta) = \begin{cases}
0, & \text{sign}(X_i^\top \theta) = y_i\\
|X_i^\top \theta|, &\text{otherwise}
\end{cases}
$$

The risk function (expectation value of $L$ on $X$ parameterized over $\theta$) is given by,

$$
R(X,\theta) = \sum_{i=1}^{n} L(\theta_i, y_i) = \sum_{i \in W} |X_i^\top \theta|
$$

* $W$: A set indices where $\hat y_i$ is wrong.

## Feature & Parameter Space Symmetry

The percepton algorithm's constrain allows for a nice symmetry between feature $X_i$ and parameter space $\theta$ which may be stated as:

* In $x$ feature space, the feature are points while the parameters are vectors that draws a hyperplane at the origin.
* In $\theta$ parameter space, the parameters are points while the features are vectors that draws a hyperplane at the origin.

It is very useful to look at the parameter space because there may exist a region bounded by the feature hyperplanes that determines the values of $\theta$ which correctly classifies any linearly separable set of training data $X$.

## Perceptron Convergence Theorem

For the modified perceptron classifier,

$$
\hat y(x) = x \cdot \theta + \theta_0
$$

If the data is linearly separable then there always exist a solution that perfectly classifies the data in at most $\mathcal P(R^2/M^2)$ iterations

* $R$ : $\max\lvert X_i \rvert$
* $M$ : Maximal margin.