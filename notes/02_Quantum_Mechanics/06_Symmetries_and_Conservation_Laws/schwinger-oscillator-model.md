---
id: schwinger-oscillator-model
title: Schwinger's oscillator model of angular momentum
summary: Angular momentum built from two independent harmonic oscillators. With J₊ = a₊†a₋, J₋ = a₋†a₊ and J_z = (N₊ − N₋)/2 the angular momentum commutation relations hold identically, J² = (N/2)(N/2 + 1), and the oscillator state with n₊ and n₋ quanta is |j, m⟩ with j = (n₊ + n₋)/2, m = (n₊ − n₋)/2. A state of angular momentum j is pictured as 2j spin-1/2 quanta. Because a rotation simply mixes the two creation operators, the model gives Wigner's general formula for d^j(β) in a few lines.
status: in-progress
kind: derivation
level: intermediate
tags: [schwinger-oscillator-model, angular-momentum, harmonic-oscillator, ladder-operators, wigner-d-matrix, bosons, su2, sakurai]
prerequisites: [harmonic-oscillator-ladder-operators, orbital-angular-momentum, wigner-rotation-matrices]
related: [rotations-su2-so3-and-euler-angles, addition-of-angular-momenta, spin-one-half, creation-and-annihilation-operators]
order: 36
date: 2026-11-15
---

## Two oscillators

Take two independent oscillators, labelled $+$ and $-$, with annihilation operators $a_\pm$ obeying

$$
[a_+,a_+^\dagger] = [a_-,a_-^\dagger] = 1 ,\qquad [a_+,a_-^\dagger] = [a_+,a_-] = 0 ,
$$

number operators $N_\pm = a_\pm^\dagger a_\pm$ and the usual eigenstates ([[harmonic-oscillator-ladder-operators]])

$$
|n_+,n_-\rangle = \frac{(a_+^\dagger)^{n_+}(a_-^\dagger)^{n_-}}{\sqrt{n_+!\,n_-!}}\,|0,0\rangle .
$$

The oscillators need not describe any physical vibration; only their algebra is used.

## Angular momentum from the oscillators

Define

$$
\boxed{\,J_+ = \hbar\,a_+^\dagger a_- ,\qquad J_- = \hbar\,a_-^\dagger a_+ ,\qquad J_z = \frac\hbar2\big(N_+ - N_-\big)\,}
$$

$J_+$ moves one quantum from the $-$ oscillator to the $+$ oscillator. Using only the oscillator commutators,

$$
[J_z,J_\pm] = \pm\hbar J_\pm ,\qquad [J_+,J_-] = 2\hbar J_z ,
$$

the angular momentum algebra. With $N = N_+ + N_-$ the total number of quanta, a short calculation gives

$$
\mathbf J^2 = J_z^2 + \tfrac12(J_+J_- + J_-J_+) = \hbar^2\,\frac N2\Big(\frac N2 + 1\Big) .
$$

So the oscillator state $|n_+,n_-\rangle$ is an eigenstate of $\mathbf J^2$ and $J_z$ with

$$
j = \frac{n_+ + n_-}{2} ,\qquad m = \frac{n_+ - n_-}{2} ,
$$

and every $j = 0,\tfrac12,1,\tfrac32,\dots$ appears exactly once, each with all its $2j+1$ values of $m$, among the states with $N = 2j$. Inverting,

$$
|j,m\rangle = \frac{(a_+^\dagger)^{j+m}\,(a_-^\dagger)^{j-m}}{\sqrt{(j+m)!\,(j-m)!}}\,|0\rangle .
$$

The standard matrix element comes out directly: $J_+|j,m\rangle = \hbar\sqrt{(j+m+1)(j-m)}\,|j,m+1\rangle = \hbar\sqrt{j(j+1) - m(m+1)}\,|j,m+1\rangle$, since $a_+^\dagger$ contributes $\sqrt{n_++1}$ and $a_-$ contributes $\sqrt{n_-}$.

All of these relations, and the normalization of $|j,m\rangle$, were checked numerically in a truncated two-oscillator space for $j$ up to 3 (restricting to states well below the truncation).

**Picture.** One $+$ quantum is a spin-$\tfrac12$ particle with spin up, one $-$ quantum a spin-$\tfrac12$ particle with spin down. The state $|j,j\rangle = (a_+^\dagger)^{2j}|0\rangle/\sqrt{(2j)!}$ is $2j$ spin-up particles. The quanta are bosons, so the states are automatically symmetric under their exchange, and a symmetric combination of $2j$ spins $\tfrac12$ has total spin $j$. Any angular momentum is thus built from spin-$\tfrac12$ units, which is the reason the spin-$\tfrac12$ representation underlies all the others.

## Rotations and Wigner's formula

Because $\mathbf J$ is bilinear in the oscillator operators, a rotation acts on $(a_+^\dagger, a_-^\dagger)$ as on a spinor. For a rotation by $\beta$ about $y$, with $J_y = (J_+ - J_-)/2i$,

$$
\mathcal D(\beta)\,a_+^\dagger\,\mathcal D^{-1}(\beta) = a_+^\dagger\cos\frac\beta2 + a_-^\dagger\sin\frac\beta2 ,\qquad \mathcal D(\beta)\,a_-^\dagger\,\mathcal D^{-1}(\beta) = a_-^\dagger\cos\frac\beta2 - a_+^\dagger\sin\frac\beta2 ,
$$

exactly the transformation of spin up and spin down under $d^{(1/2)}(\beta)$ (checked numerically). Since the vacuum is invariant, $\mathcal D|0\rangle = |0\rangle$,

$$
\mathcal D(\beta)\,|j,m\rangle = \frac{\big[a_+^\dagger\cos\frac\beta2 + a_-^\dagger\sin\frac\beta2\big]^{j+m}\big[a_-^\dagger\cos\frac\beta2 - a_+^\dagger\sin\frac\beta2\big]^{j-m}}{\sqrt{(j+m)!\,(j-m)!}}\,|0\rangle .
$$

Expanding both brackets by the binomial theorem and reading off the coefficient of $(a_+^\dagger)^{j+m'}(a_-^\dagger)^{j-m'}|0\rangle$, which is $\sqrt{(j+m')!(j-m')!}\,|j,m'\rangle$, gives Wigner's formula

$$
d^{(j)}_{m'm}(\beta) = \sum_k(-1)^{k-m+m'}\frac{\sqrt{(j+m)!\,(j-m)!\,(j+m')!\,(j-m')!}}{(j+m-k)!\;k!\;(j-k-m')!\;(k-m+m')!}\Big(\cos\frac\beta2\Big)^{2j-2k+m-m'}\Big(\sin\frac\beta2\Big)^{2k-m+m'} ,
$$

used in [[wigner-rotation-matrices]]. For $j = 2$, $\beta = 0.83$, the matrix computed by rotating the oscillator states agrees with the formula to $4\times10^{-16}$.

## Remarks

- The construction is an example of a general device: representing a Lie algebra by bilinear combinations of boson operators (here $\mathfrak{su}(2)$ by two bosons). The same idea, with fermion operators, is used for spin operators in second quantization (Part 4).
- Coupling two angular momenta corresponds to four oscillators, and Schwinger used this to derive the Clebsch-Gordan coefficients as well. This is not developed here.
- A related trick represents a single spin by bosons with a constraint (the Holstein-Primakoff and Schwinger-boson representations of magnetism); these are mentioned only for orientation.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.9.1, pp. 218-222 (oscillator algebra (3.394)-(3.396), definitions of $J_\pm$ and $J_z$, $\mathbf J^2$ in terms of $N$, the states (3.411)-(3.412), the spin-$\tfrac12$ picture); Sec. 3.9.2, pp. 222-223 (rotation of the creation operators (3.418)-(3.420) and Wigner's formula (3.426)). Sakurai attributes the model to Schwinger's unpublished notes, reprinted in Biedenharn and Van Dam (1965).

The remarks on boson representations are orientation only, not from Sakurai. Checks are in `sakurai/companions_ch2_ch4.py` (section D).
