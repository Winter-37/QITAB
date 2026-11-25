---
id: differential-calculus
title: Differential calculus - derivatives, the differentiation rules, the mean value theorem and L'Hôpital's rule, partial derivatives, total differentials, Jacobians, stationary points and Lagrange multipliers
summary: The derivative f'(a) is the limit of the difference quotient, the slope of the best linear approximation at a. From the definition follow the product, quotient and chain rules, the derivatives of inverse and implicit functions, the mean value theorem, and L'Hôpital's rule for 0/0 limits. For functions of several variables come partial derivatives, the total differential, the multivariable chain rule (including the cyclic relation of thermodynamics), Jacobian matrices, and the Hessian test for stationary points. Constrained stationary points are found with Lagrange multipliers. Worked examples: a derivative checked by finite differences, the cyclic relation for an ideal gas, a saddle point, and a constrained maximum.
status: in-progress
kind: theory
level: introductory
tags: [derivative, chain-rule, product-rule, implicit-differentiation, mean-value-theorem, lhopital, partial-derivative, total-differential, jacobian, hessian, stationary-point, lagrange-multipliers]
prerequisites: [limits-and-continuity]
related: [integral-calculus, scalar-and-vector-fields-and-the-gradient, multivariable-taylor-expansion, taylor-and-maclaurin-expansions, floating-point-and-numerical-error]
key: deriv
order: 30
date: 2026-11-25
---

Real functions. Subscripts on a parenthesis, $(\partial P/\partial V)_T$, name the variable held fixed, as in thermodynamics.

## The derivative

**Definition.** $f$ is differentiable at $a$ if the limit

$$
f'(a) = \frac{df}{dx}\Big|_a = \lim_{h\to0}\frac{f(a + h) - f(a)}{h}
\label{deriv}
$$

exists. Equivalently, $f(a + h) = f(a) + f'(a)h + o(h)$: the tangent line is the best linear approximation, and the error vanishes faster than $h$. Differentiability implies continuity; the converse fails ($|x|$ at 0 has one-sided slopes $\pm1$).

**Rules.** From Eq. [[#deriv]] and the algebra of limits ([[limits-and-continuity]]):

| rule | statement |
|---|---|
| linearity | $(af + bg)' = af' + bg'$ |
| product | $(fg)' = f'g + fg'$ |
| quotient | $(f/g)' = (f'g - fg')/g^2$ |
| chain | $\frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$ |
| inverse function | $(f^{-1})'(y) = 1/f'(x)$ with $y = f(x)$, where $f'(x)\ne0$ |

The Leibniz rule generalizes the product rule: $(fg)^{(n)} = \sum_k\binom nkf^{(k)}g^{(n-k)}$.

**Elementary derivatives.** $(x^n)' = nx^{n-1}$ (any real $n$, $x > 0$); $(e^x)' = e^x$; $(\ln x)' = 1/x$; $(\sin x)' = \cos x$ (using $\sin x/x\to1$); $(\cos x)' = -\sin x$; $(\arctan x)' = 1/(1 + x^2)$; $(\arcsin x)' = 1/\sqrt{1 - x^2}$, the last two from the inverse-function rule.

**Implicit differentiation.** If $F(x, y) = 0$ defines $y(x)$, differentiate the whole equation with the chain rule and solve for $y'$. For $x^2 + y^2 = 25$: $2x + 2yy' = 0$, so $y' = -x/y$.

**Higher derivatives.** $f''$ measures curvature: $f'' > 0$ means convex (the graph lies above its tangents). Logarithmic differentiation, $f'/f = (\ln f)'$, simplifies products and powers.

## Mean value theorem and L'Hôpital's rule

**Rolle and the mean value theorem.** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, there is a $c\in(a, b)$ with

$$
f'(c) = \frac{f(b) - f(a)}{b - a}.
$$

Rolle's theorem is the case $f(a) = f(b)$, which gives $f'(c) = 0$. Consequences:

- $f' = 0$ on an interval means $f$ is constant there;
- $f' > 0$ means $f$ is strictly increasing;
- $|f(b) - f(a)|\le\max|f'|\,|b - a|$, the basis of most error bounds, including Taylor's remainder ([[taylor-and-maclaurin-expansions]]).

**L'Hôpital's rule.** If $f(a) = g(a) = 0$ (or both tend to $\pm\infty$), $g'\ne0$ near $a$, and $\lim f'/g'$ exists, then $\lim_{x\to a}f/g = \lim_{x\to a}f'/g'$. Apply it repeatedly if the new quotient is again $0/0$. The other indeterminate forms are first rewritten as quotients: $x\ln x = \ln x/(1/x)$, and $1^\infty$ forms through the logarithm.

**Stationary points in one variable.** At an interior extremum of a differentiable $f$, $f'(a) = 0$. Then $f''(a) > 0$ gives a minimum, $f''(a) < 0$ a maximum; $f''(a) = 0$ is inconclusive ($x^3$, $x^4$).

## Several variables

**Partial derivatives.** For $f(x_1,\dots,x_n)$, $\partial f/\partial x_i$ differentiates with respect to $x_i$ holding the others fixed. If the second partials are continuous, mixed partials commute (Schwarz): $\partial^2f/\partial x\partial y = \partial^2f/\partial y\partial x$. This is what makes the Maxwell relations of thermodynamics and the symmetry of a Hessian hold.

**Total differential.** If the partials are continuous, $f$ is differentiable and

$$
df = \sum_i\frac{\partial f}{\partial x_i}dx_i = \nabla f\cdot d\mathbf x .
\label{totaldiff}
$$

A differential form $M\,dx + N\,dy$ is **exact** (the $df$ of some $f$) when $\partial M/\partial y = \partial N/\partial x$ on a simply connected region. State functions have exact differentials; heat and work do not.

**Chain rule.** If $x_i = x_i(t)$, then $\frac{d}{dt}f(\mathbf x(t)) = \sum_i\frac{\partial f}{\partial x_i}\frac{dx_i}{dt}$. If $x_i = x_i(u_1,\dots,u_m)$, then $\frac{\partial f}{\partial u_j} = \sum_i\frac{\partial f}{\partial x_i}\frac{\partial x_i}{\partial u_j}$.

**The cyclic relation.** For three variables tied by one relation $F(x, y, z) = 0$, setting $dz = 0$ in $dz = (\partial z/\partial x)_ydx + (\partial z/\partial y)_xdy$ gives

$$
\Big(\frac{\partial x}{\partial y}\Big)_z\Big(\frac{\partial y}{\partial z}\Big)_x\Big(\frac{\partial z}{\partial x}\Big)_y = -1 ,
\label{cyclic}
$$

not $+1$, as naive cancellation would suggest.

**Jacobian.** For a map $\mathbf y = \mathbf f(\mathbf x)$ from $\mathbb R^n$ to $\mathbb R^m$, the Jacobian matrix $J_{ij} = \partial y_i/\partial x_j$ is the best linear approximation, $d\mathbf y = \mathbf J\,d\mathbf x$. For $m = n$ its determinant gives the local volume scaling, which is what appears in a change of variables in integrals ([[integral-calculus]]). Chains of maps multiply their Jacobians.

**Stationary points and the Hessian.** At a stationary point $\nabla f = 0$. The Hessian $H_{ij} = \partial^2f/\partial x_i\partial x_j$ decides its type through its eigenvalues ([[multivariable-taylor-expansion]]):

- all positive: minimum;
- all negative: maximum;
- mixed signs: saddle point, with one negative eigenvalue for a first-order saddle (a transition state);
- a zero eigenvalue: inconclusive at second order.

**Lagrange multipliers.** To make $f(\mathbf x)$ stationary subject to $g(\mathbf x) = 0$, make $\mathcal L = f - \lambda g$ stationary in $\mathbf x$ and $\lambda$:

$$
\nabla f = \lambda\nabla g,\qquad g = 0 .
$$

At the solution the gradient of $f$ has no component along the constraint surface. Several constraints get one multiplier each. Orbital orthonormality in Hartree–Fock enters this way, and the multipliers become the orbital energies. Arfken Sec. 17.6 gives the variational form.

## Worked examples

!!! example "Derivatives, a cyclic relation, a saddle and a constrained maximum (computed for this note)"
    **Chain and product rules.** $\frac{d}{dx}\big[e^{-x^2}\sin3x\big] = e^{-x^2}(3\cos3x - 2x\sin3x)$. At $x = 0.7$ this is $-1.6682009244$. A central difference $[f(x + h) - f(x - h)]/2h$ gives $-1.6676769$ at $h = 10^{-2}$ and $-1.6682008720$ at $h = 10^{-4}$: the error falls as $h^2$ ([[floating-point-and-numerical-error]] for why $h$ cannot be made arbitrarily small).

    **Cyclic relation.** For $PV = RT$: $(\partial P/\partial V)_T = -RT/V^2$, $(\partial V/\partial T)_P = R/P$, $(\partial T/\partial P)_V = V/R$. The product is $-RT/(PV) = -1$, Eq. [[#cyclic]].

    **Stationary points of $f = x^3 - 3x + y^2$.** $\nabla f = (3x^2 - 3, 2y) = 0$ at $(\pm1, 0)$. The Hessian is $\mathrm{diag}(6x, 2)$: eigenvalues $(6, 2)$ at $(1, 0)$, a minimum, and $(-6, 2)$ at $(-1, 0)$, a first-order saddle.

    **Constrained maximum.** Maximize $xy$ on $x + y = 10$: $\nabla(xy) = \lambda\nabla(x + y)$ gives $y = \lambda$, $x = \lambda$, so $x = y = \lambda = 5$ and $xy = 25$. The multiplier is the rate of change of the optimum with the constraint: for $x + y = c$ the maximum is $c^2/4$, with derivative $c/2 = 5 = \lambda$.

    **Mean value theorem.** For $x^3$ on $[0, 2]$ the mean slope is 4, and $3c^2 = 4$ at $c = 2/\sqrt3 = 1.1547$, inside the interval.

    **L'Hôpital.** $\lim_{x\to0}(1 - \cos x)/x^2 = \lim\sin x/(2x) = \lim\cos x/2 = \tfrac12$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.6 (gradient and the total differential), Sec. 17.6 (Lagrange multipliers). The single-variable rules, the mean value theorem and L'Hôpital's rule are standard calculus, written for this note. Calculations in `Claude outputs/part0_math_batchE.py`, section A.
