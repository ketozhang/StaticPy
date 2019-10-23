---
title: Example Page
---

![](example.png){.center}

## Some Math

The energy-momentum relation for a relativistic system is,

$$
\begin{equation}
E^2 = (\abs{\vec p}c)^2 + (m_0 c^2)^2
\end{equation}
$$


Proof
: This is derived from the vector form of the four-momentum's self inner product

	$$
	p^2 = \frac{E^2}{c^2} - \abs{\vec{p}}^2
	$$

	Since the inner product of four-momentum is Lorentz invariant we can take any reference frame and the easiest one to take is the frame at rest (the zero momentum frame).

	$$
	\begin{gather*}
	\vec{p} = 0 	\\
	\big\Downarrow 	\\
	p^2 = m_0 c^2	\\
	\big\Downarrow	\\
	m_0^2 c^2 = \frac{E^2}{c^2} - \abs{\vec{p}}^2
	\end{gather*}
	$$

<!-- Yep, as you may know Markdown rendering allows raw HTML -->
<small>
**Note:** The `\abs` is defined with `\newcommand` at the base HTML to be loaded onto the whole website. You may move this to the `note.html` template. This is the same reason why `\vec` is bolded instead of the arrow/anchor above.
Alternatively, MathJax 3.0 has the physics extension (and many others) which natively supports regularly used syntax like `\abs, \braket, \vec`
</small>

## Some Code
Here's some random python code

```py
import numpy
import matplotlib as plt

x = np.array([1,2,3])
plt.plot(x, x**2)
plt.show()
```

<small>
**Note:** Syntax highlighted can be JS libraries like PrismJS (see StaticPy documentation)
Otherwise, you can add your own CSS to `pre>code` for block code or `p>code` for inline paragraph code.
</small>