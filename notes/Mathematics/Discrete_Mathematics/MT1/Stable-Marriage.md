---
title: Stable Marriage
---

The stable marriage problem is a matching problem where there are $n$ men and $n$ women who have a preference list that ranks every men and every women.

* **Goal:** Create a set of pairs such that there exists no rogue couple.
* **Rogue Couple ** A pair that prefer to be together rather than their designated partner. For instance:

    if the pairing is,

    $$ \set{(A,1), (B,2)} $$

    However, the male preference list is $A : 2 > 1$ and $B: 1 > 2$ while the female preference list is $1: B > A$ and $2: A > B$ then of course $(A,2)$ and $(B,1)$ prefers to be with each other thus we have two rogue couples.


## The Gale-Shapley Algorithm

The Gale-Shapley or propose-and-reject algorithm (usually called the SMA) is a solution to the marriage problem.

The algorithm follows as so:

1. At the start of the day, every men propose to the women that's top of their list
2. Of the women proposed, each women choose the top man and puts him on hold and rejects the rest.
3. Repeat step 1. given the rejected men can no longer propose to the women that rejected him.

This cycle goes on until every man has a woman.

### Properties

* SMA always halts and it would take at most $n^2$ (loose upper bound). See [Problems](#Problems) for the exact maximum days.
* **Improvement Lemma:**
    * Every day, the women either gets the same result or gets a better result
    * Every day, the men either gets the same result or gets a worse result.
    * For every woman that has rejected a man, each woman must have a man on hold.
* SMA always produce a stable pairing
    * The stable pairing is **male optimal** (i.e., consider all possible stable pairing, the male gets a pairing with the best women of all stable pairings)
* If a man proposes to a woman, then this is either his first proposal or have proposed to other women more preferable than his current proposal.
* If a woman holds a man, then no man less preferable than the current hold can propose to the woman.

### Problems

* The maximum number of rejections is,

    $$ \max(\text{rejection}) = (n-1)^2 $$

* The maximum days of SMA one more than the maximum number of rejections,

    $$ d_\text{max} = 1 + \max(\text{rejection}) = n^2 - 2n + 2 $$

* All men get their top preferences if all their top preferences are unique. This is true regardless of the women's preferences.

    |   Men    |                |
    | :------: | :------------: |
    |  $M_1$   | $W_1 > \ldots$ |
    |  $M_2$   | $W_2 > \ldots$ |
    | $\vdots$ | $W_3 > \ldots$ |
    |  $M_n$   | $W_n > \ldots$ |

    $$ \set{(M_1,W_1), (M_2,W_2), \ldots, (M_n,W_n)}  $$

    * If the women's preference also prefers the respective men's first choice as their first choice then this result is both male and female optimal.
    * This table always finish on day $d=1$

* If all men has the same preference say $W_1 > W_2 > \ldots > W_n$, then $W_1$ gets her first choice, $W_2$ her best choice that isn't chosen by $W_1$, $W_3$ her best choice that isn't chosen by previous two, and so on.

    |   Men    |                   |
    | :------: | :---------------: |
    |  $M_1$   | $P: W_1 > \ldots$ |
    |  $M_2$   |        $P$        |
    | $\vdots$ |     $\vdots$      |
    |  $M_n$   |        $P$        |

## The Roommates' Problem

If we remove gender from the stable marriage problem, then we have the roommates problem. For $n$ even number of people each person has a preference list of size $n-1$.

* Unfortunately this problem does not always have a stable pairing. For example,

    |       |         |
    | :---: | :-----: |
    |  $A$  | $B>C>D$ |
    |  $B$  | $C>A>D$ |
    |  $C$  | $A>B>D$ |
    |  $D$  |   Any   |