---
title: Schedules
---

For transactions to satisfy isolaton, we need a scheduler called the **transaction manager**. The transaction manager must schedule actions such that the sequence of actions (or **schedule**) do not conflict with each other.

## Serial Schedule

A naive solution is the **serial schedule**. Here each transaction runs right after another. This issue with this transactions is inefficiency (e.g., the user who called for the last transaction has to wait for the other users before him/her).

* **Equivalence**: Any two schedule are equivalent if:
    1. Involves the same transactions
    2. Each individual transaction's actions are ordered the same.
    3. Both schedule leave the DB in the same final state.

## Serializable Schedules

A serializable schedule is equivalent to a serial schedule however allows interleaved transactions.

* **Serial Schedule**
    A trivial schedule that lets one transaction run first then the other. There are no intervening intstructions from multiple transactions.
    * Serial schedule are equivalent if:
        * Involves the same transactions
        * each individual transaction are ordered the same
        * same final state of the database.
* **Serializable**
    A schedule is serializable if it is equivalent to any of the possible serial schedules.

## Conflicts

Two actions on the same object (e.g., row, page, table, or databse) of two different transactions are in conflict if at least one of them is a write.

* **Conflict Equivalent**
    Two schedule are conflict equivalent if all below satisfies:
    * Involve the same actions of the same transactions
    * Every pair of conflicting actions is ordered the same way.

* **Conflict Serializable**

    A schedule is conflict serializable if all below satisfies:
    * The schedule is serializable
    * The schedule is conflict equivalent to some serial schedule

* **Dependency Graphs**

    A dependency graph is a directed graph with transactions as nodes and dependency as edges. The edges point are "dependent by" relations. The edge may be labeled with the object names.

    **Theorem:** Schedule is conflict serializable if and only if its dependency graph is acyclic.

    * Topological sorting (order of least from edges) the graph will give a equivalent serial schedule.

## View Serializable

* **View Equivalent:**

    Two schedules are view equivalent if all of the following satisfies:
    * Same initial reads
    * Same dependent reads
    * Same winning writes (last write on some record)

All conflict serializable are view serializable.