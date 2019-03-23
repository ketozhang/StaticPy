---
title: Countability
---

## Bijection

Two sets $A$ and $B$ have the same size if there exists a function $f : A \rightarrow B$ is a bijection. A function is bijection if and only if:

1. $f$ is injective (one to one)

    $$ a_1 \neq a_2 \implies f(a_1) \neq f(a_2) \qquad (\forall a_1,a_2 \in A) $$
    $$ \abs{A} \le \abs{B} $$

2. $f$ is surjective

    $$ f(a) = b \qquad (\forall b \in B,~\exists a \in A) $$
    $$ \abs{A} \ge \abs{B} $$

* A function is also a bijection if an inverse function exists.
* In an infinite set even if $A \subset B$ the cardinality $\abs{A} = \abs{B}$ as long as there exists a bijective function between them.

### Proving Bijections

1. **Find a identity mapping**
    $$ f(a_i) = b_i $$
2. **Find an offset mapping**
    $$ f(a_{i} = b_{i+1}) $$
3. **Find an alternating mapping**
    $$ f(a_{i}) = \begin{cases} b_\text{odd} & i\text{ is odd}\\ b_\text{even} & i\text{ is even} \end{cases} $$
4. **Cantor-Bernstein Theorem**

    If there exists an injection for $A \rightarrow B$ and for $B \rightarrow A$ then there exists a bijection between $A$ and $B$.

    Unfortunately this method is hard to do.

## Countable

A set is **countable** if there exists a bijetion between $S$ and $\mathbb N$ or some subset of $\mathbb N$. Equivalently, a set is **countable** if there exists an injection between $S$ and $\mathbb N$ (an onto relationship for $f: S \to A$ for $A \subseteq N$). This is simply denoted as,

$$ S \longrightarrow N \implies |S| \le |N| $$

The following set are countables:

1. Natural numbers $\mathbb N$
1. Rational numbers $\mathbb Q$
1. A string of $n$ radix $\set{0,1,2,\ldots,n-1}^*$

The following set are not countable:

1. Real numbers $\mathbb R$
2. The power set of the natural numbers $\mathcal P(\mathbb N)$

## N-Radix Strings

For a positive integer $N$, $N$-radix string denoted as $\set{0,1,\ldots,N-1}^*$ is countable and has a bijection to $\mathbb N$

$$ \set{0,1,\ldots,N-1}^* \longleftrightarrow \mathbb N $$

N-radix strings become useful if you can encode some set $\mathbb N(x) $ with $N$ radices (aka indices). Doing so allow an injection from $\mathbb N(x) \rightarrow \set{0,1,\ldots,N-1}^*$ thus,

$$
\begin{gather*}
    \mathbb N(x) \rightarrow \set{0,1,\ldots,N-1}^* \longleftrightarrow \mathbb N \\
    \downarrow
    \mathbb N(x) \rightarrow \mathbb N
\end{gather*}
$$

### Binary Strings

Let's start out with considering a 2-radix string (i.e., binary string). We may denote all possible binary string as the set,

$$ \set{0,1}^* : \emptyset, 0, 1, 00, 01, 10, 11, \ldots $$

* Notice that $0$ and $00$ are not equal (even thought they represent the integer $0$ in binary).

### Ternary String

The more useful string is the ternary string $\set{0,1,2}^*$. We can use $1$ and $0$ to build the integer and $2$ as a delimiter.

* For instance the polynomial $5x^24 + 2x^4 + 7x^3 + 4x + 6$ can be presented as,

    $$ 1012~~102~~1112~~2~~1002~~110 $$

    With this we can prove that the set of all integer coefficient polynomials are countable.

### Uncountability by Cantor's Diagonalization

A set $S$ is uncountable if the diagonal of the row sets $f(1), f(2), f(3), \ldots, f(n)$ for $f: S \rightarrow \mathbb N$ generates another row set not in $f$ then the set is not countable.

* **$\mathbb R$ is not countable**

    We continue to prove this by showing that that interval $\mathbb R[0,1]$ is not countable. Using Cantor's theorem, we see that $\mathbb R \rightarrow \mathbb N$ now we can test on $\mathbb N \rightarrow \mathbb R$

    To do this, let's assume for contradiction that the interval is countable $N \rightarrow \mathbb R [0,1]$. That means for every $n \in \mathbb N$ $f$ is a bijection function that maps to every real number denoted as $0.d_1d_2d_3\ldots$,

    $$
    \begin{matrix}
    f(0) = 0.&\boxed{9} &8  &7  &\ldots\\
    f(1) = 0.&8   &\boxed{7}  &6    &\ldots\\
    f(2) = 0.&7 &6    &\boxed{5} &\ldots\\
    \vdots & \vdots
    \end{matrix}
    $$

    Let the diagonal be another decimal number $r=0.975\ldots$ and take each digit $d+2 \bmod 10$ such that $s=0.197\ldots$

    We know for sure that $s$ does not exist in the table since every digit differs from each row. However, this contradicts $\mathbb N \rightarrow \mathbb R$ thus $\mathbb R$ is not countable.

* **No power set are countable**
    We prove this by proving that $\mathscr{P}(\mathbb N)$ is not countable. We do this by contradiction assuming there exists an injection from $N \rightarrow \mathscr{P}(\mathbb N)$. We may denote all power set as a binary string with the mapping bijective function $f$. Let the $i$th position of the string denote each natural number. Let $1$ denote that the natural number is present in the set and $0$ means not.

    $$
    \begin{matrix}
               &0   &1   &2   &\ldots\\
        f(0)   &\boxed 0   &0   &0   &\ldots\\
        f(1)   &1   &\boxed 0   &0   &\ldots\\
        f(2)   &1   &1   &\boxed 0   &\ldots\\
        \vdots  &&\vdots
    \end{matrix}
    $$

    Flipping every bit along the diagonal we get the binary string $b$. $b$ should be part of the power set however this isn't possible since every row should be different from $b$. This contradiction shows that $\mathscr P (\mathbb N)$ is not countable.