---
id: functional-derivatives
title: Functional derivatives - definition through the first variation, rules, local and gradient-dependent functionals, the Hartree potential and kernel, chain rule through orbitals, second derivatives, and the Euler equation of density functional theory
summary: The functional derivative δF/δρ(r) is defined by δF = ∫ (δF/δρ)(r) δρ(r) dr for every small change δρ. It is the continuum analogue of a gradient, the change of F per unit change of ρ at the point r. For a local functional ∫ f(ρ) dr it is f'(ρ). For a gradient-dependent one, ∫ f(ρ, ∇ρ) dr, it is ∂f/∂ρ − ∇·(∂f/∂∇ρ), the Euler–Lagrange expression. The Hartree energy gives the Hartree potential, and its second derivative is the Coulomb kernel 1/|r − r'|. Sum, product and chain rules hold, including derivatives with respect to orbitals: δF/δφ* = φ δF/δρ for ρ = |φ|². Stationarity of E[ρ] at fixed electron number gives the Euler equation δE/δρ = μ, with the multiplier μ the chemical potential. Worked examples on a radial grid for the hydrogen 1s density: Thomas–Fermi, Dirac exchange and von Weizsäcker derivatives checked against the definition, the Hartree potential and kernel, and an exact Euler equation with μ = −½ hartree.
status: in-progress
kind: theory
level: intermediate
tags: [functional-derivative, first-variation, local-functional, gradient-functional, hartree-potential, coulomb-kernel, chain-rule, thomas-fermi, dirac-exchange, von-weizsacker, euler-equation, chemical-potential, second-functional-derivative, functional-taylor-expansion]
prerequisites: [calculus-of-variations-and-the-euler-lagrange-equation]
related: [lagrange-multipliers-and-kkt-conditions, vector-identities-and-the-laplacian, kohn-sham-dft, exchange-correlation-functionals, hartree-fock-equations, matrix-calculus]
key: fd
order: 80
date: 2026-11-26
---

Atomic units. $\rho(\mathbf r)$ is a density (or any function on $\mathbb R^3$), $F[\rho]$ a functional, and $\delta\rho(\mathbf r)$ a small change. Integrals without limits are over all space. The constants $C_F = \tfrac{3}{10}(3\pi^2)^{2/3} = 2.8712$ and $C_x = \tfrac34(3/\pi)^{1/3} = 0.7386$ are the Thomas–Fermi and Dirac (LDA) exchange constants for a spin-unpolarized density.

## Definition

**The first variation.** Extend the variation of [[calculus-of-variations-and-the-euler-lagrange-equation]] from paths to fields. If

$$
F[\rho + \delta\rho] - F[\rho] = \int\frac{\delta F}{\delta\rho(\mathbf r)}\,\delta\rho(\mathbf r)\,d\mathbf r + O(\delta\rho^2)
\label{fd}
$$

for all small $\delta\rho$, the function $\delta F/\delta\rho(\mathbf r)$ is the functional derivative of $F$ at $\rho$. Equivalently, $\frac{d}{d\epsilon}F[\rho + \epsilon\eta]\big|_{\epsilon=0} = \int\frac{\delta F}{\delta\rho}\eta\,d\mathbf r$ for every test function $\eta$.

**The discrete picture.** Represent $\rho$ by its values $\rho_i$ on a grid with quadrature weights $w_i$. Then $F$ becomes an ordinary function, and $\delta F/\delta\rho(\mathbf r_i) = (\partial F/\partial\rho_i)/w_i$. The weight is there because $\delta\rho$ at one grid point represents a change spread over the volume $w_i$. A functional derivative is a gradient with respect to the metric of $\int d\mathbf r$, which is exactly how DFT codes compute potentials on integration grids.

**A formal shortcut.** Physicists also write $\delta\rho(\mathbf r)/\delta\rho(\mathbf r') = \delta(\mathbf r - \mathbf r')$. With it, functional derivatives can be computed like partial derivatives with continuous labels, and every rule below follows.

## Rules and standard results

**Rules.** Linearity, the product rule, and the chain rule $\delta G[F[\rho]]/\delta\rho = G'(F)\,\delta F/\delta\rho$ hold as for ordinary derivatives. A function of the density at one point, $\rho(\mathbf r_0) = \int\rho\,\delta(\mathbf r - \mathbf r_0)$, has derivative $\delta(\mathbf r - \mathbf r_0)$.

**Local functionals.** For $F = \int f(\rho(\mathbf r))\,d\mathbf r$ the derivative is just $f'(\rho(\mathbf r))$:

| functional | $F[\rho]$ | $\delta F/\delta\rho$ |
|---|---|---|
| external potential energy | $\int v\rho$ | $v(\mathbf r)$ |
| Thomas–Fermi kinetic energy | $C_F\int\rho^{5/3}$ | $\tfrac53C_F\rho^{2/3}$ |
| Dirac (LDA) exchange | $-C_x\int\rho^{4/3}$ | $-\tfrac43C_x\rho^{1/3}$ |

**Gradient-dependent functionals.** For $F = \int f(\rho, \nabla\rho)\,d\mathbf r$, integrate the $\nabla\delta\rho$ term by parts as in the Euler–Lagrange derivation. Surface terms vanish for decaying densities ([[divergence-and-gauss-theorem]]), leaving

$$
\frac{\delta F}{\delta\rho} = \frac{\partial f}{\partial\rho} - \nabla\cdot\frac{\partial f}{\partial\nabla\rho} .
\label{gga}
$$

This is the form of every GGA exchange-correlation potential ([[exchange-correlation-functionals]]). For the von Weizsäcker kinetic energy $T_W = \tfrac18\int|\nabla\rho|^2/\rho$:

$$
\frac{\delta T_W}{\delta\rho} = \frac{|\nabla\rho|^2}{8\rho^2} - \frac{\nabla^2\rho}{4\rho} .
$$

$T_W$ is the exact kinetic energy of any density that comes from a single real orbital, $\rho = \phi^2$ (a one-electron system, or two electrons in one spatial orbital). In general it is a lower bound to the noninteracting kinetic energy.

**Nonlocal functionals: the Hartree energy.** For $J[\rho] = \tfrac12\iint\frac{\rho(\mathbf r)\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}d\mathbf r\,d\mathbf r'$, varying $\rho$ in both factors gives two equal terms. The $\tfrac12$ cancels:

$$
\frac{\delta J}{\delta\rho(\mathbf r)} = \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}d\mathbf r' = v_H(\mathbf r),\qquad
\frac{\delta^2J}{\delta\rho(\mathbf r)\,\delta\rho(\mathbf r')} = \frac1{|\mathbf r - \mathbf r'|} .
\label{hartree}
$$

$v_H$ solves Poisson's equation $\nabla^2v_H = -4\pi\rho$ ([[vector-identities-and-the-laplacian]]). The second derivative, the Hartree kernel, is the Coulomb part of the response kernel in TDDFT and RPA.

**Functional Taylor series.** Second derivatives define the kernel of a quadratic expansion: $F[\rho + \delta\rho] = F + \int\frac{\delta F}{\delta\rho}\delta\rho + \frac12\iint\frac{\delta^2F}{\delta\rho\,\delta\rho'}\delta\rho\,\delta\rho' + \cdots$. This is the continuum form of the multivariable Taylor expansion ([[multivariable-taylor-expansion]]).

## Derivatives with respect to orbitals

**The chain rule through orbitals.** If $\rho = \sum_i|\phi_i|^2$, treat $\phi_i$ and $\phi_i^*$ as independent, as in Wirtinger calculus. Then

$$
\frac{\delta F}{\delta\phi_i^*(\mathbf r)} = \frac{\delta F}{\delta\rho(\mathbf r)}\,\phi_i(\mathbf r) .
\label{orbital}
$$

For real orbitals, $\delta F/\delta\phi_i = 2\phi_i\,\delta F/\delta\rho$.

**From energy functionals to one-electron equations.** The kinetic functional $\sum_i\langle\phi_i|-\tfrac12\nabla^2|\phi_i\rangle$ gives $-\tfrac12\nabla^2\phi_i$. Adding the orthonormality constraints with a Hermitian multiplier matrix $\boldsymbol\varepsilon$, as in [[lagrange-multipliers-and-kkt-conditions]], the stationarity conditions become:

- **from a density functional:** the Kohn–Sham equations, $[-\tfrac12\nabla^2 + v + v_H + v_{xc}]\phi_i = \sum_j\varepsilon_{ji}\phi_j$ ([[kohn-sham-dft]]);
- **from the Hartree–Fock energy:** the Hartree–Fock equations, where exchange appears as a nonlocal operator because the exchange energy depends on the orbitals, not only on $\rho$ ([[hartree-fock-equations]]).

Diagonalizing $\boldsymbol\varepsilon$ gives the canonical form.

## Stationarity: the Euler equation of DFT

**The equation.** Minimizing $E_v[\rho] = F[\rho] + \int v\rho$ over densities with $\int\rho = N$ gives, with a multiplier $\mu$ for the normalization,

$$
\frac{\delta F}{\delta\rho(\mathbf r)} + v(\mathbf r) = \mu\quad\text{for every }\mathbf r .
\label{euler}
$$

**Meaning.** The left side must be the same constant everywhere. $\mu = \partial E/\partial N$ is the chemical potential: the sensitivity of the energy to the constraint, as for any multiplier. Thomas–Fermi theory is Eq. [[#euler]] with $F = T_{TF} + J$. Orbital-free DFT is the same equation with better kinetic functionals.

**A sharp test of an approximate functional.** Insert the exact density and check whether the left side of Eq. [[#euler]] is constant. For hydrogen with $F = T_W$ it is constant, and exactly equal to the energy. With $F = T_{TF} + J$ it is not constant: Thomas–Fermi is wrong for this density.

## Worked example

!!! example "Hydrogen 1s on a radial grid (computed for this note)"
    $\rho = e^{-2r}/\pi$ on a radial grid to 30 bohr (300 001 points), normalized to 1.000000.

    **Energies.** $T_{TF} = 0.289127$ against the exact $T = 0.5$, and $E_x^{\rm LDA} = -0.212742$ against the exact exchange $-J = -0.3125$ for one electron. That LDA value uses the spin-unpolarized formula. The spin-polarized form appropriate to one electron multiplies it by $2^{1/3}$, giving $-0.268039$, still 14% short.

    **The definition, Eq. [[#fd]].** Use smooth bumps $\delta\rho = \epsilon\,\rho\,e^{-((r - r_0)/0.15)^2}$ and compare $[F(\rho + \epsilon g) - F(\rho - \epsilon g)]/2\epsilon$ with $\int(\delta F/\delta\rho)\,g$:

    | bump at $r_0$ | $T_{TF}$ | $E_x^{\rm LDA}$ | $T_W$ (Eq. [[#gga]]) |
    |---:|---|---|---|
    | 0.5 | 0.10740229 / 0.10740229 | $-0.04554225$ / $-0.04554225$ | 0.14319603 / 0.14319603 |
    | 2.0 | 0.01241490 / 0.01241490 | $-0.01398484$ / $-0.01398484$ | $3.31131\times10^{-4}$ / $3.31131\times10^{-4}$ |
    | 5.0 | $3.5951\times10^{-6}$ / $3.5951\times10^{-6}$ | $-2.97867\times10^{-5}$ / $-2.97867\times10^{-5}$ | $-3.66198\times10^{-4}$ / $-3.66198\times10^{-4}$ |

    Each pair is variation / formula. For $T_W$ the variation was computed with numerical gradients on the grid, the formula from the analytic $\rho'$ and $\nabla^2\rho$.

    **von Weizsäcker and the Euler equation.** $T_W[\rho_{1s}] = 0.500000$, the exact kinetic energy. With $\rho' = -2\rho$ and $\nabla^2\rho = (4 - 4/r)\rho$, $\delta T_W/\delta\rho = \tfrac12 - 1 + \tfrac1r$. So $\delta T_W/\delta\rho - 1/r = -0.50000000$ at $r = 0.5$, 2 and 5. Eq. [[#euler]] holds exactly, with $\mu = -\tfrac12$ hartree, the energy and the negative of the ionization energy.

    **Hartree, Eq. [[#hartree]].**

    - $v_H(1) = 0.729329$ by the shell theorem, against the exact $1/r - (1 + 1/r)e^{-2r} = 0.729329$; $J = 0.312500 = 5/16$.
    - On a coarser grid, perturbing $J$ as a quadratic form gives $\delta J/\delta\rho = 0.72930$, 0.199943 and 0.099999 at $r = 1$, 5 and 10, equal to $v_H$.
    - The mixed second difference at $r = 1.5$, $r' = 7.5$ is 0.133332, equal to $1/\max(r, r')$: the spherical average of $1/|\mathbf r - \mathbf r'|$.

    **Chain rule, Eq. [[#orbital]].** With $\phi = \sqrt\rho$, $\delta T_{TF}/\delta\phi$ at $r = 1$ is 0.24410932 numerically and $2\phi\cdot\tfrac53C_F\rho^{2/3} = 0.24410933$.

    **Thomas–Fermi fails the test.** $\tfrac53C_F\rho^{2/3} - 1/r + v_H$ is 0.0418 at $r = 0.5$ and 0.1275 at $r = 2$. It is not constant, so the exact density is far from stationary for the Thomas–Fermi energy.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 17.4 (several independent variables, the Euler–Lagrange equation as a PDE), Sec. 17.7 (variation with constraints). The definition and rules of functional derivatives, the Thomas–Fermi, Dirac and von Weizsäcker results and the DFT Euler equation are standard material, written and checked here. The standard textbook treatment is Appendix A of Parr and Yang's book on density-functional theory of atoms and molecules (1989). It was not consulted for this note, so the reference is to verify. Calculations in `Claude outputs/part0_math_batchF.py`, section F.
