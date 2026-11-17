---
id: quantum-fourier-transform
title: The quantum Fourier transform
summary: The QFT maps |j⟩ → 2^{−n/2} Σ_k e^{2πijk/2ⁿ}|k⟩, the discrete Fourier transform on the 2ⁿ amplitudes, with N&C's + sign, so QFT = √N·ifft in NumPy. Its output on a basis state factorizes into single-qubit states, (|0⟩ + e^{2πi0.jₙ}|1⟩)⊗…⊗(|0⟩ + e^{2πi0.j₁…jₙ}|1⟩). This product form gives a circuit of n Hadamards, n(n−1)/2 controlled-R_k phase gates and ⌊n/2⌋ swaps, Θ(n²) gates against Θ(n2ⁿ) for the classical FFT. Verified against the matrix for n = 1–5, including Box 5.1's 3-qubit case. Dropping the smallest rotations gives the approximate QFT. Measured on 8 qubits, keeping R_k up to k = 6 uses 25 of 28 controlled rotations at operator-norm error 0.12, and up to k = 7 uses 27 at 0.025. The amplitudes cannot be read out; the QFT is useful only inside algorithms such as phase estimation.
status: in-progress
kind: algorithm
level: intermediate
tags: [quantum-fourier-transform, qft, discrete-fourier-transform, product-representation, controlled-phase, binary-fraction, approximate-qft, nielsen-chuang]
prerequisites: [fourier-transforms-and-the-dirac-delta, controlled-operations, single-qubit-gates-and-rotations]
related: [quantum-phase-estimation, deutsch-jozsa-and-quantum-parallelism, universal-gate-sets]
order: 20
date: 2026-11-17
---

## Overview

The discrete Fourier transform is one of the most used algorithms in computing. Its quantum version acts on the $2^n$ amplitudes of an $n$-qubit register using only $O(n^2)$ gates, exponentially fewer than the classical FFT's $O(n2^n)$ operations on the same vector. The catch is that the transformed amplitudes cannot be read out. The QFT is useful as a subroutine that turns information stored in phases into information stored in bit values, as phase estimation does ([[quantum-phase-estimation]]).

## Definition

With $N=2^n$ and integers $j,k\in\{0,\dots,N-1\}$ identified with their binary strings,

$$
\mathrm{QFT}\,|j\rangle=\frac1{\sqrt N}\sum_{k=0}^{N-1}e^{2\pi ijk/N}|k\rangle ,
\qquad
\sum_jx_j|j\rangle\ \mapsto\ \sum_ky_k|k\rangle,\quad y_k=\frac1{\sqrt N}\sum_jx_je^{2\pi ijk/N}.
$$

The matrix $F_{kj}=\omega^{jk}/\sqrt N$, with $\omega=e^{2\pi i/N}$, is unitary (Exercise 5.1). $\mathrm{QFT}|0\ldots0\rangle$ is the uniform superposition (Exercise 5.2).

**Sign convention.** Nielsen and Chuang use $e^{+2\pi ijk/N}$, the opposite of NumPy's forward FFT. Numerically $\mathrm{QFT}=\sqrt N\cdot$`numpy.fft.ifft`, verified for $N=16$. The same warning appears in [[fourier-transforms-and-the-dirac-delta]].

## Product representation

Write $j=j_1j_2\cdots j_n$ in binary, so $j=\sum_lj_l2^{n-l}$, and use binary fractions $0.j_lj_{l+1}\cdots j_m=\sum_{p=l}^mj_p2^{-(p-l+1)}$. Expanding $k$ in bits, the sum over $k$ factorizes:

$$
\mathrm{QFT}|j_1\cdots j_n\rangle=\frac{\big(|0\rangle+e^{2\pi i\,0.j_n}|1\rangle\big)\big(|0\rangle+e^{2\pi i\,0.j_{n-1}j_n}|1\rangle\big)\cdots\big(|0\rangle+e^{2\pi i\,0.j_1j_2\cdots j_n}|1\rangle\big)}{2^{n/2}} .
$$

The key step is $e^{2\pi ijk_l2^{-l}}$, which depends only on the last $l$ bits of $j$, because integer multiples of $2\pi$ drop out. Checked for $j=5$, $n=3$.

Two consequences follow:

- **No entanglement.** The QFT of a basis state is a product state. Each output qubit carries one binary fraction of $j$.
- **A short circuit.** Each factor can be built from one Hadamard and controlled phases. The Hadamard on $|j_l\rangle$ gives $|0\rangle+e^{2\pi i\,0.j_l}|1\rangle$, because $e^{2\pi i\,0.j_l}=(-1)^{j_l}$, and controlled phases add the later bits.

## The circuit

With $R_k=\mathrm{diag}(1,e^{2\pi i/2^k})$:

1. **Qubit 1.** Apply $H$, then controlled-$R_2$ from qubit 2, controlled-$R_3$ from qubit 3, …, controlled-$R_n$ from qubit $n$. Qubit 1 now holds $|0\rangle+e^{2\pi i\,0.j_1\cdots j_n}|1\rangle$.
2. **Qubit 2.** Apply $H$, then controlled-$R_2,\dots,R_{n-1}$ from qubits $3,\dots,n$.
3. **Continue** down to qubit $n$, which gets only $H$.
4. **Swap.** Reverse the qubit order with $\lfloor n/2\rfloor$ swaps. Without the swaps, the factors come out in reverse order.

**Cost.** $n$ Hadamards and $n(n-1)/2$ controlled rotations, $n(n+1)/2$ gates in all, plus $\lfloor n/2\rfloor$ swaps of three CNOTs each: $\Theta(n^2)$. Verified to reproduce the QFT matrix exactly for $n=1,\dots,5$.

!!! example "Three qubits (Box 5.1)"
    $F$ has entries $\omega^{jk}/\sqrt8$ with $\omega=e^{2\pi i/8}=\sqrt i$. The circuit is: $H$ on qubit 1; controlled-$S$ ($=R_2$) from qubit 2; controlled-$T$ ($=R_3$) from qubit 3; $H$ on qubit 2; controlled-$S$ from qubit 3; $H$ on qubit 3; then swap qubits 1 and 3.

**Inverse QFT.** Reverse the gate order and conjugate the phases (Exercise 5.5). This is the version used in phase estimation.

## Approximate QFT

The rotations $R_k$ with large $k$ are tiny: $|1-e^{2\pi i/2^k}|\approx2\pi/2^k$. Dropping all $R_k$ with $k>m$ removes $(n-m)(n-m+1)/2$ of the $n(n-1)/2$ controlled rotations, leaving about $nm$. Since errors add (Box 4.1, [[universal-gate-sets]]), the operator-norm error is at most about $n\cdot2\pi/2^m$.

!!! example "Eight qubits"

    | keep $R_k$ for $k\le$ | controlled rotations | $E(U,V)$ |
    |---:|---:|---:|
    | 4 | 18 of 28 | 1.13 |
    | 5 | 22 | 0.41 |
    | 6 | 25 | 0.12 |
    | 7 | 27 | 0.025 |
    | 8 | 28 | 0 |

    $m\approx\log_2n$ plus a few bits is enough for a fixed accuracy, so the gate count becomes $O(n\log n)$. Exercise 5.6 makes the related point that each gate needs only polynomial precision.

## What the QFT is not

The QFT does not let one compute Fourier transforms of classical data faster. Loading $2^n$ numbers into amplitudes and reading the result out both cost exponentially. Its power is structural: it converts a periodic phase pattern $\sum_ke^{2\pi i\varphi k}|k\rangle$ into a sharply peaked distribution on the bits of $\varphi$. That conversion is the last step of phase estimation, order finding and Shor's algorithm.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 5.1, pp. 217–221:

- Eqs. (5.1)–(5.19);
- the product representation, Eqs. (5.4)–(5.10);
- the circuit, Figure 5.1 and Eqs. (5.11)–(5.18);
- Box 5.1 (three qubits);
- the $\Theta(n^2)$ count;
- Exercises 5.1–5.6.

Page numbers are those printed in the book. The approximate-QFT table is computed here. All checks are in `nielsen_chuang/part5_batch7.py` (section E).
