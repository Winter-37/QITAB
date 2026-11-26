---
id: laplace-transform
title: The Laplace transform - definition and existence, the standard table, derivatives and shifts, solving linear ODEs and rate equations, convolution, inversion by the Bromwich integral and residues, and exponential sums for 1/x behind Laplace-transformed MP2
summary: The Laplace transform f(s) = ∫₀^∞ e^{−st} F(t) dt turns functions of time on [0, ∞) into analytic functions in a right half plane. Derivatives become multiplication by s minus initial values, so linear ODEs with initial conditions become algebraic equations. Shifts and Heaviside steps become exponential factors, and convolutions become products. Partial fractions and the Bromwich integral, evaluated as a sum of residues of e^{st} f(s), invert it. Applied to rate equations, it gives the consecutive-reaction kinetics A → B → C in a few lines. The transform of e^{−iHt} is the resolvent. Read the other way, the identity 1/x = ∫₀^∞ e^{−xt} dt, discretized as a short sum of exponentials, factorizes an energy denominator into separate occupied and virtual parts. That is the idea of Laplace-transformed MP2. Worked examples: the table, kinetics, a damped oscillator, convolution, inversion by residues, exponential-sum fits of 1/x, and a Laplace-factorized MP2-type energy.
status: in-progress
kind: theory
level: intermediate
tags: [laplace-transform, integral-transform, bromwich-integral, inverse-laplace-transform, convolution-theorem, heaviside-function, transfer-function, rate-equations, consecutive-reactions, resolvent, exponential-sum, laplace-mp2, energy-denominators]
prerequisites: [laurent-series-singularities-and-residues, fourier-transforms-and-the-dirac-delta]
related: [first-order-differential-equations, second-order-linear-differential-equations, neumann-series-and-operator-expansions, gaussian-quadrature, numerical-integration-of-odes, moller-plesset-and-coupled-cluster-perturbation-theory]
key: lt
order: 40
date: 2026-11-26
---

$F(t)$ is defined for $t\ge0$; $f(s) = \mathcal L[F](s)$ with complex $s$. $u(t - a)$ is the Heaviside step at $t = a$. The convolution on $[0, t]$ is $(F_1 * F_2)(t) = \int_0^tF_1(t - z)F_2(z)\,dz$. Notation follows Arfken Secs. 15.8–15.12.

## Definition and table

**Definition** (Arfken Eq. 15.99):

$$
f(s) = \mathcal L[F](s) = \int_0^\infty e^{-st}F(t)\,dt .
\label{lt}
$$

**Existence.** The integral converges for $\mathrm{Re}\,s > \sigma_0$ if $F$ is piecewise continuous and of exponential order: $|F|\le Me^{\sigma_0t}$ for large $t$. In that half plane $f(s)$ is analytic ([[analytic-functions-and-cauchy-theorem]]). Its singularities lie to the left, and they encode the long-time behaviour of $F$.

**Relation to Fourier.** For $F = 0$ at $t < 0$, $f(-i\omega)$ is the Fourier transform of $F$ ([[fourier-transforms-and-the-dirac-delta]]). The Laplace variable $s$ is a frequency continued into the complex plane, which buys convergence for growing or non-decaying $F$.

**Standard transforms** (Arfken Sec. 15.8):

| $F(t)$ | $f(s)$ |
|---|---|
| $1$ | $1/s$ |
| $t^n$ | $n!/s^{n+1}$ |
| $e^{-at}$ | $1/(s + a)$ |
| $t\,e^{-at}$ | $1/(s + a)^2$ |
| $\sin\omega t$ | $\omega/(s^2 + \omega^2)$ |
| $\cos\omega t$ | $s/(s^2 + \omega^2)$ |
| $u(t - a)$ | $e^{-as}/s$ |
| $\delta(t - a)$ | $e^{-as}$ |

## Properties

**Rules** (Arfken Secs. 15.9–15.10):

- **Derivatives.** $\mathcal L[F'] = sf(s) - F(0)$ and $\mathcal L[F''] = s^2f(s) - sF(0) - F'(0)$. Differentiation becomes multiplication, and the initial conditions are built in.
- **Shifts.** $\mathcal L[e^{-at}F(t)] = f(s + a)$ and $\mathcal L[F(t - a)u(t - a)] = e^{-as}f(s)$.
- **Moments and integrals.** $\mathcal L[t^nF] = (-d/ds)^nf$ and $\mathcal L[\int_0^tF] = f(s)/s$.
- **Limits.** $F(0^+) = \lim_{s\to\infty}sf(s)$, and $F(\infty) = \lim_{s\to0}sf(s)$ when the limit exists.

**The convolution (Faltung) theorem** (Arfken Sec. 15.11):

$$
\mathcal L[F_1 * F_2] = f_1(s)\,f_2(s) .
\label{conv}
$$

For a linear time-invariant system, the response to an input is the convolution of the input with the impulse response. Its transform is the input's transform times the transfer function (Arfken Sec. 15.7).

## Solving linear equations

**The method.** Transform the equation, solve the resulting algebra for $f(s)$, decompose into partial fractions, and invert term by term using the table.

**Consecutive first-order reactions.** $A\to B\to C$ with rate constants $k_1$, $k_2$ and $[A](0) = 1$, $[B](0) = 0$. The rate equations $[A]' = -k_1[A]$ and $[B]' = k_1[A] - k_2[B]$ transform to $s\tilde A - 1 = -k_1\tilde A$ and $s\tilde B = k_1\tilde A - k_2\tilde B$. Hence

$$
\tilde B(s) = \frac{k_1}{(s + k_1)(s + k_2)}\quad\Rightarrow\quad [B](t) = \frac{k_1}{k_2 - k_1}\big(e^{-k_1t} - e^{-k_2t}\big),\qquad t_{\max} = \frac{\ln(k_1/k_2)}{k_1 - k_2} .
$$

The poles of $\tilde B$ sit at the negative rate constants. Every linear kinetic scheme works this way, with a matrix $(s\mathbf 1 - \mathbf K)^{-1}$ in place of the scalar fraction.

**Oscillators.** Damped and driven oscillators transform the same way (Arfken Examples 15.9.1, 15.10.1, 15.11.1). The poles of $1/(s^2 + 2\gamma s + \omega_0^2)$ at $-\gamma\pm i\omega_d$ give the damped oscillation ([[second-order-linear-differential-equations]]).

**The resolvent.** For a time-independent Hamiltonian, $\mathcal L[e^{-i\hat Ht}] = (s + i\hat H)^{-1}$. With $s = -iE + \eta$ this is $i(E - \hat H + i\eta)^{-1}$, $i$ times the retarded resolvent of [[neumann-series-and-operator-expansions]]. Time propagation and energy-domain Green's functions are the two sides of one transform.

## Inversion

**The Bromwich integral** (Arfken Sec. 15.12, Eq. 15.212):

$$
F(t) = \frac1{2\pi i}\int_{\gamma - i\infty}^{\gamma + i\infty}e^{st}f(s)\,ds,
$$

taken along a vertical line to the right of every singularity of $f$.

**By residues.** For $t > 0$, close the contour to the left. When $f\to0$ at large $|s|$, Jordan's lemma removes the arc ([[laurent-series-singularities-and-residues]]), and

$$
F(t) = \sum_{\text{poles }s_k}\mathrm{Res}_{s_k}\big[e^{st}f(s)\big].
$$

**Reading the result.**

- A simple pole at $s_k$ contributes $e^{s_kt}$ times its residue.
- A double pole contributes $t\,e^{s_kt}$ terms.
- The poles' real parts are decay rates and their imaginary parts frequencies.
- Branch cuts give non-exponential (power-law) long-time tails.

Partial fractions are the same computation done by hand.

## Exponential sums for 1/x: Laplace-transformed MP2

**The identity.** For $x > 0$,

$$
\frac1x = \int_0^\infty e^{-xt}\,dt\approx\sum_{k=1}^Kw_k\,e^{-\alpha_kx}\qquad(x\in[x_{\min}, x_{\max}]).
\label{expsum}
$$

This is Eq. [[#lt]] with $F = 1$ read backwards. A short exponential sum approximates $1/x$ uniformly on a finite interval. With nodes and weights optimized for the ratio $R = x_{\max}/x_{\min}$ (minimax exponential sums), the error falls roughly exponentially in $K$. A plain Gauss–Laguerre rule for the integral is good only near $x_{\min}$, because $e^{-xt}$ at large $x$ is far from a low-degree polynomial times $e^{-t}$ ([[gaussian-quadrature]]).

**Why it matters for MP2.** The closed-shell MP2 energy has denominators $\Delta_{ijab} = \varepsilon_a + \varepsilon_b - \varepsilon_i - \varepsilon_j > 0$. With Eq. [[#expsum]],

$$
\frac1{\Delta_{ijab}} \approx \sum_kw_k\,e^{-\alpha_k(\varepsilon_a - \varepsilon_i)}\,e^{-\alpha_k(\varepsilon_b - \varepsilon_j)} .
$$

The denominator no longer couples the four indices. Each quadrature point becomes a product of occupied and virtual factors, which can be absorbed into energy-weighted occupied and virtual density matrices. That is what allows atomic-orbital-based and reduced-scaling MP2 formulations, and their combination with density fitting and Cholesky decomposition. The idea is due to Almlöf (Chem. Phys. Lett. 181, 319 (1991); to verify, not consulted). The same factorization is used in RPA and in Laplace-transformed coupled-cluster triples (general knowledge).

## Worked examples

!!! example "Table, kinetics, inversion and exponential sums (computed for this note)"
    **Table.** sympy reproduces every row above, including $\mathcal L[u(t - 2)] = e^{-2s}/s$ and $\mathcal L[te^{-at}] = 1/(s + a)^2$.

    **Kinetics.** Inverting $k_1/((s + k_1)(s + k_2))$ gives $\frac{k_1}{k_1 - k_2}(e^{-k_2t} - e^{-k_1t})$, the formula above. For $k_1 = 2$ and $k_2 = 0.5$:

    - $[B](3) = 0.2942018773$, equal to a numerical integration to all digits;
    - the maximum is at $t_{\max} = \ln4/1.5 = 0.92420$.

    **Damped oscillator.** $y'' + 0.4y' + 4y = 0$ with $y(0) = 1$, $y'(0) = 0$ gives $\tilde y = (s + 0.4)/(s^2 + 0.4s + 4)$. Its inverse is $e^{-t/5}\big[\cos\frac{3\sqrt{11}}5t + \frac{\sqrt{11}}{33}\sin\frac{3\sqrt{11}}5t\big]$.

    **Convolution, Eq. [[#conv]].** $\mathcal L[e^{-t} * \sin t] = 1/(s^3 + s^2 + s + 1) = \frac1{s + 1}\cdot\frac1{s^2 + 1}$.

    **Bromwich by residues.** $f = 1/((s + 1)(s + 3)^2)$ has a simple pole at $-1$ and a double pole at $-3$. Summing the residues of $e^{st}f$ gives $\tfrac14e^{-3t}(e^{2t} - 1 - 2t) = \tfrac14e^{-t} - \tfrac14e^{-3t} - \tfrac12te^{-3t}$, identical to sympy's inverse transform. The double pole gives the $t\,e^{-3t}$ term.

    **Exponential sums for $1/x$ on $[1, 100]$** (fitted by reweighted least squares, close to minimax), maximum relative error:

    | $K$ | 2 | 4 | 6 | 8 |
    |---|---|---|---|---|
    | error | $3.4\times10^{-1}$ | $2.2\times10^{-2}$ | $1.1\times10^{-3}$ | $4.9\times10^{-5}$ |

    Each pair of extra terms gains a factor of about 20. Gauss–Laguerre with $K = 8$ is exact at $x = 1$, but wrong by 20% at $x = 10$ and by 100% at $x = 100$.

    **A Laplace-factorized MP2-type energy.** Random model with 5 occupied and 20 virtual levels, denominators between 3.81 and 27.62, and $E^{(2)} = -\sum v^2/(\Delta_{ia} + \Delta_{jb})$. The exact value is $-2.1752601551$. An 8-term exponential sum fitted on $[3.81, 27.62]$ gives $-2.1752601550$, a relative error of $4\times10^{-11}$. The ratio $R = 7.2$ here is small; real molecules with core orbitals and diffuse virtuals have much larger $R$ and need more points.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 15.7 (transfer functions), Sec. 15.8 (Laplace transforms, Eq. 15.99, table, Examples 15.8.1–15.8.2), Sec. 15.9 (transforms of derivatives, Examples 15.9.1–15.9.3), Sec. 15.10 (other properties, Example 15.10.1), Sec. 15.11 (convolution theorem, Example 15.11.1), Sec. 15.12 (inverse transform, Bromwich integral, Eq. 15.212, Example 15.12.1). The Laplace-MP2 reference is from memory and marked to verify. The exponential-sum fits are computed here, not taken from published minimax tables. Calculations in `Claude outputs/part0_math_batchG.py`, section E.
