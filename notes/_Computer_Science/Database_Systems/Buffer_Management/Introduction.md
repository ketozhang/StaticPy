---
title: Introduction
---

The buffer management handles interactions between the RAM and the disk. It creates the illusion that the file system is always working with the RAM. The buffer management handles read/write request passed to the RAM and in which decides if it needs to interact with the disk.

From now on the faster storage right above the disk is called the buffer pool. The buffer pool is commonly the ram.

## Buffer Initialization

1. DBMS server boots
2. Buffer allocates a chunk of the memory for the buffer pool.
3. A part of the buffer pool stores the metadata of the database.

## Dirty Pages
A page in the buffer pool is considered dirty if any changes was made to the page in the buffer pool.
