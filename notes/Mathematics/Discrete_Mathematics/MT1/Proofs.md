---
title: Proofs
---

## Proof by Contradiction
For a single statement $P$ (does not have to be an implication), a proof by contradiction is done by first assuming $\neg P$ is true then find another statement $R$ that is true and also $\neg R$ is true.

$$ \Big[\neg P \implies \underbrace{(R \land \neg R}_\text{true})\Big] \implies P$$

## Proof by Cases
If $P$ can be decomposed into different statements such that $P$ can be prove if all cases prove $P$ to hold.

## Proof by Induction
A proof by induction proves that an infinite series or an infinite list of numbers can be proven with finite means. A statement that may be proven be induction is in the form

$$
    \forall n \in \mathbb U P(n)
$$

1. **Base Case**

    We must begin by proving the base case (e.g., $n=0$)

2. **Induction Hypothesis**

    Assume $P(n)$ is true from the base case to some value $k$. Say $n-j$ then we assume the theorem is true for $0 \le j \le k$. Alternatively you may just assume true for some single value $k$.

3. **Induction Step**

    With the assumptoin that $P(n=k)$ is true, prove that $P(n = k + 1)$ is true.

## Proving Implications

A proof of implication is the processing of proving that some statement in the form,

$$ P \implies Q $$

is true.

Recall that an implication is only if $P$ is true and $Q$ is false,

$$ (P \implies Q) \equiv (\neg P \lor Q) $$

### Direct Proofs
A direct proof first assumes that $P$ is true then prove $Q$ is true

$$ P \land Q$$

### Proof by Contraposition
A contraposition is a proof of the contrapositive of the statement,

$$ (P \implies Q) \equiv (\neg Q \implies \neg P) $$

### Implication Contradiction

Because we usually assume $P$ is true, implication has a special identity that,

$$ P \implies Q \equiv \lnot\big(P \implies \lnot Q\big)$$

Where $P$ is always true. This is equivalent to saying if $P \implies \neg Q$ causes a contradiction (or in general false) then the implication $P\implies Q$ is true.

---

## Summary

This note takes a look at all the ways one can prove a theorem. In general a theorem can be proven:

 |       Proofs       |                                                              |
 | ------------------ | ------------------------------------------------------------ |
 | **Direct**         | $$P \land  (P \implies Q)$$                                  |
 | **Contradiction**  | $$ \big[P \implies (R \land \neg R)\big] \implies \lnot P $$ |
 | **Contraposition** | $$ \neg Q \implies \neg P $$                                 |
 | **Induction**      | $$ \text{Base Case} \land (\text{IH} \implies \text{IS}) $$  |
