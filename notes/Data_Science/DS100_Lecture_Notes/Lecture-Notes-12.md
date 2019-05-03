---
title: Lecture Notes12
---
# Lecture Notes 12

## Joins
The query to join two table:

```sql
SELECT [DISTINCT] <columns>
    FROM <tables>
    ...;
```

Where `<tables>` can look like `table1 as t1, table2 as t2`. The `as` statement assigns `table1` to have an **alias** `t1`.

There are multiple types of joins:

Inner
: The **inner join** (aka **full inner join** or **natural join**) joins the intersection of the two table by looking at the shared column. This is done by default on the `FROM` clause. 

    One may do an inner join even if there exist no shared column by specifying which column and how to compare (conditional statement). The format of this is:

    ```SQL
    SELECT [DISTINCT] <columns>
        FROM <table1> INNER JOIN <table2>
        ON <condition>;
    ```

    A join by looking at the primary key is,

    ```SQL
    SELECT [DISTINCT] <columns>
        FROM <table1> NATURAL JOIN <table2>
        ON <condition>;
    ```

Left and Right:
: **Left join** and **right join** (aka **left outer join**, **right outer join**) does an inner join but includes unmatched entries from either the left table or right table.

    ```SQL
    SELECT [DISTINCT] <columns>
        FROM <left_table> <LEFT|RIGHT> JOIN <right_table>
        ON <condition>;
    ```

Note that a left join's unmatched entries will take the left index and pair it with a `NULL` index. Similar idea for right joins.

Full:
: The **full join** (aka **full outer join**) includes all entries and pairs any missing entries as `NULL`.

    ```SQL
    SELECT [DISTINCT] <columns>
        FROM <left_table> FULL JOIN <right_table>
        ON <condition>;
    ```

## NULL

A note about `NULL` values.  `NULL` values are special values for many cases signifying missing data or some aggregation/arithmetic error. There is are a few rules to follow.

Comparison with `NULL`
: Any boolean operator `< <= > >= =` applied on `NULL` returns NULL.

Finding `NULL`
: To check if an entry `NULL` use:

    ```SQL
    SELECT <columns> 
        FROM <table> 
        WHERE <column> IS NULL;
    ```

`NULL` has special booleans
: `NULL` is has special rules when special boolean operators are applied on `NULL` data. These special boolean operators are:

    ```SQL
    ...
    WHERE <column> <NOT|AND|OR> null;
    ```

    Few great examples are (in psuedo-code):

    ```python
    NOT NULL     ==   NULL
    T & NULL     ==   NULL  # as if NULL is falsy
    F & NULL     ==   F
    NULL & F     ==   F     # F is more false than NULL
    NULL & NULL  ==   F

    NULL or T    ==  T
    NULL or F    ==  NULL   # NULL is more true than F
    NULL or NULL ==  NULL
    ```

    Boolean operations on `NULL` is symmetric such the reverse of any boolean operation is the same (e.g., `NULL or T == T or NULL`).

    ## SQL Simple Random Sample
    To do a simple random sample in SQL:

    ```SQL
    CREATE TABLE <sample_name> AS
    SELECT *, RANDOM() as u
    FROM <table of data>
    ORDER BY u
    LIMIT <integer>
    ```