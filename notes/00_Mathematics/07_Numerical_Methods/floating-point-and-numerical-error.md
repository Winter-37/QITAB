---
id: floating-point-and-numerical-error
title: Floating-point arithmetic and numerical error - machine epsilon, round-off, catastrophic cancellation, truncation error, the optimal finite-difference step, conditioning and stability, and Richardson extrapolation
summary: A double-precision number carries about 16 significant digits, so every operation commits a relative error up to machine epsilon, 2.2 × 10⁻¹⁶. Round-off is harmless until two nearly equal numbers are subtracted. Then the relative error is amplified by the size of the cancellation, which ruins naive formulas such as (1 − cos x)/x² or the small root of a quadratic. Truncation error is the error of the approximation itself: Taylor terms dropped from a finite difference or quadrature rule. The two compete, so a finite-difference derivative has an optimal step near ε^{1/3}. Conditioning measures how a problem amplifies input errors, whatever the algorithm; stability measures whether an algorithm adds more than necessary. A linear solve loses about log₁₀ κ digits. Richardson extrapolation cancels the leading truncation error. Worked examples for each effect, including the Hilbert matrix and Kahan summation.
status: in-progress
kind: theory
level: introductory
tags: [floating-point, machine-epsilon, round-off-error, catastrophic-cancellation, truncation-error, finite-difference, optimal-step, condition-number, numerical-stability, richardson-extrapolation, kahan-summation, ieee-754]
prerequisites: [taylor-and-maclaurin-expansions, matrices-and-determinants]
related: [error-analysis-and-propagation-of-uncertainty, floating-point-and-eigenvalue-perturbation, differential-calculus, integral-calculus, asymptotic-expansions, matrix-eigenvalue-problem]
key: fdopt
order: 10
date: 2026-11-25
---

IEEE 754 double precision unless stated: 53-bit significand. $\mathrm{fl}(x)$ is the floating-point number nearest $x$; $\varepsilon = 2^{-52} = 2.22\times10^{-16}$ is machine epsilon (the gap between 1 and the next number). The unit round-off is $u = \varepsilon/2$.

## Floating-point numbers

**Representation.** A double is $\pm m\times2^e$ with a 53-bit significand $m\in[1, 2)$ and an exponent $e$ from $-1022$ to $1023$. Its range runs from $2.2\times10^{-308}$ (smallest normal number) to $1.8\times10^{308}$. Single precision has a 24-bit significand and $\varepsilon = 1.19\times10^{-7}$, about 7 digits. It is used on GPUs and in mixed-precision linear algebra.

**Every operation rounds.** For each basic operation $\circ$,

$$
\mathrm{fl}(a\circ b) = (a\circ b)(1 + \delta),\qquad|\delta|\le u .
$$

Consequences:

- **Inexact decimals.** Most decimal fractions are not representable: $0.1 + 0.2 - 0.3 = 5.55\times10^{-17}$, not 0.
- **Lost increments.** $1 + \varepsilon/2$ rounds to 1.
- **Non-associativity.** Floating-point addition is not associative, so the order of a sum changes its last digits. Parallel reductions are not bitwise reproducible for this reason.

**Comparisons.** Two computed numbers should be compared with a tolerance, $|a - b|\le\tau\max(|a|, |b|)$, never with `==`. Convergence thresholds in SCF and optimization codes (energy changes of $10^{-10}$ $E_h$, for instance) are set well above $\varepsilon|E|$ for the same reason.

## Round-off and cancellation

**Catastrophic cancellation.** Subtracting two nearly equal numbers $a\approx b$, each carrying relative error $u$, gives an absolute error about $u|a|$ in a result of size $|a - b|$. The relative error is amplified by $|a|/|a - b|$. The subtraction itself is exact; it exposes errors already present.

**Cures.** Rewrite the formula algebraically so the cancellation never happens:

- **$(1 - \cos x)/x^2$** becomes $2\sin^2(x/2)/x^2$.
- **The small root of a quadratic.** For $x^2 + bx + c$ with $b^2\gg|c|$, compute the large root with the sign that adds, then the small one as $c/x_{\rm large}$ (Vieta).
- **$e^x - 1$ and $\ln(1 + x)$** use `expm1` and `log1p`.
- **Energy differences.** Reaction energies, binding energies and excitation energies are small differences of large totals. They inherit the absolute errors of the totals. That is why correlated methods are often formulated to compute the difference directly (equation-of-motion, symmetry-adapted perturbation theory).

**Accumulation in sums.** Summing $n$ numbers left to right has an error bound growing like $nu$. Pairwise summation reduces this to $u\log n$, and Kahan's compensated summation to about $u$, independent of $n$.

## Truncation error

**Definition.** Truncation error is the error of the mathematical approximation: Taylor terms omitted from a finite difference, a quadrature rule or an ODE step ([[taylor-and-maclaurin-expansions]]). It is present even in exact arithmetic.

**Finite differences.**

$$
\frac{f(x + h) - f(x)}h = f'(x) + \frac h2f''(\xi),\qquad
\frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{h^2}6f'''(\xi).
$$

**The optimal step.** Round-off in evaluating $f$ adds an error of about $\varepsilon|f|/h$, which grows as $h$ shrinks. For the central difference the total error is about $\frac{h^2}6|f'''| + \frac{\varepsilon|f|}h$. It is minimized at

$$
h_{\rm opt} = \Big(\frac{3\varepsilon|f|}{|f'''|}\Big)^{1/3}\approx10^{-5}\text{ (relative to the scale of }x\text{)},\qquad\text{error}\sim\varepsilon^{2/3}\approx10^{-11} .
\label{fdopt}
$$

For the forward difference, $h_{\rm opt}\sim\sqrt\varepsilon\approx10^{-8}$ and the best error is about $10^{-8}$. Finite-difference gradients and Hessians of SCF energies need the SCF converged far tighter than the step, or the round-off term dominates.

**Richardson extrapolation.** If $A(h) = A + ch^p + O(h^{p+1})$, then $\frac{2^pA(h/2) - A(h)}{2^p - 1}$ removes the $h^p$ term. Applied to the trapezoid rule ($p = 2$) it gives Simpson's rule, and repeated it gives Romberg integration. The same idea extrapolates basis-set energies to the complete-basis limit.

## Conditioning and stability

**Condition number.** A problem is ill-conditioned if small relative changes in the input cause large relative changes in the exact answer. For solving $\mathbf A\mathbf x = \mathbf b$ the condition number is $\kappa(\mathbf A) = \|\mathbf A\|\|\mathbf A^{-1}\|$, the ratio of largest to smallest singular value. The relative error of the solution can be as large as $\kappa$ times the relative error of the data. With data good to $\varepsilon$, about $\log_{10}\kappa$ digits are lost. Conditioning is a property of the problem; no algorithm can beat it.

**In quantum chemistry.** Near-linear dependence in a basis set makes the overlap matrix ill-conditioned. Canonical orthogonalization removes eigenvectors of $\mathbf S$ below a threshold (often $10^{-6}$–$10^{-7}$) before the generalized eigenproblem is solved.

**Stability.** An algorithm is backward stable if its result is the exact answer for slightly perturbed data (perturbations of order $u$). A backward-stable algorithm applied to a well-conditioned problem gives an accurate answer. Gaussian elimination with partial pivoting, Householder QR and the symmetric eigensolvers in LAPACK are backward stable. Forming $\mathbf A^{\rm T}\mathbf A$ to solve least squares squares the condition number and is avoided for that reason. What this means for eigenvalues and eigenvectors, including near-degenerate ones, is worked out in [[floating-point-and-eigenvalue-perturbation]].

## Worked examples

!!! example "Each effect, measured (computed for this note)"
    **Machine epsilon.** $2.220446\times10^{-16}$ in double and $1.192093\times10^{-7}$ in single precision. $1 + \varepsilon/2 = 1$ is true; $0.1 + 0.2 - 0.3 = 5.551\times10^{-17}$.

    **Cancellation.**

    - $(1 - \cos x)/x^2$ at $x = 10^{-4}$: naive 0.4999999970, rewritten 0.4999999996. At $x = 10^{-8}$: naive 0 (all digits cancelled), rewritten 0.5000000000.
    - The small root of $x^2 + 10^8x + 1$: naive $-7.45\times10^{-9}$ (wrong by 25%), stable $-1.0000000000\times10^{-8}$.

    **Optimal step.** Central-difference derivative of $e^x$ at $x = 1$:

    | $h$ | $10^{-1}$ | $10^{-3}$ | $10^{-5}$ | $6\times10^{-6}$ | $10^{-7}$ | $10^{-9}$ | $10^{-11}$ |
    |---|---|---|---|---|---|---|---|
    | error | $4.5\times10^{-3}$ | $4.5\times10^{-7}$ | $5.9\times10^{-11}$ | $1.5\times10^{-11}$ | $5.9\times10^{-11}$ | $6.6\times10^{-9}$ | $1.0\times10^{-5}$ |

    The error falls as $h^2$, bottoms out near $h = 6\times10^{-6}$, and then rises as $1/h$. Eq. [[#fdopt]] predicts $h_{\rm opt} = (3\varepsilon)^{1/3} = 8.7\times10^{-6}$. The forward difference reaches only $6.6\times10^{-9}$ at $h = 10^{-8}$, and $4.3\times10^{-4}$ at $h = 10^{-12}$.

    **Summation.** Adding 0.1 two hundred thousand times in single precision: naive 19959.49, Kahan 20000.00.

    **Conditioning.** Solving $\mathbf H\mathbf x = \mathbf H\mathbf 1$ for Hilbert matrices $H_{ij} = 1/(i + j - 1)$:

    | $N$ | $\kappa$ | relative error of $\mathbf x$ |
    |---:|---:|---:|
    | 4 | $1.6\times10^4$ | $3\times10^{-14}$ |
    | 8 | $1.5\times10^{10}$ | $7\times10^{-8}$ |
    | 12 | $1.6\times10^{16}$ | $0.13$ |

    The stable solver loses the predicted $\log_{10}\kappa$ digits and no more. At $N = 12$ nothing is left.

    **Richardson.** The trapezoid rule for $\int_0^1e^x$: errors $1.432\times10^{-3}$ ($N = 10$) and $3.580\times10^{-4}$ ($N = 20$), ratio 4.000. $(4T_{20} - T_{10})/3$ has error $6.0\times10^{-8}$.

## Source

The material is standard numerical analysis, not in Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005). That book's Sec. 5.9 gives the Euler–Maclaurin formula behind the trapezoid error. The thresholds quoted for SCF codes and canonical orthogonalization are typical values, not universal ones. Calculations in `Claude outputs/part0_math_batchE.py`, section F.
