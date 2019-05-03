---
title: Shuffling
---

You can optimize shuffling

## Asymetric Shuffling

If either table $R$ or $S$ are already pre-partitioned then you can skip shuffling.

## Broadcast Join

Given a small table $R$ and any size table $S$ then we can broadcast $R$ to every machine which evaluated a partition of $S$ with all of $R$.