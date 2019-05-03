---
title: Introduction
---

## Shared Nothing

A parallelism of shared nothing is a scheme where commodity hardware has dedicated CPU, RAM, and disk. Between machines is only a network connection.

## Types of Query Parallelism

1. **Inter-query Parallelism**

    * Each query runs on a separate processor

2. **Intra-query Parallelism**

    * Each operator can be parallelized (inter-operator)
    * Within each operator, we can parallelize its components (intra-operator)