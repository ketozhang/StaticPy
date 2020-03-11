---
title: Example Page
---

![](example.png){.center}

## Some Math

The energy-momentum relation for a relativistic system is,

$$
E^2 = (pc)^2 + (m_0 c^2)^2
$$

This is derived from the vector form of the four-momentum self inner product

$$
p^2 = \frac{E^2}{c^2} - \abs{\vec{p}}^2
$$

<!-- Yep, as you may know Markdown rendering allows raw HTML -->
<small>
Note: The `\abs` is defined with `\newcommand` at the base HTML to be loaded onto the whole website. You may move this to the `note.html` template. This is the same reason why `\vec` is bolded instead of the arrow/anchor above.
Alternatively, MathJax 3.0 has the physics extension (and many others) which natively supports regularly used syntax like `\abs, \braket, \vec`
</small>

## Some Code
Some Python

```py
import numpy
import matplotlib as plt

x = np.array([1,2,3])
plt.plot(x, x**2)
plt.show()
```

<small>
Syntax highlighted can be JS libraries like PrismJS (see StaticPy documentation)
Otherwise you can add your own CSS to `pre>code` for block code or `p>code` for inline paragraph code.
</small>