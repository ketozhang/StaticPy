---
title: Proofs Examples
---
## Stable Marriage

* _**Theorem.** The stable marriage algorithm always halts._

    _Proof._ First, the SMA halts if no women rejects a man that day. While SMA is running, at least one man gets rejected every day thus crossing a woman off his list. There are $n$ list with $n$ woman in each list. At the very least, one man crosses off a woman per day, SMA halts at most $n^2$ days.

* _**Improvement Lemma.** If man $M$ propose to woman $W$ on the $k$th day, then the following day $W$ has a man on hold that she like as much as $M$_

    _Proof._

    The lemma implies:
    * Every day, the women either gets the same result or gets a better result
    * Every day, the men either gets the same result or gets a worse result.




## Modular Arithmetic

## Graphs

### FindTour

For a graph of even degree, FindTour is an algorithm for finding a tour in a graph. The algorithm goes as so,

1. Start from vertex $s \in V$
2. Walk from $s$ to an untraversed edge incident to the current vertex.
3. Repeat until there are no more untraversed edge adjuacent to the current.

* _**Theorem**_: _FindTour must get stuck at $s$_
* _**Proof**_:

    * If the current vertex is $s$ then the number of untraversed edges are even, else if the current vertex is not $s$ then the nubmer of untraversed edges are odd.

    Because if the current vertex is not $s$, then there exist at least one untraverse edge thus FindTour must get stuck at $s$.

### Eulerian Tour Theorem

_**Theorem**_: _A graph has an Eulerian tour if and only if all vertices have even degree._

* _**Lemma**_: If a graph has an Eulerian tour then for every vertex, its adjacent edges can be paired up.

* _**Proof (only if)**_: Assume the graph is an Eulerian tour. By the lemma above, if every edge for every vertex can be paired up then the vertex has an even degree

* _**Proof (if)**_: Assume the graph's vertices all have even degree.

### Tree Definition Theorem

_**Theorem**_: