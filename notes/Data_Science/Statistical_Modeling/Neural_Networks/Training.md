---
title: Training
---

From here on, we will deal with only single layer NN for simplicity.

The final loss function is given as $\mathcal L (z,y)$ where $z = h(X_i)$ and is a vector of size $k$. $h(X_i)$ is treated as $k$ predictions of the label vector $y$ hence the loss function actually takes in $Y \in \mathbb R^{n \times k}$

$$
\mathcal L = \frac{1}{n}\sum_{i=1}^n L(h(X_i), Y_i )
$$

With the loss function established we begin the algorithm:

1. Set all weights to random in all transformation matrix $T^{(\ell)}$. This also motivates an alias for $T$ which is the weight matrix (sometimes written as $V,W$ for one-layer NN)
2. Calculate the error $\varepsilon$
3. Gradient descent update to the weights.

Now the hard part is computing the gradient. Naively one may compute the gradient for each weight (i.e., each edge) of the NN which would cost $\Theta(\text{edges})^2$. The better idea is to update the edges as it goes through dynamic programming. Using this idea we get **backpropagation**.

## Backpropagation

An update rule that cost $\mathcal O(\text{edges})$ to calculate the gradient. There's two parts of back pass which is forward pass and backward propagating. 

We simplify the problem by doing stochastic gradient descent on one sample point.
The goal is to solve for,

$$
\nabla_{T^{(\ell)}} L
$$

Let's start with  $T^{(1)}$ which is an input of both $h$ thus also $z$ since $L \circ (z, y) \circ (h, T^{(2)}) \circ (x, T^{(1)})$.

For each row or node $T_i^{(1)}$
$$
\nabla_{T_i^{(1)}}L = \underbrace{\frac{\partial L}{\partial h_i}}_\text{back pass} \overbrace{\nabla_{T_i^{(1)}} h_i}^\text{foward pass}
$$