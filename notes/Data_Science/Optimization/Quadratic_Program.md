---
title: Quadratic Program
---

A quadratic program is a quadratic optimization convex function (defined by the matrix $Q$) with a linear inequality constraint. The goal is to find the paramters $\theta$ that minimizes the optimization function:

$$
f(\theta) = \theta^T Q \theta + c^T \theta + \alpha, \qquad A\theta \le b
$$

* If $Q$ is positive definite then there exists only one local extrema.

## Simplex Algorithm

## Sequential Minimal Optimization (SMO)

* Used by `LIBSVM`

## Coordinate Descent

* Used by `LIBLINEAR`