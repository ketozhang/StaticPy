---
title: Pages
---

## Fixed Length Records
Pages will pack records (i.e., there is empty spaces between records)

* Record ID as a byte offset
    * Deletion requires repacking if deleted from the middle.
* Reocrd ID in a bitmap can be used to store free space in header of each record and the record ID is the number in page
    * Deletion is done by changing full to free space.

## Variable Length Records

Metadata is placed on the footer (hence no longer called the header).

* Slotted Page as Record ID
    * The first pointer (index 0) of Record ID starts from the right of the footer
    * Each pointer in the footer carries the length of the reference record
    * One pointer points to the free space immediately after the last record
    * Record ID = Length + Pointer
    * Deletion changes length to null
    * Insertions are appended after the last record, the footer then changes a null pointer to point to the record recording its size.
    * Fragmentation can occur since deletion may be made in the middle while insertions are always after the last record
        * Solution, defragmentation by reorganizing and update pointers back to sequential order
        * Defragmentation can be done either every deletion (eager) or when the page is full (lazy)
    * Footer size is also variable which grows right to left
    * Once a footer and a record meet, the page is considered full
    * May be used for fixed length records but its costly
    * **Size** is computed knowing the number of records $n$, the footer size (with pointer size, size to store offset, and a free space pointer), and the record size (with size of a single record)

        $$
        \begin{gather*}
            P = F + R\\
            F = (\texttt{pointer} + \texttt{offset}) \cdot (n + 1)\\
            R = \texttt{record_size} \cdot n
        \end{gather*}
        $$