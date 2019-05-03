---
title: Storage Hardware
---

Storage on hardware for DBMS differs from CPU architecture by:

* No pointer dereferences, API is used instead:
    * READ: Transfers a page of data from disk to RAM
    * WRITE: Transfers a page of data from RAM to disk
* Very slow API calls
* Minimizes pointer errors

## Magnetic Disk (HDD)

Still in use today because how cheap it is.

Platter
: The assortment of disks in an HDD

Arm Assembly
: Move in or out the **head** to a **track**

Sector
: A fixed amount of data taking the space of a arc sector of a disk.

### Accessing Disk

Seek time
: Time it takes to move disk head on track
    * 2-3 ms

Rotational delay
: Waiting for block to rotate under head to the right place
    * 0-4 ms

Transfer time
: Moving data from disk surface
    * ~0.25 ms per 64KB page

## Flash Memory (SSD)

Let's focus on NAND technology,

    * Fine grain reads (4-8k reads), course-grain write (1-2 MB writes)

* **Pros: **
    * SSD is fast read and predictable with writes being slower (i.e., random 4K writes).
* **Cons: **
    * Only 2k-3k erasures (i.e., multiple writes), the cell will fail.
    * Slows down from
        * Wear leveling (preventing a cell from multiple writes)
        * Write amplification (movement of data from cell to cell)
        * Writing a single unit may require multiple units in order to move units around
        * Large transfer sizes