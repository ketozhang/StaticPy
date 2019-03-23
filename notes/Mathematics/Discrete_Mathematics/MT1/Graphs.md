---
title: Graphs
---

A graph is a set of pairs of vertices which the pairs are connected by some relationship. The syntax for a graph is for instance,

\$$ G = \set{(v_1,v_2), (v_2,v_3), \ldots}~, \qquad \forall v_i \in V\$$

* $V$ : The set of all vertices $\set{v_1,v_2,v_3,\ldots}$
* $(v_1,v_2)$ : Edge describing the connection betwen two vertices. We consider $a$ and $b$ to be **adjacent** or **neighbors** if there exists an edge between them.
* In general, a graph is directed so $(a,b) \neq (b,a)$ otherwise undirected
* The following are not conisdered graphs in this class:
    1. Self loops (e.g., $(a,a)$)
    2. Multiple loops (i.e., sets are unique)

## Properties

Degree
: Number of neighbors for some vertex

    $$ \deg(a) = \abs{G(a)} $$

    * $G(a)$ : All edges in $G$ that has the vertices $a$
    * The sum of the degrees of all vertices (let the set of all vertices be $V$) is,

        $$ \sum_{v \in V}{\deg(v)}  = 2|G|$$

Path
: A sequence of edges. We may denote this with lines (undirected) or arrows (directed)

    $$ v_1 - v_2 - \ldots $$

    * A **walk** allows multiple visits of a vertice

Cycle
: A path that ends where it starts

    $$ v_1 - v_2 - \ldots - v_1 $$

    * A **tour** allows multiple visits of a vertice

Connected
: A graph is connected if there exist a path to every pair of vertices.

## Eulerian Tour
An **Eulerian tour** of $G$ is a tour that traverses every edge exactly once.

**_Theorem: (Eulrian Tour Theorem)_**
: An undirected graph $G$ has an Eulerian tour $\iff$ all vertices of $G$ have an even degree and $G$ is connected.

## Eulerian Walk

An **Eulerian walk** of $G$ is a walk that traverses every edge exactly once.

## Hamiltonian Cycle

A **Hamiltonian cycle** or a **simple cycle** is a cycle that visits every vertex exactly once

* No simple characterization
* NP-complete

## Trees
A graph is a tree if any of the following satisfies:

1. Graph is connected and no cycles.
2. Graph is connected and exactly n-1 edges
3. Graph is connected and removal of any edge disconnects the graph
4. Graph has no cycle and the addition of any edge creates a cycle

## Complete Graph

The maximally connected graph where every possible edge on $n$ vertices,

$$ |E| = \binom{n}{2}  $$

* $K_n$: A graph with n vertices
* $K_{n,m}$: A graph with n vertices by m vertices in a 3D assortion

## Planar Graph

A graph is planar if it can be drawn in the plane such that none of its edges cross.

* The whole graph can be colored with four colors such that no two vertices share the same color and same edge.
* **Euler's Formula**: A graph is planar if,

    $$ v- e + f = 2 $$

    * $v$: vertices
    * $e$: edges
    * $f$: faces (inner and outer closed loops with no edges in between)

    Unfortunately, this formula is not so useful because the graph must at first be drawn planar.
* For any planar graph $G$ with $e \ge 2$, we have

    $$\text{Planar} \implies  e \le 3v - 6$$

* A graph is planar $\iff$ G does not contain $K_{3,3}$ or $K_5$

## Connectivity

* A tree is minimally connected
* A complete graph is maximally connected

_**Theorem: For a hypercube of dimension $n$, let $S \subseteq V$ then $|S| \le \frac{1}{2}\abs{V} = 2^{n-1}$**_

## Hypercube

A hypercube (denoted as $H_n$ for $n$ dimensions) is a connected graph of $2^n$ vertices with every vertex having degree $n$.

$$ \deg(v) = n$$

* Vertices of a hypercube can be represent as binary bits. Each vertex's neighbors are on bit away from the vertex (known as hamming distance 1). In other words a hypercube is generated as,

    $$H_n = \set{(v_i, v_j) \mid d(v_i, v_j) = 1}$$

    Where $d(v_i,v_j)$ is the hamming distance between two vertices.

* All hypercubes have a Hamiltonian tour since the cycle $(s,s+1,s+2,\ldots,s+2^n,s)$ always exists
* All hypercubes of even $n$ has a Eulerian tour since the all degrees are even.

## Bipartite Graphs

A graph is bipartite if two unique set $L$ and $R$ such that there exists no edge with two vertices that are part of the same set.

* A graph is bipartite if there exists no odd tours.