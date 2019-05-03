## Axioms
### 1. Non-negative Probability

The probability of any event must be non-negative:

$$
    P(x) \ge 0
$$

### 2. Outcome Space is Unitary

The length of the outcome space must be 1,

$$
P(\Omega) = 1\\
\text{or}\\
\sum_{x \in X}p(x) = 1
$$

### 3. Mutually Exclusive - Addition Rule

* Two events are mutually exclusive if the intersection is the empty set

    $$A \cap B = \emptyset$$

* If two events are mutually exclusive then the probability is additive:

    $$ P(A \cup B) = P(A) + P(B)$$

    In general, one may see the notation

    $$ P\left(\bigcup_i^n A_i\right) = \sum_{i}^n P(A_i) $$

    This is called the **addition rule**

## Rules

### Difference Rule

From the additive rule we can derive the difference rule. The difference rule is if we have two events of relations $B \subseteq A$ then we can find the probability of events in $A$ but not in $B$ denoted as $A \backslash B$ or $A - B$,

$$
    P(A \backslash B) = P(A - B) = P(A) - P(B)
$$

Additionally another result of the difference rule is the **complement set** $B^c$ which means the event that $B$ doesn't happen,

$$
B^C = \Omega - B\\
P(B^C) = 1-P(B)
$$