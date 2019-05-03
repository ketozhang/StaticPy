---
title: Transactions
---

The solution to concurrency control is to treat the user's queries as a single transaction. A  **transaction** (or Xact) is a batch of queries that are extracted to line by line instructions.

* A sequence of read and writes to the DBMS
* Transactions are applied to the database once commited and ended or else they are aborted.
* Any logic (e.g., arithmetic) are computed within the transaction and not known to the DBMS.

## Properties
The basic properties of a transaction are acronymed to be ACID:

* **Atomicity**

    All actions in the transaction happen or none of it happen.

    * Solved by requiring every transaction to have a `COMMIT` action at the end of their transaction. This line must be ran otherwise the transaction aborted.

* **Consistency**

    If the DB starts out consistent, it ends up consistent at the end of the transaction.

    * You can intepret consistency using the schema.

* **Isolation**

    Execution of each transaction is isolated from that of the others

    * Solved with a transaction manager/scheduler

* **Durability**

    If a transaction commits, then its effects persist.

    * Transactions are logged, if the transaction is not commited then use the log to undo. If the transaction is commited then use the log to redo.