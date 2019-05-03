---
title: Nested Queries
---

## Where Predicate

A nested query in a where precdicate can be used after a nested query keyword

`IN`
: Return the column entires that intersects with the column output of subquery

```sql
WHERE <col> <keyword>
    (<subquery>)
```

`NOT IN`
: Return the column entires that doesn't intersect with the column output of subquery

`EXISTS`
: <center>**Return if true for each row**</center>

    For each row in the table, plug it into the subquery. If the subquery returns true, return that row.

    The format of `EXISTS` does not need require a column, however must have a correlation (i.e., outer table is referenced inside inner table) in the subquery where predicate:

    ```sql
    WHERE EXISTS
        (
            ...
            WHERE <correlation-prediate>
        )
    ```


* `NOT EXISTS`

* `ANY`
<center> **Return if predicate satisfies any subquery**</center>

```sql
WHERE <col> <condition> <ANY|ALL>
    (<subquery>)
```

* `ALL`
<center> **Return if predicate satisfies all subquery**</center>