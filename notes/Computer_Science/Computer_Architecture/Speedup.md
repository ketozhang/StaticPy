---
{}
---

# Speedup
- [Speedup](#speedup)
- [Unrolling](#unrolling)
- [Cache Blocking](#cache-blocking)

There are many ways to speedup a program. We'll use matrix operations as the classical example. This section will not cover parallel processing.

# Unrolling
Optimize the use of independent instruction to accumulate as much binary size (registers) as possible.

```Python
result = 0
for i in range(0, len(arr), 4):
    result += arr[i]  
    result += arr[i+1]
    result += arr[i+2]
    result += arr[i+3]
```


# Cache Blocking
Optimize temporal locality of cache by changing the way we access data.

* For NxN matrix operations one method is to split the matrices into sub-matrix