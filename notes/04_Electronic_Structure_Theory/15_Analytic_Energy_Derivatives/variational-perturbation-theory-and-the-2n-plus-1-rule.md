---
id: variational-perturbation-theory-and-the-2n-plus-1-rule
title: Variational perturbation theory - response equations to any order, the 2n + 1 rule for energy derivatives, and the 2n + 2 rule for multipliers
summary: For an energy E(λ, ε) that is stationary in its parameters λ at every perturbation strength ε, differentiating the stationarity condition gives one linear response equation per order, all with the same Hessian. The derivative expressions then simplify. The second derivative needs first-order parameters; it can be written asymmetrically, with errors linear in the parameter error, or symmetrically, with errors quadratic. The third derivative still needs only first-order parameters, while the fourth needs second-order ones: n-th order parameters give derivatives through order 2n + 1 (Wigner). For a single linear perturbation the third derivative equals the third derivative of E along the straight line λ = ελ⁽¹⁾. Lagrange multipliers obey the stricter 2n + 2 rule. Demonstrated for the RHF static hyperpolarizability of HF/6-31G.
status: in-progress
kind: derivation
level: advanced
tags: [variational-perturbation-theory, 2n-plus-1-rule, wigner, response-equations, hyperpolarizability, cphf, lagrangian, finite-field]
prerequisites: [lagrangian-for-nonvariational-energies, cphf-closed-shell]
related: [rspt-wigner-rule-and-hylleraas-functional, rhf-analytic-hessian, molecular-properties-and-response, quasienergy-and-time-dependent-variational-principle, coupled-cluster-response-functions]
conventions: [atomic-units]
key: third
order: 110
date: 2026-11-24
---

$E(\boldsymbol\lambda,\boldsymbol\varepsilon)$ is an energy function of variational parameters $\boldsymbol\lambda$ (orbital rotations, CI coefficients) and perturbation strengths $\boldsymbol\varepsilon$ (fields, nuclear displacements). Subscripts on $E$ denote partial derivatives, e.g. $E_{A i} = \partial^2E/\partial\varepsilon_A\partial\lambda_i$, with $A, B, C, D$ for perturbations and $i, j, k, l$ for parameters, summed when repeated. A prime on $\lambda$ denotes a derivative of the optimal parameters, $\lambda^A_i = \partial\lambda_i/\partial\varepsilon_A$. All derivatives are taken at $\boldsymbol\varepsilon = 0$.

## Total and partial derivatives

**The chain rule.** The perturbation strengths are independent variables; the parameters follow them through the optimization, $\boldsymbol\lambda = \boldsymbol\lambda(\boldsymbol\varepsilon)$. Hence

$$
\frac{dE}{d\varepsilon_A} = E_A + E_i\,\lambda^A_i.
$$

**Variational condition.** Variational methods (HF, KS-DFT, MCSCF, CI in its own coefficients) satisfy $E_i(\boldsymbol\lambda(\boldsymbol\varepsilon),\boldsymbol\varepsilon) = 0$ at every field strength. The first derivative is then purely explicit, $dE/d\varepsilon_A = E_A$: the Hellmann-Feynman form of [[hellmann-feynman-and-virial-theorems]].

## Response equations

Because $E_i = 0$ holds identically in $\boldsymbol\varepsilon$, all its total derivatives vanish. First and second order:

$$
E_{Ai} + E_{ij}\lambda^A_j = 0,
\label{first}
$$

$$
E_{ABi} + E_{Aij}\lambda^B_j + E_{Bij}\lambda^A_j + E_{ijk}\lambda^A_j\lambda^B_k + E_{ij}\lambda^{AB}_j = 0.
\label{second}
$$

Every order is a linear equation with the same matrix, the parameter Hessian $E_{ij}$. Only the right-hand side changes. For HF with $\varepsilon$ a field, Eq. [[#first]] is the CPHF equation of [[cphf-closed-shell]].

## Energy derivatives

**Second order.** Differentiating $dE/d\varepsilon_A = E_A$ once more:

$$
\frac{d^2E}{d\varepsilon_A d\varepsilon_B} = E_{AB} + E_{Ai}\lambda^B_i.
\label{asym}
$$

This form is not symmetric in $A$ and $B$. Starting instead from the chain rule before using $E_i = 0$ gives the symmetric form

$$
\frac{d^2E}{d\varepsilon_A d\varepsilon_B} = E_{AB} + E_{Ai}\lambda^B_i + E_{Bi}\lambda^A_i + E_{ij}\lambda^A_i\lambda^B_j.
\label{sym}
$$

With exact $\boldsymbol\lambda^A$ the two agree: insert Eq. [[#first]] into the last term. With an approximate response $\boldsymbol\lambda^A + \boldsymbol\delta$ (an unconverged iterative solve), the errors behave differently:

- **Asymmetric form.** The error is $E_{Ai}\delta_i$, linear in the error of the response.
- **Symmetric form.** For $A = B$ the error is exactly $\boldsymbol\delta^{\mathsf T}\mathbf E_{\lambda\lambda}\boldsymbol\delta$, quadratic, since Eq. [[#sym]] is stationary in $\boldsymbol\lambda^A$.

NRS cite H. Sellers, Int. J. Quantum Chem. 30, 433 (1986) for the higher accuracy of the symmetric form.

**Third order: only first-order parameters.** Differentiating Eq. [[#asym]] brings in $\lambda^{BC}$ through the term $E_{Ai}\lambda^{BC}_i$. By Eq. [[#first]], $E_{Ai} = -E_{ij}\lambda^A_j$, so this term becomes $-\lambda^A_jE_{ji}\lambda^{BC}_i$. Eq. [[#second]] (for the pair $B, C$) then replaces $E_{ij}\lambda^{BC}_i$ by terms with first-order parameters only. The result is

$$
\frac{d^3E}{d\varepsilon_A d\varepsilon_B d\varepsilon_C} = E_{ABC} + \sum_{\text{3 perm.}}E_{ABi}\lambda^C_i + \sum_{\text{3 perm.}}E_{Aij}\lambda^B_i\lambda^C_j + E_{ijk}\lambda^A_i\lambda^B_j\lambda^C_k,
\label{third}
$$

with the sums over the three ways of choosing which perturbation(s) enter the partial derivative.

**The line form.** For a single perturbation $\varepsilon$ the right-hand side of Eq. [[#third]] is

$$
\frac{d^3E}{d\varepsilon^3} = \frac{d^3}{ds^3}E\big(s\boldsymbol\lambda^{(1)},s\big)\Big|_{s=0},
\label{line}
$$

the third derivative of the energy along the *straight line* through parameter space with the first-order slope. Expanding $E(s\boldsymbol\lambda^{(1)},s)$ to third order gives exactly the four terms of Eq. [[#third]] with $A = B = C$. The true optimal path curves, $\boldsymbol\lambda(\varepsilon) = \varepsilon\boldsymbol\lambda^{(1)} + \tfrac12\varepsilon^2\boldsymbol\lambda^{(2)} + \cdots$, but the curvature does not matter through third order. This gives a practical recipe: one first-order (CPHF) solve plus energies along a line give the hyperpolarizability $\beta$.

**Fourth order.** Here no reduction removes the second-order parameters: the expression contains $\lambda^{AB}$ contracted with the Hessian and with third derivatives. The **$2n+1$ rule** (Wigner; already in Hylleraas, 1930) states: parameters through order $n$ determine energy derivatives through order $2n+1$. The perturbation-theory version is in [[rspt-wigner-rule-and-hylleraas-functional]].

## Non-variational energies and the 2n + 2 rule

**Lagrangian.** When the energy is not stationary in all parameters (CI on HF orbitals, MP2, coupled cluster), it is made stationary with multipliers $\bar{\boldsymbol\lambda}$, as in [[lagrangian-for-nonvariational-energies]]. For CI with HF orbitals NRS write $L = E_{CI}(\mathbf R,\boldsymbol\kappa) + \bar\kappa_{pq}\,\partial E_{HF}/\partial\kappa_{pq}$. Stationarity gives:

- the CI conditions;
- the HF conditions;
- a single linear equation $\partial E_{CI}/\partial\kappa_{rs} + \bar\kappa_{pq}\,\partial^2E_{HF}/\partial\kappa_{pq}\partial\kappa_{rs} = 0$ for the multipliers, independent of the perturbation.

**First derivative.** $dL/d\varepsilon_A = \partial E_{CI}/\partial\varepsilon_A + \bar\kappa_{pq}\,\partial^2E_{HF}/\partial\varepsilon_A\partial\kappa_{pq}$, with zeroth-order multipliers only.

**2n + 2 rule.** In the second derivative of $L$, the first-order multipliers multiply the left-hand side of the first-order HF response equation, which vanishes. So multipliers through order $n$ give derivatives through order $2n+2$. The second derivative needs first-order parameters but only zeroth-order multipliers. NRS cite Helgaker et al., Chem. Rev. 112, 543 (2012) for the proof.

## Worked example

!!! example "RHF static hyperpolarizability of HF/6-31G by the 2n + 1 rule (computed for this note)"
    HF molecule, F at the origin, H at $z = 1.733$ bohr, 6-31G, field along $z$ (electron energy $+Fz$), so $E = E_0 - \mu F - \alpha F^2/2 - \beta F^3/6 - \gamma F^4/24$. The parameters are the 30 real occupied-virtual rotations, with $\mathbf C(\boldsymbol\kappa) = \mathbf C_0e^{-\mathbf K}$. The energy $E(\boldsymbol\kappa, F)$ is coded explicitly. The Hessian $E_{\kappa\kappa}$ and the mixed derivative $E_{F\kappa}$ come from finite differences of $E$, and $\boldsymbol\lambda^{(1)}$ from Eq. [[#first]]. Derivatives along lines use a Cauchy contour in complex $s$ (the energy is analytic in $\boldsymbol\kappa$ and $F$).

    | | from $\boldsymbol\lambda^{(1)}$ only | with $\boldsymbol\lambda^{(1)}$ and $\boldsymbol\lambda^{(2)}$ | relaxed finite field |
    |---|---:|---:|---:|
    | $\alpha_{zz}$ | 3.869485 | | CPHF $-E_{F\kappa}\boldsymbol\lambda^{(1)}$: 3.869465 |
    | $\beta_{zzz}$ | −18.27404 | −18.27429 | −18.2964, −18.2798 ($h$ = 0.01, 0.005) → −18.27430 |
    | $\gamma_{zzzz}$ | −55.431 | 134.051 | 133.954, 134.031 ($h$ = 0.02, 0.01) → 134.057 |

    - **$\beta$ by Eq. [[#line]].** One CPHF solve and energies along a line give $\beta$. The finite-field column needs fully converged SCF runs at five field strengths and Richardson extrapolation.
    - **$\gamma$.** The straight line gives a wrong value, even of the wrong sign. Adding the second-order correction, with $\boldsymbol\lambda^{(2)}$ from Eq. [[#second]], restores the finite-field value: the $2n+1$ rule exactly.
    - **Second derivative with an inexact response.** $\boldsymbol\lambda^{(1)}$ was given a random error of 1% and 0.5% of its norm. The asymmetric form Eq. [[#asym]] erred by −6.6 and −3.3 $\times10^{-4}$ (linear). The symmetric form Eq. [[#sym]] erred by −2.4 and −0.6 $\times10^{-3}$, i.e. by $-\boldsymbol\delta^{\mathsf T}\mathbf E_{\kappa\kappa}\boldsymbol\delta$ (quadratic). At these error sizes its prefactor still makes it the worse of the two. Extrapolating the two laws, the symmetric form wins below about 0.3% error here, which a converged iterative solver easily reaches.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Appendix H, pp. 445–450, Eqs. (H.1)–(H.25), and Sec. 5.5, Eqs. (5.171) and (5.190) for the time-dependent analogue. The line form, Eq. [[#line]], is an observation made here; it is equivalent to Eq. (H.17) for a single linear perturbation. The calculations are in `Claude outputs/part4_response_batchA.py`, section F (PySCF 2.15.1).
