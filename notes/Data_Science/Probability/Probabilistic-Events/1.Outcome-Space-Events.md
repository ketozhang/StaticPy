---
title: Outcome Space and Events
---

## Outcome Space
For a probabilistic system, there exist all possible outcomes denoted as a set $\Omega = \set{\omega_1, \omega_2, \ldots, \omega_n}$ known as the **set of outcomes**, **sampling space**, **outcome space**.

The probability of an outcome in the outcome space is denoted simply as,

$$ P(\omega) $$

## Event
An event $A$ is formally a subset of the outcome space.

$$A \subseteq \Omega $$

The probability of event $A$ is the sum of each outcome probability of $A$,

$$P(A) = \sum_{\omega \in A} P(\omega)$$

* **Uniform Distribution:** If it so happens that the probability of $P(\omega)$ is equal for all $\omega$ then the outcome space is said to have a uniform distribution. This simplifies the probability of an event which is,

    $$ P(A) = \frac{\abs{A}}{\abs{\Omega}} $$

* Some motivation on why an event is a subset and not simply an outcome $\omega$:

    For a dice, the outcome space is $\set{1,2,3,4,5,6}$. An event could be if we roll a $6$. An event can also be if we roll an even number. These events are denoted as $\set{6}$ and $\set{2,4,6}$.

    Thus the purpose of seeing events that are sets is the logic that some events are consist of multiple outcomes.
