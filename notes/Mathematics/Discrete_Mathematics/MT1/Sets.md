---
title: Set
---
A set (notated as a capitalized letter) is a collection of objects called elements or members.

## Notation

* Element $x$ is in set $A$:

$$
x \in A
$$

* Element $y$ is not in set $A$

$$
y \notin A
$$

* Set comprehension are denoted after the vertical line $\{\ \vert\ \}$

$$
\set{ab \mid a,b \in \mathbb{Z}}
$$

## Special Sets
There are some sets denoted as blackboard bold capital letters that are reserved for special sets:

* $\mathbb N$ : Natural numbers (alternatively $\mathbb Z^+$)
* $\mathbb Z$ : Integer numbers
* $\mathbb Q$ : Rational numbers
* $\mathbb R$ : Real numbers
* $\mathbb C$ : Complex numbers

Others:

* $\Box ^+$ or $\Box^-$: Positive/negative set of $\Box$
* $\mathbb R \backslash \mathbb Q$ : Irrational numbers

## Cardinality

The **cardinality** of a set is the length of the set denoted as $\abs{A}$.

* If $\abs{A} = 0$ then $A$ is an **empty set** ($A = \emptyset$)

## Set Comparison

There are three types of comparison between sets:

**Intersection**
: An intersection is the set of elements shared between two sets:

    $$
    A \cap B
    $$

    * If $A \cap B = \emptyset$ then the two set are **disjoint**

**Union**:
: A union is the set of elements joined by two sets:

    $$
    A \cup B
    $$

**Difference**
: The set **difference** or **relative complement** between two sets:

    $$
    B - A\\
    B \setminus A \\
    $$

## Subset

If every element in set $A$ is also in set $B$ then we consider $A$ a **subset** of $B$,

$$
A \subseteq B
$$

A set is $A$ is a **proper subset** of set $B$ if $A \subseteq B$ and $A \ne B$. This is denoted as,

$$
A \subset B
$$

## Cartesian Product

The **Caretesian product** or **cross product** of two set is a set containing the pairs of all elements in one set to another.

$$
A \times B = \set{(a,b) \mid a \in A, b \in B}
$$

For instance if $A = \set{1,2}, B=\set{a,b}$ then:

$$
A\times B = \set{(1,a), (1,b), (2,a), (2,b)}
$$

## Power Set

The **power set** is the set of all subsets or defined as,

$$
\mathscr{P}(S) = S: \set{T \mid T \subseteq S}
$$

* The length of a power set is $2^k$ where $k$ is the length of the original set or,

$$
\abs{\mathscr{P}(S)} = 2^{\abs{S}}
$$