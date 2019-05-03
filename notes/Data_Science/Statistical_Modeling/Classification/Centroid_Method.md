---
title: Centroid Method
---

The centroid method generates a hyperplane decision boundary using the center of masses of each class. With two classes, two mean positions are calculated from each class. A line is drawn between the two mean points and the hyperplane is drawn perpendicular to the line at the midpoint. The decision function is given by,

$$
f(x) = (\mu_A - \mu_B) \cdot x - (\mu_A - \mu_B) \cdot \frac{\mu_A + \mu_B}{2}
$$