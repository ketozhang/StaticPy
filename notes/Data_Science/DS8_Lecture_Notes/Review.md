---
title: Data 8 Review
---

## Summary Statistics
Total Variation Difference
: Given the residual between the model and sample, a good metric to measure the distance between the two is the **TVD**:

    $$
    \frac{1}{2}\sum_i|\hat Y_i - y_i|
    $$

    This is often used when the distribution interested $y$ is multi-dimensional (e.g., ethnicities) where $\sum _i Y_i -  y_i = 0$