---
title: Inter-Operator Parallelism
---

## Types of Partitioning

Shared data can be partitioned in three ways by:

1. **Range**
    * Great for equijoins, ranged queries, and group by
2. **Hash**
    * Great for equijoins and group by
3. **Random (Round-Robin)**
    * Good for spreading load

## Queries

* **Scan**
    * Scan in parallel and merge before output
    * $\sigma_p$ skip entire machines that has no tuples satisfying $p$
* **Search by Key**
    * If data partitioned by range of key then use only that machine
    * Otherwise have every machine do lookup.
* **Insert**
    * If partitioned by key, then insert there
    * Otherwise insert anywhere
    * If the key field is unique then check everything.