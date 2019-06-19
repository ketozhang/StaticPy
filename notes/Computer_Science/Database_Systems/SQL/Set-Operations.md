---
title: Set Operations
---

All set operations output a set of unique values unless the keyword `ALL` is appended after.

## UNION

$$ A \cup B$$

* Distinct
    $$ |A| + |B|$$
* ALL
    $$ |A| + |B|$$

## INTERSECT

$$ A \cap B$$

* Distinct
$$ \min(|A|, |B|)$$

* ALL
$$ \sum_i\min(|a_i|,|b_i|), \qquad a \subseteq A,~ b \subseteq B$$

## EXCEPT

$$ A \backslash B$$

* ALL
$$ \sum_i \Delta_i, \qquad a \subseteq A,~ b \subseteq B\\
    \Delta_i =
    \begin{cases}
    0~,                 &|a_i| - |b_i| < 0 \\
    |a_i| - |b_i|~,     &\text{else}\\
    \end{cases}
$$