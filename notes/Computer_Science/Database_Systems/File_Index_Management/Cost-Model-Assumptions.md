---
title: Cost Model Assumptions
---

* **B**: Number of data blocks in the file
* **R**: Number of records per block
* **D**: Average time to read/write disk to block
    * Ignore difference between sequential vs. Random I/O

## Assumptions

* Average case for uniform random workloads
* Ignore:
    * Sequential vs. Random I/O
    * Pre-fetching
    * Any in-memory cost

Further strict assumptions:

* Single record insert and delete
* Exactly one match for equality
* Heap files always append at end of file
* Sorted files are packed and sorted according to search key