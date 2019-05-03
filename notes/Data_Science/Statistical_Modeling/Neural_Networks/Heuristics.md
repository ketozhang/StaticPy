---
title: Heuristics
---

## Performance

* Stochastic gradient descent.
* Standardization
* Centering the hidden units. For example replacing sigmoid with tanh function.
* Differing learning rate for each layer of weights.
* Emphasize rare classes by using it more often.
* Second-order optimization
    * Nonlinear conjugate gradient
    * Stochastic Levenberg Marquardt
* Acceleration schemes:
    * RMSprop
    * Adam
    * AMSGrad

## Avoid Bad Local Minima

* Stochastic gradient descent.
* Momentum

## Avoid Overfitting

* Ensembles of neural nets with random intnial weights and bagging.
* L2 regularization (aka weight decay)
* Dropout, randomly disable a set of nodes of some hidden layers every epoch. When a node is disabled its weight is stored however it's just not participating in changing its weight on the epoch. This simulates an ensemble.