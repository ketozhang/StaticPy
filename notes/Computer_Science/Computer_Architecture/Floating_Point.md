---
title: Floating Point
---

# Floating Point
A floating point is a binary representation to include non-integer numbers along with $\pm \infty$ and `NaN`.

The format of the floating point in binary is always,

| Sign | Exponent | Manitssa |


## Floating Point Single Precision

The single precision floating point is a 32-bit representation of the floating point. 

Where we have,

|              | Symbol | Size (bits) |                    Description                     |
| ------------ | :----: | :---------: | -------------------------------------------------- |
| **Sign**     |  $S$   |      1      | the sign where `0` is positive and `1` is negative |
| **Exponent** |  $E$   |      8      |                                                    |
| **Mantissa** |  $M$   |     23      |                                                    |

### Floating Point to Decimal
Giving the floating point $F_2$ one may disect it from the definition that $F_2 \equiv S_2||E_2||M_2$. The following equation is used to construct the decimal representation $D$ given the floating point.

$$D = (-1)^S \cdot (1.M) \cdot 2^{E-127}$$

* $\{S, E, M\}$ is the decimal form of $\{S_2, E_2, M_2\}$.
* **Note:** any number without a subscript is represented in decimal form.


### Decimal to Floating Point
Given a decimal representation $D$ we may convert the floating point by determining each part of the floating point (sign, exponent and mantissa).

Three useful equations is given as so,

|   |   |
|---|---|
| **Sign**  | $$(-1)^S = \frac{D}{\|D\|}$$  |
| **Exponent** | $$E = \lfloor{\log_2{D} + 127}\rfloor$$ |
| **Mantissa** | $$M = 0.M \cdot 2^{23} = \frac{D-2^{E-127}}{2^{E-127}}\cdot 2^{23}$$|

* The first line is redundant math; just take the sign of $D$ and consider what $S$ is
* $\lfloor x \rfloor$ is the floor (round down) of $x$