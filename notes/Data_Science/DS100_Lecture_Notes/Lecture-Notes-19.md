---
title: Lecture Notes19
---
# Lecture Notes 19

Recall the expectation of the squared loss of some sample $(X,Y)$ with some error $Y \equiv h(x) + \varepsilon$,

$$ 
\Expected{\left( Y - f_{\hat \theta}(x) \right)^2} = \text{Observational Variance} + (\text{Bias})^2 + \text{Model Variance}
$$

## Model Complexity
Model complexity can be thought of as the "capcity of the model to fit the data"

## Least Square Linear Regression
The least square linear regression is a model (denoted as either $\hat y$ or $f_\theta(x)$) with the form,

$$ \hat y = \sum_{j=1}^{d}{\theta_j\phi_j(x)}$$

* $\theta_j$ : The parameter which must be linear by definiton
    * When we say linear we simply mean that each term must look like $f(\theta,\phi) = \theta\phi(x)$ where $\theta$ must be a constant for $f(\theta, \phi)$ to be linear.
    * To be honest, it's a convoluted way of saying the weight/parameter must be constant.
* $\phi_j(x)$ : The feature function

The "least square" part of course means we're attempting to find the parameter $\hat \theta$ that minimizes the squared loss function

$$ \hat \theta \equiv \arg\min{\frac{1}{n}\sum_i\left(y_i - \hat y(\theta, x_i)\right)^2} $$

* $\hat \theta$ : Note that the optimal paramter $\hat theta$ can be a vector of length/dimension $d$, where $\theta = [\theta_1, \theta_2, ..., \theta_d]$

## Feature Engineering
The process of transforming the inputs to a model to improve prediction accuracy

Allows you to:
* capture domain knowledge
* encode non-numeric features
* express non-linear relationships

Basic transformations:

* Remove uninformative data (e.g., UID)
* Quantitative features (e.g., age)
    * Non-linear transformation (e.g., log)
    * Normalize/standardize (e.g., (x-mean)/stdev)
* Categorical features (e.g, state)
    * One-hot-Encode transformation

### One-Hot Encoding
One-hot encoding is simply transform a categorical data into a representation of states.

If you're not familiar with states it goes somewhat like this. Say there are 3 states labled 'A', 'B', 'C'. Each data can either be part of state 'A', 'B', and/or 'C' denoted by either `1` (yes) or `0` (no). For example, if data 1 is in state 'A' it will be:

```
Data    A   B   C
   1    1   0   0
``` 

### Encoding Missing Values
For either quantitative or categorical data missing values can be encoded as:

* infer what the missing value should be (mean, median, infer from other columns)
* add this missing value's name to a column called "missing_col_name

Never delete the whole just because there exist a missing value. There might be a reason why it is missing.

### Bag-of-Words Encoding (Encoding Text)
The bag-of-words encoding literally means there is a list of words (e.g., common words in the English alphabet) that carries the count of the words in the data you're encoding.

Cons
* Does not preserver sentence order

### N-Gram Encoding
To solve the problem of word order instead of mapping counting a single word we count a group of size $N$-words.

Cons
* Extremely complex

### Feature Matrix
All of the transformations above is to attempt to create a quantitative matrix of features called the **feature matrix**. Given $n$ datasets and $d$ features the feature matrix is $\Phi$ which is a $n \times d$ matrix.

In our model, this is quite simply to transform to a matrix if you consider two indices $j$ is the row index for which data it's referring to and $\phi$ by definition is the feature column index 

$$ \hat y = \sum_{j=1}^{d}{\theta_j\phi_j(x)} = \Phi\hat\theta$$

We will not prove this (requires matrix calculus) but $\hat \theta$ that minimizes the squared loss function is given by the **normal equation**

$$ \hat \theta = (\Phi^T\Phi)^{-1}\Phi^TY $$