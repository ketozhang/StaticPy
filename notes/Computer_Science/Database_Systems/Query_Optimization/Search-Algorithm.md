---
title: Search Algorithm
---

## Dynamic Programming
We will implement dynamic programming (implementation changes depending on input and query) with the idea of principle of optimality.


* **Principle of Optimality**: The best overall plan is composed of best decision of the sub plans
* From the lowest height we find the best plan and combine it with the plan before it.
* Plans are stored in a lookup table. Each field in the lookup table corresponse to a pair of tables, the best plan, and the cost.
    * To implement physical property of some joins which may not be the best plan for the subplan but best for another (e.g., sortmerge outputs sorted table which may be useful for another subplan), we can add the same pair of tables along with the ordering of the columns and the plan that orders them.
* Cartesian products are ignored on some plan $i$ until:
    * There is a joint condition between them, **or**
    * All `WHERE` clause are used up by previous plans.