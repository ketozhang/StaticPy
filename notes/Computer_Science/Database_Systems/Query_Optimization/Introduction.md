---
title: Introduction
---

## Query Parser

The query first gets parsed:

* Check for correctness and authorization
* Generate a parse tree

## Query Rewriter

Rewrites query to its canonical form,

* Flatten views
* Subqueries into blocks
* The weak spot of many DBMS

## Query Optimizer

Creates the plan and estimates the cost.

* Per query block, the optimizer will use the least cost plan.
* Query block can be converted to relational algebra.
* Relational algebra to tree.
* Each operator has a choice of implementation.
* Operators can be applied in different orders.