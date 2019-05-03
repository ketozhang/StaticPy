---
title: Introduction
---

## Single Hidden Layer

Adding a single hidden layer, the math gets quite verbose. It is easier to treat an input to a node as a transformation matrix $T$. For the single hidden layer NN, there are two transformations $T^{(1)}$ and $T^{(2)}$.

Let's begin with a single sample $x \in \mathbb R^{d}$. At every step along the way we will always add the ficticious dimension of value 1 for the intercept.
* $T^{(1)}$ takes in $x$ as $d+1$ input nodes and outputs $h \in \mathbb R^{m}$
* $T^{(2)}$ takes in $h$ as $m+1$ nodes and outputs $z \in \mathbb R^{k}$