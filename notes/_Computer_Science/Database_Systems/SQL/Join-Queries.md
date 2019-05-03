---
title: Join Queries
---

The standard SQL join are part of the `FROM` clause. The syntax is,

```sql
FROM <tbl1> [ INNER | NATURAL | <LEFT | RIGHT | FULL> <OUTER>]
JOIN <tbl2>
ON <qualification_list>
```

### Inner or Natural Join

An `INNER JOIN` joins the intersection of two or more tables for columns determined by the `ON` clause.

While, `NATURAL JOIN` is a special case of `INNER JOIN` which assumes that the `ON` clause is for all columns that share the same name.

Equivalently, `INNER` is selected by default so this syntax is also an `INNER JOIN` where `ON` is replace by the `WHERE` clause.

```sql
SELECT <column expr>
FROM <tbl1>, <tbl2>
WHERE <tbl1>.<col1> = <tbl2>.<col2>
```

### Outer Join

An outer join always return all rows of the `LEFT` table, `RIGHT` table, or `FULL` (union, both) tables. Matched rows are combined as one row and unmatched rows replaces the data with `NULL`.