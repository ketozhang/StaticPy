---
title: Poisson and Laplace's equation
---

The motivation for using the Laplace's equation in electrostatics is to solve for the electric potential $V(\boldsymbol r)$. Recall that from Gauss' law one may derive the Poisson equation,

$$
\nabla^2 V = -\frac{\rho}{\epsilon_0}
$$

The **Laplace's equation** applies to electrostatics is the cases that one attempts to determine the electric potential for a region of space with no electric charges (thus, $\rho = 0$). With the RHS being zero we arrive at the Laplace's equation,

$$
\nabla^2 V = 0 \tag{Region of Zero Charge}
$$

## Separation of Variables
The direct approach to solve the Laplace's equation given that we are dealing with partial differential equation is to use the **separation of variables**.

## Uniqueness Theorem
A tool for solving the Laplace's equation is the **uniqueness theorem**.

Theorem 1
: The solution to Laplace's equation in some volume $\mathcal V$ is uniquely determined if $V$ is specified in the boundary surface $S$.

    In other words if the solution to the Laplace's equation $V=V(\boldsymbol r)$ satisfies the boundary surface $\Big(V(\boldsymbol r' \in S) = V(\boldsymbol r)\Big)$ then this solution will uniquely satisfies the volume $\Big(V(\boldsymbol r' \in \mathcal V) = V(\boldsymbol r)\Big)$.

    **Usage: ** To solve a problem you may simplify the problem to one that also satisfies the boundary conditions at the boundary surface. You must also make sure that the equivalent problem stil satisfies that $\rho=0$ for $V$ within the region wanted.The solution $V$ to this simplified problem is also the solution to the original problem.

Theorem 2
: For a region of volume $\mathcal V$ surrounded by conductors of charge $Q_i$ and surrounded by a charge density $\rho$ where there are no conductors, the electric field is uniquely determined if all $Q_i$ and $\rho$ is known.