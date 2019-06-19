---
title: Multipole Expansion
---

At a large distance $d$ from a charge source, we can approximate the charge to be a point source. However, we wish to generalize for any distance away from a source. Consider a charge source well-structured in an $n$-pole configuration. The potential located at $\boldsymbol r$ from the origin and $d$ distance away from the a geometric slice of the source $\mathrm d \mathcal V$ located at $\boldsymbol r'$ is given by,

$$
V(\boldsymbol{r}) = \frac{1}{4\pi \epsilon_0}\int{\frac{\rho(\boldsymbol{r'})}{d} \mathrm d \mathcal V}
$$

The distance here however changes as the geometric slice $\mathrm d \mathcal V$ changes. It turns out that the inverse distance $1/d$ are the Legendre polynomials.

$$
\frac{1}{d} = \frac{1}{r} \sum_{n=0}^{\infty}\left(\frac{r'}{r}\right)^n P_n (\cos \alpha)
$$

Where $\alpha$ is the angle between $\boldsymbol{r}$ and $\boldsymbol{r'}$. Thus the exact potential is,

$$
V(\boldsymbol{r}) = \frac{1}{4\pi\epsilon_0}\sum_{n=0}^{\infty}\frac{1}{r^{n+1}}\int{(r')^n}P_n(\cos\alpha)\rho(\boldsymbol r') \mathrm d \mathcal V
$$