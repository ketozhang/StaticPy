---
title: Linear Transformation
---

A linear transformation is an operation on a vector that preserves the operations of addition and scalar multiplication,

* $L(u + v) = L(u) + L(v)$
* $L(\alpha u) = \alpha L(u)$

## Matrix-Vector Multiplication
The most intuitive way to think of a matrix matrix-vector multiplication is to see it as a transformation in two steps:

1. The matrix applies a linear transformation to the basis vectors

    $$
    \begin{bmatrix}
        a_1 & b_1\\
        a_2 & b_2
    \end{bmatrix} \implies
    \begin{matrix}
        \hat x \rightarrow \begin{bmatrix}
            a_1\\
            a_2
        \end{bmatrix}\\
        \hat y \rightarrow \begin{bmatrix}
            b_1\\
            b_2
        \end{bmatrix}
    \end{matrix}
    $$

    * Note that it is not necessary for the basis vector to be normalized.

2. The scalar of the vector scales the basis vectors

    $$
    \begin{bmatrix}
        a_1 & b_1\\
        a_2 & b_2
    \end{bmatrix}
    \begin{bmatrix}
        x\\
        y
    \end{bmatrix} =
    x
    \begin{bmatrix}
        a_1 \\
        a_2
    \end{bmatrix} +
    y
    \begin{bmatrix}
        b_1\\
        b_2
    \end{bmatrix}
    $$

## Matrix-Matrix Multiplication

Consider the linear transformation where $M_1$ and $M_2$ are matrices of linear transformation,

$$
L(v) = M_2M_1 v
$$

We can think of $M_1M_2$ as a matrix-matrix multiplication whose product is called the **composite matrix**. The composite matrix can be thought of appying a single linear transformation to $v$ rather than one after another.

You can easily see how matrix multiplication affects the basis vectors. Consider the columns of $M_1$ as the new basis vectors because that is exactly correct by vector-matrix multiplication. What $M_2$ does to $M_1$ is to apply another linear transformation to the new basis vectors.

$$
\begin{bmatrix}
    c_1 & d_1\\
    c_2 & d_2
\end{bmatrix}
\begin{bmatrix}
    a_1 & b_1\\
    a_2 & b_2
\end{bmatrix}
=
\begin{bmatrix}
    a_1 & b_1\\
    a_2 & b_2
\end{bmatrix}
$$

$$
AB \neq BA
$$