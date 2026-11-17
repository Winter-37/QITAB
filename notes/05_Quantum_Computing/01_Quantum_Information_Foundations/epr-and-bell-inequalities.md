---
id: epr-and-bell-inequalities
title: EPR, Bell's inequality and the CHSH bound
summary: Local realism (definite pre-existing values, no influence between distant measurements) implies E(QS) + E(RS) + E(RT) − E(QT) ≤ 2 (CHSH). For the singlet with Q = Z₁, R = X₁, S = −(Z₂ + X₂)/√2, T = (Z₂ − X₂)/√2, quantum mechanics predicts 2√2. Tsirelson's identity B² = 4I + [Q,R]⊗[S,T] shows that 2√2 is the largest possible quantum value. Also gives Sakurai's three-direction form, P(a+;b+) ≤ P(a+;c+) + P(c+;b+). With the singlet value ½ sin²(θ/2) it is violated for every coplanar bisecting geometry with 0 < θ < π/2, as 0.500 > 0.293 at θ = π/4. Starts from the EPR perfect anticorrelation of the singlet along every axis.
status: in-progress
kind: theory
level: intermediate
tags: [bell-inequality, chsh, tsirelson-bound, epr, local-realism, singlet, entanglement, nonlocality, nielsen-chuang, sakurai]
prerequisites: [projective-and-povm-measurements, multi-qubit-states-and-bell-states, addition-of-angular-momenta]
related: [quantum-postulates-for-information, schmidt-decomposition-and-purification, spin-one-half]
order: 30
date: 2026-11-17
---

## Overview

Quantum mechanics predicts only probabilities for measurement outcomes. Einstein, Podolsky and Rosen (EPR) argued that this makes it incomplete: a better theory would assign definite values that measurements merely reveal. Bell showed that this question can be tested. Any theory with definite pre-existing values and no influence between distant measurements obeys an inequality that quantum mechanics violates, and experiments side with quantum mechanics. For quantum information the lesson is practical: entangled states supply correlations that no classical resource can reproduce.

## EPR anticorrelation

Take the singlet $|\psi\rangle=(|01\rangle-|10\rangle)/\sqrt2$, with qubit 1 held by Alice and qubit 2 by Bob. For any single-qubit unitary $U$,

$$
(U\otimes U)\,|\psi\rangle=\det(U)\,|\psi\rangle ,
$$

so the singlet looks the same in every basis, up to a global phase (Box 2.7). Measuring $\mathbf v\cdot\boldsymbol\sigma$ on both qubits therefore always gives opposite results, whatever the axis $\mathbf v$. More generally $\langle(\mathbf a\cdot\boldsymbol\sigma)\otimes(\mathbf b\cdot\boldsymbol\sigma)\rangle=-\mathbf a\cdot\mathbf b$.

EPR's reasoning: Alice can predict Bob's result along any axis with certainty, without touching his qubit, so by their criterion that result is an "element of reality". Quantum mechanics assigns no such value for every axis at once, so it must be incomplete.

## The CHSH inequality (local realism)

Forget quantum mechanics for the derivation. Charlie repeatedly prepares two particles and sends one each to Alice and Bob. Alice measures one of two properties with values $Q,R=\pm1$, and Bob one of $S,T=\pm1$. Each chooses at random, and the two measurements are causally disconnected. Assume:

1. **Realism.** $Q,R,S,T$ have definite values before measurement, with some joint distribution $p(q,r,s,t)$.
2. **Locality.** Alice's choice cannot affect Bob's value, and vice versa.

For every assignment,

$$
QS+RS+RT-QT=(Q+R)S+(R-Q)T=\pm2 ,
$$

because one of $Q+R$ and $R-Q$ vanishes and the other is $\pm2$. Averaging over $p(q,r,s,t)$ and using linearity of the mean,

$$
\boxed{\ \mathrm E(QS)+\mathrm E(RS)+\mathrm E(RT)-\mathrm E(QT)\ \le\ 2\ }
$$

This is the CHSH (Clauser–Horne–Shimony–Holt) form of Bell's inequality. Each term can be estimated from the runs in which that pair of settings was chosen.

## The quantum prediction

Use the singlet and the observables

$$
Q=Z_1,\qquad R=X_1,\qquad S=\frac{-Z_2-X_2}{\sqrt2},\qquad T=\frac{Z_2-X_2}{\sqrt2}.
$$

Then $\langle QS\rangle=\langle RS\rangle=\langle RT\rangle=1/\sqrt2$ and $\langle QT\rangle=-1/\sqrt2$, so

$$
\langle QS\rangle+\langle RS\rangle+\langle RT\rangle-\langle QT\rangle=2\sqrt2\approx2.828>2 .
$$

All four axes lie in the $xz$ plane. Each correlation is the singlet value $-\mathbf a\cdot\mathbf b$ for Alice's axis $\mathbf a$ and Bob's axis $\mathbf b$; the three positive terms come from pairs $45^\circ$ from antiparallel, and the negative term from a pair $45^\circ$ from parallel.

## Tsirelson's bound: 2√2 is the quantum maximum

For $Q=\mathbf q\cdot\boldsymbol\sigma$ and similarly for $R,S,T$, with unit vectors, each operator squares to $I$. A direct expansion (N&C Problem 2.3) gives

$$
B\equiv Q\otimes S+R\otimes S+R\otimes T-Q\otimes T,\qquad
B^2=4I+[Q,R]\otimes[S,T].
$$

Each commutator has norm at most 2, so $\|B^2\|\le8$ and $|\langle B\rangle|\le2\sqrt2$ in every state. The singlet example reaches the bound. Numerically, over 2000 random choices of the four axes, the largest $|$eigenvalue$|$ of $B$ was 2.8284. Quantum correlations exceed every local-realistic model but are themselves bounded. The bound is due to Tsirelson.

## Sakurai's three-direction form

Sakurai derives Bell's original style of inequality from a model due to Wigner. Each particle of a singlet pair carries definite signs for spin along three unit vectors $\hat a,\hat b,\hat c$, with perfect anticorrelation between partners. With populations $N_1,\dots,N_8$ of the eight types, the pairs giving "A finds $\hat a+$, B finds $\hat b+$" are $N_3+N_4$. Positivity gives $N_3+N_4\le(N_2+N_4)+(N_3+N_7)$, that is,

$$
P(\hat a+;\hat b+)\ \le\ P(\hat a+;\hat c+)+P(\hat c+;\hat b+).
$$

Quantum mechanics gives, for the singlet, $P(\hat a+;\hat b+)=\tfrac12\sin^2(\theta_{ab}/2)$. Take coplanar vectors with $\hat c$ bisecting, $\theta_{ab}=2\theta$ and $\theta_{ac}=\theta_{cb}=\theta$. The inequality then becomes

$$
\sin^2\theta\ \le\ 2\sin^2(\theta/2),
$$

which fails for every $0<\theta<\pi/2$. At $\theta=\pi/4$ it reads $0.500\le0.293$, which is false. The largest violation, $\tfrac14$, occurs at $\theta=\pi/3$; that maximum is my addition, checked numerically.

## What is given up

The derivation used only realism and locality, plus free choice of settings, so experiments that violate CHSH rule out **local realism**. At least one of the two assumptions must go. Most physicists drop realism: values do not exist before measurement. A minority keep realism and give up locality. Experiments with photon polarization and, in one case, proton spins agree with the quantum predictions within error. Sakurai cites violations by more than nine standard deviations.

## Why it matters later

- **Entanglement is a resource.** Superdense coding and teleportation ([[multi-qubit-states-and-bell-states]], and the planned [[quantum-teleportation]]) do things impossible with classical correlations.
- **Device-independent tests.** A measured CHSH value above 2 certifies entanglement without trusting the devices. This underlies device-independent key distribution and randomness certification.
- **Benchmarking hardware.** Preparing a Bell pair and measuring the CHSH combination is a standard check of two-qubit gate quality.

## Source

- Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 2.6, pp. 111–117: Box 2.7 (Eqs. 2.213–2.217); the CHSH derivation, Eqs. (2.219)–(2.225); the quantum example, Eqs. (2.226)–(2.230); local realism, p. 117. Problem 2.3 (Tsirelson's inequality), Eqs. (2.233)–(2.234), p. 118. Page numbers are those printed in the book.
- Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.10, pp. 224–231: Wigner's model (3.431), Table 3.2, Bell's inequality (3.432)–(3.435), the quantum probability (3.436)–(3.437), the violation (3.438)–(3.441).

All numbers are checked in `nielsen_chuang/part5_batch6.py` (section C).
