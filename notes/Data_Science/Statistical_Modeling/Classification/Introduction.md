---
title: Introduction to Support Vector Machine
---

## Decision Bound

A **decision bound** is a boundary chosen by the classifier to determine if data points are within a certain class or another. Typically a decision bound is a function $f: x \in \mathbb R^d \rightarrow \mathbb R$ such that $f(x)=0$.


### Hyperplane as Decision Bounds

A hyperplane is a $p-1$ dimension subspace living in $p$-dimension. The hyperplane is mathmetically described as the equation,

$$ \theta \cdot x + \theta_0 = 0 $$
$$ \theta_0 + \theta_1x_1 + \theta_2x_2 + \ldots + \theta_px_p = 0 $$

* $\theta$ : A vector normal to the hyperplane. This determines the direction that the hyperplane points to.
* $\theta_0$ : The intersect point which may be interpeted as the distance the hyperplane is from the origin.

We may use the hyperplane as a decision bound. In 2D, the hyperplane is a line. In this case the decision function is  thought of as:

> If the input falls on the left of the line then it's class A otherwise class B.

In math, the decision function takes in an input vector $X_i$ and outputs a label (strictly this is numerically represented),

$$
y = \begin{cases}
    \text{1}, & \theta \cdot X_i > 0\\
    \text{-1}, & \theta \cdot X_i < 0
\end{cases}
$$

* $y=1$ can be represent class A and $y=-1$ can be class B
* You can immediately tell that hyerplane are great for **linearly separable** data
