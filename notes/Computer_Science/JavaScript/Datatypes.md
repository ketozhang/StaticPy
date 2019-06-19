---
title: Datatypes
---

Here are the following common datatypes in JavaScript,

* `Number`
* `String`
* `Boolean`
* `Symbol`
* `Object`
    * `Function`
    * `Array`
    * `Date`
    * `RegExp`
* `null`
* `undefined`

## Numbers

Since there are a single type of number there must be some compromises in the size. Numbers are initially a 32-bit integer but officially a 64-bit double precision float.

* Math operations uses arithmetic operators as expected but there exist an object called `Math` that has methods like `Math.sin`
* You may parse `String`, binary,  hexadecimal, etc using `parseInt`, `parseFloat`, or in generally you can use the unary operator `+` to parse to number. For instance,

    ```js
    + '0x10'; // 16
    ```
* Operations with number may return `NaN` (not `null`) for cases that are not `Infinity` or `-Infinity` (which are other number types).

## Strings

Almost exactly like Java.

## Boolean
Uses the "truthy" and "falsy" concept that Python uses.