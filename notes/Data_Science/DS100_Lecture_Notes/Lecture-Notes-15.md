---
title: Lecture Notes15
---
# Lecture Notes 15

## Modeling and Estimation
The steps of modeling is summarized to:

1. Define the Model
    * Simplified representation of the world
2. Define the Loss Function
    * Measures how well a particular instance of the model "fits" the data.
3. Minimize the Loss Function
    * Analytically using calculus
    * Numerically using gradient descent

### Loss Function

* Absolute Loss $\mathbb{L}^1$
    * Not Sensitive to outliers
    * Difficult to differentiate
    * Minimizes at the **median**
    $$ \mathbb{L}^1(\theta) = \frac{1}{n}\sum_{i=1}^{n}\abs{y_i - \theta}$$
* Square Loss $\mathbb{L}^2$
    * Sensitive to outliers
    * Easily differentiable
    * Average square loss minimizes at the **mean**
    $$ \mathbb{L}^2(\theta) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \theta)^2 $$
* Huber Loss 
    * Not Sensitive to outliers
    * Numerically differentiable

### Gradient Descent

$$\boxed{ \theta^{(t+1)} = \theta^{(t)} - \alpha\nabla \ell(\theta^{(t)}) }$$

$$\boxed{ \mathbf x^{(n)} =  \mathbf x^{(0)} - a_1 \nabla f(\mathbf x^{(0)}) - a_2 \nabla f(\mathbf x^{(1)}) - \ldots - a_n\nabla f(\mathbf x^{(n-1)})}$$

## Coding

* Python (basics)
* Matplotlib (`plt.plot`, `plt.xlabel`, `plt.ylabel`)
* Numpy
* Pandas (Dataframe, Series)
    * Indexing
    * Groupby
    * Joins, Merge
* SQL
* Regex

## Data Visualization

* Differentiate quantitative, nominal, ordinal
* Histogram, rug/scatter plot, smoothed density estimator
* Example of bad plots
    * Pie charts
    * stacking (placing data on top of data)
    * jiggling (data's y-value is consistent across each data plot)
    * overplotting

## Web Technology
* GET - get information
* POST - send information
* Languages
    * XML, HTML, JSON

## String Manipulation and Regular Expression