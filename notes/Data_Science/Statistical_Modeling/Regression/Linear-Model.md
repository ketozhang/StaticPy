---
title: Linear Model
---

Consider a dataset as a matrix of $X \in \mathbb{R}^{m\times n}$ where we've extracted $m$ numbers of data records/rows and $n$ numbers of feature columns. We may map the dataset $X_0$ to a feature function which outputs the design matrix $X = f(X_0)$. Our linear model can easily be written in the form of a dot product,

$$ \hat y = X \beta $$

* $\hat y$ : Model output vector
* $\beta^T$ : Row vector of the transposed parameter vector
* $X$ : Feature or Design matrix

## Solution to Square Design Matrix

In rare cases, the design matrix is a square matrix. In this case the solution is possibly,

$$ \beta = X^{-1}\hat y $$

## Normal Equation

We may force the design matrix to be a square matrix by multiplying both sides by its transpose,

$$ X^T\hat y = X^T X \beta  $$

We still have a linear equation and the solution for $\beta$ is can be done in two ways:

1. Assuming $X^TX$ is an invertible matrix,

    $$ \beta = (X^TX)^{-1} X^T\hat y $$

2. Gaussian Elimination (traditional way of solving linear algebra equations)