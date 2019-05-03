---
title: Exponential Decay Distribution
---

The exponential decay distribution is a continuous distribution,

$$ f_X(x) = \lambda e^{-\lambda x}~, \qquad x \ge 0 $$

$$ P(X>x) = e^{-\lambda x} $$

* Continuous analogy to the geometric distribution.
* Often used to answer "probability that event occurs above at time $t>x$"
* $\lambda$ : Interpet as the probability frequency of the event.

    You can see this setting $x = 1/\lambda$ then $P(X>x) = 1/e$. So $1/\lambda$ is the period to decrease the probability that $P(X>x)$ by a factor of $e^{-1}$.

* **Memoryless Property:**

    $$ P(X > a + b \mid X > a) = P(X > b) $$