---
title: Hashing
---

## Divide and Conquer

We assume $N \le B$

First the divide step:

1. Read and store to an input buffer
2. Apply hash function $h_p$
3. Output to $B-1$ output buffers.
4. $B-1$ partition generated written to disk.

Then conquer:

1. Read the hashed disk into buffer with another hashing function $h_r$
2. Write to another disk.

* **Cost:**
    $$ 2N \cdot \# \text{passes} = 4N $$

* **Two-pass Memory Requirement:**
    $$ B = \sqrt{N} $$

## Recursive Partitioning.

For partition that is $> B$

1. Follow the same steps as divide
2. Continue divide on the disk with a difference hash function $h_p$
3. Once each partition is $\le B-1$ then we perform conquer with $h_r$

* If a partition is full of the same keys, then the division hash would be useless. We're required to identify these cases and stop dividing.

## Parallel Hashing

For $n$ machines we can take the data of all its disk and partition them into $n$ buffers. Each data is hashed with $h_n$ and the value will decided which machine the data belongs to.