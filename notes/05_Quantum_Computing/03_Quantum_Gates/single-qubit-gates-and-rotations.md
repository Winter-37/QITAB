---
id: single-qubit-gates-and-rotations
title: Single-qubit gates, rotations and the Z-Y decomposition
summary: Single-qubit gates are 2×2 unitaries. The standard set is X, Y, Z, H, S and T, with H = (X+Z)/√2, S = T² and T = e^{iπ/8}R_z(π/4). The rotation R_n(θ) = exp(−iθ n·σ/2) = cos(θ/2) I − i sin(θ/2) n·σ turns the Bloch vector by θ about n. Every single-qubit unitary is e^{iα}R_z(β)R_y(γ)R_z(δ) (Theorem 4.1, verified with an explicit angle extraction). Corollary 4.2 writes U = e^{iα}AXBXC with ABC = I, the key to controlled gates; for H the angles are α = π/2, β = 0, γ = π/2, δ = π. Covers the circuit identities HXH = Z, HYH = −Y, HZH = X and HTH = R_x(π/4). For the composition of two rotations, the printed Eq. (4.20) holds for the product in the opposite order to the one the exercise describes.
status: in-progress
kind: theory
level: intermediate
tags: [single-qubit-gates, pauli-gates, hadamard, phase-gate, t-gate, rotation-operators, bloch-sphere, euler-angles, zyz-decomposition, nielsen-chuang]
prerequisites: [qubits-and-the-bloch-sphere, rotations-su2-so3-and-euler-angles, functions-of-matrices]
related: [controlled-operations, universal-gate-sets, unitary-matrices-exponential-logarithm, spin-one-half, two-level-systems-and-rabi-oscillations]
order: 10
date: 2026-11-17
---

## Overview

A gate on one qubit is a $2\times2$ unitary matrix, since it must preserve normalization. This note lists the gates used throughout Part 5 and gives their geometric meaning as rotations of the Bloch sphere. It then proves that every single-qubit gate is a product of three rotations about two fixed axes, which is also the Euler-angle parametrization of SU(2) from [[rotations-su2-so3-and-euler-angles]]. The final result, Corollary 4.2, is what makes controlled gates buildable from CNOTs.

## The standard gates

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
S=\begin{pmatrix}1&0\\0&i\end{pmatrix},\quad
T=\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}.
$$

- **$X$ (NOT, bit flip)** swaps $|0\rangle\leftrightarrow|1\rangle$. **$Z$** flips the sign of $|1\rangle$. **$Y=iXZ$**.
- **Hadamard** $H=(X+Z)/\sqrt2$ maps $|0\rangle\to|+\rangle$ and $|1\rangle\to|-\rangle$. It is its own inverse and exchanges the $Z$ and $X$ bases.
- **Phase gate** $S=T^2$, and **$T$** (historically the "$\pi/8$ gate", because $T=e^{i\pi/8}\,\mathrm{diag}(e^{-i\pi/8},e^{i\pi/8})$).

**Conjugation identities** (N&C Exercise 4.13):

$$
HXH=Z,\qquad HYH=-Y,\qquad HZH=X,\qquad HTH=R_x(\pi/4)\ \text{(up to global phase)}.
$$

Conjugating by $H$ swaps the roles of the $x$ and $z$ axes.

## Rotations

For a real unit vector $\hat n$, $(\hat n\cdot\boldsymbol\sigma)^2=I$, so $e^{iAx}=\cos x\,I+i\sin x\,A$ for any $A$ with $A^2=I$ gives

$$
\boxed{\,R_{\hat n}(\theta)\equiv e^{-i\theta\,\hat n\cdot\boldsymbol\sigma/2}=\cos\tfrac\theta2\,I-i\sin\tfrac\theta2\,(n_xX+n_yY+n_zZ)\,}
$$

and in particular

$$
R_x(\theta)=\begin{pmatrix}\cos\frac\theta2&-i\sin\frac\theta2\\-i\sin\frac\theta2&\cos\frac\theta2\end{pmatrix},\quad
R_y(\theta)=\begin{pmatrix}\cos\frac\theta2&-\sin\frac\theta2\\\sin\frac\theta2&\cos\frac\theta2\end{pmatrix},\quad
R_z(\theta)=\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}.
$$

**Geometric meaning (Exercise 4.6).** $R_{\hat n}(\theta)$ rotates the Bloch vector by $\theta$ about $\hat n$, right-handed. This was checked against the SO(3) rotation matrix $e^{\theta K_{\hat n}}$ for a random axis and state. The half angle in $R$ is the half angle of the Bloch parametrization: Hilbert-space angles are half of sphere angles ([[qubits-and-the-bloch-sphere]]). It is also why $R_{\hat n}(2\pi)=-I$, the spin-½ sign change of [[rotation-operator-and-rotational-symmetry]].

**Every gate is a rotation up to phase (Exercise 4.8).** $U=e^{i\alpha}R_{\hat n}(\theta)$ for some $\alpha,\theta,\hat n$, because $e^{-i\alpha}U$ can be made special unitary. For example,

$$
H=e^{i\pi/2}R_{\hat n}(\pi)\ \ \text{with}\ \hat n=(1,0,1)/\sqrt2 ,\qquad
S=e^{i\pi/4}R_z(\pi/2),\qquad T=e^{i\pi/8}R_z(\pi/4).
$$

So $H$ is a half-turn about the axis halfway between $x$ and $z$, and $S$ and $T$ are quarter- and eighth-turns about $z$.

**Composing two rotations (Exercise 4.15).** Let $c_i=\cos(\beta_i/2)$ and $s_i=\sin(\beta_i/2)$. Multiplying out with $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma)=(\mathbf a\cdot\mathbf b)I+i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$, the rotation by $\beta_1$ about $\hat n_1$ *followed by* $\beta_2$ about $\hat n_2$, i.e. $R_{\hat n_2}(\beta_2)R_{\hat n_1}(\beta_1)$, is a rotation $\beta_{12}$ about $\hat n_{12}$ with

$$
c_{12}=c_1c_2-s_1s_2\,\hat n_1\cdot\hat n_2,\qquad
s_{12}\hat n_{12}=s_1c_2\,\hat n_1+c_1s_2\,\hat n_2+s_1s_2\,\hat n_2\times\hat n_1 .
$$

Nielsen and Chuang print the last term as $-s_1s_2\,\hat n_2\times\hat n_1$ (Eq. 4.20). That sign is correct for the product in the other order, $R_{\hat n_1}(\beta_1)R_{\hat n_2}(\beta_2)$. Both statements were checked numerically. Whichever order is meant, the cross term records that rotations do not commute.

## Theorem 4.1: the Z-Y decomposition

**Theorem.** For every single-qubit unitary $U$ there are real $\alpha,\beta,\gamma,\delta$ with

$$
U=e^{i\alpha}R_z(\beta)\,R_y(\gamma)\,R_z(\delta)
=\begin{pmatrix}
e^{i(\alpha-\beta/2-\delta/2)}\cos\frac\gamma2 & -e^{i(\alpha-\beta/2+\delta/2)}\sin\frac\gamma2\\
e^{i(\alpha+\beta/2-\delta/2)}\sin\frac\gamma2 & e^{i(\alpha+\beta/2+\delta/2)}\cos\frac\gamma2
\end{pmatrix}.
$$

**Proof.** The columns of $U$ are orthonormal, so the entries have the moduli shown, with a common $\gamma$. The four phases of a unitary matrix satisfy one relation (the product of the diagonal phases equals minus the product of the off-diagonal phases), which leaves exactly three free phases, $\alpha,\beta,\delta$.

**Extracting the angles.**

1. $\alpha=\tfrac12\arg\det U$.
2. With $V=e^{-i\alpha}U\in\mathrm{SU}(2)$, take $\gamma=2\arctan(|V_{10}|/|V_{00}|)$.
3. Take $\beta=\arg V_{11}+\arg V_{10}$ and $\delta=\arg V_{11}-\arg V_{10}$.

This reproduced 20 random unitaries to machine precision. These are the Euler angles of the rotation (z-y-z convention), and $\alpha$ is the U(1) phase that SU(2) lacks.

**Any two non-parallel axes work (Exercise 4.11):** $U=e^{i\alpha}R_{\hat n}(\beta)R_{\hat m}(\gamma)R_{\hat n}(\delta)$. This is used below and in [[universal-gate-sets]] with the two axes generated by $T$ and $HTH$.

## Corollary 4.2: the ABC form

**Corollary.** Every single-qubit unitary can be written

$$
U=e^{i\alpha}AXBXC,\qquad ABC=I,
$$

with

$$
A=R_z(\beta)R_y(\tfrac\gamma2),\qquad
B=R_y(-\tfrac\gamma2)R_z\big(-\tfrac{\delta+\beta}2\big),\qquad
C=R_z\big(\tfrac{\delta-\beta}2\big).
$$

**Proof.**

1. $ABC=I$ by direct multiplication: the $R_y$ factors cancel, then the $R_z$ factors.
2. $XR_y(\theta)X=R_y(-\theta)$ and $XR_z(\theta)X=R_z(-\theta)$ (Exercise 4.7). Hence $XBX=R_y(\tfrac\gamma2)R_z(\tfrac{\delta+\beta}2)$.
3. Therefore $AXBXC=R_z(\beta)R_y(\gamma)R_z(\delta)$.

Checked for 20 random unitaries. The point of the construction: when the two $X$ gates are switched off, the remaining product is $ABC=I$. When they are on, it is $e^{-i\alpha}U$. Replacing the $X$ gates by CNOTs therefore gives a controlled-$U$ ([[controlled-operations]]).

!!! example "Hadamard (Exercise 4.12)"
    The extraction gives $\alpha=\pi/2$, $\beta=0$, $\gamma=\pi/2$ and $\delta=\pi$, so $H=e^{i\pi/2}R_y(\pi/2)R_z(\pi)$. The ABC factors are then $A=R_y(\pi/4)$, $B=R_y(-\pi/4)R_z(-\pi/2)$ and $C=R_z(\pi/2)$.

## Physical realization

On hardware a single-qubit gate is a resonant drive pulse ([[two-level-systems-and-rabi-oscillations]]). The drive's phase selects an axis in the $xy$ plane, and its area selects the angle. $R_z$ is often implemented "virtually" by shifting the phase reference of later pulses, so it is free. Common native sets are therefore {virtual $R_z$, $\sqrt X$}, and every other single-qubit gate is compiled to a Z-X-Z-X-Z sequence by the same Euler-angle logic. This remark is general hardware practice, not from Nielsen and Chuang.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 1.3.1, pp. 17–20: single-qubit gates, Eqs. (1.8)–(1.17), and Box 1.1.
- Sec. 4.2, pp. 174–177:
  - the gate definitions, Eqs. (4.1)–(4.3);
  - rotations, Eqs. (4.4)–(4.8);
  - Theorem 4.1, Eqs. (4.11)–(4.12);
  - Corollary 4.2, Eqs. (4.14)–(4.17);
  - Exercises 4.1–4.15, Eqs. (4.18)–(4.22).

Page numbers are those printed in the book. All identities and the composition-order check are in `nielsen_chuang/part5_batch6.py` (section G).
