---
title: Queries
---

## Table Creation
```sql
CREATE TABLE <table_name> (
    <column_name> <type>,
    ...
    PRIMARY KEY (<columns>)
    FOREIGN KEY (<column>) REFERENCES <table>
);
```

## Update, Delete

```sql
<UPDATE|DELETE FROM> <table>
SET <column> = <value>
WHERE <pred>;
```

## Retrieval Queries

```sql
SELECT [DISTINCT] <column expr>
FROM <table>
[WHERE <pred>]
[GROUP BY <columns>]
[HAVING <pred>]
[ORDER BY <column expr> [DESC|ASC]]
[LIMIT <int>];
```

## Order of Operation

1. `FROM`
2. `WHERE`
3. `SELECT`
4. `GROUP BY`
5. `HAVING`
6. `DISTINCT`
7. `ORDER BY`
8. `LIMIT`

## Column Expression

