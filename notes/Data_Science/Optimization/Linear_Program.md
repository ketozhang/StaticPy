---
title: Linear Program
---

A linear program is a linear optimization convex function (defined by the matrix $L$) with a linear inequality constraint. The goal is to find the paramters $\theta$ that minimizes the optimization function:

$$
f(\theta) = \theta^T L \theta + c^T \theta + \alpha, \qquad A\theta \le b
$$

## Simplex Algorithm