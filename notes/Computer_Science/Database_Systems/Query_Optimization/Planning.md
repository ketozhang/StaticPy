---
title: Planning
---

# Left Join
The following optimizes a left join.

* Pushing selection down on the left
* Choosing the selection that reduce the left the most to be pushed down.
* Pushing any cartesian operator up.
* Create temporary tables from result of selection instead of doing things iteratively.
* Switch join algorithm (SNLJ, PNLJ, BNLJ)
* Cascade and push down projections.