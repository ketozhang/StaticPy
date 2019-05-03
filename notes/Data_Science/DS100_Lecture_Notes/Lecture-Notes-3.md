---
title: Lecture Notes3
---
# Lecture Notes 3

## Conditional Probability

A conditional probability can be generalized by the phrase.

<center> **"What is the probability of B given A"** </center>

Which is notated as,

$$ \begin{align}
    \boxed{P(B | A) \equiv \frac{P(A\cap B )}{P(A)}}
    \label{eq:b-given-a}
\end{align} $$

## Bayes' Rule
Bayes rule changes Equation \eqref{eq:b-given-a} with the identity,

$$ P(A\cap B ) \equiv P(B)\cdot P(B|A) $$

$$
\begin{align}
    \boxed{P(B | A) = \frac{P(B)}{P(A)}\cdot P(A|B)}\\
\end{align}
$$

It is often useful as a way to invert $P(A|B)$ to $P(B|A)$ by the ratio of their probability as the inversion factor,


## Bias Data vs SRS

* Big data is not enough to compare to the accuracy of an SRS.
* We see that an SRS of 100 samples out perform an administrative data by a accuracy difference of 90%.

## Getting Started with Pandas
We will use many packages along with Pandas:

* Python essential packages for data science:
    
    ```python
    %mathplotlib inline #this is only for jupyter
    import matplotlib.pyplot as plt # for plotting
    import seaborn as sns # for fancy plots
    import numpy as np # math matrix or vector tools
    import pandas as pd # table tools
    ```

* Packages listed below are recommended:
    ```python
    from pathlib import Path # replaces os.path which deals with file management
    import zipfile # useful for previewing, extracting, and zipping zip files
    ```

The following is a typical method to import a data file like a properly delimited text file and create a Pandas data table called a `DataFrame`:

```python
"""
The line below about datafile is psuedocode, just assume datafile is a pointer to some file on your desktop. 
There are many ways to do this such as the zipfile method shown in the lecture.
"""
datafile = import_file('data.txt')  #psuedo code
column_names = ['colA', 'colB', 'colC']
df = pd.read_csv(datafile, header=None, names=column_names)
```

Once your data is imported into a `DataFrame` which is stored in the variable `df`. You may now use the following methods of a `DataFrame` 

|                      |                       Description                       |                  Code                  |
| -------------------- | ------------------------------------------------------- | --------------------------------------------- |
| Get Column           | Get a column by column name returned as a Pandas series | `df['colname']`                        |
| Get Rows             | Get a column by range of row indices                    | `df[row1:row2]`                        |
| Get Rows and Columns | Get a column by range of row indices and column names   | `df.loc(row1:row2, colname1:colname2)` |
| Get Rows and Columns | Get a column by range of row and column indices         | `df.iloc(row1:row2, col1:col2)`        |
