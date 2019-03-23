---
title: Modular Arithmetic
---

The statement "$a$ modulo $b$" is how many learn modular arithmetic which treats $\text{mod}$ as an operator like,

$$
\begin{gather*}
   r = a \bmod b \\
    \big\Downarrow \\
    a = bc + r
\end{gather*}
$$

This notation suggest that when $a / b$ there exist a remainder $r$ for $c$ is some integer.

A more formal way of writing this is to treat $\text{mod}$ as a space called the **modular space**. In this notation it means that the remainder $r$ and the dividend $a$ are congruent in the space of $\bmod b$.

$$
    \begin{align*}
    r &\equiv a \pmod b \\
    &\big \Downarrow \\
    a - &r = bc
\end{align*}
$$

Here we say that $r$ and $a$ are congruent modulo if they have the same remainder (note $r \bmod b = r$).

* All values in $\bmod m$ lives in the set $\set{0, \ldots, m-1}$


## Rules
Modulo arithmetic has the basic rules of arithmetic except for the divison operation.

* $(x + y) \bmod a \equiv (x \bmod a) + (x\bmod a)$
* $(x y) \bmod a \equiv (x \bmod a) \cdot (x\bmod a)$

## Division and Inverses
For divison, it gets complicated and we wish to preserve the rule of **multiplicative inverse** which states that,

$$
\begin{gather*}
    x \cdot y \equiv 1 \pmod m \\
    \big \Downarrow \\
    x \equiv \frac{1}{y} \pmod m
\end{gather*}
$$

For $x$ and $y$ inverse of each other.

* Inverses doesn't exist because it only exist if say for a fixed value $x$ and varying value $y$,

    $$ x \cdot y = c\cdot m + 1 $$

* The statement above can be quite difficult to solve since there are two varying parameters ($c$ and $y$). However the statement above is equivalent to,

    $$ \forall x \exists y \Big[(xy) \bmod m = 1 \iff \gcd{(x,m)} = 1  \Big] $$

    This statement's RHS is equivalently _**"$x$ is a coprime of $m$"**_

* If the modular space value $p$ in $\pmod p$ is prime then there always exists an inverse,

    $$ \forall x \forall p \in \text{prime 0} \exists y \Big( x\cdot y \equiv 1 \pmod{p}  \Big) $$

### Euclid's Algorithm

The Euclid's algorithm begins with assuming that the gcd can be written as a linear combination of $x, y$,

$$ \gcd(x,y) = ax + by $$

Where $a$ and $b$ are integers (remember, it's possibly negative). It's not a surprise that we can find,

$$
\begin{align*}
    am + bx &= 1 \\
    &\big\Downarrow \\
    bx &\equiv 1 \pmod m
\end{align*}
$$

We now see that $b$ is the inverse of $x$. So all we need to do is fine $a$ and $b$. To do that we need to know the gcd. This is where Euler's algorithm comes in,

_**Theorem:** $x \ge y > 0 \implies \gcd(x,y) = \gcd(y,x\bmod y)$_

1. Take the smaller value $y$ to be the mod space.
2. Continue Euclid's theorem until one of the input variables is zero
3. When an input variable is zero the gcd is simply the non-zero value,

    $$
        \begin{align*}
            \gcd(x,y) &= \gcd(y,x \bmod y)\\
            &= \ldots \\
            &= \gcd(d,0)\\
            &= d
        \end{align*}
    $$

Now we are going to use this for $\gcd(x,y) = ax + by$,

$$
    \begin{align*}
        d &= ay + b(x \bmod y)\\
        d &= bx + \left(a-\left\lfloor\frac{x}{y}\right\rfloor b\right)y
    \end{align*}
$$

## Negation
Unfortunately negation is not like basic arithmetic. For instance,

$$
\begin{gather*}
    4 \bmod 3 = 1\\
    -4 \bmod 3 = 2
\end{gather*}
$$

The relation for negation is simple,

$$
\begin{align*}
    -a \bmod b &= b - (a \bmod b)\\
    &= (b-a) \bmod b
\end{align*}
$$