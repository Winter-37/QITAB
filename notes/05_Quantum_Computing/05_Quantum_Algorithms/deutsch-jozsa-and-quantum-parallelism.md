---
id: deutsch-jozsa-and-quantum-parallelism
title: Quantum parallelism, Deutsch's algorithm and the Deutsch–Jozsa algorithm
summary: A reversible oracle U_f|x,y⟩ = |x, y⊕f(x)⟩ applied once to a uniform superposition produces Σ_x|x,f(x)⟩, but measuring it yields only one value: parallelism alone gains nothing. Interference does. With the answer qubit in |−⟩, the oracle writes f into phases, (−1)^{f(x)}|x⟩ (phase kickback). A final Hadamard layer then makes the amplitude of |0…0⟩ equal Σ_x(−1)^{f(x)}/2ⁿ. Deutsch's algorithm finds f(0)⊕f(1) with one query. Deutsch–Jozsa decides constant versus balanced with one query, where a deterministic classical algorithm needs 2^{n−1}+1 in the worst case. Verified for n = 1–4. Notes that a randomized classical algorithm also solves the problem with high probability, so the separation is for exact answers.
status: in-progress
kind: algorithm
level: introductory
tags: [quantum-parallelism, oracle, phase-kickback, deutsch-algorithm, deutsch-jozsa, interference, hadamard-transform, query-complexity, nielsen-chuang]
prerequisites: [controlled-operations, measurement-in-quantum-circuits]
related: [quantum-fourier-transform, quantum-phase-estimation, concentration-inequalities-and-sampling]
order: 10
date: 2026-11-17
---

## Overview

Why can a quantum computer be faster? It is *not* simply that it evaluates a function on all inputs at once, since a measurement returns only one result. The speed-up comes from **interference**. Many evaluations are combined so that the amplitudes of unwanted answers cancel and the wanted global property survives. Deutsch's and the Deutsch–Jozsa algorithms are the smallest examples. They are of no practical use, but they contain the structure of phase estimation and Shor's algorithm:

1. superpose;
2. query, with the answer written into phases;
3. interfere with a Fourier-type transform;
4. measure.

## The oracle and quantum parallelism

A function $f:\{0,1\}^n\to\{0,1\}$ is made reversible as

$$
U_f|x\rangle|y\rangle=|x\rangle|y\oplus f(x)\rangle ,
$$

which is unitary for any $f$; a classical circuit for $f$ can be compiled into one with Toffoli gates ([[controlled-operations]]). Applying $U_f$ once to the uniform superposition $H^{\otimes n}|0\rangle^{\otimes n}=2^{-n/2}\sum_x|x\rangle$, with $y=0$, gives

$$
\frac1{\sqrt{2^n}}\sum_x|x\rangle|f(x)\rangle .
$$

Every value of $f$ appears in the state after **one** call: this is **quantum parallelism**. But measuring returns a single random pair $(x,f(x))$, no better than one classical evaluation. Useful algorithms must extract a *global* property of $f$.

## Phase kickback

Put the answer qubit in $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$. Then

$$
U_f|x\rangle|-\rangle=(-1)^{f(x)}|x\rangle|-\rangle ,
$$

because $|0\oplus f\rangle-|1\oplus f\rangle=(-1)^f(|0\rangle-|1\rangle)$. The answer qubit is unchanged, and $f$ appears as a **phase** on the input register. This is the same kickback as CNOT in the $\pm$ basis ([[controlled-operations]]) and in phase estimation.

## Deutsch's algorithm (n = 1)

1. Start in $|0\rangle|1\rangle$ and apply $H\otimes H$, giving $|{+}\rangle|{-}\rangle$.
2. Query: the first qubit becomes $\tfrac1{\sqrt2}\big[(-1)^{f(0)}|0\rangle+(-1)^{f(1)}|1\rangle\big]$.
3. Apply $H$ to the first qubit. Up to a sign, the result is $|f(0)\oplus f(1)\rangle|{-}\rangle$.
4. Measuring the first qubit gives $f(0)\oplus f(1)$ with certainty, using **one** query. Classically two are needed.

Checked for all four functions on one bit, together with the parallel state $(|0,f(0)\rangle+|1,f(1)\rangle)/\sqrt2$.

## The Deutsch–Jozsa algorithm

**Promise problem.** $f$ on $n$ bits is either **constant** or **balanced** (0 on exactly half the inputs). Decide which.

1. Start in $|0\rangle^{\otimes n}|1\rangle$ and apply $H^{\otimes(n+1)}$, giving $2^{-n/2}\sum_x|x\rangle|-\rangle$.
2. Query: the register becomes $2^{-n/2}\sum_x(-1)^{f(x)}|x\rangle$.
3. Apply $H^{\otimes n}$, using $H^{\otimes n}|x\rangle=2^{-n/2}\sum_z(-1)^{x\cdot z}|z\rangle$:
$$
\frac1{2^n}\sum_z\Big[\sum_x(-1)^{x\cdot z+f(x)}\Big]|z\rangle .
$$
4. Measure. The amplitude of $z=0\ldots0$ is $\sum_x(-1)^{f(x)}/2^n$:
   - **$f$ constant:** the amplitude is $\pm1$, so the result is all zeros with certainty.
   - **$f$ balanced:** the contributions cancel exactly, so the result is never all zeros.

!!! example "Check"

    | $n$ | $P(0\ldots0)$, constant $f$ | $P(0\ldots0)$, 6 random balanced $f$ | classical deterministic, worst case |
    |---:|---:|---:|---:|
    | 1 | 1 | 0 | 2 queries |
    | 2 | 1 | 0 | 3 queries |
    | 3 | 1 | 0 | 5 queries |
    | 4 | 1 | 0 | 9 queries |

    The quantum algorithm uses one query in every case. A deterministic classical algorithm may see $2^{n-1}$ equal values before it can conclude, so it needs $2^{n-1}+1$ queries.

**Caveat.** A randomized classical algorithm that queries $k$ random inputs and answers "constant" if they all agree errs with probability at most $2^{1-k}$ for a balanced $f$, independent of $n$ (N&C Exercise 1.1). The exponential separation therefore holds only for *exact* answers. Speed-ups that survive against bounded-error classical algorithms, such as Simon's and Shor's, need more structure. Phase estimation, built on the same superpose–query–interfere pattern, is the general tool ([[quantum-phase-estimation]]).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Secs. 1.4.1–1.4.2, pp. 29–31: reversible oracles and quantum parallelism, Eqs. (1.37)–(1.40).
- Sec. 1.4.3, pp. 32–33: Deutsch's algorithm, Eqs. (1.41)–(1.45).
- Sec. 1.4.4, pp. 34–36: Deutsch–Jozsa, Eqs. (1.46)–(1.51), and Exercise 1.1.

Page numbers are those printed in the book. All checks are in `nielsen_chuang/part5_batch7.py` (section D).
