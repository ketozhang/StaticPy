
## Join (Merge)
[*Documentation*](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html)

A `merge` is a join in Pandas.Two tables can be joined by appending records onto another. 

### Inner Joins
The inner join is similar to SQL intersection joins.

```python
df.merge(
    how='inner')
```

### Left Joins

```python
df.merge(
    how='left')
```