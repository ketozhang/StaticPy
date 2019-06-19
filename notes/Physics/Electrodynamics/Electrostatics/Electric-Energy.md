---
title: Electric Energy
---

## Work

As usual, to speak of the amount of energy an object has you must define what work is. For the electric force work is simple in terms of the electric potential for a single charge being sent from $\boldsymbol r' = \infty$  to $\boldsymbol r' = \boldsymbol r$,

$$
W(\boldsymbol{r}) = \int_\infty^\boldsymbol{r} q\boldsymbol E \cdot \ \mathrm d \boldsymbol r'\\
\boxed{W(\boldsymbol{r}) = qV(\boldsymbol{r})}
$$

Where we set the origin $V(\infty) = 0$

For a continuous collection of charges one can see that as you add each charge to the collection, the following charge must overcome the potential of all previous charges. This is quite an iterative process which looks like,

$$
W = \frac{1}{4\pi\epsilon_0} \sum_{i}^n\sum_{j > i}^n{\frac{q_iq_j}{|\boldsymbol r_i| - |\boldsymbol r_j|}} = \frac{1}{2}\frac{1}{4\pi\epsilon_0} \sum_{i}^n\sum_{j \ne i}^n{\frac{q_iq_j}{|\boldsymbol r_i| - |\boldsymbol r_j|}}\\
W = \frac{1}{2}\sum_{i}^{n}{q_iV(\boldsymbol{r}_i)}
$$

We can easily convert this to continuous form

$$
\boxed{W = \frac{1}{2}\int{V(\boldsymbol{r})\ \mathrm dq}}
$$

In terms of the electric field,

$$
\boxed{W = \frac{\epsilon_0}{2}\int\limits_\mathrm{all}{|\boldsymbol{E}|^2\ \mathrm d\mathcal{V}}}
$$