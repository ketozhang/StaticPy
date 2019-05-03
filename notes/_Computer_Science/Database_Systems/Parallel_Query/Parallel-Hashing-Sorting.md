---
title: Parallel Hashing and Sorting
---

## Hash Join

We first distribute the workload with $h_n$ and apply the divide phase. Then we continue with the next phase locally.

* Two tuples that need to join always end up at the same machine

## Sort-Merge Join

* Partition data by range at pass 0
    * To prevent data skew, we must determine the distribution. This can be done efficiently with random sampling.
* Remaining pass are local.

## Symmetric Join

We can add symmetry to either hash or sort join to allow for a paralleled pipeline that's always streaming. We do this by doing a local merge on both $R$ and $S$ as the input comes.