---
title: Conditional Probability
---

A conditional probability can be generalized by the phrase.

<center> **"What is the probability of y given x"** </center>

Which is defined with the **division rule** and notated as,

$$ \boxed{P(y \mid x) \equiv \frac{P(x\cap y )}{P(x)}} $$

* $P(x\cap y)$ : The joint probability of both $x$ and $y$ occuring
* The RHS comes from an axiom of probability.

## Bayes' Rule
**Bayes' rule** (or **Bayes' Theorem**)  describes the probability of two relating events $x$ and $y$. If we have information on _a priori_ (i.e., first event) then we can more accurately determine the probability of _a posteriori_ (i.e., second event)

$$
\boxed{P(y \mid x) = \frac{P(x \mid y) P(y)}{P(x)}}\\
$$

* $P(y \mid x)$ : **Posterior**
* $P(y)$ : **Prior**

* The denominator is called the **marginal probability** which is given by,

    $$
        P(x) = \sum_{y \in Y}{P(x \mid y)P(y)}
    $$


* The numerator is the joint probability between $x$ and $y$
    $$
        P(x \cap y) = P(x \mid y) P(y)
    $$

    Once again the $x$ and $y$ can be swapped since $x \cap y = y \cap x$

* Plugging in the marginal probability and the joint probability, we see that the conditional probability is the joint probability normalized by the marginal.

    $$ P(y \mid x) = \frac{P(x \cap y)}{\sum_\limits{y\in Y} P(x \cap y)} $$

* **Uniform Distribution:** Like before, when each event in the outcome space are equally likely then the conditional probability is,

$$ P(A\mid B) = \frac{\abs{A \cap B}}{\abs B} $$
