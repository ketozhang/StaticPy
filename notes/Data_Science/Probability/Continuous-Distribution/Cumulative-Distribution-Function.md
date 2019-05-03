---
title: Cumulative Distribution Function
---

A cumulative distribution function is defined as the sum of the probabilty from the left to some point $x$ on the right,

$$ F(x) = \int_{-\infty}^x f_X~\mathrm dx $$

* Non-decreasing
* Right continuous
* Decreasing to zero
    $$ \lim_{x\rightarrow -\infty} F(x) = 0 $$
* Increasing to one
    $$ \lim_{x\rightarrow \infty} F(x) = 1 $$

## CDF to PDF

The CDF is the anti-derivative of the PDF,

$$ f_X(x) = \frac{\mathrm d F}{dx} $$

Proof
: Recall that the anti-derivative is defined by an indefinite integral. The first axiom of probabilty implies that $f_X$ converges from towards the left $f(-\infty) \rightarrow 0$. Using this fact, the indefinite integral of $f_X(x)$ can be described by the left bound of $-\infty$ and an arbritrary right bound $x$.

    $$ \int f_X(x)~\mathrm dx = \int_{-\infty}^{x} f_X(x)~\mathrm dx = F(x)$$