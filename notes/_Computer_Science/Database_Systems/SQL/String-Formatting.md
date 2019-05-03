---
title: String Formatting
---

## Old Style

| Syntax  | Description  | Regex Equivalent |
|---|---|---|
| `%` | Match zero or one wildcard | `.?` |
| `_` | Repeat previous character | `*` |


## Predicate

A predicate either in the `WHERE` or `HAVING` clause can use strings.

**Old Style**
```sql
<WHERE|HAVING> <column> LIKE '<like clause>'
```

**Standard Regular Expression**

```sql
<WHERE|HAVING> <column> ~ '<regex>'
```