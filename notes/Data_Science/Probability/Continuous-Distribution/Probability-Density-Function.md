---
title: Probability Density Function
---

For a continuous random variable $X$ there may exist a **probability density function (PDF)** $f_X$ which is the density of probability among its events. We can find the probability of a continuous event $A = [a,b]$ by integrating over the PDF,

$$ P(a \le X \le b) = \int_a^b f_X ~\mathrm dx $$


## Properties

* The axioms of probability applies:
    1. The PDF is non-negative,

        $$ f_X(x) \ge 0 $$

    2. The area of the PDF is norm-1.

        $$ \int_{-\infty}^\infty f_X(x)~\mathrm dx = 1 $$

    3.


## Joint Density Functions

The probability of two events,

$$ P(X \in A, Y \in B) = \int_B\int_A f_{XY}(x,y)~\mathrm dx \mathrm dy $$
