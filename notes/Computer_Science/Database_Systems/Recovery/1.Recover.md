---
title: Recovery
---

## Disk & Buffer Management

A naive policy implements the following:

* **No Steal Policy**

    Don't allow buffer-pool frames with uncommited updates to be replace (pin those pages)

    * No need for UNDO logging
    * Cause bad performance taking up buffer

* **Force Policy**

    Force all updates onto the  disk before commit.
    * No need for REDO logging
    * Bad performance (random I/O writes  for commits)

What we actually want is the opposite.

* **No Force Policy**

    Flush as little as possible to a REDO log prior to commit. This enforces durability (if commited -> REDO).

* **Steal Policy**

    Remember old values of flushed pages to an UNDO log. This enforaces atomicity (if abort -> UNDO).

## Log Records

An ordered list of records that allow REDO/UNDO

* Transaction ID
* Page ID
* Offset
* Length
* Old data
* New data

### ARIES Protocol

This log record follows the **ARIES protocol**.

* **prevLSN**: LSN of the previous log record written by the specific transaction.
* **Transaction Table**
    A table of active transactions
* **Dirty Page Table**
    A table of dirty pages stores information for UNDO.

    * **recLSN**: LSN of the first action that dirtied the page.
* **Log record types**:
    * Update, Commit, Abort
    * Checkpoint (for log maintenance)
    * Componensation Log Records (CLRs, for UNDO actions)
    * End (end of commit or abort)

* **Abort and Checkpoint**
    When abort and checkpointing we need to implement UNDO. Before we start the UNDO we need
     * get lastLSN
     * write abort log
     * follow the chain of log records using prevLSN
     * Componensation Log Record (CLR):
        A log to insure crashes while undoing.
        * Contains REDO info
        * UNDO persists.
    * Write end log record.

### ARIES Recovery Phases

During a crash the following is ran

1. **Analysis (Checkpoint)**

    If checkpoint exists, figure out which transaction was commited since checkpoint and which failed.

    * End record
        * Remove transaction from table
    * Update record
        * If the page is not in the dirty page table, add to it.  Set `recLSN=LSN`
    * Else
        * Add transaction to table. Set `lastLSN=LSN`
        * change transaction status on commit.

2. **REDO**

    Redo all actions since the smallest `recLSN` in the dirty page.

    * Start at the smallest `recLSN` (oldest update log that dirtied the page).
    * For each CLR, REDO the aciton unless either
        * Affected page isn't in the dirty page table
        * Affected page is in the dirty page table but has `recLSN > LSN`
        * `pageLSN >= LSN`
    * Apply REDO:
        * Reapply logged action
        * Set `pageLSN=LSN`

3. **UNDO**
    Undo the effects of the failed transaction.

    * Start with the transaction with the largest `lastLSN`. For each transaction `lastLSN` (stored in a list of undo),
        * If the `lastLSN` log is a CLR
            * Add the `nextLSN` to the undo list if it isn't null.
            * Otherwise write an end record.
        * Otherwise the record is an update
            * Write a CLR for the undo in the log.
            * Perform the undo.
            * Add the `prevLSN` to the list of undo

## SQL Commands

* `BEGIN`

    Start a transaction that won't commit until the `COMMIT` is ran.

* `COMMIT`

    Commit the transaction if all transactions above (until the `BEGIN`) suceeded.
* `ROLLBACK`

    Rollback the transaction.

* `SAVEPOINT <name>`

    Save the current.

* `RELEASE SAVEPOINT <name>`

    Delete the savepoint.

* `ROLLBACK TO SAVEPOINT <name>`

    Rollback to the savepoint.

## Why Database Crash?

From the most common to least:

1. **Operation Error**

    The user caused the error.

1. **Configuration Error**

    Error on requirements (e.g., disk space, file permission, etc).

1. **Software Failure**

    Bugs (DBMS bugs, security flaws, OS bugs, etc).

1. **Hardware Failure**