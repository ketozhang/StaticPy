---
title: Introduction
---

We will focus only on hard disk drives when speaking of disks.

The disk space management is the lowest layer of DBMS which manages space on disk.

* Map pages to locations on disk
* Load pages from disk to memroy
* Save pages back to disk & ensuring writes

Higher level can call the following API

* Read/write a page
* Allocate/de-allocate logical pages

## Block Level Storage

* Read and Write large chunks of sequential bytes
* **Sequential**: Access of a neighboring disk block. Access of sequential blocks are fastest
* Prediction increases performance
    * Cache popular blocks
    * Buffer writes to sequential blocks

Block
: A unit of transfer for disk read/write

    * Typically 64KB or 128KB

Page
: A synonym for block

    * Sometimes used for block-size chunk in RAM

* The **next** or **neighboring block** is any of the following:
    * Same track but the block immediately after
    * Same cylinder but different disk
    * Adjacent cylinder

## Implementation

DPM are implemented with the OS' file system.

* Allocate single large "contiguous" file on a nice empty disk, and assume sequential/nearby byte access are fast
* Most FS optimize disk layout for sequential access
* "DBMS file" may span multiple FS files on multiple disks/machines
