---
title: Logic
---

## Proposition
A proposition is a mathematical statement that is either True or False. In math, we do not focus on propositions that are vague either because the proposition contains a vague term or the answer can vaguely either be True or False.

## Notation

**Conjunction / And**
:
    $$
    P \land Q
    $$

**Disjoint / Or**
:
    $$
    P \lor Q
    $$

**Negation / Not**
:
    $$
    \neg P
    $$

**Implications**
: "$P$ implies $Q$" is the same as "if $P$, then $Q$" and is denoted as,

    $$
    P \implies Q \equiv \neg P \lor Q
    $$

    * An implication is only false if $Q$ is false and $P$ is true.

    * If $P$ is false, then the implication is always true.

    * If $P \implies Q$ and $Q \implies P$ then this means "$P$ if and only if $Q$" in notation,

        $$P \iff Q$$

        The advantage of IFF is that if $P$ then it must be that $Q$ is true.

| $P$ | $Q$ | $P\implies Q$  |
|---|---|:---:|
| T  | T  | T  |
| T  | F  | F  |
| F  | T  | T  |
| F  | F  | T  |


Here $P$ is the **hypothesis** and $Q$ is the **conclusion**

## Logical Truths

* **Truth Table**: For every logical statement, a truth table can be made
* **Logically Equivalent** : Two logical statement are considered logically equivalent if the truth table are the same. This is notated as,

$$
(P) \equiv (Q)
$$

* **Vacuously True**: A statement is vacuously true when an implication is stupidly true because the hypothesis is false

## Contrapositive and Converse

Contrapositive
: The contrapositive is the negation of both propositions:

$$ \neg Q \implies \neg P $$

Converse
: The converse is the flip if the implication,

$$ Q \implies P $$

## Universal and Existential Quantifiers

**For all**
: The symbol $\forall$ denotes the statement "for all $\ldots$"

A full statement with a logical statement $P$ is used as so:

$$
\forall x P
$$

This means $``$For all $ x\ P"$ where $ x$ is often some set

**There exists**
: The sybmol $\exists$ denotes the statement "There exists $\ldots$".

The relationship between $\forall$ and $\exists$ statement is given by a negation relationship,

1. If there exists $x$ where $P(x)$ is false, then not all $x$ makes $P(x)$ true
$$
\neg(\forall x P( x)) \equiv \exists x \neg P( x)\\
$$

2. If all $x$ where $P(x)$ is false, then there does not exists $x$ where $P(x)$ is true
$$
\neg(\exists x P( x)) \equiv \forall x \neg P( x)
$$

## De Morgan's Laws

1. If "$P$ and $Q$" is false then "$P$ is false or $Q$ is false"

    $$
    \neg (P \land Q) \equiv (\neg P \lor \neg Q)
    $$

2. If "$P$ or $Q$" is false then "$P$ is false and $Q$ is false"

    $$
    \neg (P \lor Q) \equiv (\neg P \land \neg Q)
    $$

4. If "for all $x$, $P(x)$ is false" then "there must exist an $x$ that makes $P(x)$ false":

    $$\neg(\forall x P(x)) \equiv \exists x (\neg P (x))$$

5. If "there does not exist an $x$ that $P(x)$ is true" then "for all $x$, $P(x)$ is false"

    $$\neg(\exists x P(x)) \equiv \forall x (\neg P(x))$$

The De Morgan's laws can be summarize to fully describe the negation operator $\neg$ such that:

$$
\begin{align*}
    \neg \land \equiv \lor\\
    \neg \lor \equiv \land\\
    \neg \forall \equiv \exists\\
    \neg \exists \equiv \forall
\end{align*}
$$

---

## Summary
This notes comprise of:

* Logical symbols

    | Symbol            |             |
    | ----------------- | ----------- |
    | $\land$           | and         |
    | $\lor$            | or          |
    | $\lnot$           | not         |
    | $\Longrightarrow$ | implies     |
    | $\equiv$          | Equivalence |


* Implications are not as intuitive as one may think. Since implication is only false if the then statement is false while the if statment is true.

    $$ P \implies Q \equiv \lnot P \lor Q $$

* De Morgan's Law is the property of negating a logical statement. It can be summarized to:

$$
\begin{gather*}
    \lnot\land \equiv \lor\\
    \lnot\lor \equiv \land\\
    \lnot\forall \equiv \exists\\
    \lnot\exists \equiv \forall
\end{gather*}
$$