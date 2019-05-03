---
title: Bayes Decision Rule
---

For some loss function $L$ the **Bayes Decision Rule** simply chooses the class with the maximum posterior distribution scaled by the loss of misclassification. For the cases of two classes, the decision rule looks like,

$$
\hat y(x) = \mathop{\arg\max}_A L(\neg A,A)P(A\mid x)
$$

A motivation why the sign is greater than is because we assign a greater loss if say class $A$ was classified wrong. If it was classified wrong, there should be a greater chance that the classifier will change its decision rule to choose classify $A$ better.

## Zero-One Loss

The risk function for the 0-1 loss is,

$$
R(\hat y) = P(\hat y(x)\text{ is wrong})
$$

This suggest that the decision boundary is the set of all points where $\set{x : P(A \mid x) = 0.5}$