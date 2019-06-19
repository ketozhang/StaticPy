---
title: Moment of Inertia
---

## Moment

When one begin classical mechanics you've likely taken for granted that the **moment** is the **moment of inertia**. The **moment** is defined as

$$
I = \sum{m_\alpha r_\alpha} \\
I = \int{r \d m}
$$

* $r_\alpha$ : distance away from the origin (often the origin of rotation).

## Product of Inertia

## Inertia Tensor and Inertia Matrix
The moment of inertia can be described as a rank/degree 2 tensor (a $3 \times 3$ matrix) :

$$ \mathbf{I} = \sum_{i=1}^3{\sum_{j=1}^3{I_{ij}~\mathbf e_1 \otimes \mathbf e_2}} $$

If you're not familiar with tensors you can simply transform the line above to the following matrix,

$$ \mathbf{I} = \begin{pmatrix} I_{xx} & I_{xy} & \ldots \\ I_{yx} & \ddots & \vdots \\ \vdots & \ldots & \ddots \end{pmatrix} $$

$$ I_{ij} = \sum{m_\alpha(r_\alpha^2\delta_{ij} - i_\alpha j_\alpha)} = \begin{cases} \sum{m_\alpha (r_\alpha^2 - j^2)} &  i = j \\ \sum{m_\alpha ij} &  i = j \end{cases} $$

Properties
:
* $\mathbf I$ : This matrix is symmetric $\mathbf I = \mathbf I^T$

Useful volume differentials
:

   Shape    |          Volume           |  Differential Volume   |       Relations
----------- | ------------------------- | ---------------------- | ---------------------
Rectangular | $V = a_xa_ya_z$           | $\d V = \d x\d y\d z$  |
Spherical   | $V = \frac{4}{3}\pi R^3$  | $\d V = 4\pi r^2 \d r$ |
Conic       | $V = \frac{1}{3}\pi R^2h$ | $\d V = 2\pi r h \d r$ | $r = z \cdot \tan\theta \\ r = z \cdot \frac{R}{h}$

#### Surface Area of a Cone

##### Naive

$$ r(z) = \frac{R}{h}z\\
\boxed{\int_0^h{2\pi r \d z} }$$

##### Correct

$$\int_0^h{2\pi r \d s}\\
ds^2 = dr^2 + dz^2 \implies ds = \sqrt{1 + \frac{dr^2}{dz^2}} \d z = \sqrt{1 + \frac{R^2}{h^2}} \d z\\
\boxed{\int_0^h{2\pi r \sqrt{1 + \frac{R^2}{h^2}} \d z}}
$$

* $ds$: Differential path along the inclined plane of the cone