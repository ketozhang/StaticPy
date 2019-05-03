---
title: Lasso Regression
---

The **least absolute shrinkage and selection operator** (LASSO) regression is regression with $L_1$ loss,
$$
\mathcal L(\theta) = \sum_{i=1}^n L(y,\hat y) +  \lambda\|\theta\|_1
$$
The name is appropriate because the LASSO often sets a subset of the feature parameters to zero.