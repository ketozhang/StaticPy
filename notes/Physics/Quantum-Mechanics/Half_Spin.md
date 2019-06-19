---
title: Half Spin
---

# Eigenvalue Relations

$$
\begin{gather*}
    \hat S_n \ket{\uparrow_n} = \frac{\hbar}{2}\ket{\uparrow_n}, \qquad \hat S_n \ket{\downarrow_n} = -\frac{\hbar}{2}\ket{\downarrow_n}
\end{gather*}
$$

# Spin States

$$
\begin{gather*}
    \ket{\uparrow_z} = \begin{pmatrix}
        1 \\ 0
    \end{pmatrix} \qquad
    \ket{\downarrow_z} = \begin{pmatrix}
        0 \\ 1
    \end{pmatrix}\\
        \frac{1}{\sqrt{2}}\ket{\uparrow_x} = \begin{pmatrix}
        1 \\ 1
    \end{pmatrix} \qquad
    \frac{1}{\sqrt{2}}\ket{\downarrow_x} = \begin{pmatrix}
        1 \\ -1
    \end{pmatrix}\\
        \frac{1}{\sqrt{2}}\ket{\uparrow_y} = \begin{pmatrix}
        1 \\ i
    \end{pmatrix} \qquad
    \frac{1}{\sqrt{2}}\ket{\downarrow_y} = \begin{pmatrix}
        1 \\ -i
    \end{pmatrix}
\end{gather*}
$$

# Spin Operators and Pauli Matrices

$$
\begin{gather*}
    \hat S_n = \frac{\hbar}{2}\sigma_n\\\\
    \sigma_x = \begin{pmatrix}
        0 & 1 \\ 1 & 0
    \end{pmatrix}, \qquad
    \sigma_y = \begin{pmatrix}
        0 & -i \\ i & 0
    \end{pmatrix}, \qquad
    \sigma_z = \begin{pmatrix}
        1 & 0 \\ 0 & 1
    \end{pmatrix}
\end{gather*}
$$

# Arbritrary Spin States and Operators

For an arbritrary direction $\hat n = (\sin\theta \cos\phi, \sin\theta\sin\phi, \cos\theta)$,

$$
\begin{gather*}
    \hat S_n = \frac{\hbar}{2}\begin{pmatrix}
    \cos\theta & \sin\theta^{i\phi} \\ \sin e^{i\phi} & -\cos\theta\\
    \end{pmatrix}\\\\
    \ket{\uparrow_n} = \begin{pmatrix}
        \cos\frac{\theta}{2} \\ \sin\frac{\theta}{2}e^{i\phi}
    \end{pmatrix} \qquad \ket{\downarrow_n} = \begin{pmatrix}
        -\sin \frac{\theta}{2}e^{i\phi} \\ \cos \frac{\theta}{2}
    \end{pmatrix}
\end{gather*}
$$