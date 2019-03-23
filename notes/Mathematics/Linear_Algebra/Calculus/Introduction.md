---
title: Introduction
---
From here on out matrix are $A \in \mathbb R^{m \times n}$ and vectors $v \in \mathbb R^{1 \times n}$ are column vectors. It is also equivalent to simply denote vectors as a matrix with a single column dimension.

## Matrix Gradient
The **gradient** is defined as the derivative of some scalar function $f$ with respect to some matrix $A \in \mathbb R^{n \times m}$.

We take the convention that the gradient of a scalar function $f$ with respect to a vector (i.e., a matrix $v \in \mathbb R^{1 \times n}$) gives us a column vector,

$$
\nabla f(v) = \begin{bmatrix} \frac{\partial f}{v_1} & \frac{\partial f}{v_2} & \ldots & \frac{\partial f}{v_n} \end{bmatrix}^\top
$$

It's is natural that if $v$ is expanded to a general matrix and let's renotated it as $A \in \mathbb R^{m \times n}$ there should simply just be $m$ more rows. Notice that this convention preserves the shape of the $A$. We will change the notation a bit to allow the subscript to denote "with respect to".

$$
\nabla_A f = \begin{bmatrix}
\frac{\partial f}{\partial A_{11}} & \frac{\partial f}{\partial A_{12}} & \ldots & \frac{\partial f}{\partial A_{1n}}\\
\frac{\partial f}{\partial A_{12}} & \frac{\partial f}{\partial A_{22}} & \ldots & \frac{\partial f}{\partial A_{2n}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial f}{\partial A_{m1}} & \frac{\partial f}{\partial A_{m2}} & \ldots & \frac{\partial f}{\partial A_{mn}}\\
\end{bmatrix}
$$

It is crucially important to note that the resulting gradient matrix can only be applied to a row vector $v^\top \in \mathbb R^{1 \times n}$. Alternatively we can use the transpose of the gradient vector which by convention we have another notation,

$$
\frac{\partial f}{\partial A} \equiv \nabla_A f^\top
$$

## Jacobian - Vector by Vector

Let $f(x): \mathbb R^n \rightarrow \mathbb R^m$ be a vector function. It's derivative with respect to the vector $x \in \mathbb R^n$ is called the **Jacobian matrix** $J \in \mathbb R^{m \times n}$.

$$
J(f) \equiv \frac{\partial f}{\partial x} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \ldots & \frac{\partial f_1}{\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_m}{\partial x_1} & \ldots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$

## Hessian - Gradient by Vector

Now let $f$ be a twice-differential scalar function of the vector $x$. It's **Hessian** is defined as the Jacobian of its gradient vector.

$$
H(f) \equiv J(\nabla f^\top) = \nabla_x^2 f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2_1} & \ldots & \frac{\partial f}{\partial x_1 \partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial f}{\partial x_n \partial x_1} & \ldots & \frac{\partial^2 f_m}{\partial x^2_n}
\end{bmatrix}
$$

$$
H_{ij}(f) = \frac{\partial f}{\partial x_i \partial x_j}
$$

The Hessian can be interpreted as the second gradient of a scalar function. Take note that  $\nabla_x(\nabla_x f) \neq \nabla^2_x f$ because we can't take the gradient of a vector so its technically not the second gradient. We should actualaly mean that the Hessian build up of the second derivative of the gradient which entials the Jacobian of the gradient (modulo the transpose).

$$
H(f) = \frac{\partial }{\partial x}\begin{bmatrix}
(\nabla_x f)_1 \\
(\nabla_x f)_2 \\
\vdots \\
(\nabla_x f)_n
\end{bmatrix}
$$