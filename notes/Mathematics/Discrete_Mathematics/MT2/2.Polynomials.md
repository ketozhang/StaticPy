---
title: Polynomials
---

The polynomials is a set of functions in the form,

$$ p(x) = a_0 + a_1x + a_2x^2 + \ldots + a_dx^d $$

* $d$ : Degree

## Properties

* **Roots**: A non-zero polynomial of degree $d$ has at most $d$ roots.

    Thus, we can write all polynomial as a product of roots $\lambda_i$ for some constant $c$.

    $$ p(x) = c(x-\lambda_1)\cdots(x-\lambda_d) $$

* **Uniqueness**: A set of points with unique $x_i$,

    $$
    \begin{gather*}
        \set{(x_i,y_i) | f(x_i) = y_i, ~ \text{unique } x_i}\\
        \abs{(x_i,y_i)} = d+1
    \end{gather*}
    $$

    Uniquely describes a polynomial of degree $d$

## Lagrange Interpolation

The second property of the polynomial can be interpreted as a set of pair of values where the $x$'s are unique of size $d+1$ can always be described by a polynomial of degree $d$. We can construct such polynomial by Lagrange interpolation:

### General Case

The general case of Lagrange interpolation is similar let's once again define,

$$ \Delta_i = \frac{\prod_{j\neq i}(x-x_j)}{\prod_{j \neq i} (x_i - x_j)} $$
$$ \Delta_i(x) = \begin{cases} y_i~, & x = x_i \\ 0~, & x = x_{j\neq i} \\ \text{arb.}~, & \text{otherwise} \end{cases}$$

The polynomial interpolation $p (x)$ is then,

$$\hat p(x) = \sum_{i=1}^{d+1} y_i \Delta_i(x) $$

## Coefficient Interpolations

Lagrange interpolation may be a pain so another method is to determine the $x$'s of $P(x)$ as a linear system of equations. Given that we have $d+1$ points ($\boldsymbol x$, $\boldsymbol y$) we can construct the matrix equation,

$$\begin{gather*}
    P(\boldsymbol x) =\boldsymbol y\\
    \big\Downarrow \\
    \left(\hat D\boldsymbol x\right) \boldsymbol a =\boldsymbol y
\end{gather*}
$$

* $\hat D$ : The polynomial expansion that takes in $\boldsymbol{x}$ and transform it into a $x \times d$ matrix.
* $\boldsymbol{a}$: The polynomial coefficients

## Polynomial Division
A polynomial $p(x)$ can be described by the divsion by a divisor $q(x)$, the  quotient $q'(x)$ and the remainder $p(x)$,

$$ p(x) = q(x)q'(x) + r(x) $$

The degree of $q(x)$ is $\le d$ and the degree of $r(x)$ is $<d$

## Modular Polynomials
Let $p$ be a prime number such that the modular space forms a field $\mathbb F_p$. In fields many properties in real space acts the same in fields.

* The number of polynomials of degree $d$ in $\text{mod } p$ is,

    $$ p^{d+1} $$

* The number of polynomials of degree $d$ that goes through $k$ points for $k \le d+1$ is,

    $$ p^{d+1-k} $$

## Secret Sharing

The criteria for secret sharing is:

There are $n$ generals to share a secret $s \pmod p$ (for $p$ is a large prime). If there are $k$ generals then the secret can be revealed otherwise not.

To do so:

1. Construct a random polynomial $p(x) \pmod p$ of degree $d = k-1$ such that $p(0) = s$
2. Give each general the value $p(i)$ where $1 \le i \le k$
3. If at least $k$ generals come together, then by Lagrange interpolation $p(x)$ thus $s=p(0)$ can be revealed.