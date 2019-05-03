---
title: Cost Estimation
---

| Statistics |           Description            |
| ---------- | -------------------------------- |
| NTuples    | # of tuples in a table           |
| NPages     | # of disk pages in a table       |
| Low/High   | min/max  value in a column       |
| Nkeys      | # of distinct values in a column |
| IHeight    | Index height                     |
| INPages    | # of disk pages in an index      |

## Selectivity

The ratio of output to to all possible outputs. This is similar to probability

$$P_\text{sel} = \frac{\text{out}}{\text{in}}$$

* col = value
	$$P_\text{sel} = \frac{1}{\text{NKeys}(t)}$$

* col1 = col2
	$$P_\text{sel} = \frac{1}{\max(\text{NKeys(t1)}, \text{NKeys(t2))}}$$

* col > value
	$$P_\text{sel} = \frac{\text{High}(t) - \text{value}}{\text{High}(t) - \text{Low}(t) + 1}$$

* Missing Information $\rightarrow$ assume $1/10$

### Joint Selectivity

Selectivity on two or more tables by either `AND`, `OR`, or `JOIN` is calculated with the following two assumption:

* Each binning or grouping of the records in the table are uniformly distributed
* Each predicate is independent of the other

Thus, the three operations has the selectivity of:

* `AND`

$$ \prod P_\text{sel}(t_i) $$

* `OR`

$$ \text{Inclusion-Exclusion Principle} $$

* `JOIN`

$$ \prod P_\text{sel}(t_i) \cdot \abs{t_i} $$