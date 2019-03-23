---
title: Index Notation
---

Dot Product
:
$$
(u \cdot v)_{i} = u_iv_i
$$
Vector - Matrix Multiplication

: 
$$
(Ax)_i = A_{i}^\top x = \sum_{j}A_{ij}x_j
$$
$$
\begin{align}
(x^\top A x)_i &= ([A^\top x]^\top x)_i \\
&= \sum_{j}A_{ji}x_j x_i
\end{align}
$$



Matrix Multiplication

:
$$
(AB)_{ij} = \sum_{k} A_{ik}B_{kj}
$$

$$
\begin{align}
(A^\top A)_{ij} = \sum_{k}A_{ki}A_{kj}
\end{align}
$$



Trace

:
$$
\text{Tr}(A) = \sum_{i} A_{ii}
$$

$$
\text{Tr}(AB) = \sum_{i}(AB)_{ii} = \sum_{i}\sum_{j}A_{ij}B_{ji}
$$

