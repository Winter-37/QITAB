---
id: stark-effect
title: The Stark effect in hydrogen
summary: Energy shifts of hydrogen in a uniform electric field. Parity kills the first-order shift of any nondegenerate level, so the ground state shifts quadratically with polarizability α = (9/2) a0³ (in units of 4πε0), obtained exactly by solving the first-order equation in closed form. The sum over bound states alone gives only 81 percent of it. The n = 2 level is degenerate in l, mixes 2s with 2p0 and shifts linearly by ±3 e a0 times the field strength, which is degenerate perturbation theory at work.
status: in-progress
kind: derivation
level: intermediate
tags: [stark-effect, electric-field, polarizability, parity, degenerate-perturbation-theory, hydrogen-atom, dalgarno-lewis, sum-over-states, griffiths, sakurai]
prerequisites: [degenerate-perturbation-theory, hydrogen-atom, parity-and-parity-selection-rules]
related: [rayleigh-schrodinger-perturbation-theory, molecular-properties-and-response, rotational-selection-rules-and-wigner-eckart, zeeman-effect]
order: 14
date: 2026-11-14
---

## Setup and selection rules

A uniform field $\boldsymbol{\mathcal E} = \mathcal E\,\hat{\mathbf z}$ adds the potential energy of the electron (charge $-e$)

$$
H' = e\,\mathcal E\,z = e\,\mathcal E\,r\cos\theta
$$

to the Bohr Hamiltonian. Spin plays no role and is dropped. In atomic units ([[atomic-units]]) $H' = Fz$ with $F$ the field in units of $E_h/(e a_0) = 5.142\times10^{11}$ V/m, so every laboratory field is a small perturbation.

Two selection rules fix which matrix elements $\langle n'l'm'|z|nlm\rangle$ survive.

- **Parity.** $z$ is odd and $|nlm\rangle$ has parity $(-1)^l$, so $l' + l$ must be odd ([[parity-and-parity-selection-rules]]).
- **Rotation about z.** $[L_z, z] = 0$ gives $m' = m$. As the $q = 0$ component of a vector operator, $z$ also obeys $l' = l\pm1$ ([[rotational-selection-rules-and-wigner-eckart]]).

Consequently $\langle nlm|z|nlm\rangle = 0$: a state of definite parity has no permanent dipole moment, and a nondegenerate level has no first-order shift.

## Ground state: the quadratic effect

The ground state is nondegenerate, so $E^1 = 0$ and the leading shift is

$$
E^2 = -e^2\mathcal E^2\sum_{k\neq 1s}\frac{|\langle k|z|1s\rangle|^2}{E_k - E_1} \equiv -\tfrac12\,\alpha\,\mathcal E^2 .
$$

The sum runs over all $p$ states with $m = 0$, bound and continuum. Since every denominator is positive the shift is downward. The induced dipole is $\alpha\mathcal E$, which makes $\alpha$ the static dipole polarizability, the second derivative of the energy with respect to the field ([[molecular-properties-and-response]]).

### Exact solution of the first-order equation

The infinite sum can be avoided. The first-order wave function obeys

$$
(H^0 - E_1)\,\psi^1 = -(H' - E^1)\,\psi_{100} = -e\mathcal E\,r\cos\theta\,\psi_{100} ,
$$

and $E^2 = \langle\psi_{100}|H'|\psi^1\rangle$. Try $\psi^1 = f(r)\cos\theta\,\psi_{100}$. In atomic units, with $\psi_{100} = e^{-r}/\sqrt\pi$, the equation becomes an ordinary differential equation for $f$ whose polynomial solution is

$$
\psi^1 = -F\Big(r + \frac{r^2}{2}\Big)\cos\theta\;\psi_{100} .
$$

Then

$$
E^2 = -F^2\int\Big(r^2 + \frac{r^3}{2}\Big)\cos^2\theta\,|\psi_{100}|^2\,d^3r
= -F^2\cdot\frac13\Big(\langle r^2\rangle + \tfrac12\langle r^3\rangle\Big)
= -F^2\cdot\frac13\Big(3 + \frac{15}{4}\Big) = -\frac94\,F^2 ,
$$

using $\langle r^2\rangle = 3$ and $\langle r^3\rangle = 15/2$ for the 1s state. Hence

$$
\alpha = \frac92\,a_0^3\ \ (\text{Gaussian units})\qquad\text{or}\qquad \alpha = \frac92\,(4\pi\varepsilon_0)\,a_0^3 = 7.42\times10^{-41}\ \mathrm{C\,m^2/V} ,
$$

a polarizability volume of $0.667$ Å$^3$. This closed-form route is often called the Dalgarno-Lewis method; Griffiths sets it as a problem and Sakurai quotes the result.

### How the sum over states converges

For the bound $p$ states the matrix elements have a closed form,

$$
|\langle n10|z|100\rangle|^2 = \frac{2^8\,n^7\,(n-1)^{2n-5}}{3\,(n+1)^{2n+5}}\;a_0^2 ,
$$

so each term of the sum can be evaluated.

| Contribution to $\alpha/a_0^3$ | Value | Fraction of 9/2 |
|---|---|---|
| $n = 2$ only | 2.9596 | 65.8% |
| all bound states | 3.6633 | 81.4% |
| continuum (by difference) | 0.8367 | 18.6% |
| exact | 4.5000 | 100% |

The continuum carries almost a fifth of the polarizability. A sum over bound states cannot converge to the right answer, which is one reason response equations are solved directly in practice instead of by summing over excited states.

Simple bounds bracket the result. Keeping the $n = 2$ term alone gives a lower bound, $\alpha > 2.96\,a_0^3$. Replacing every denominator by the smallest one, $E_2 - E_1 = 3/8$, and using closure, $\sum_k|\langle k|z|1s\rangle|^2 = \langle z^2\rangle = a_0^2$, gives the upper bound $\alpha < 16a_0^3/3 = 5.33\,a_0^3$.

## The n = 2 level: the linear effect

Without spin the $n = 2$ level is four-fold degenerate: $2s$, $2p_0$, $2p_{\pm1}$. The selection rules leave a single nonzero element of $\mathbf W$,

$$
\langle 200|z|210\rangle = -3a_0 ,
$$

so in the order $(2s, 2p_0, 2p_{+1}, 2p_{-1})$

$$
\mathbf W = -3e\mathcal Ea_0
\begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix} .
$$

The first-order energies and good states ([[degenerate-perturbation-theory]]) are

| $E^1$ | Good state |
|---|---|
| $+3e\mathcal Ea_0$ | $(\psi_{200} - \psi_{210})/\sqrt2$ |
| $-3e\mathcal Ea_0$ | $(\psi_{200} + \psi_{210})/\sqrt2$ |
| $0$ (twice) | $\psi_{21\pm1}$ |

The shift is linear in the field. The mixed states have no definite parity and carry a permanent dipole moment of magnitude $3ea_0$ along or against the field. This is special to hydrogen: the $l$ degeneracy of the Coulomb potential lets an arbitrarily weak field mix states of opposite parity. In other atoms $2s$ and $2p$ are split, each level has definite parity, and the Stark effect is quadratic.

$L_z$ commutes with $H'$, which is why $m$ stays a good quantum number and the $m = \pm1$ states do not mix, an instance of the commuting-operator theorem. The degeneracy between $m = +1$ and $m = -1$ is not lifted at any order, because reflection in a plane containing the field maps one into the other.

!!! example "Size of the shifts"

    At $\mathcal E = 10^7$ V/m, a strong laboratory field:

    - $n = 2$ linear shift: $3e\mathcal Ea_0 = 1.59\times10^{-3}$ eV.
    - Ground-state quadratic shift: $\tfrac94F^2E_h$ with $F = 10^7/5.142\times10^{11} = 1.94\times10^{-5}$, that is $2.3\times10^{-8}$ eV.

    The linear formula assumes the Stark shift is large compared with the fine-structure splitting of $n = 2$, $4.5\times10^{-5}$ eV ([[hydrogen-fine-structure]]), which requires $\mathcal E\gg3\times10^5$ V/m. In weaker fields the fine-structure states are the right starting point.

## Caveats

- With the field on, the potential $-e^2/(4\pi\varepsilon_0r) + e\mathcal Ez$ falls without limit for $z\to-\infty$. No state is strictly bound: the electron can tunnel out, and the perturbation series is asymptotic. For laboratory fields the ionization rate of low levels is negligible.
- For $n = 3$ the same method gives a $9\times9$ matrix that splits into blocks of fixed $m$ (Griffiths' Problem 7.46).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Problems 7.45 and 7.46 (Stark effect for $n = 1, 2, 3$), 7.51(a) (direct solution of the first-order equation for the ground state) and 7.54 (polarizability). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.1, Eqs. (5.62)-(5.72), pp. 297-299 (quadratic effect, bounds and the exact polarizability), and Sec. 5.2, Eqs. (5.89)-(5.94), pp. 303-304 (linear effect for $n = 2$).

The first-order wave function, $\langle200|z|210\rangle$, the closed form for $|\langle n10|z|100\rangle|^2$ (checked against direct integration for $n = 2$) and the table of partial sums are computed in `griffiths/ch07_perturbation.py` (section E) with SymPy. The closed form itself is a standard result, not quoted from either book.
