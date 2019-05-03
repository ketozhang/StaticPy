---
title: Feature Selection
---



## Forward Stepwise Selection

$\mathcal O(d^2)$ algorithm that builds a model by adding features iteratively:

1. Start with no features (null model)
2. Score single-feature models
3. Add the best scoring single-feature model to the null model
4. Repeatedly add the best scoring feature until validation error starts increasing.



## Backward Stepwise Selection

$\mathcal O(d^2)$ algorithm that builds a model by removing features iteratively:

1. Start with all-features model
2. Remove the feature that results to the best $d-1$ feature model.



## Selection by Parameter

Remove features with small parameters. This is best used for normalized data.



If the data is not normalized, alternatively some metric called the **z-score** can be used to score the features' importance.
$$
z_j = \frac{\theta_j}{\sigma \sqrt{(X^\top X)_{jj}}}
$$

### LASSO

Naturally adding the LASSO regularization would set some of the features to zero. Using this these features may as well be removed from the dataset.

