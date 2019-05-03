---
title: Ensemble Learning
---

Decision tree themselves are low bias and high variance models. High variance mdoels are susceptible to different training datasets. Hence, decision trees are called **weak learners**.
It is found that if multiple different models of decision trees were to be esembled where their predicted labels are aggregated in some way, the performance is better than any one decision tree.

Here are a few ways of generating unique weak learners:
* Use different learning algorithms for each learner
* Use same algorithm on many different training sets
* Bagging: same learning algorithm on random subsamples with replacements.
* Random forest: Bagging with random decision trees by taking subset of features.