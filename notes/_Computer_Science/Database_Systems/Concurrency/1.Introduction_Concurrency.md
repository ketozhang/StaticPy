---
title: "Introduction: Concurrency"
---

Allows multiple queries from multiple users to be executed in an efficient order.

* Not concurrent if queries are running sequentially

### Concurency Problems

We will need to tackle the following problems when allowing concurrency.

* **Inconsistent Read**
    User reads in the middle of a transaction

* **Lost Update**
    * A conflict with update where multiple users update the record. Any update may have been rejected.

* **Dirty Read**
    * Reading transactions to be rejected

_Confusion: Even with concurrency control, in using SQL interactively what happens when User A reads before and after User B changes the database_


