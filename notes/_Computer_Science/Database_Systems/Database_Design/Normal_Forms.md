---
title: Normal Forms
---

## First Normal Form

All attributes are atomic such that each attribute cannot be broken down further.

* Known as the **relational models**

## Boyce-Codd Normal Form (BCNF)

For at table with functional dependencies is in BCNF if for all $X \rightarrow A$,

* $A \subseteq X$
* $X$ is a superkey for $R$

In other words, a table is in BCNF if there exist no attribute that is a functional dependency of another except for the trivial functional dependency of the key constraint.