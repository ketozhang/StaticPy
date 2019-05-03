---
title: Electric Potential
---
Here we describe the conservative thus scalar nature of the electric field as a conservative quantity called the **electric potential**,

$$
\boxed{V(\boldsymbol r) \equiv -\int_{\mathcal O}^{\boldsymbol{r}} \boldsymbol{E} \cdot \mathrm d \boldsymbol{r'}}
$$

One may solve for the electric potential itself only knowing the geometry and position of the charge. First for a single point charge,

$$
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\frac{q}{|\boldsymbol{r}|}
$$

For a continuous charge,

$$
\boxed{V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\int {\frac{1}{|\boldsymbol{r}|}\ \mathrm dq}}
$$

### The Reference Point $\mathcal O$

The reference point is simply where we define the origin of the electric potential $V(\mathcal{O} = 0)$. In most situations such that the electric potential converges to zero the distance away from the source charge goes to infinity ($V(\infty) = 0$) we choose the origin to be at infinity,

$$
V(\boldsymbol r) = - \int_{\infty}^{r} \boldsymbol{E} \cdot \mathrm d \boldsymbol{r'}
$$

## Electric Field to a Scalar Quantity

We can related how the electric potential is considered the scalar quantity of the electric field. First, what's often more of a useful quantity is the difference of the electric betwteen two points $a$ and $b$ thus $\Delta V$.

$$
\Delta V \equiv \int_a^b \boldsymbol{E} \cdot \ \mathrm d \boldsymbol{r'}
$$

We can write $\Delta V$ as a line integral of the gradient w.r.t. the line (fundamental theorem of calculus).

$$
\Delta V = \int_{a}^{b}{\nabla V} \cdot \ \mathrm d \boldsymbol{r'}
$$

Equating the two we now form the equation to relate the electric field is related to a scalar quantity -- the electric potential.

$$
\boxed{\boldsymbol{E} = - \nabla V}
$$