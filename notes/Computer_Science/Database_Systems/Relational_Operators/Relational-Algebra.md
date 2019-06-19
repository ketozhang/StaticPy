---
title: Relational Algebra
---

## Relational Calculus
Relational calculus is a declarative representation of queries with operation description which we see in relational algebra (Codd's Theorem).

## Operators

Unary
: Operators of a single relation

* **Projection** ($\pi$): Retains only desired columns
    * `SELECT`
    $$ \pi_\texttt{col_expr} $$

    * Cascade property:
    $$ \pi_{c1} \equiv \pi_{c1}(\pi_{c1 \land c2}) $$

* **Selection** ($\sigma$): Select a subset of rows
    * `WHERE`
    $$\sigma_\texttt{pred}$$
    * Cascade property:
    $$ \sigma_{c1 \land c2} \equiv \sigma_{c1}\sigma_{c2} $$

    * Commutative property:
    $$ \sigma_{c1}\sigma_{c2} \equiv \sigma_{c2}\sigma_{c1} $$
* **Renaming** ($\rho$): Rename attributes and relations
    * `AS`
    $$\rho(\texttt{rename}, \texttt{relational_expr})$$

Binary
: Operators of a pair relations

* **Union**  ($\cup$)
    * `UNION [ALL]`
    * Think of it as concatenation
    * Requires the pairs to be union compatible (same number of field in the same order)
* **Difference** ($-$)
    * `EXCEPT [ALL]`
* **Cross Product** ($\times$)
    * `JOIN`

Compound
: A combination of operators

* **Intersection** ($\cap$)
    * `INTERSECT`
    $$ A \cap B \equiv A - (A-B) $$
* **Join** ($\Join$)
    * Theta join
        $$ \Join_\texttt{ON} $$
        $$ A \Join B \equiv \sigma_\texttt{pred}(A \times B) $$
    * Natural join
        $$ A \Join B \equiv \pi_\texttt{col_expr} \sigma_\texttt{pred}(A \times B) $$

        Where $\texttt{pred}$ is common columns.

Other
: Some academics use the following as useful macros

    * Group by, aggregation, and having
        $$ \gamma_\texttt{groupby, aggregate, having} $$