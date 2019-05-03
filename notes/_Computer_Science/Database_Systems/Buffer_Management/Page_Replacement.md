---
title: Page Replacement
---

A page replacement takes note in the buffer whether or not the page to be replaced is either pinned or dirty.

* **Pinned Page**: A pinned page signify that the page is still being used.
* **Dirty Page**: If a dirty page was selected to be replaced that must mean the page must be written back to the disk before replacement.

1. Scan for unpinned page
2. Check dirty bit. If dirty write to disk.
3. Replace page and pin.

## Least Recently Used (LRU)

The LRU tracks when the page was last recently used (last unpinned).

* LRU ignores all pinned pages.
* Benefits from a buffer pool larger than the requested files.
* Very bad on sequential scan causing sequential flooding.

## Most Recently Used (MRU)
A counterintuitive policy opposite of the LRU.

* Only good for sequential scan and optimal for sequential flooding scenarios.
* For cases where the number of files requested is bigger than the buffer ($N > B$), the hit rate goes as,

    $$ \frac{B-1}{N} $$

## Clock Policy

Imagine the pages gathered in a circle.

* **Clock hand**: A pointer at the center pointing at the page it's currently scanning.
* **Reference bit**: Every page gets a reference bit that's either filled or empty.
* A page is replace if the clock hand points to the page and its reference bit is unfilled. All given that the page isn't  pinned.
* Once a new page is appended, we pin the page and the reference bit is filled.
* Because we don't need a comparator, the clock policy runs faster than LRU.

The clock policy is considered a second chance policy due to the reference bit.

The full algorithm would go as so:

1. Ignore the clock policy until the buffer is full.
2. Once full, place the clock hand at the first page inserted.
3. Insert a file:
    * If file exist in buffer, turn on the reference bit of that page but do not advance hand.
    * If file does not exist in buffer, check the page the clock hand pointed to. If the reference bit is on, turn it off and advance. If the reference bit is off, replace the page.
    * If a page is replace, place a pin and reference bit on the page. Advance the clock. **Never penalize the new page**.
