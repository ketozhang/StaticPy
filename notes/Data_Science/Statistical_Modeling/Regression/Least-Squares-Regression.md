---
title: Least Squares Regression
---

The **linear least squares** is a linear model with $L_2$ lost function and mean error cost function $\mathcal L = \langle L_2(X) \rangle$. The linear model is given by,

$$
\hat y(X) = X \theta
$$

* $\hat y$ : Length $n$ vector of dependent values
* $X$ : The feature or design matrix of dimension $d+1$ where $d$ is the number of features.

The optimization problem is then given by

$$
\begin{align}
\theta &= \mathop{\arg\min}_{\theta} \frac{1}{n} \sum_{i=1}^n \left[y_i - X_i^\top\theta\right]^2\\
&= \mathop{\arg\min}_{\theta} \frac{1}{n} |y-X\theta|^2
\end{align}
$$

## Invertible Solution
Given the square of the feature matrix $X^\top X$ is invertible,

$$
\theta = (X^\top X)^{-1}X^\top y
$$

* $(X^\top X)^{-1}X^\top$ : This is called the **pseudoinverse** of $X$ often notated as $X^+$. Notice that,

    $$ X^+X = I $$

    Hence $X^+$ is also known as the **left inverse**

    Additionally also observe that,

    $$ \hat y = X\theta = XX^+ y $$

    Where $XX^+$ is called the **hat matrix** often notated as $H$.

### Normal Equation

An alternative way for the solution without using optimization is to note that the linear model spans a $n$-dimensional hyperplane which is also the span of $\hat y$,

$$
\hat y = X \theta
$$

To minimize the square distance between $y$ and $\hat y$ we wish the hyperplane to be perpendcular to the vector $y$,

$$
X^\top (\hat y - y) = 0
$$

This is then the **normal equation**.

## Polynomial Least Squares

Let the design matrix be denoted as $\Phi(X)$ that transform add polynomials features to the feature matrix.

For example, we can do a degree $k$ polynomial transformation with no cross terms. It's easier to write this consider every row of $X$ as $X_i$.

$$
\Phi(X_i^\top) = \begin{bmatrix}
    X_{i1} & X_{i1}^2 & \ldots & X_{i1}^k & \ldots & X_{id} & X_{id}^2 & \ldots & X_{id}^k
\end{bmatrix}
$$

## Weighted Least Squares

Sometimes you may want to weigh your data by some sort of importance or confidence metric (e.g., inverse of the data's error).

For simplicity we are only going to weigh each row. In this case, the weight can be represented as a diagonal weight matrix $\Omega$ such that $\omega_i$ is the weight the row $X_i$.

The optimization becomes,

$$
\mathop{\arg\min}_{\theta} \sum_{i=1}^n \omega_i(X_i^\top \theta - y_i)^2 = \mathop{\arg\min}_{\theta} (X\theta - y)^\top \Omega (X\theta - y)
$$