---
title: Conditional Statements
---

## If Statement

```js
if ([cond]) {
    [body]
} else if ([cond]){
    [body]
} else {
    [body]
}
```

## While and Do-While Loop

`while` statements are the same as Java,

```js
while [cond] {
    [body]
}
```

However, the `do-while` statement are one where you want the body to run at least run then check for `while` condition,

```js
do {
    [body]
} while ([cond])
```

## For Loop

There exist Java-like `for` loops

```js
for ([init]; [stop cond]; [increment]){
    [body]
}
```

Also Python-like `for` loops use the `for ... of` loop,

```js
for (let item of items) {
    [body]
}
```

You may also iterate over indices or keys by the `for ... in` loop (**not the same as Python's** `in`)
```js
for (let item in items) {
    [body]
}
```
