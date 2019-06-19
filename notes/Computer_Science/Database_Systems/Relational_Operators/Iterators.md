---
title: Iterators
---

Each operator has an iterator interface which may streamline the output

## Select

* On the fly
```python
def init(predicate):
    child.init()
    pred = predicate
    current = NULL

def next():
    while(current != EOF and !pred(current)):
        current = child.next()
    return current

def close():
    child.close()
```

## Heap Scan
