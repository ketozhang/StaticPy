---
title: Introduction
---

The decision tree is a nonlinear method for classification and regression. The decision tree is a tree with two node types:

* Internal nodes for each features
* Leaf nodes for each class

## Tree Algorithm

The tree algorithm goes as follows:

1. Import all sample points at the top level calling the set of indices $S$
2. Case:
    * If all sample points belong to a certain class $y_i = c; \exists (c \in C)\forall (i \in S)$ then return a new leaf with class $c$. This is condition is called when the leaves are **pure**.
    * Otherwise choose a splitting feature $j$ and splitting boundary $\beta$ where we partition the class into left and right subsets:
        * $S_L = \{i : X_{ij} < \beta\}$
        * $S_R = \{i : X_{ij} \ge \beta\}$

Note that if the first case in step two succeeds then we have a classified all those points where $y_i = c$ as class $c$.

## Splitting Feature

Given $d$ splitting features indexed by $j \in \{1,2,\ldots,d\}$, there are a few way of choosing best splitting feature to implement in the second condition of the tree algorithm at step 2.

The most natural one would be to compute some loss fuction. Let $\mathcal L_j(S)$ be the cost function using splitting feature $j$. The best split can be chosen to be the one that has the least weighted average cost:

$$
d = \mathop{\arg\min}_{d} \frac{|S_L|\mathcal L_j(S_L) + |S_R|\mathcal L_j(S_R)}{|S_L| + |S_R|}
$$

Now the problem left is to choose a loss function. A heuristic choice is the cross entropy.

## Splitting Boundary

An algorithm of finding the bondary cost $\mathcal O(n \cdot d \cdot \texttt{depth})$. 

## Regression

Using decision trees to do regression requires choosing piecewise boundaries at every node. At the leaf you may get a subset of sample points which a single value can be outputted by taking some aggregate.

## Stopping Condition

The tree training algorithm can be stopped to:

* Limit tree depth
* Limit tree size
* Prevent overfit

The following are examples of stopping conditions
* Next split doesn't reduce entropy/error enough
* Most of the node points are in the same class
* Nodes contains few sample points
* Cell's edges are all tiny
* Depth is too great
* Validation performance does not improve.
* Pruning
    * Remove splits that the removal will improve cross-validation.

When a stopping condition is made the leaves may not be pure thus we need a decision rule for the unpure leaves:

* Return the majority (classification).
* Return the posterior probability.
* Return the aggregate (regression).