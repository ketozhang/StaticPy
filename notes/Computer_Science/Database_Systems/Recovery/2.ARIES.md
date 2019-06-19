---
title: ARIES
---

The **Algorithms for Recovery and Isolation Exploiting Semantics (ARIES)** is a recovery algorithm began by preparing the logs using **Write Ahead Logging**. During recovery we perform the following phases:

1. **Analysis Phase**
2. **REDO Phase**
3. **UNDO Phase**

### Write Ahead Logging (WAL)

At all times we must:

1. Flush & update log record before the data page gets to the disk.
2. Flush all log records of a transaction before commit.

The following condition must be met:

* In the buffer,
    * Disk keeps the log ordered by its **Log Sequence Number (LSN)**
    * Buffer keep track of the `flushedLSN` which points to the position in the disk that was latest LSN flushed so far.
    * In the database, each page holds the `pageLSN` that points the the latest LSN used to update the page.
* When flushing we require,

    `pageLSN < flushedLSN`

## Analysis Phase

At the time of crash, the transaction table and dirty page table (DPT) read from the disk stores the state at latest `BEGIN CHECKPOINT`. The analysis phase rebuilds the transaction table and DPT that was erased during the crash.

Begin at the latest `BEGIN CHECKPOINT`:

```python
For each LSN from BEGIN CHECKPOINT LSN to CRASH:
    if END:
        Remove Xact from Xact table
    else if UPDATE:
        If (page not in DPT) ADD TO DPT
        page.recLSN = LSN
    else:
        If (Xact not in Xact table) Add Xact to Xact table
        Xact.lastLSN = LSN
        IF COMMIT:
            Xact.status = 'committing'

# At the end of Analysis Phase end committing Xact
For each Xact with Xact.status == 'committing':
    ADD END(Xact) to log
    Remove Xact from Xact table
```

The information we have now is:

1. Which transaction were active during the time of crash.
2. Which dirty page that might not been flushed to disk.

## REDO Phase

The analysis phase gives us the state of the table at crash (ideally), we have information to decide which LSN to redo. We begin with the smallest LSN that dirtied a page in the DPT (i.e., smallest `recLSN`)

We do not redo if the page was already flushed to disk. Unfortunately the DPT isn't enough to guarantee this so the REDO algorithm goes as:

```python
toREDO = []
For each LSN from smallest recLSN in DPT:
    if (LSN corresponds to UPDATE or CLR):
        if (page not in DPT) or (recLSN > LSN) or (pageLSN >= LSN):
            continue
        else:
            toREDO.append(LSN)

For each redoLSN in toREDO:
    redo logged action
    Xact.pageLSN = redoLSN
```

Why do we have these 3 conditions?

* Page is not in DPT

    Page was flushed to DB before checkpoint.

* Page is in DPT but has DPT `recLSN > LSN`

    Page was flushed before checkpoint, then reused before checkpoint

    ```SQL
    UPDATE P1
    COMMIT P1
    END P1
    UPDATE P1
    BEGIN CHECKPOINT
    ```

* `pageLSN >= LSN`

    Page was updated again and flushed to DB after the log record.

## UNDO Phase

At this point everything in the buffer is at the state of the crash.

```python
toUndo = [lastLSNs for all Xacts in Xact table]

while toUndo is not empty:
    logRecord = toUndo.find_and_remove_largest_LSN()
    if logRecord is CLR:
        if (logRecord.prevLSN != null):
            Add logRecord.prevLSN to toUndo
        else:
            END logRecord.Xact
    else:
        Write a CLR for this logRecord
        Undo the update in the database
        Add logRecord.prevLSN to toUndo
```