---
title: Sorting
---

## Streaming

Streaming is a strategy to have a function that maps input data from the database into the buffer and outputs it to the RAM and then loads it into the disk.

* **Single-pass:** Simply a single stream of input to output.
* **Double Buffering:** With two threads, one manages computation and the other manages loading and unloading the buffer.

## Divide and Conquer

### 2-Way Strawman Merge Sort

1. For each page, sort them in the buffer and write to disk
2. Now we will read from the disk which now has sorted pages and write this to another disk. We will allocate two input buffers to read two pages and merge them into one. Now the last buffer has two pages.
3. We continue this with four input buffers, merge then write. Then double up every step.

## Full External Merge Sort

We will now use the strawman sort much more efficiently. Instead of going back and forth we can fully sort $N$ pages with $B < N$ sized buffer.

1. Use $B$ size buffer to read $B$ pages. Continue to do so until $N$ pages are read. Read pages are placed in the allocated to an intermediate disk of $\lceil{N/B}\rceil$ buffers of size $B$.
2. In parallel for $B-1$ buffers, are merged and written to the final disk. The amount of block written is $B(B-1)$.
3. We continue another pass thru once all $\lceil N/B \rceil$ finish sorting.

* **Number of passes**:
    $$ 1 + \left\lceil \log_{B-1}\left\lceil \frac{N}{B}\right\rceil \right\rceil $$

* **Cost**:
    $$ 2N \cdot \#\text{passes} $$

*  **Two-pass Buffer Required**:

    $$ N = B(B-1) $$
    $$B \approx \sqrt{N}  $$

### Problems

1. **Number and Size of Partition**

    This question is easy when we have to preserve $N$ the number of pages we're sorting.

$$
\begin{gather*}
    N = (\#\text{partition})(\text{size of partition})\\
    N = P_i \cdot |P_i|\\\\
    P_i = \begin{cases}
        \lceil N/B \rceil & i = 0\\
        \frac{\lceil N/B \rceil}{(B-1)^i} & i > 0
    \end{cases}\\\\
    |P_i| = \begin{cases}
        B & i = 0\\
        B(B-1)^i & i > 0
    \end{cases}
\end{gather*}
$$

## Parallel Sorting

For $n$ machines we will have $n$ buffers with each buffer dedicated to a range of the data.

* We'd like each range to have the same amount of values from the data. However if the data is skewed, then this is a problem since one machine has more to do than the others.