---
title: Distributed Transaction
---

A distributed transaction required a distributed database among many machines. Typically these machine follow the share-nothing set up.

* Each machine has their own:
    * Lock table
* Each machine partitions:
    * Table
* Master Node
    The master machine that overseas the global locks (coarse grain locks)
* Distributed Voting
    * Votes for commitement are unanimous

## 2 Phase Commit
A policy for commit voting to insure synchronized commits. The master node acts as the coordinator.

1. Phase 1
    1. Coordinator sends a prepare message (nodes log the prepare)
    2. Each node respond with yes/no (coordinator log the result)
    3. Coordinator determines the result (commit or not)
2. Phase 2
    1. If commit then coordinator sends a commit message to each node otherwise abort.
    2. Each node upon receiving the message responds with an acknowledgement (log the acknowledgement)
    3. Coordinator receive the acknowledge deem the transaction commited. (coordinator log the end)

* Logging provides recovery however we didn't log all the information needed.
    * Logs are always flushed before the actions made.
    *  If any participant node crashes without writing a log, it should be an abort.
