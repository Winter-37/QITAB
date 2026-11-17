---
id: wkb-connection-formulas-and-quantization
title: WKB connection formulas and quantization rules
summary: How to join WKB solutions across a classical turning point, where the approximation itself fails. Linearizing the potential gives the Airy equation, and matching its asymptotic forms to the WKB functions yields the connection formulas with their phase of π/4. Bound states then obey ∫p dx = (n - 1/2)πħ for two soft turning points and (n - 1/4)πħ for one wall and one turning point. Tested on the oscillator, the bouncing ball, the quartic well and hydrogen with the Langer correction.
status: in-progress
kind: derivation
level: intermediate
tags: [wkb, connection-formulas, airy-functions, turning-points, bohr-sommerfeld, quantization-condition, bouncing-ball, langer-correction, griffiths, sakurai]
prerequisites: [wkb-approximation, harmonic-oscillator-analytic-solution]
related: [wkb-tunneling-and-alpha-decay, hydrogen-atom, harmonic-oscillator-ladder-operators, central-potentials-and-spherical-harmonics]
order: 20
date: 2026-11-15
---

## The problem at a turning point

The WKB functions of [[wkb-approximation]] hold on either side of a turning point but diverge like $1/\sqrt{p}$ at the point itself. A bound state needs the oscillating solution inside the well tied to the decaying solution outside, so the two sides must be connected through a region where neither is valid. The cure is to solve the Schrödinger equation near the turning point with the potential replaced by its tangent line, and to use that "patching" function as a bridge.

## Patching with Airy functions

Put the turning point at $x = 0$ with the classical region on the left ($V$ rising through $E$). The WKB solutions are

$$
\psi(x) \approx
\begin{cases}
\dfrac{1}{\sqrt{p(x)}}\Big[B\,e^{\frac{i}{\hbar}\int_x^0p\,dx'} + C\,e^{-\frac{i}{\hbar}\int_x^0p\,dx'}\Big] , & x<0 ,\\[2ex]
\dfrac{D}{\sqrt{|p(x)|}}\,e^{-\frac1\hbar\int_0^x|p|\,dx'} , & x>0 ,
\end{cases}
$$

where the growing exponential has been dropped because $E<V$ all the way to $+\infty$.

Near the turning point $V(x)\approx E + V'(0)\,x$ and the Schrödinger equation becomes

$$
\frac{d^2\psi_p}{dz^2} = z\,\psi_p ,\qquad z = \alpha x ,\qquad \alpha = \Big[\frac{2m}{\hbar^2}V'(0)\Big]^{1/3} .
$$

This is Airy's equation, with independent solutions $\mathrm{Ai}(z)$ and $\mathrm{Bi}(z)$ and $\psi_p = a\,\mathrm{Ai}(\alpha x) + b\,\mathrm{Bi}(\alpha x)$. Their asymptotic forms are

| | $z\gg0$ | $z\ll0$ |
|---|---|---|
| $\mathrm{Ai}(z)$ | $\dfrac{1}{2\sqrt\pi\,z^{1/4}}\,e^{-\frac23z^{3/2}}$ | $\dfrac{1}{\sqrt\pi\,(-z)^{1/4}}\sin\!\Big[\tfrac23(-z)^{3/2} + \tfrac\pi4\Big]$ |
| $\mathrm{Bi}(z)$ | $\dfrac{1}{\sqrt\pi\,z^{1/4}}\,e^{\frac23z^{3/2}}$ | $\dfrac{1}{\sqrt\pi\,(-z)^{1/4}}\cos\!\Big[\tfrac23(-z)^{3/2} + \tfrac\pi4\Big]$ |

(At $|z| = 8$ the asymptotic forms are within 0.5 percent of the exact functions.)

**Overlap regions.** Suppose that on each side there is an interval close enough to the turning point for the linear potential to hold, yet far enough ($|\alpha x|\gg1$) for both the WKB and the asymptotic Airy forms to hold. In the linearized potential

$$
p(x) = \hbar\,\alpha^{3/2}\sqrt{-x} ,\qquad \frac1\hbar\int_0^x|p|\,dx' = \tfrac23(\alpha x)^{3/2}\ \ (x>0) ,\qquad \frac1\hbar\int_x^0p\,dx' = \tfrac23(-\alpha x)^{3/2}\ \ (x<0) .
$$

On the right the WKB function is $D\,e^{-\frac23(\alpha x)^{3/2}}/(\sqrt\hbar\,\alpha^{3/4}x^{1/4})$. Comparing with the table, $b = 0$ and $a = D\sqrt{4\pi/(\alpha\hbar)}$. On the left the patching function is then proportional to $\sin[\tfrac23(-\alpha x)^{3/2} + \tfrac\pi4]$, which fixes $B = -ie^{i\pi/4}D$ and $C = ie^{-i\pi/4}D$.

## The connection formulas

Moving the turning point to $x_2$:

$$
\boxed{\;
\psi(x) \approx
\begin{cases}
\dfrac{2D}{\sqrt{p(x)}}\,\sin\!\Big[\dfrac1\hbar\displaystyle\int_x^{x_2}p\,dx' + \dfrac\pi4\Big] , & x<x_2 ,\\[2.5ex]
\dfrac{D}{\sqrt{|p(x)|}}\,\exp\!\Big[-\dfrac1\hbar\displaystyle\int_{x_2}^x|p|\,dx'\Big] , & x>x_2 .
\end{cases}\;}
$$

For a turning point $x_1$ with the classical region on the right ($V$ falling through $E$) the mirror image holds:

$$
\psi(x) \approx
\begin{cases}
\dfrac{D'}{\sqrt{|p(x)|}}\,\exp\!\Big[-\dfrac1\hbar\displaystyle\int_x^{x_1}|p|\,dx'\Big] , & x<x_1 ,\\[2.5ex]
\dfrac{2D'}{\sqrt{p(x)}}\,\sin\!\Big[\dfrac1\hbar\displaystyle\int_{x_1}^xp\,dx' + \dfrac\pi4\Big] , & x>x_1 .
\end{cases}
$$

Three remarks.

- The decaying exponential connects to an oscillation with **twice** the amplitude and a phase of $\pi/4$ measured from the turning point. Compared with a hard wall, where the phase would be zero, the wave leaks a little into the forbidden region.
- From the $\mathrm{Bi}$ row, the growing exponential $|p|^{-1/2}e^{+\frac1\hbar\int|p|}$ connects to $p^{-1/2}\cos[\frac1\hbar\int p + \frac\pi4]$, with no factor of 2. This is needed for tunnelling through a barrier with sloping walls.
- The formulas should be used in the direction in which they were derived: from the decaying solution into the classical region. Going the other way, an undetectably small admixture of the growing solution would be missed.

Sakurai writes the same formulas with $\cos[\,\cdot - \pi/4]$, which equals $\sin[\,\cdot + \pi/4]$.

## Quantization rules

**Two soft turning points.** In a well with turning points $x_1<x_2$ the two connection formulas give two expressions for $\psi$ in the classical region:

$$
\frac{2D'}{\sqrt p}\sin\Big[\theta_1(x) + \frac\pi4\Big] ,\qquad \frac{2D}{\sqrt p}\sin\Big[\theta_2(x) + \frac\pi4\Big] ,\qquad \theta_1 = \frac1\hbar\int_{x_1}^xp\,dx' ,\quad \theta_2 = \frac1\hbar\int_x^{x_2}p\,dx' .
$$

Since $\theta_1 + \theta_2 = \Theta\equiv\frac1\hbar\int_{x_1}^{x_2}p\,dx$ is independent of $x$, the first is $-\sin[\theta_2 - \Theta - \pi/4]$, and it is proportional to the second for all $x$ only if $\Theta + \pi/2 = n\pi$:

$$
\boxed{\,\int_{x_1}^{x_2}p(x)\,dx = \big(n - \tfrac12\big)\pi\hbar ,\qquad n = 1,2,3,\dots\,}
$$

**One wall, one soft turning point.** If the potential has an infinite wall at $x = 0$ and a turning point at $x_2$, the function $\sin[\theta_2(x) + \pi/4]$ must vanish at the wall:

$$
\boxed{\,\int_0^{x_2}p(x)\,dx = \big(n - \tfrac14\big)\pi\hbar ,\qquad n = 1,2,3,\dots\,}
$$

**Summary.**

| boundaries | condition on $\int p\,dx$ |
|---|---|
| two walls | $n\pi\hbar$ |
| one wall, one turning point | $(n - \tfrac14)\pi\hbar$ |
| two turning points | $(n - \tfrac12)\pi\hbar$ |

Each wall costs a phase $\pi$ per reflection and each soft turning point $\pi/2$. Over a full classical period the last line reads $\oint p\,dx = (n - \tfrac12)h$, the Bohr-Sommerfeld rule of the old quantum theory with the half-integer it lacked. In every case $n$ counts the states from the bottom and the wave function has $n - 1$ nodes.

## Tests

!!! example "Harmonic oscillator and half oscillator"

    For $V = \tfrac12m\omega^2x^2$ the turning points are $\pm x_0$ with $x_0 = \sqrt{2E/m\omega^2}$, and

    $$
    \int_{-x_0}^{x_0}\sqrt{2m\big(E - \tfrac12m\omega^2x^2\big)}\,dx = \frac{\pi E}{\omega} = \big(n - \tfrac12\big)\pi\hbar \quad\Rightarrow\quad E_n = \big(n - \tfrac12\big)\hbar\omega ,
    $$

    the exact spectrum. With a wall at $x = 0$ the integral is halved and the rule is $n - \tfrac14$, so $E_n = (2n - \tfrac12)\hbar\omega = \tfrac32,\tfrac72,\tfrac{11}2,\dots\,\hbar\omega$: exactly the odd oscillator levels, which are the true eigenstates of the half oscillator. The exactness is special to the quadratic potential.

!!! example "Bouncing ball"

    A ball of mass $m$ above a hard floor, $V = mgx$ for $x>0$. The turning point is $x_2 = E/mg$ and

    $$
    \int_0^{E/mg}\sqrt{2m(E - mgx)}\,dx = \frac{2\sqrt{2m}}{3mg}E^{3/2} = \big(n - \tfrac14\big)\pi\hbar \quad\Rightarrow\quad E_n = \Big[\tfrac{3\pi}{2}\big(n - \tfrac14\big)\Big]^{2/3}\Big(\frac{mg^2\hbar^2}{2}\Big)^{1/3} .
    $$

    The exact solution is $\psi\propto\mathrm{Ai}[(2m^2g/\hbar^2)^{1/3}(x - E/mg)]$, so the exact levels are $-a_n\,(mg^2\hbar^2/2)^{1/3}$ with $a_n$ the zeros of $\mathrm{Ai}$. In units of $(mg^2\hbar^2/2)^{1/3}$:

    | $n$ | WKB | exact | error |
    |---|---|---|---|
    | 1 | 2.3203 | 2.3381 | $-0.76\%$ |
    | 2 | 4.0818 | 4.0879 | $-0.15\%$ |
    | 3 | 5.5172 | 5.5206 | $-0.06\%$ |
    | 4 | 6.7845 | 6.7867 | $-0.03\%$ |
    | 5 | 7.9425 | 7.9441 | $-0.02\%$ |
    | 10 | 12.8281 | 12.8288 | $-0.005\%$ |

    These agree with Sakurai's Table 2.2. The rule with $n - \tfrac12$ (wrong for a wall) would put the ground state at 1.77, 24 percent low.

!!! example "Power-law wells and the quartic oscillator"

    For $V = \alpha|x|^\nu$ the rule with two turning points gives

    $$
    E_n = \alpha\Big[\big(n - \tfrac12\big)\hbar\sqrt{\frac{\pi}{2m\alpha}}\;\frac{\Gamma(\frac1\nu + \frac32)}{\Gamma(\frac1\nu + 1)}\Big]^{2\nu/(\nu+2)} .
    $$

    For $\nu = 2$ this is the oscillator. For $\nu = 4$ with $\hbar = m = \alpha = 1$, against a numerical diagonalization:

    | $n$ | WKB | exact | error |
    |---|---|---|---|
    | 1 | 0.5463 | 0.6680 | $-18.2\%$ |
    | 2 | 2.3636 | 2.3936 | $-1.3\%$ |
    | 3 | 4.6705 | 4.6968 | $-0.56\%$ |
    | 4 | 7.3148 | 7.3357 | $-0.29\%$ |
    | 5 | 10.2265 | 10.2443 | $-0.17\%$ |
    | 8 | 20.2082 | 20.2209 | $-0.06\%$ |

    The ground state is poor because one half wavelength spans the whole well, so the potential is nowhere slowly varying on that scale. The error falls roughly as $1/n^2$.

## Radial problems and the Langer correction

For a central potential the radial function $u(r) = rR(r)$ obeys a one-dimensional equation with the effective potential $V_{\rm eff} = V(r) + \hbar^2l(l+1)/(2mr^2)$ ([[central-potentials-and-spherical-harmonics]]). For $l>0$ there are two soft turning points and the $n - \tfrac12$ rule applies with $n\to n_r = 1,2,\dots$ counting radial states.

For hydrogen, with $\Lambda$ standing for $l(l+1)$,

$$
\int_{r_1}^{r_2}\sqrt{2m\Big(E + \frac{e^2}{4\pi\epsilon_0r}\Big) - \frac{\hbar^2\Lambda}{r^2}}\;dr = \pi\Big[\frac{e^2}{4\pi\epsilon_0}\sqrt{\frac{m}{-2E}} - \hbar\sqrt\Lambda\Big] = \big(n_r - \tfrac12\big)\pi\hbar ,
$$

so

$$
E = \frac{E_1}{\big[n_r - \tfrac12 + \sqrt\Lambda\,\big]^2} ,\qquad E_1 = -13.6\ \text{eV} .
$$

With $\Lambda = l(l+1)$ this resembles the Bohr formula but is not it. The **Langer correction** replaces $l(l+1)$ by $(l + \tfrac12)^2$ in the WKB integrand. Then $n_r - \tfrac12 + l + \tfrac12 = n_r + l = n$ and the Bohr levels come out exactly, for every $l$ including $l = 0$.

| $l$ | $n_r$ | $\Lambda = l(l+1)$ | $\Lambda = (l+\frac12)^2$ | exact |
|---|---|---|---|---|
| 0 | 1 | $-2.0000$ | $-0.5000$ | $-0.5000$ |
| 0 | 2 | $-0.2222$ | $-0.1250$ | $-0.1250$ |
| 0 | 3 | $-0.0800$ | $-0.0556$ | $-0.0556$ |
| 1 | 1 | $-0.1365$ | $-0.1250$ | $-0.1250$ |
| 1 | 2 | $-0.0589$ | $-0.0556$ | $-0.0556$ |
| 1 | 3 | $-0.0326$ | $-0.0313$ | $-0.0313$ |

(Energies in hartree.) The reason for the correction is that $r = 0$ is a singular end point, not an ordinary turning point: the centrifugal term varies too fast there for the WKB condition to hold. The substitution $r = e^x$ maps the half line to the whole line, where the standard derivation applies, and in the new variable the centrifugal coefficient becomes $(l + \tfrac12)^2$. Without the correction the $l = 0$ case is useless, as the first rows show.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 9.3, Eqs. (9.32)-(9.52), Examples 9.3 (half oscillator) and 9.4 (two turning points); Problems 9.6 and 9.7 (bouncing ball), 9.8 (oscillator), 9.10 (downward-sloping turning point), 9.13 (power-law potential, whose stated answer is the formula above), 9.15 and 9.16 (radial WKB and hydrogen with $l(l+1)$). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 2.5.4, Eqs. (2.251)-(2.262) and Table 2.2, pp. 105-108 (connection formulas, the consistency condition, the Sommerfeld-Wilson rule, the bouncing ball); Sec. 2.5.3, p. 101, for the exact linear-potential solution.

The Langer correction is not in either book. Original paper, quoted from memory and to verify: R. E. Langer, Phys. Rev. 51, 669 (1937).

All tables are computed in `griffiths/ch09_wkb.py` (sections A, B and F).
