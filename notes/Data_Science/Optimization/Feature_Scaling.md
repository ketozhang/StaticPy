---
title: Feature Scaling
---

Feature scaling can improve gradient descent by scaling the contours that look too long (e.g., too elliptical) to something more symmetric (e.g., more spherical). The problem comes from units of features living in different orders of magntiudes.

For example, in houses area is measured in square footage which may be in the order of $10^3$ while the number of rooms are in the zeroth order. We can see that the area feature would stretch the contour much more than the number of rooms feature.

## Standardization

A common useful method of feature scaling is to shift each feature column in $X$  to a zero mean and divide it by either size or the standard deviation.

$$ x'_j = \frac{x_j - \mu_j}{s_j} $$

* $x'_j$ : Normalized $j$-th feature column
* $\mu_j$ : mean of the $j$-th feature column
* $s_j$ : Either the size or standar deviation of the $j$-th feature column