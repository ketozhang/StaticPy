---
title: Records
---

A record is a row of columns called fields.

## Fixed Length Fields

* Field types same for all records in a file
* `NULL`
    * Are wasted empty space

## Variable Length Fields

* Fixed size field stored with padding
    * Issue occurs when the field data is bigger than the field size
* Record header stores position of variable fields
    * Variable fields are place at the end of the record
    * Pointers point to the end of a field
