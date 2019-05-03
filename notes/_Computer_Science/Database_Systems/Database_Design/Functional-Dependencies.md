---
title: Functional Dependencies
---

A functional dependence betweeen two attributes $X$ and $Y$ are notated as $X \rightarrow Y$. This implies for any two rows $r_1$ and $r_2$ in the table,

$$ \pi_X(r_1) = \pi_X(r_2) \implies \pi_Y(r_1) = \pi_Y(r_2) $$

## Keys

Functional dependency plays a role on the definition of keys.

* **Superkey**:
A set of keys $K$ that determine the rest of the columns in the table.

$$ K \rightarrow \text{all attributes} $$

* **Candidate Key**
A minimal set of keys $K$ that such that for $L \subset K$

$$ L \not \rightarrow \text{all attributes} $$

* **Primary Key**
A single candidate key.

## Armstrong's Axiom

1. Reflectivity: $X \supseteq Y \implies X \rightarrow Y$
2. Augmentation: $X \rightarrow Y \implies XZ \rightarrow YZ$
3. Transitivity: $X \rightarrow Y \land Y \rightarrow Z \implies X \rightarrow Z$

In corollarly,

* Union and Decomposition: $X \rightarrow Y \land X \rightarrow Z \iff X \rightarrow YZ$