---
title: Nulls
---

`NULL` follows many specific rules:

## 1. Null Operators

`IS` (`IS NOT`)
: Equality operator

## 2. Logic and Null

* `NULL` operated with `False`

```
F & N == F
F | N == N
```

* `NULL` operated with `True`

```
T & N == N
T | N == T
```

* `NOT NULL`

```
!N = N
```

## 3. Traditonal Operators with Null

Any operators outside the context of `NULL` applied to `NULL` will always return `NULL` or equivalently false (doesn't output)

## 4. Aggregating Null

Aggregation with `NULL` ignores all `NULL` values.