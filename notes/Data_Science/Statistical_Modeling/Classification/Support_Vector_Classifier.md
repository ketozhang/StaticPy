---
title: Support Vector Classifier
---

Given that not all data can be fitted by a **maximal margin classifier** (MMC), the **Support Vector Classifier** attempts to generalize this classifier.

## Hard Margin SVC

This term is equivalent to the MMC which perfectly separates a linearly separable dataset in the feature space. As usually it's easier to talk about binary classes. The goal of hard margin SVC is to separate one class of points away from the other class by a hyperplane decision boundary in the feature space given by,
$$
X^\top \theta + \theta_0 = 0
$$
The minimum distance between all points to the hyperplane is called the **margin** $M$. We motivate that the larger the $M​$ the more confident the SVC successfully separate the two classes. Hence, the optimization problem for the SVC is to maximize the margin given,
$$
\begin{gather}
\max_{\theta, \theta_0} M~; \qquad |\theta|=1\\
y_i(X_i^\top\theta + \theta_0) \ge  M~; \qquad i \in [1,n]
\end{gather}
$$
![SVC](D:\Google Drive\Documents\Notes\_Data_Science\Statistical_Modeling\Classification\SVC.png)

We can remove the constraint of $|\theta|=1$  by noting that when $\theta$ isn't normalized, $M \propto 1/|\theta|$. This justify that it is equivalent to let the optimization problem be in terms purely of $|\theta|$ (i.e., $M:= 1/|\theta|$),
$$
\begin{gather}
\min_{\theta, \theta_0} |\theta|~\\
y_i(X^\top\theta + \theta_0) \ge 1~; \qquad i \in [1,n]
\end{gather}
$$




## Soft Margin SVC

To be **soft margin** is to allow some training points to lie within the margin $y(X_i) \le M$ and some points to be on the wrong side of the decision boundary. This could lead to training error but improve MMC in:

* Greater robustness to new training points.
* Can describe more general training points.

We relax the conditions by introducing a slack variable $\epsilon$.

$$
\begin{gather*}
     \min_{\theta} |\theta|\\
     y_i(\theta^TX_i + \theta_0) \ge 1-\epsilon_i~; \qquad i \in [1,n]\\ \epsilon_i \ge 0~; \qquad \sum_{i=1}^n\epsilon_i \le C
\end{gather*}
$$

* $\epsilon$ : **slack variable** or **error variable**
    * If $\epsilon_i > 0$ then $i$-th point is on the wrong side of the margin
    * If $\epsilon_i > 1$ then the $i$-th point is on the wrong side of the hyperplane.
* $C$: **C penalty**, a hyperparameter that can be intuitively think of as the budget for the amount of training points that can violate the margin (be within the margin or even on the opposite side).
    * For $C>0$, there can be no more than $C$ training points on the wrong side of the hyperplane (being on the hyperplane is also being on the wrong side).
* **Support Vectors**: we redefine support vectors to be the training points that lie on or within the margin. In fact, only support vectors effective the decision boundaries. Any new data point outside the margin (not a support vector) have no effect on the decision boundary.

We can convert the SVC into a quadratic form,

$$
\begin{gather*}
    \min_{\theta, \epsilon}{\lvert \theta \rvert^2} + \frac{1}{C} \sum_{i=1}^n \epsilon_i\\
    y_i(\theta^TX_i + \alpha) \ge 1 - \epsilon_i~; \qquad i \in [1,n]\\
    \epsilon_i \ge 0\\
\end{gather*}
$$



## Solutions to SVC

The solution (the hyperplane) to the SVC optimizing problem can be shown to always take the form,

$$ f(x) = \theta_0 + \sum_{i=1}^n{\alpha_i K(X_i,x)} $$

* $K(X_i,x)$ : The kernel function that takes in the training points and the input value. Here are the following frequently used kernels:
    * **Linear:**
        $$K(X_i,x) = X_i \cdot x$$
    * **Polynomial**
        $$K(X_i,x) = (1 + X_i \cdot x)^d$$
    * **Radial:**
        $$K(X_i,x) = \exp\left(-\gamma \sum_{j=1}^p{(X_{ij} - x_{j})^2}\right)$$
* $\alpha_i$: Nonzero only for support vectors.

## Nonlinear Feature Transformation

### Feature Lifting
For example, a parabolic feature transformation adds another dimension to the feature vector where the new dimension is $X_{i, d+1} = \lvert{X_i}^2\rvert$,

$$
\Phi(X_i) = \begin{bmatrix}
    X_i \\
    \lvert X_i \rvert^2
\end{bmatrix}
$$

Effectively this adds a squared length feature as the $(d+1)$th dimension that lifs feature points up higher if they are further away from the origin. A hyperplane can then slice through the gap if say class A is lifted higher than class B.

Theorem
: $\Phi(X)$ are linearly separable iff $X$ is separable by a hypersphere.