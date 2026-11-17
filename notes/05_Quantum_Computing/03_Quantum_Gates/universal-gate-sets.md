---
id: universal-gate-sets
title: Universal gate sets - two-level unitaries, CNOT plus single-qubit gates, and H, S, T
summary: Three universality results in sequence. (1) Any d×d unitary is a product of at most d(d−1)/2 two-level unitaries, by Givens-type elimination, checked for d = 3, 4 and 8. (2) Each two-level unitary on n qubits is a Gray-code sequence of multiply-controlled gates, so CNOT plus single-qubit gates are exactly universal, though a generic n-qubit unitary costs O(n² 4ⁿ) gates. (3) The finite set {H, S, T, CNOT} approximates any unitary arbitrarily well. T·HTH is a rotation by θ = 2 arccos(cos²(π/8)) = 1.096057 about an axis along (cos π/8, sin π/8, cos π/8). θ is an irrational multiple of 2π, so its powers approach any rotation about that axis; numerically, reaching accuracy 10⁻², 10⁻³ needs about 47 and 2340 powers. The error measure E(U,V) bounds probability changes by 2E and adds along a circuit. Solovay–Kitaev improves the cost to O(logᶜ(1/ε)).
status: in-progress
kind: theory
level: intermediate
tags: [universality, two-level-unitary, givens-rotation, gray-code, clifford-t, solovay-kitaev, approximation, gate-synthesis, nielsen-chuang]
prerequisites: [single-qubit-gates-and-rotations, controlled-operations]
related: [unitary-matrices-exponential-logarithm, groups-representations-and-characters, matrix-eigenvalue-problem]
order: 30
date: 2026-11-17
---

## Overview

A gate set is **universal** if any unitary on any number of qubits can be approximated to arbitrary accuracy by a circuit built from it. Universality separates what a quantum computer *can* do from what it can do *efficiently*. This note follows Nielsen and Chuang's three steps:

1. Every unitary reduces to two-level unitaries.
2. Those reduce exactly to CNOT plus single-qubit gates.
3. Single-qubit gates reduce approximately to the finite set $\{H,S,T\}$.

A counting argument then shows that most unitaries cannot be built efficiently from any finite gate set.

## Step 1: two-level unitaries are universal

A **two-level unitary** acts nontrivially on only two basis vectors of $\mathbb C^d$. It is the identity except for a $2\times2$ unitary block, like a Givens rotation.

**Claim.** Any $d\times d$ unitary $U$ is a product of at most $d(d-1)/2$ two-level unitaries.

**Construction.**

1. **Clear the first column.** For each row $j>1$ with $U_{j1}\ne0$, apply a two-level unitary acting on rows 1 and $j$ that zeros $U_{j1}$, using the $2\times2$ block
$$
\frac{1}{\sqrt{|a|^2+|b|^2}}\begin{pmatrix}a^*&b^*\\ b&-a\end{pmatrix},\qquad (a,b)=(U_{11},U_{j1}).
$$
After at most $d-1$ such steps the first column is $(e^{i\phi},0,\dots,0)^T$. Unitarity then makes the first row zero apart from that entry too.
2. **Recurse.** Repeat on the remaining $(d-1)\times(d-1)$ block.
3. **Count.** This takes at most $(d-1)+(d-2)+\cdots+1=d(d-1)/2$ factors. Nielsen and Chuang choose each factor so the pivot becomes 1. Here the pivots keep their phases, leaving a diagonal matrix of phases that can be absorbed into the last factor of each column.
4. **Invert.** $U$ is then the product of the inverses, which are also two-level.

!!! example "Check"

    | $d$ | two-level factors used | bound $d(d-1)/2$ |
    |---:|---:|---:|
    | 3 | 3 | 3 |
    | 4 | 6 | 6 |
    | 8 | 28 | 28 |

    Random unitaries were used, and the leftover factor was diagonal in every case. For $n$ qubits ($d=2^n$) the bound is $2^{n-1}(2^n-1)$, which is 28 for $n=3$. Some unitaries need at least $d-1$ factors (Exercise 4.38), so exponential cost in $n$ cannot be avoided this way.

This is the same elimination used in QR factorization and in Jacobi diagonalization ([[matrix-eigenvalue-problem]]), here applied to unitary matrices.

## Step 2: CNOT plus single-qubit gates are universal

A two-level unitary on $n$ qubits acts on two basis states $|s\rangle$ and $|t\rangle$.

1. **Connect them by a Gray code.** Choose bit strings $s=g_1,g_2,\dots,g_m=t$, each differing from the next in one bit, with $m\le n+1$.
2. **Bring the states together.** Multiply-controlled NOTs permute $|g_1\rangle\to|g_2\rangle\to\cdots\to|g_{m-1}\rangle$. The two states now differ in a single qubit.
3. **Apply the gate.** A multiply-controlled single-qubit gate acts on that qubit.
4. **Undo the permutation.**

Each multiply-controlled gate costs $O(n)$ CNOTs and single-qubit gates ([[controlled-operations]]), so one two-level unitary costs $O(n^2)$. Combined with Step 1, an arbitrary $n$-qubit unitary costs $O(n^24^n)$ gates. The result is exact universality, at exponential cost for generic unitaries.

## Step 3: a finite set {H, S, T} approximates any single-qubit gate

**Error measure.** For gates $U$ and $V$, define

$$
E(U,V)=\max_{|\psi\rangle}\big\|(U-V)|\psi\rangle\big\| ,
$$

the operator norm of $U-V$. Two properties make it practical (Box 4.1):

- For any POVM element $M$, $|P_U-P_V|\le2E(U,V)$. Small $E$ means all measurement probabilities are close; the worst ratio seen over 200 random trials was 0.54, well inside the bound of 2.
- Errors add along a circuit: $E(U_m\cdots U_1,V_m\cdots V_1)\le\sum_jE(U_j,V_j)$.

So an $m$-gate circuit is approximated to accuracy $\Delta$ if each gate is approximated to $\Delta/(2m)$.

**An irrational rotation from H and T.**

1. $T=R_z(\pi/4)$ and $HTH=R_x(\pi/4)$, up to phase.
2. Their product is
$$
e^{-i\frac\pi8Z}e^{-i\frac\pi8X}=\cos^2\tfrac\pi8\,I-i\Big[\cos\tfrac\pi8(X+Z)+\sin\tfrac\pi8\,Y\Big]\sin\tfrac\pi8 ,
$$
a rotation $R_{\hat n}(\theta)$ about $\hat n\propto(\cos\frac\pi8,\sin\frac\pi8,\cos\frac\pi8)$ with $\cos(\theta/2)=\cos^2(\pi/8)$. This gives $\theta=1.096057$, and $\theta/2\pi=0.1744428601\ldots$
3. Nielsen and Chuang state that $\theta$ is an irrational multiple of $2\pi$. A numerical check cannot prove that.
4. Given irrationality, the angles $k\theta\bmod2\pi$ are dense, so some power $R_{\hat n}(\theta)^k$ comes within any $\varepsilon$ of any rotation $R_{\hat n}(\alpha)$, using $E(R_{\hat n}(\alpha),R_{\hat n}(\alpha+\beta))=|1-e^{i\beta/2}|$.

!!! example "How many powers? (target $R_{\hat n}(1.234)$)"

    | accuracy $E<$ | first power $k$ that works |
    |---:|---:|
    | $10^{-1}$ | 1 |
    | $10^{-2}$ | 47 |
    | $10^{-3}$ | 2340 |

    The count grows roughly like $1/\varepsilon$, with large fluctuations, as the pigeonhole argument predicts.

**Completing the argument.** Conjugating by $H$ gives a second axis: $HR_{\hat n}(\alpha)H=R_{\hat m}(\alpha)$ with $\hat m\propto(\cos\frac\pi8,-\sin\frac\pi8,\cos\frac\pi8)$, not parallel to $\hat n$. By the two-axis Euler decomposition ([[single-qubit-gates-and-rotations]]), every single-qubit $U$ equals $R_{\hat n}(\beta)R_{\hat m}(\gamma)R_{\hat n}(\delta)$ up to phase. Each factor is approximated by powers of $R_{\hat n}(\theta)$, the middle one conjugated by $H$. So $H$ and $T$ approximate every single-qubit gate.

$S=T^2$ adds nothing to this argument; it belongs to the standard set as a Clifford gate. Combined with Steps 1–2, **$\{H,S,T,\mathrm{CNOT}\}$ is universal**.

**Efficiency.** The pigeonhole construction needs about $1/\varepsilon$ gates per single-qubit gate. The **Solovay–Kitaev theorem** (N&C Appendix 3) reduces this to $O(\log^c(1/\varepsilon))$ with $c\approx2$. A circuit of $m$ arbitrary gates is then simulated to accuracy $\varepsilon$ with $O(m\log^c(m/\varepsilon))$ gates from the finite set, a polylogarithmic overhead.

## Most unitaries are hard

A counting argument (N&C Sec. 4.5.4, not reproduced here) shows that circuits of polynomial size from a finite gate set cover only a vanishing fraction of $n$-qubit unitaries: most need exponentially many gates. Universality says everything can be done; efficient algorithms are the rare cases with special structure. The structure exploited for chemistry is locality. Hamiltonian simulation and the circuits of Part 6 use only polynomially many local terms.

## Why it matters later

- **Fault tolerance.** Error-correcting codes make Clifford gates ($H$, $S$, CNOT) cheap but $T$ expensive. Resource estimates for chemistry on fault-tolerant hardware are therefore quoted in $T$ counts.
- **Compilation.** Near-term hardware compiles arbitrary single-qubit gates exactly (continuous rotations) and two-qubit gates into native entanglers. Gate counts in VQE and SQD circuits are counts of two-qubit gates.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 4.5, pp. 188–198:

- Sec. 4.5.1, pp. 189–191: two-level unitaries, Eqs. (4.41)–(4.52); Exercises 4.37–4.38.
- Sec. 4.5.2, pp. 191–193: Gray codes, Eqs. (4.53)–(4.60), and the $O(n^24^n)$ count.
- Sec. 4.5.3, pp. 194–197: the error measure, Eqs. (4.61)–(4.63); Box 4.1, Eqs. (4.64)–(4.73); the $H$, $T$ construction, Eqs. (4.74)–(4.81); Exercise 4.40; Solovay–Kitaev, with its proof in Appendix 3.
- Sec. 4.5.4, p. 198: hardness of approximating generic unitaries.

Page numbers are those printed in the book. The decomposition counts, error bounds, rotation angle and power counts are computed in `nielsen_chuang/part5_batch6.py` (section I).
