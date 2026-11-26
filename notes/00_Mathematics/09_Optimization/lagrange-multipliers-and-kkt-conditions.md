---
id: lagrange-multipliers-and-kkt-conditions
title: Constrained stationary points - Lagrange multipliers, the multiplier as sensitivity, second-order conditions with the projected Hessian, matrix constraints such as orbital orthonormality, and the KKT conditions for inequalities
summary: At a constrained stationary point of f subject to c(x) = 0, the gradient of f is a combination of the constraint gradients, ∇f = Σᵢ λᵢ∇cᵢ. Equivalently, the Lagrangian f − λᵀc is stationary in both x and λ. The multipliers are the rates at which the optimal value changes when the constraints are shifted. Whether the point is a minimum is decided by the Hessian of the Lagrangian projected onto the tangent space of the constraints, not by the Hessian of f. Matrix constraints get a matrix of multipliers: minimizing an energy over orthonormal orbitals gives a symmetric multiplier matrix, which is the occupied block of the Fock matrix, and its eigenvalues are the orbital energies. The alternative is to parametrize the constraint away with orbital rotations. Inequality constraints lead to the Karush–Kuhn–Tucker conditions: multiplier signs and complementarity. Worked examples: a sensitivity check, maximum entropy giving the Boltzmann distribution, the Rayleigh quotient's saddle points, a random RHF model, and a KKT problem.
status: in-progress
kind: theory
level: intermediate
tags: [lagrange-multipliers, constrained-optimization, lagrangian, kkt-conditions, complementarity, sensitivity, projected-hessian, orthonormality-constraint, rayleigh-quotient, maximum-entropy, boltzmann-distribution, hartree-fock, orbital-energies, licq]
prerequisites: [matrix-calculus, multivariable-taylor-expansion]
related: [envelope-theorem-and-the-lagrangian-method, differential-calculus, calculus-of-variations-and-the-euler-lagrange-equation, optimality-conditions-and-convergence-rates, hartree-fock-equations, hartree-fock-csf-parametrization-and-canonical-conditions, unitary-matrices-exponential-logarithm]
key: kkt
order: 10
date: 2026-11-26
---

Minimize (or make stationary) $f(\mathbf x)$, $\mathbf x\in\mathbb R^n$, subject to equality constraints $c_i(\mathbf x) = 0$, $i = 1..m < n$, and in the last section inequality constraints $c_i(\mathbf x)\ge0$. $\mathbf A(\mathbf x)$ is the $m\times n$ matrix whose rows are $\nabla c_i^{\rm T}$. The sign convention $\mathcal L = f - \boldsymbol\lambda^{\rm T}\mathbf c$ follows Nocedal and Wright. Physics texts often write $f + \boldsymbol\lambda^{\rm T}\mathbf c$, which flips the sign of every multiplier but nothing else.

## Equality constraints

**The geometric condition.** At a constrained stationary point, moving along the constraint surface does not change $f$ to first order. The allowed directions $\mathbf d$ satisfy $\mathbf A\mathbf d = 0$, so $\nabla f$ must be orthogonal to all of them. It then lies in the span of the constraint normals:

$$
\nabla f(\mathbf x^*) = \sum_i\lambda_i^*\nabla c_i(\mathbf x^*),\qquad c_i(\mathbf x^*) = 0 .
\label{lagrange}
$$

**As stationarity of the Lagrangian.** Equivalently, $\mathcal L(\mathbf x,\boldsymbol\lambda) = f - \boldsymbol\lambda^{\rm T}\mathbf c$ is stationary in all $n + m$ variables: $\nabla_{\mathbf x}\mathcal L = 0$ is the first condition and $\nabla_{\boldsymbol\lambda}\mathcal L = -\mathbf c = 0$ the second. This is the form introduced briefly in [[differential-calculus]] and used for functionals in [[calculus-of-variations-and-the-euler-lagrange-equation]] (Arfken Sec. 17.6).

**Constraint qualification.** The multipliers exist and are unique if the active constraint gradients are linearly independent (LICQ, Nocedal and Wright Definition 12.1). Without it, Eq. [[#lagrange]] can fail even at a true minimum. Writing a constraint as $c^2 = 0$ instead of $c = 0$ makes its gradient vanish on the constraint surface and destroys the multiplier.

**Saddle points of the Lagrangian.** $\mathcal L$ is linear in $\boldsymbol\lambda$, so its stationary points are saddle points in the joint space, never minima, even when $\mathbf x^*$ minimizes $f$ on the constraint surface. Minimizing $\mathcal L$ with an unconstrained minimizer therefore does not work. Constrained algorithms either eliminate the constraint or treat $\boldsymbol\lambda$ separately.

## What the multipliers mean

**Sensitivity.** Shift the constraints to $c_i(\mathbf x) = \epsilon_i$ and let $f^*(\boldsymbol\epsilon)$ be the optimal value. To first order (Nocedal and Wright Sec. 12.2, Eq. 12.33):

$$
\frac{\partial f^*}{\partial\epsilon_i} = \lambda_i^* .
\label{sens}
$$

The multiplier is the price of the constraint: how much the optimum would improve per unit relaxation. This is a special case of the envelope theorem of [[envelope-theorem-and-the-lagrangian-method]].

**Examples of multipliers with a physical meaning.**

- **Thermodynamics.** Maximizing the entropy at fixed normalization and mean energy gives $p_i\propto e^{-\beta E_i}$, with the energy multiplier $\beta = \partial S/\partial U = 1/k_BT$.
- **Normalization.** For the Rayleigh quotient, minimizing $\mathbf x^{\rm T}\mathbf A\mathbf x$ on $\mathbf x^{\rm T}\mathbf x = 1$, the multiplier is the eigenvalue: $\mathbf A\mathbf x = \lambda\mathbf x$. In the Schrödinger case it is the energy (Arfken Example 17.7.3).
- **Chemical potential.** In DFT the multiplier of $\int\rho = N$ is the chemical potential $\mu = \partial E/\partial N$ ([[functional-derivatives]]).

## Second-order conditions

**The projected Hessian.** At a point satisfying Eq. [[#lagrange]], let the columns of $\mathbf Z$ span the null space of $\mathbf A$ (the tangent space of the constraints). The point is a strict local minimum if (Nocedal and Wright Theorems 12.5–12.6, Sec. 12.4)

$$
\mathbf Z^{\rm T}\,\nabla^2_{\mathbf{xx}}\mathcal L(\mathbf x^*,\boldsymbol\lambda^*)\,\mathbf Z\quad\text{is positive definite.}
\label{proj}
$$

It is a local maximum if this matrix is negative definite, and a saddle point if it is indefinite. Positive semidefiniteness is necessary for a minimum.

**Why $\mathcal L$ and not $f$.** The relevant Hessian is that of $\mathcal L$, not of $f$. The term $-\sum\lambda_i\nabla^2c_i$ accounts for the curvature of the constraint surface, which second-order moves along it must follow. For the Rayleigh quotient, $\nabla^2_{\mathbf{xx}}\mathcal L = 2(\mathbf A - \lambda\mathbf 1)$. Projected onto the tangent space, it is positive definite only for the lowest eigenvector: the $k$-th eigenvector is a saddle point with $k - 1$ downhill directions. This is the finite-dimensional statement that excited states are saddle points of the energy, and why variational optimizers collapse to the ground state.

## Matrix constraints: orthonormal orbitals

**The problem.** Minimize $E(\mathbf C)$ over $n\times k$ coefficient matrices with $\mathbf C^{\rm T}\mathbf S\mathbf C = \mathbf 1_k$. That is $k(k + 1)/2$ independent constraints (the matrix is symmetric). It needs a symmetric multiplier matrix $\boldsymbol\Lambda$:

$$
\mathcal L = E(\mathbf C) - \mathrm{tr}\big[\boldsymbol\Lambda(\mathbf C^{\rm T}\mathbf S\mathbf C - \mathbf 1)\big],\qquad
\frac{\partial E}{\partial\mathbf C} = 2\,\mathbf S\mathbf C\boldsymbol\Lambda
\label{orth}
$$

([[matrix-calculus]] for $\partial\,\mathrm{tr}(\boldsymbol\Lambda\mathbf C^{\rm T}\mathbf S\mathbf C)/\partial\mathbf C = 2\mathbf S\mathbf C\boldsymbol\Lambda$).

**Two model cases.**

- **A one-body trace.** For $E = \mathrm{tr}(\mathbf C^{\rm T}\mathbf A\mathbf C)$ with $\mathbf S = \mathbf 1$, Eq. [[#orth]] gives $\mathbf A\mathbf C = \mathbf C\boldsymbol\Lambda$. The minimum is the sum of the $k$ lowest eigenvalues, attained by any orthonormal basis of the lowest eigenspace. $\boldsymbol\Lambda = \mathbf C^{\rm T}\mathbf A\mathbf C$ is symmetric but not diagonal unless the columns are the eigenvectors themselves.
- **Closed-shell Hartree–Fock.** The energy gradient is $\partial E/\partial\mathbf C_{\rm occ} = 4\mathbf F\mathbf C_{\rm occ}$. Eq. [[#orth]] becomes $\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon$ with $\boldsymbol\varepsilon = \tfrac12\boldsymbol\Lambda$ symmetric. The energy is invariant to rotations among occupied orbitals, so $\boldsymbol\varepsilon$ can be diagonalized without changing anything. Doing so gives the canonical orbitals and the Roothaan–Hall eigenvalue problem, with the orbital energies as the eigenvalues of the multiplier matrix ([[hartree-fock-equations]]).

**The alternative: parametrize the constraint away.** Write $\mathbf C = \mathbf C_0e^{-\boldsymbol\kappa}$ with antisymmetric $\boldsymbol\kappa$. Then orthonormality holds for every $\boldsymbol\kappa$, and the problem becomes unconstrained in the independent rotation parameters ([[unitary-matrices-exponential-logarithm]]). The redundant occupied–occupied rotations are dropped. The stationarity condition then reads $F_{ai} = 0$ (the Brillouin condition), and canonicalization is a separate, optional step. HJO Sec. 10.3.5 compares these "variational" and "canonical" conditions ([[hartree-fock-csf-parametrization-and-canonical-conditions]]).

**Which to use.** Lagrange multipliers keep the problem in the original variables and give the orbital energies directly. The exponential parametrization removes the constraints and suits second-order (Newton) optimizers. Both describe the same stationary points.

## Inequality constraints: the KKT conditions

**The conditions.** For constraints $c_i(\mathbf x)\ge0$, $i\in\mathcal I$, together with equalities $i\in\mathcal E$, a local minimum satisfying LICQ obeys (Nocedal and Wright Theorem 12.1, Eq. 12.30):

$$
\nabla f = \sum_i\lambda_i\nabla c_i,\qquad c_i = 0\ (i\in\mathcal E),\qquad c_i\ge0,\ \ \lambda_i\ge0,\ \ \lambda_ic_i = 0\ (i\in\mathcal I).
\label{kkt}
$$

**Reading the conditions.**

- **Complementarity.** $\lambda_ic_i = 0$ says each inequality is either active ($c_i = 0$, acting like an equality) or inactive ($c_i > 0$, with zero multiplier, as if it were absent).
- **The sign of $\lambda_i$.** It says the constraint pushes the solution in the right direction: relaxing it could only lower $f$.

**Where inequalities appear.**

- **Occupation numbers.** $0\le n_i\le1$ in ensemble or fractional-occupation methods.
- **Positivity.** $N$-representability conditions on reduced density matrices in variational 2-RDM methods. These are semidefinite rather than scalar inequality constraints, with the same structure.
- **Trust regions.** The trust-region subproblem $\|\mathbf p\|\le\Delta$, whose multiplier is the level shift of the exact trust-region step.

## Worked examples

!!! example "Multipliers in numbers (computed for this note)"
    **Sensitivity, Eq. [[#sens]].** Minimize $x^2 + 2y^2$ with $x + y = c$: $x^* = 2c/3$, $y^* = c/3$, $f^* = 2c^2/3$, $\lambda = 2x^* = 4c/3$. From $c = 1$ to $1.1$, $f^*$ rises from 0.666667 to 0.806667, a slope of 1.400000. That equals $\lambda$ at the midpoint $c = 1.05$.

    **A constraint surface with curvature.** Nocedal and Wright's example: minimize $x_1 + x_2$ on $2 - x_1^2 - x_2^2 = 0$. The solution is $(-1, -1)$ with $\lambda^* = \tfrac12$. The Hessian of $f$ is zero, so all curvature comes from the constraint. The projected Hessian of $\mathcal L$ is $+1$, a minimum. At the other stationary point $(1, 1)$ it is $-1$, a maximum.

    **Maximum entropy.** Levels $E = (0, 1, 2.5, 4)$ with $\langle E\rangle = 1.2$. Maximizing $-\sum p\ln p$ numerically gives $p = (0.409524, 0.296201, 0.182200, 0.112075)$. That is exactly the Boltzmann distribution with $\beta = 0.323957$. A finite difference of the maximum entropy with respect to $U$ gives $dS/dU = 0.323957 = \beta$.

    **Rayleigh quotient.** A random symmetric $4\times4$ matrix. The eigenvalues of the projected Hessian at the four eigenvectors are $(2.63, 3.64, 6.48)$, $(-2.63, 1.00, 3.85)$, $(-3.64, -1.00, 2.85)$, $(-6.48, -3.85, -2.85)$. Their signs give one minimum, two saddle points, and one maximum.

    **Orthonormal columns.** Minimizing $\mathrm{tr}(\mathbf X^{\rm T}\mathbf A\mathbf X)$ over $4\times2$ matrices with $\mathbf X^{\rm T}\mathbf X = \mathbf 1$ (projected gradient descent with QR retraction) gives $-2.36082479$, the sum of the two lowest eigenvalues. The multiplier matrix is $\boldsymbol\Lambda = \begin{pmatrix}-1.45685&0.59763\\0.59763&-0.90397\end{pmatrix}$: symmetric, not diagonal, with eigenvalues $-1.83888$ and $-0.52195$, the two lowest eigenvalues of $\mathbf A$.

    **A random closed-shell RHF model.** 6 basis functions, 2 doubly occupied orbitals, random $\mathbf h$, overlap, and positive-semidefinite 8-fold-symmetric two-electron integrals.

    - $\partial E/\partial\mathbf C = 4\mathbf F\mathbf C$ agrees with finite differences to $2\times10^{-10}$.
    - At SCF convergence, $\|4\mathbf F\mathbf C - 4\mathbf S\mathbf C\boldsymbol\varepsilon\| = 1\times10^{-10}$, $\boldsymbol\varepsilon$ is symmetric, and the occupied–virtual Fock block vanishes to $4\times10^{-11}$.
    - Rotating the occupied orbitals by 0.3 rad changes $E$ by $7\times10^{-15}$, but makes $\boldsymbol\varepsilon$ non-diagonal, with off-diagonal element $-0.684$.

    **KKT, Eq. [[#kkt]].** Minimize $(x - 2)^2 + (y - 1)^2$ with $x + y\le2$ and $x\ge0$. The solution is $(1.5, 0.5)$, with $\nabla f = (-1, -1)$.

    - $x + y\le2$ is active, with multiplier 1.000 > 0.
    - $x\ge0$ is inactive, with multiplier 0.
    - Complementarity holds to $3\times10^{-16}$.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, 1999), Sec. 12.2 (first-order conditions, Definition 12.1 LICQ, Theorem 12.1 KKT conditions, Eq. 12.30; sensitivity, Eq. 12.33), Sec. 12.4 (second-order conditions, Theorems 12.5–12.6, projected Hessians). Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 17.6 (Lagrangian multipliers), Example 17.7.3 (the Schrödinger equation as a constrained variation). Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 10.3.5 (variational and canonical conditions compared). The maximum-entropy and $N$-representability remarks are general knowledge. Calculations in `Claude outputs/part0_math_batchF.py`, section C.
