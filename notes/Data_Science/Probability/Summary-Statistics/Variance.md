---
title: Variance
---

## Variance

$$\text{Var}[X] = \mathbb E\left[ (X-\mu)^2 \right]$$

* More useful identity:

    $$\text{Var}[X] = \mathbb E[X^2] - \mathbb E[X]^2$$

* Sum

    $$\text{Var}\left[\sum X_i\right] = \sum \text{Var}[X_i] + \sum_{i \neq j} \text{Cov}[X_i,X_j]$$

    If all random variable are independent:

    $$\text{Var}\left[\sum X_i\right] = \sum \text{Var}[X_i] $$

## Covariance

### Properties

* Positive covariance:

    $$
    \text{Cov}[X,Y] > 0 \implies \abs{X - E[X]} > 0 \land \abs{Y - E[Y]} > 0
    $$

* Negative covariance:

    $$
    \text{Cov}[X,Y] > 0 \implies \Big( \abs{X - E[X]} > 0 \land \abs{Y - E[Y]} < 0 \Big) \lor \Big(\abs{X - E[X]} < 0 \land \abs{Y - E[Y]} > 0 \Big)
    $$

* Bilinearity:

    $$
    \text{Cov}[\boldsymbol{a \cdot X}, \boldsymbol{b \cdot Y}] = \sum_{i}\sum_{j}a_ib_j \text{Cov}[X_i,X_j]
    $$

## Correlation

### Properties

* **Standardized Random Variables**
    With standardized random variables $X'$ and $Y'$:

    $$ X' = \frac{X - \mathbb E[X]}{\sigma(X)} $$
    $$ Y' = \frac{Y - \mathbb E[Y]}{\sigma(Y)} $$

    $$ \text{Corr}[X,Y] = E[X'Y']  $$

* **Unity Bound**

    $$ -1 \le \text{Corr}[X,Y] \le 1 $$

    Proof
    : Consider the standardize random variable $X'$ and $Y'$. By the Cauchy-Schwarz Inequality

    $$ \abs{\mathbb E[X'Y']} \le \abs{\mathbb E[X'] \mathbb E[Y']} = 1$$

    Thus,

    $$ -1 \le \text{Corr}[X,Y] \le 1  $$

* **Perfectly Correlated or Anticorrelated**

$$ \text{Corr}[X,Y] = 1 \implies X = Y $$
$$ \text{Corr}[X,Y] = -1 \implies X = -Y$$
