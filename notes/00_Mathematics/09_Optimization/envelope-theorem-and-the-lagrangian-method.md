---
id: envelope-theorem-and-the-lagrangian-method
title: Derivatives of optimized and constrained quantities - the envelope theorem, Hellmann-Feynman as its special case, the Lagrangian (adjoint) method for quantities defined by equations, its cost, and the 2n + 1 rule
summary: If a quantity is the optimum (or any stationary value) of a function of parameters λ, its total derivative with respect to an external parameter α is just the partial derivative at fixed λ. The response of λ drops out (the envelope theorem), and Hellmann–Feynman is the case where λ is a wave function. If instead λ is defined by equations f(α, λ) = 0 that are not stationarity conditions of E, the response does not drop out. Adding the conditions with multipliers, L = E + λ̄ᵀf, gives a function that is stationary in both λ and λ̄. Its multipliers come from one linear equation (∂f/∂λ)ᵀλ̄ = −∂E/∂λ, independent of α, and dE/dα = ∂L/∂α. One adjoint solve replaces one response solve per perturbation: this is the Z-vector method, and in other fields the adjoint method. The same stationarity gives the 2n + 1 rule: a wave function known to order n determines the energy to order 2n + 1. Worked examples: Hellmann–Feynman, a 20-perturbation linear model solved with one adjoint solve, a nonlinear model, and the 2n + 1 rule.
status: in-progress
kind: theory
level: intermediate
tags: [envelope-theorem, hellmann-feynman, lagrangian-method, adjoint-method, z-vector, nonvariational-energy, response, sensitivity-analysis, 2n-plus-1-rule, stationarity, implicit-function-theorem]
prerequisites: [lagrange-multipliers-and-kkt-conditions]
related: [eigenvalue-and-eigenvector-derivatives, lagrangian-for-nonvariational-energies, z-vector-method, variational-perturbation-theory-and-the-2n-plus-1-rule, hellmann-feynman-and-virial-theorems, selected-ci-analytic-gradient, ci-analytic-gradient]
key: lagr
order: 20
date: 2026-11-26
---

$\alpha$ is an external parameter (a nuclear coordinate, a field strength), $\boldsymbol\lambda\in\mathbb R^m$ are internal parameters (orbital rotations, CI coefficients, cluster amplitudes), and $E(\alpha,\boldsymbol\lambda)$ is the energy function. $\boldsymbol\lambda^*(\alpha)$ is the solution actually used at each $\alpha$, and $E(\alpha)\equiv E(\alpha,\boldsymbol\lambda^*(\alpha))$. Partial derivatives are at fixed values of the other arguments, evaluated at $\boldsymbol\lambda^*$. Notation follows HJO Sec. 4.2.8, with $\bar{\boldsymbol\lambda}$ for the multipliers.

## The chain rule and what makes it expensive

**The total derivative.** By the chain rule,

$$
\frac{dE}{d\alpha} = \frac{\partial E}{\partial\alpha} + \frac{\partial E}{\partial\boldsymbol\lambda}\cdot\frac{d\boldsymbol\lambda^*}{d\alpha}
\label{chain}
$$

(HJO Eq. 4.2.78).

**Where the cost is.** The response $d\boldsymbol\lambda^*/d\alpha$ is the expensive part. It is the solution of a linear system the size of $\boldsymbol\lambda$, and it differs for every perturbation. A molecular gradient has $3N$ of them, and a field-dependent property three or more. Everything below is about avoiding it.

## Stationary quantities: the envelope theorem

**Statement.** If $\boldsymbol\lambda^*$ makes $E$ stationary at each $\alpha$, $\partial E/\partial\boldsymbol\lambda = 0$ at $\boldsymbol\lambda^*$, and the second term of Eq. [[#chain]] vanishes:

$$
\frac{dE}{d\alpha} = \frac{\partial E(\alpha,\boldsymbol\lambda)}{\partial\alpha}\Big|_{\boldsymbol\lambda^*} .
\label{envelope}
$$

The optimal-value function is the envelope of the family $E(\alpha,\boldsymbol\lambda)$ at fixed $\boldsymbol\lambda$, touching each member where that member is optimal.

**Constrained version.** With constraints, replace $E$ by its Lagrangian: $df^*/d\alpha = \partial\mathcal L/\partial\alpha$ at $(\mathbf x^*,\boldsymbol\lambda^*)$. The sensitivity $\partial f^*/\partial\epsilon_i = \lambda_i$ of [[lagrange-multipliers-and-kkt-conditions]] is the case where $\alpha$ shifts a constraint.

**Hellmann–Feynman.** For a variational wave function, $E(\alpha,\boldsymbol\lambda) = \langle\boldsymbol\lambda|\hat H(\alpha)|\boldsymbol\lambda\rangle$, and Eq. [[#envelope]] gives $dE/d\alpha = \langle\hat H'\rangle$ (HJO Sec. 4.2.6). It holds for the exact wave function and for any wave function variational in all its parameters. Basis functions that move with the nuclei are parameters that are not optimized, and they bring the Pulay terms ([[hellmann-feynman-and-virial-theorems]], [[rhf-analytic-gradient]]). In matrix form this is Eq. [[eigenvalue-and-eigenvector-derivatives#dlam]].

**Second derivatives.** They do need the first-order response: $d^2E/d\alpha^2 = \partial^2E/\partial\alpha^2 + (\partial^2E/\partial\alpha\partial\boldsymbol\lambda)\cdot d\boldsymbol\lambda^*/d\alpha$. The response satisfies $\mathbf E_{\lambda\lambda}\,d\boldsymbol\lambda^*/d\alpha = -\mathbf E_{\lambda\alpha}$, from differentiating the stationarity condition (the implicit function theorem). This is the general form of the coupled-perturbed equations.

## Quantities defined by equations: the Lagrangian method

**The problem.** Many methods determine their parameters by conditions $\mathbf f(\alpha,\boldsymbol\lambda) = 0$ that are not stationarity conditions of the energy they report (HJO Eqs. 4.2.75–4.2.76):

- coupled-cluster amplitude equations;
- MP2 on Hartree–Fock orbitals;
- CI on SCF orbitals (stationary in the CI coefficients, not in the orbitals);
- truncated or selected CI, where the orbitals come from another calculation;
- embedding schemes, where fragment and bath parameters solve their own equations.

**The Lagrangian.** Then $\partial E/\partial\boldsymbol\lambda\ne0$. Add the conditions with multipliers (HJO Eq. 4.2.84):

$$
L(\alpha,\boldsymbol\lambda,\bar{\boldsymbol\lambda}) = E(\alpha,\boldsymbol\lambda) + \bar{\boldsymbol\lambda}^{\rm T}\mathbf f(\alpha,\boldsymbol\lambda) .
\label{lagr}
$$

At $\boldsymbol\lambda^*$, $L = E$ for every $\bar{\boldsymbol\lambda}$, since $\mathbf f = 0$. Choose $\bar{\boldsymbol\lambda}$ to make $L$ stationary in $\boldsymbol\lambda$ too:

$$
\frac{\partial L}{\partial\boldsymbol\lambda} = \frac{\partial E}{\partial\boldsymbol\lambda} + \Big(\frac{\partial\mathbf f}{\partial\boldsymbol\lambda}\Big)^{\rm T}\bar{\boldsymbol\lambda} = 0,\qquad
\frac{\partial L}{\partial\bar{\boldsymbol\lambda}} = \mathbf f = 0
\label{stat}
$$

(HJO Eqs. 4.2.85–4.2.86). $L$ is stationary in all its variables, so Eq. [[#envelope]] applies to it:

$$
\frac{dE}{d\alpha} = \frac{\partial L}{\partial\alpha} = \frac{\partial E}{\partial\alpha} + \bar{\boldsymbol\lambda}^{\rm T}\frac{\partial\mathbf f}{\partial\alpha} .
\label{dEda}
$$

**Why it works.** Differentiating $\mathbf f(\alpha,\boldsymbol\lambda^*(\alpha)) = 0$ gives $\mathbf J\,d\boldsymbol\lambda^*/d\alpha = -\partial\mathbf f/\partial\alpha$, with Jacobian $\mathbf J = \partial\mathbf f/\partial\boldsymbol\lambda$. The response term of Eq. [[#chain]] is then

$$
\frac{\partial E}{\partial\boldsymbol\lambda}\cdot\frac{d\boldsymbol\lambda^*}{d\alpha} = -\frac{\partial E}{\partial\boldsymbol\lambda}\mathbf J^{-1}\frac{\partial\mathbf f}{\partial\alpha} = \bar{\boldsymbol\lambda}^{\rm T}\frac{\partial\mathbf f}{\partial\alpha},\qquad\bar{\boldsymbol\lambda} = -\mathbf J^{-\rm T}\Big(\frac{\partial E}{\partial\boldsymbol\lambda}\Big)^{\rm T} .
$$

The inverse is moved from the perturbation side ($\mathbf J^{-1}\,\partial\mathbf f/\partial\alpha$, one solve per $\alpha$) to the energy side ($\mathbf J^{-\rm T}\,\partial E/\partial\boldsymbol\lambda$, one solve in total). This is the Handy–Schaefer interchange behind the Z-vector method ([[z-vector-method]]) and its Lagrangian form ([[lagrangian-for-nonvariational-energies]]). In optimal control, PDE-constrained optimization and machine learning (backpropagation) the same construction is called the adjoint method.

**What it costs.**

| | response (direct) | Lagrangian (adjoint) |
|---|---|---|
| linear solves for $p$ perturbations | $p$ (one per $\alpha$) | 1 (independent of $\alpha$) |
| per perturbation afterwards | contraction with $\partial E/\partial\boldsymbol\lambda$ | contraction of $\bar{\boldsymbol\lambda}$ with $\partial\mathbf f/\partial\alpha$ |
| best when | few perturbations, many outputs | many perturbations, one output (an energy) |

**Properties of $L$.** HJO notes that its stationary point is a saddle point, never a minimum, since $L$ is linear in $\bar{\boldsymbol\lambda}$. The multipliers have a physical reading as relaxation densities: contracted with the operators in $\partial\mathbf f/\partial\alpha$, they turn unrelaxed into relaxed (response) densities. For any method, this is the step that decides whether an analytic gradient is cheap. If the conditions $\mathbf f$ are not stationarity conditions (selected CI on non-optimized orbitals, embedding self-consistency), the gradient costs one extra adjoint solve per set of conditions, not one per coordinate ([[selected-ci-analytic-gradient]]).

## The 2n + 1 rule

**Statement.** For a variational energy, an error $\delta\boldsymbol\lambda$ in the parameters gives an energy error of order $|\delta\boldsymbol\lambda|^2$, because the energy is stationary. Expand $\boldsymbol\lambda^*(\alpha)$ in powers of $\alpha$ and keep terms through order $n$. The error in $\boldsymbol\lambda$ is $O(\alpha^{n+1})$, so the energy error is $O(\alpha^{2n+2})$. The energy is therefore correct through order $2n + 1$.

**Consequences.**

- First-order wave functions give energies through third order (Wigner's rule, HJO Sec. 14.1.2).
- For the Lagrangian of a nonvariational energy, the rule applies to the parameters together with the multipliers. Parameters and multipliers known to order $n$ give the energy through order $2n + 1$. Order $2n + 2$ needs the parameters to order $n + 1$ but the multipliers still only to order $n$: the $2n + 2$ rule for the multipliers.

The perturbation-theory form is in [[variational-perturbation-theory-and-the-2n-plus-1-rule]].

## Worked examples

!!! example "Envelope, adjoint and 2n + 1 in numbers (computed for this note)"
    **Hellmann–Feynman.** Lowest eigenvalue of a random $6\times6$ $\mathbf H_0 + \alpha\mathbf V$ at $\alpha = 0$: the finite-difference slope is 3.0709291670, and $\langle\mathbf v_0|\mathbf V|\mathbf v_0\rangle = 3.0709291674$. No eigenvector response was computed.

    **A linear model with 8 parameters and 20 perturbations.** The parameters solve $\mathbf A(\alpha)\boldsymbol\lambda = \mathbf b(\alpha)$, like amplitude or CPHF equations. The energy $E = \mathbf c(\alpha)\cdot\boldsymbol\lambda + \tfrac12\boldsymbol\lambda^{\rm T}\mathbf M\boldsymbol\lambda$ is not stationary in $\boldsymbol\lambda$. Errors against finite differences:

    - partial derivative only (Hellmann–Feynman wrongly applied): 0.46;
    - direct response, 20 linear solves: $5\times10^{-11}$;
    - Lagrangian, Eq. [[#dEda]], with one solve $\mathbf A^{\rm T}\bar{\boldsymbol\lambda} = -(\mathbf c + \mathbf M\boldsymbol\lambda)$: $5\times10^{-11}$.

    The adjoint result is identical, at 1/20 of the solving cost.

    **Nonlinear conditions.** $\mathbf f = \boldsymbol\lambda + 0.2\boldsymbol\lambda^{\circ3} + \mathbf K\boldsymbol\lambda - \mathbf b(\alpha)$ (elementwise cube) and $E$ with a quartic term. Eq. [[#dEda]] with $\mathbf J = \mathbf 1 + 0.6\,\mathrm{diag}(\boldsymbol\lambda^2) + \mathbf K$ gives $-3.6114422499$, against the finite difference $-3.6114422493$. At the solution $|\partial L/\partial\boldsymbol\lambda| = 1\times10^{-15}$ and $|\partial L/\partial\bar{\boldsymbol\lambda}| = |\mathbf f| = 1\times10^{-15}$.

    **2n + 1.** Lowest eigenvalue of $\mathbf H_0 + \alpha\mathbf V$ (diagonal $\mathbf H_0$, random $\mathbf V$):

    | $\alpha$ | error of $E^{(0)} + E^{(1)} + E^{(2)}$ | error of the Rayleigh quotient with $\mathbf c_0 + \alpha\mathbf c_1$ |
    |---:|---:|---:|
    | 0.1 | $-4.0\times10^{-6}$ | $1.9\times10^{-7}$ |
    | 0.05 | $-5.1\times10^{-7}$ | $1.2\times10^{-8}$ |
    | 0.025 | $-6.4\times10^{-8}$ | $7.7\times10^{-10}$ |

    Halving $\alpha$ divides the first error by 8 ($\alpha^3$) and the second by 16 ($\alpha^4$). The first-order vector gives the energy through third order.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 4.2.6 (the Hellmann–Feynman theorem), Sec. 4.2.8 (variational reformulation of nonvariational energies, Eqs. 4.2.75–4.2.86), Sec. 14.1.2 (Wigner's 2n + 1 rule). Nocedal and Wright, *Numerical Optimization* (Springer, 1999), Sec. 12.2 (sensitivity of the optimal value). The adjoint-method and backpropagation remarks are general knowledge. Calculations in `Claude outputs/part0_math_batchF.py`, section D.
