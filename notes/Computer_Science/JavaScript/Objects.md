---
title: Objects
---

JavaScript objects comprised of the remaining datatypes built like Python dictionaries but implemented with hashes. The syntax for Java object can either be its legacy/original syntax or the more popular JSON (JavaScript Object Notation) syntax.


* Instantiation
: Once a gain there are two syntax to instantiate
    ```js
    var obj = new Object(); // legacy
    var obj = {} // JSON
    ```
* Get
: To get an attribute you may use the dot-notation or Python-like getter `obj[<key>]` notation,

    ```js
    var obj = {
        name: 'Carrot',
        for: 'Max', // 'for' is a reserved word, use '_for' instead.
        details: {
            color: 'orange',
            size: 12
        }
    };

    obj.details.color; // orange
    obj['details']['size']; // 12
    ```