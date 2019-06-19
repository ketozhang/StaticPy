---
title: Join Operators
---

A single I/O in the operator model includes:

* Accessing the page or record (whichever highest)

Exclude:

* Predicate comparison

## Syntax

* $[L]$: Number of pages to store $R$
* $p_R$: Number of records per page of $R$
* $|R|$: The number of records in $R$

    $|R| = p_R [L]$

## Theta Join
* **Simple Nested Loops Join**

    ```py
    for r in R.records:
        for s in S.records:
            <pred>
    ```
    Consider joining two table with records labeled $R$ and $S$ respectively with an on clause. The cost is,

    $$ [L] + |R|[R] $$

* **Order of Join**

    Take note of the order you join. It may be cheaper doing $S$ join $R$ than $R$ join $S$.

* **Page Nested Loop Join**

    ```py
    for r in R.pages:
        for s in S.pages:
            for records_r in r:
                for records_s in s:
                    <pred>
            <pred>
    ```
    Instead of scanning each record of $R$ to a page of $S$ we yse page of $R$

    $$ [L] + [L][R] $$

* **Chunk Nested Loop Join**

    We will chunk the records into $B-2$ pages.

    $$ [L] + \left\lceil{\frac{[L]}{B-2}}\right\rceil \cdot [R] $$

* **Index Nested Loop Join**

    * Unclustered
        $$ [L] + |R| * (\texttt{Search} + \texttt{HeapAccess}) $$
    * Clustered
        $$ [L] + |R| * \texttt{Search} + \texttt{HeapAccess} \cdot \texttt{distinct_vals(R)} $$

## Sort-Merge Join

A sort-merge join is a join using lexographical ranges which has an equality join with less cost than purely doing a cartesian join.

```py
if (not mark):
    while (r<s): r++
    while (r>s): s++
    mark = s
if (r==s):
    result = (r,s)
    s++
    return result
else:
    s = mark
    r++
    mark = NULL
```

The cost using $B = \sqrt{\max{[L],[R]}}$ is,

$$\texttt{Sort}(R) + \texttt{Sort}(S) + ([L] +[R])$$

### Improvement

We can increase the buffer to $B = \sqrt{[L]} + \sqrt{[R]}$ and first sort both $R$ and $S$ simultaneously then at the last pass merge while finding pairs. The cost for this is,

$$ (\#\text{passes} - 1)([L] + [R]) $$

## Hash Join
We wish to join two tables $R$ and $S$ by comparing their hash.

### Naive Hash Join
Assuming $B < [L]$, we can create a big enough buffer to compare the hashes between $R$ and $S$ by creating a hash table of size $B-2$ (the remaining 2 is taken up by storing $R$ and $S$).

* **Cost**

    $$[L] + [R]$$

* **Buffer Management**
    $$B$$

### Grace Hash Join

Using external hashing, for every pass we can take the partition and do **Build & Probe** which is a pass that uses naive hash join on the partition

For each partiton:

1. Load pages of $R$ into the input buffer
2. Store input buffer to hash table
3. Repeat steps 1-2 until no more $R$ pages
4. Store pages of $S$ into the input buffer
5. Search the hash table for match. Write matches to output
6. Continue until no more $S$. Remember to flush out the output if full.

* **Cost**:
    $$ 3([L] + [R])$$
* **Buffer (2-Pass)**
    $$ [L] = (B-1)(B-2) $$