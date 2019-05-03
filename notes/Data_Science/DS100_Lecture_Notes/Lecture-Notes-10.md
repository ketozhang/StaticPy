---
title: Lecture Notes10
---
# Lecture Notes 10

## Python String Methods
All python string methods are called by `"str".method` for some method.
The following methods were cover in the lecture:

* `str.strip`: Remove all white spaces
* `str.lower`: Turn all lower case `az` characters to upper case `AZ`
* `str.replace(old, new)`: Replace some `old` string with a `new` string.
* `str.split(delimiter)` : Return strings as a list delimited by some string

## Regular Expression
Learning regular expression is not easy. I do not recommend reading these notes as no lecture notes can really help. Please see the webcast, live demonstration makes a lot of sense.

```python
import re
```

A typical **regular expression (regex)** use in python is the `re.findall` method which takes in a regular expression `regex` to match with some string `string`,

```python
re.findall(regex, string)
```
Here are a list of some regex operators:

* `.`: Wildcard, match any character
* `+`: Match 1 or more
* `()`: Match and extract pattern inside parenthesis to list
* `?` : Immediate character before is optional
* `^` : Don't match the immediate character after
* `$` : Match end of line
* `\`: The immediate character after this is to be treated as a literal string not an operator
* `[AB]`: Match `A` or `B` (however not both)
* `AB|BC`: Match `AB` or `BC`
* `[0-9]`: Match numbers
* `[a-z]`: Match any lower case alphabet
* `[A-Z]`: Match any upper case alphabet
* `[a-zA-Z]`: Match any alphabet
* `\w`: Match Alphanumeric characters
* `\d`: Match numbers (digits)
* `[\t\n\f\r\p{Z}]` : Match these type of whitespace