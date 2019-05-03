---
title: Naive Bayes
---

The Naive Bayes is an algorithm for classification. Let's first define Naive Bayes it for two categories. $Y$ is either in category $A$ or category $B$ where $Y$ has features notated as the random variable $\Phi=\set{\phi_1,\phi_2,\ldots,\phi_n}$

$$ O = \frac{P(A|\Phi)}{P(B|\Phi)} = \frac{\prod{P(A|\phi_i)}}{\prod{P(B|\phi_i)}} $$

* This formula is interpreted as the odds that $Y$ is either $A$ vs $B$ given $\Phi$
* Naive Bayes is naive simply because we assume a commutative/independent relation between each feature (order does not matter).

## Python - sklearn

Naive bayes package: `sklearn.naive_bayes`

```py
from sklearn.naive_bayes import __NB
clf = __NB()
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
```