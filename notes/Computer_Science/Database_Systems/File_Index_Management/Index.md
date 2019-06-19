---
title: Index
---

**Index** is a data structure that enables fast lookup and modification of data entries by search keys. Often times the index is stored with the data pages which the whole file is called an **indexed file**

Lookup
: A function  that may include equality, 1-d range, 2-d region, etc.

Search Key
: Any subset of columns in the relation. Search key does not need to be unique.

**Modification**
: Support for fast insert and delete

* We consider index as a tuple of search key and record ID serving as a pointer to the reference heap file.

##  Indexed Sequential Access Method

The **index sequential access method (ISAM)** is a  high fan out tree.

**Key Invariant**
: For node $[...,(K_L, P_L), (K_R, P_R),...]$, the parent node must be greater than or equal to nodes on the children to the right and less than the children to the left.

    $$K_L < K \le K_R$$

* **Search**
    * Time complexity of $O(\log_F(P))$ where $F$ is the fanout (the maximum number of pointers pointed to a single data page)
* **Insert**
    * Append to free space and resort
    * If there are no free space then a linked list is appended to the leaf page and becomes overflow (**major flaw**)

## B+ Tree

A similar tree to ISAM and improves some flaws of ISAM.

* Same interior node structure with key invariant
* Same search routine
* Dynamic tree index:
    * Always balanced
    * Support efficient insertion & deletion
    * Grows at root not leaves
* All data stored at the leaves (the B tree store at the nodes so B+ was named for this variant)

**Occupancy Invariant**
: Each interior node (excluding the root) is at least partly full:

    * $d \le |\text{node}| \le 2d$ where $d$ is the order of the tree and $|\text{node}|$ is the number of entries on a node.
    * The maximum fanout is
        $$ F_\text{max} = 2d+1 $$
    * The maximum number of entries in a single node is $2d$
    * The maximum number of records is given by its height $h$ ($\texttt{depth}-1$) and maximum number of entires $2d$,

        $$ |B|_\text{max} =  (2d+1)^{h-1} \cdot 2d$$

* Scan all and range are slower since the data linked list can be partially full.
* **Insertion**
    * If data/leaf node is full, split the node in half placing the middle number at the right half. Then, copy that middle number to the parent node. Sorting must be done at both instructions
    * If index node is full, split in half placing the middle number to the parent node.
    * If root is full, increase the height and follow the index node instructions.
* **Deletion**
    * Occupancy invariants don't need to be followed for deletion so there is no need for deletion unless a page becomes full.
* **Bulk Loading**
    * Multiple insertion is quite slow.
    1. Sort the input records by key
    2. Once page is filled with $d + 1$ (or occupancy of a node is equal to the fill factor), create the parent node.
    3. Continue until parent node is full where you need to split.
    * Bulk loading is faster, have leaves be stored sequentially, and you can control the fill factor (default $d + 1$) of the pages.

### Cost Model

* **Scan**

    During scanning, we ignore traversing the tree and go straight to the leaf nodes. The number of elements in all leaf nodes depends on the fill factor $f$. For $B$ data pages in the leaf node there are a total of $B/f$ pages,

    $$ C = \frac{BD}{f} $$

### Problems

1. **Maximum Number of Children**

    The number of children of any node is given by the fanout $F$,

    $$N_\text{chidren} = F = 2d + 1$$

1. **Number of Leaf Nodes For Given Height**

    The number of leaf nodes for a given height $h$ and fanout $F$ is given by,

    $$N_\text{leaf} = (N_\text{children})^h = F^h$$
1. **Maximum Occupancy For Given Height**

    The maximum occupancy (sum of the number of elements in the leaf node) is,

    $$
    \begin{align*}
        N &= N_\text{leaf} \cdot (F - 1) \\
        &= (F-1)F^h
    \end{align*}
    $$