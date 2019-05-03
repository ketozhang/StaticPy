---
title: Operators
---

## Comparison

JavaScript has the normal comparison operators `>`, `<`, `>=`, `<=` but differs when using equals because there are two types of equality:

* Type Coercion equality `==`, `!=`
: Values at both ends are evaluated to the same type and then compared.

    ```js
    123 == '123' // true
    1 == true // true
    ```

* Triple Equality `===`, `!==`
: The data type of values at both ends are also compared.

    ```js
    123 === '123' // false
    1 === true // false
    ```

## Bitwise Operators
Similar to Java