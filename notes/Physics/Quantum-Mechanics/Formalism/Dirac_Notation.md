---
title: Dirac Notation
---
*alias: Bra-ket notation*

The dirac notation is widely used in quantum mechanics similar how vectors are widely used in electromagnetism. We use this because quantum mechanics is natural a linear algebra problem. 

A vector in Dirac notation is written as $|\alpha\rangle$ which is called a **bra vector** defined to be a general vector in **any** basis. For example we say that $|\alpha\rangle$ may be represented in a $N$-dimension space using the cartesian basis,

$$ |\alpha\rangle \rightarrow \boldsymbol{a} \equiv \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_N \end{pmatrix}$$

* $\boldsymbol{a}$ : a vector in the cartesian basis.
* $a_1, a_2, ... a_N$ : the weights of their corresponding basis.
* Recall in cartesian basis each row correspond to the basis vectors $(\hat x, \hat y, \hat z, ...)$

## Conjugate Vector - Ket

The **ket vector** is the conjugate of the **bra vector** such that,

$$\langle \alpha | \;\equiv\; |\alpha \rangle ^*$$

## Inner Product
*alias: dot product, braket*

The inner product of two vectors is the product of a bra and ket vector.

$$ \boxed{\langle \alpha | \beta \rangle \equiv  a_1^*b_1 + a_2^*b_2 + ... a_N^*b_N}$$

### Properties

* $\langle \alpha | \beta \rangle^* = \langle \beta | \alpha \rangle$

## Hilbert Space

Many times it is not very useful to think of inner product as of the definition above because it is not necessary that $\alpha$ and $\beta$ is a easy vector to comprehend. In this case how do you represent a function like $\Psi(x,t)$ as a vector? 

The answer is you don't; we take a look at the fact that for a **square-integrable function** which is defined as a function who's conjugate square has a non-infinite area thus follows,

$$ \langle f | f \rangle = \int_a^b{|f(x)|^2 \;dx} < \infty \tag{square-integrable}$$

Then, the inner product of square-integrable functions is,

$$ \langle f | g \rangle \equiv \int_a^b{f(x)^*g(x)\;dx}  $$

In quantum mechanics we deal with only wavefunctions that are normalizable. You may check that all normalizable functions are also square-integrable since the area is non-infinite. We may introduce such a space where the wavefunction and all square-integrable functions live. This is called the **Hilbert space** or the **complete inner product space**. 

### Properties

* **Self inner product:** The self inner product is defined as,

    $$ \langle f | f \rangle \equiv \int_a^b{|f(x)|^2 \;dx} $$

    The self inner product is always non-negative and real,
    
    $$ \langle f | f \rangle > 0, \qquad \langle f | f \rangle \in \mathbb{R} $$

    The self inner product is only zero for the zero function $f(x)=0$,

* **Schwarz inequality:**

    $$ \left\lvert{\int_a^b{f(x)^*g(x)\;dx} }\right\rvert \le \sqrt{\int_a^b{|f(x)|^2\;dx}\int_a^b{|g(x)|^2\;dx}}$$

