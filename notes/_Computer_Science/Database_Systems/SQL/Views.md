
---
title: Views
---

A view is a namespace for sql query similar to how functions are namespaces for code. This is syntaxed as,

```sql
CREATE VIEW <view_name>(<columns>)
AS
    <query>;
```

## Temporary View

A temporary view can be made inside a `FROM` clause.

```sql
...
FROM (<query>) as <view_name>;
```

Another way is with the `WITH` clause

```sql
WITH <view_name>(<columns>) AS
    <query_for_view>
<query>;
```