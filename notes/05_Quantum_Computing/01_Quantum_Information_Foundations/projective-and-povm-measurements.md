---
id: projective-and-povm-measurements
title: Projective measurements, POVMs, and why non-orthogonal states cannot be distinguished
summary: Two special cases of the general measurement postulate. A projective measurement is the spectral decomposition of an observable, with average ⟨M⟩ = ⟨ψ|M|ψ⟩ and repeatable outcomes. A POVM keeps only the positive operators E_m = M_m†M_m, which fix all outcome probabilities. Proves that non-orthogonal states cannot be distinguished reliably (Box 2.3), and works the Nielsen-Chuang POVM that identifies |0⟩ or |+⟩ without ever erring. It succeeds with probability 1 − 1/√2 = 0.2929, the optimal value for unambiguous discrimination of these two states. Also covers spin measurement along an axis, the uncertainty relation of Box 2.4, the polar form M_m = U_m√E_m, and an unambiguous POVM for any set of linearly independent states.
status: in-progress
kind: theory
level: intermediate
tags: [projective-measurement, povm, state-discrimination, unambiguous-discrimination, observable, uncertainty-principle, spin-measurement, nielsen-chuang]
prerequisites: [quantum-postulates-for-information, spectral-decomposition-and-normal-operators]
related: [generalized-uncertainty-principle, polar-and-singular-value-decompositions, concentration-inequalities-and-sampling, qubits-and-the-bloch-sphere]
order: 20
date: 2026-11-17
---

## Overview

Postulate 3 ([[quantum-postulates-for-information]]) describes any measurement by operators $M_m$ with $\sum_mM_m^\dagger M_m=I$. Two restrictions of it are used constantly:

- **Projective measurements**, the measurement of an observable familiar from Part 2. These are what a quantum computer does at the end of a circuit.
- **POVMs**, which keep only what determines the outcome probabilities. These are the right tool when the post-measurement state does not matter, as in state discrimination and the analysis of sampling.

## Projective measurements

An observable is a Hermitian operator with spectral decomposition $M=\sum_m m\,P_m$, where $P_m$ projects onto the eigenspace of eigenvalue $m$. Measuring it on $|\psi\rangle$ gives

$$
p(m)=\langle\psi|P_m|\psi\rangle ,\qquad |\psi\rangle\mapsto\frac{P_m|\psi\rangle}{\sqrt{p(m)}} .
$$

This is Postulate 3 with $M_m=P_m$ orthogonal projectors, $P_mP_{m'}=\delta_{mm'}P_m$. Two consequences:

- **Averages.** $\mathrm E(M)=\sum_mm\,p(m)=\langle\psi|M|\psi\rangle$, and $[\Delta(M)]^2=\langle M^2\rangle-\langle M\rangle^2$.
- **Repeatability.** Measuring again gives the same $m$ with certainty and leaves the state unchanged. Many real measurements, such as detecting a photon by absorbing it, are not repeatable, which is one reason to keep the general postulate.

"Measuring in the basis $\{|m\rangle\}$" means using $P_m=|m\rangle\langle m|$.

**Spin along an axis.** For a real unit vector $\mathbf v$, the observable $\mathbf v\cdot\boldsymbol\sigma=v_1X+v_2Y+v_3Z$ has eigenvalues $\pm1$ and projectors $P_\pm=(I\pm\mathbf v\cdot\boldsymbol\sigma)/2$ (N&C Exercise 2.60). On $|0\rangle$ the result $+1$ occurs with probability $(1+v_3)/2$. Measuring $X$ on $|0\rangle$ gives $\langle X\rangle=0$ and $\Delta X=1$.

**Uncertainty (Box 2.4).** For observables $C,D$, the Cauchy–Schwarz inequality gives

$$
\Delta(C)\,\Delta(D)\ \ge\ \tfrac12\,\big|\langle\psi|[C,D]|\psi\rangle\big| ,
$$

the same Robertson relation as in [[generalized-uncertainty-principle]]. For $X$ and $Y$ on $|0\rangle$, $[X,Y]=2iZ$ gives $\Delta X\Delta Y\ge1$, and both deviations equal 1, so the bound is reached. The relation concerns the spreads of results on identically prepared copies. It says nothing about a measurement of $C$ disturbing a later measurement of $D$.

## POVMs

Define $E_m=M_m^\dagger M_m$. Then $E_m\ge0$, $\sum_mE_m=I$, and $p(m)=\langle\psi|E_m|\psi\rangle$. The **POVM** $\{E_m\}$ (positive operator-valued measure) fixes all the outcome statistics but not the post-measurement state. Conversely, any set of positive operators summing to $I$ is a POVM, realized for example by $M_m=\sqrt{E_m}$. In general the measurement operators are $M_m=U_m\sqrt{E_m}$ for some unitaries $U_m$ (N&C Exercise 2.63; this is the polar decomposition, [[polar-and-singular-value-decompositions]]). Different $U_m$ change the post-measurement state but not the statistics.

A projective measurement is the special case where $E_m=M_m=P_m$. A measurement whose operators coincide with its POVM elements is necessarily projective (Exercise 2.62).

## Non-orthogonal states cannot be distinguished reliably

Alice gives Bob one state from a known set $\{|\psi_i\rangle\}$, and Bob must name $i$.

- **Orthonormal states.** Measure with $M_i=|\psi_i\rangle\langle\psi_i|$, plus $M_0=\sqrt{I-\sum_i|\psi_i\rangle\langle\psi_i|}$ for completeness. Outcome $i$ occurs with certainty.
- **Non-orthogonal states (Box 2.3).** Suppose a measurement distinguished $|\psi_1\rangle$ and $|\psi_2\rangle$ perfectly. Group outcomes by Bob's guess: $E_i=\sum_{j:f(j)=i}M_j^\dagger M_j$. Perfect distinction means $\langle\psi_1|E_1|\psi_1\rangle=\langle\psi_2|E_2|\psi_2\rangle=1$. Then $\langle\psi_1|E_2|\psi_1\rangle=0$, so $\sqrt{E_2}|\psi_1\rangle=0$. Write $|\psi_2\rangle=\alpha|\psi_1\rangle+\beta|\varphi\rangle$ with $|\varphi\rangle\perp|\psi_1\rangle$ and $|\beta|<1$. This gives

$$
\langle\psi_2|E_2|\psi_2\rangle=|\beta|^2\langle\varphi|E_2|\varphi\rangle\le|\beta|^2<1 ,
$$

a contradiction. The overlap of the states is information Bob can never fully recover. This is the basis of quantum key distribution, and of the impossibility of copying unknown states (the planned [[no-cloning-theorem]]).

## Unambiguous discrimination: a worked POVM

Bob can still identify the state *sometimes*, provided he is allowed an inconclusive answer. For $|\psi_1\rangle=|0\rangle$ and $|\psi_2\rangle=|+\rangle$, Nielsen and Chuang take

$$
E_1=\frac{\sqrt2}{1+\sqrt2}\,|1\rangle\langle1| ,\qquad
E_2=\frac{\sqrt2}{1+\sqrt2}\,|-\rangle\langle-| ,\qquad
E_3=I-E_1-E_2 .
$$

$E_1$ is orthogonal to $|0\rangle$, so outcome 1 certifies $|+\rangle$. $E_2$ is orthogonal to $|+\rangle$, so outcome 2 certifies $|0\rangle$. Outcome 3 is inconclusive.

!!! example "Outcome probabilities"

    | state | $p(E_1)$ | $p(E_2)$ | $p(E_3)$ |
    |---|---:|---:|---:|
    | $\lvert0\rangle$ | 0 | 0.292893 | 0.707107 |
    | $\lvert+\rangle$ | 0.292893 | 0 | 0.707107 |

    Bob never errs, and succeeds with probability $1-1/\sqrt2=1-|\langle0|+\rangle|$ for either state. The prefactor $\sqrt2/(1+\sqrt2)$ is the largest that keeps $E_3$ positive: $E_3$ has a zero eigenvalue. For two pure states with equal prior probabilities, $1-|\langle\psi_1|\psi_2\rangle|$ is the known optimum of unambiguous discrimination (the Ivanovic–Dieks–Peres limit). That optimality statement is my addition and is not proved in Nielsen and Chuang.

**Linearly independent states (Exercise 2.64).** For linearly independent $|\psi_1\rangle,\dots,|\psi_m\rangle$, let $|d_i\rangle$ be the dual vectors, $\langle d_i|\psi_j\rangle=\delta_{ij}$ (rows of the inverse of the matrix whose columns are the $|\psi_j\rangle$). Then $E_i=\lambda|d_i\rangle\langle d_i|/\langle d_i|d_i\rangle$ for $i\le m$, and $E_{m+1}=I-\sum_iE_i$, form an unambiguous POVM. Here $\lambda$ is the inverse of the largest eigenvalue of $\sum_i|d_i\rangle\langle d_i|/\langle d_i|d_i\rangle$. Checked for three random states in $\mathbb C^3$: all elements are positive, $\langle\psi_j|E_i|\psi_j\rangle=0$ for $i\ne j$, and every success probability is positive. Linearly dependent states admit no such scheme.

## Why it matters later

- **The end of every quantum circuit is a projective measurement** in the computational basis. Estimating $\langle P\rangle$ for a Pauli string from repeated shots is a statistics problem ([[concentration-inequalities-and-sampling]]), and is the cost driver of VQE.
- **Sample-based methods** read out computational-basis bit strings and use only their frequencies, a POVM view of the device.
- **Noise and error correction** (planned chapters) describe imperfect measurements and decoherence with the same operator language.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 2.2.4, pp. 86–87: distinguishing quantum states, and Box 2.3 (Eqs. 2.99–2.101).
- Sec. 2.2.5, pp. 87–90: projective measurements, Eqs. (2.102)–(2.116); Box 2.4 (Eqs. 2.105–2.109); Exercises 2.58–2.61.
- Sec. 2.2.6, pp. 90–93: POVMs, Eq. (2.117); Box 2.5; the example (2.118)–(2.120); Exercises 2.62–2.64.

Page numbers are those printed in the book. The probabilities, the optimality comparison and the Exercise 2.64 construction are computed in `nielsen_chuang/part5_batch6.py` (section B).
