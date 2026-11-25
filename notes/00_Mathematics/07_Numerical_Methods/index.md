Numerical methods with their error estimates. Most quantities in this notebook are integrals, roots or interpolated values that cannot be found in closed form. Examples include the Boys function behind Gaussian integrals, the grids of density functional theory, and the turning points of WKB. This chapter starts with what limits every such calculation, the errors of floating-point arithmetic and of truncated formulas, and will add the methods themselves. Large linear-algebra problems such as iterative diagonalization belong to Part 7.

## What this chapter is about

A computed number carries two kinds of error:

- **round-off**, because every floating-point operation rounds to about 16 digits;
- **truncation**, because a formula approximates a limit (a derivative, an integral, an infinite series).

They behave in opposite ways as a step size shrinks, so there is a best step. On top of both, the **conditioning** of a problem decides how many digits any algorithm can keep, and the **stability** of an algorithm decides whether it keeps them.

## Why it matters

- **Energy differences cancel.** Reaction, binding and excitation energies are small differences of large totals, so absolute errors in the totals matter.
- **Finite differences have a floor.** Numerical gradients and Hessians, used to check analytic derivatives, cannot be more accurate than about $10^{-11}$ (central) or $10^{-8}$ (forward) in relative terms, and need tightly converged energies.
- **Near-linear dependence costs digits.** An ill-conditioned overlap matrix loses $\log_{10}\kappa$ digits, which is why basis sets are pruned by canonical orthogonalization.

## The main ideas, in order

1. **Floating point:** machine epsilon, rounding of every operation, comparisons with tolerances.
2. **Cancellation** and how to rewrite formulas to avoid it; compensated summation.
3. **Truncation error** of finite differences, the optimal step, Richardson extrapolation.
4. **Conditioning and stability:** condition numbers and backward-stable algorithms.

## How to read it

**Path.** [[floating-point-and-numerical-error]].

**Needs.** Chapter 1 (matrices) and Chapter 4 (Taylor series, for truncation errors).

**Leads to.** Eigenvalue accuracy and backward stability in Part 7 ([[floating-point-and-eigenvalue-perturbation]]), and the error estimates of every worked example.

**Planned sections:** Numerical integration and quadrature; Root finding; Interpolation.
