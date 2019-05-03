---
title: Ranking
---

## Vector Space Model

Consider each document as a vector with the basis being all possible terms of all documents.p

* **Cosine Similarity Distance Metric**

    This metric ignores the document length (normalize to unit vectors) thus only care about the relative angle between documents. The actual metric is the cosine of the relative angle which is just their dot product.

* **Rank**

    Documents are ranked by its term frequency and inverse document frequency. To do so we need two schema:

    1. `TermInfo(string term, int numDocs)`
    2. `InvertedFile(string term, int docID, float DocTermRank)`

    The extra `DocTermRank` is to store the result of the rankings of the following formula known as the **TFIDF**:

    ```
    TF = #occurrences of term in doc
    IDF = log((total #docs) / (#docs with this term))
    DocTermRank = TF * IDF
    ```

    * Rare terms that appear in fewer documents are ranked the highest.
    * Common terms that appear in many docments are ranked the lowest.
## Goodness of Search

We measure goodness of search by precision and recall.

* **Precision:** Fraction of true positives to claimed positives
* **Recall:** Fraction of true positives to actual positives

## Parallelization
We can parallelize by either:

1. Each machine gets different documents.
    * Not too bad, however bad for rare terms since machines don't know about the other documents.
2. Each machine get different search terms.
    * Bad if any term is too popular (they usually are by the 80/20 rule[^1])

    [^1]: The 80/20 rule or the Pareto distribution (discrete form is the Zipf distribution) is a power law distribution. An intuition for this used in search engine is that this distribution says things that are popular are very popular while things that aren't are very unpopular.

## Ranking Algorithms

* **N-Grams**

    Index $N$ neighboring words instead of just one word. Higher rank given to matches of higher N-word.

* **Q-Grams**

    Index $Q$ neighboring letters of a word into a subset of each element of size $Q$ string.

    * Can search for mispellings.

* **Citation Analysis**

    A ranking scored using the number of times the document was cited.

    * Google's original search engine was a web graph based citation analysis called PageRank. This algorithm is currently used today.