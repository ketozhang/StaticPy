---
title: Lecture Notes5
---
# Data Cleaning and EDA

## Exploratory Data Analysis

### Key Data Properties to Consider in EDA
The first thing one does when they get data is to look at the key properties of the data:

* Structure: The shape of the data file
    * Rectangular structure
    * Tabular data may be in the format: CSV (comma), TSV (tabbed), Excel, SQL
    * Nested data are often formatted as JSON files or even XML
    * How are data organized in records (how do you organize a data so there is a key-value relation)?
    * What are the fields in each records (data types of say a column)
* Granularity: How fine/course is each datum
* Scope: How complete is the data
* Temporality: How is the data situated in time
* Faithfulness: How well does the data capture reality

### Fields Types

* Quantitative Data: Meaningful data such as differences and ratios.
* Ordinal Data: Data where relative order matters
    * Cannot take differences between ordinal data
    * Ex: Yelp Reviews
* Nominal Data: Data with no numerical meaning
    * Ex: Names, credit card numbers.

### Keys
* Primary Key: A column that uniquely identifies the data on a particular row (e.g., student ID).
* Foreign Key: A column or sets of columns that reference primary keys in other tables.

## Granularity
Granularity is how fine/course a data is. What this means is whether or not a data is a summarize version of what it can be (course) or is it very detailed to the most tediously recorded data.