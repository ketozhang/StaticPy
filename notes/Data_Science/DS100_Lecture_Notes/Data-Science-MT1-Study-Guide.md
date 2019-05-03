---
title: Data-Science-MT1-Study-Guide
---
# Data Science MT1 Study Guide

## Data Models

* Absolute Loss $\mathbb{L}^1$
	* $L^1$ is minimum at median
		* If data points are even then there exist 3 possible minima
		* If data points are odd then there exist 1
    * Not Sensitive to outliers
    * Difficult to differentiate
    * Minimizes at the **median**
    $$ \mathbb{L}^1(\theta) = \frac{1}{n}\sum_{i=1}^{n}\abs{y_i - \theta}$$
* Square Loss $\mathbb{L}^2$
	* $L^2$ is minimum at mean
    * Sensitive to outliers
    * Easily differentiable
    * Average square loss minimizes at the **mean**
    $$ \mathbb{L}^2(\theta) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \theta)^2 $$
* Huber Loss 
    * Not Sensitive to outliers
    * Numerically differentiable
	* Hobbs is minimum at numerical solution
## Languages

* Matplotlib (`plt.plot`, `plt.xlabel`, `plt.ylabel`)
* Numpy
* Regex
* Pandas Method
* Pandas DataFrame
    * Indexing
    * Groupby
    * Joins, Merge
* Pandas Series
	* Indexing
* Seaborn KDE Plots
* SQL
	* FROM clause if you have 3 tables and you want WHERE to match columns but one of the table isn't joined.
	* Types of Joins
		* `INNER JOIN`
		* `LEFT JOIN`
		* `RIGHT JOIN`
		* `FULL JOIN`
		* `ON` requires a conditional statement not only column names

## Sampling
* Probability
	* Permutation
	* Combination