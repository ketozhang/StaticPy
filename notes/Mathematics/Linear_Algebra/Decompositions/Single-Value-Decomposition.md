---
title: Single Value Decomposition
---

$$ A = U S V^T$$

* $V$ : Orthogonal matrix of $M \times M$
* $S$ : Rank diagonal matrix of $m \times m$
* $U$ : Column orthogonal matrix of $n \times m$

## Rank Diagonal Matrix

$S$ is a diagonal matrix limited by its rank. This means that the number of nonzero entries are determined by the rank of $A$ (let $r = \text{rank} (A)$)

$$ S = \begin{pmatrix}
    \lambda_1   &   0           &   \ldots  &   0\\
    0           &   \lambda_2   &   \ldots  &   0\\
    \vdots           &   0           &   \ddots  &   0\\
               &              &     &   \lambda_r\\
               &              &     &   &      0
\end{pmatrix} $$