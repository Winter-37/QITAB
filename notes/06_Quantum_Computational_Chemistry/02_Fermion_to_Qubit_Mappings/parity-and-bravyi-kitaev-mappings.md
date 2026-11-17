---
id: parity-and-bravyi-kitaev-mappings
title: Parity and Bravyi–Kitaev mappings - encodings as binary matrices, update and parity sets, Pauli weights
summary: An encoding stores a binary vector b = B n (mod 2) in the qubits instead of the occupations n. Jordan–Wigner has B = 1, parity stores prefix sums, and Bravyi–Kitaev stores Fenwick-tree partial sums. The map |n⟩ → |Bn⟩ is a CNOT circuit, so every encoding is a Clifford rotation of Jordan–Wigner. A ladder operator becomes a_j† = ½(X_U X_j Z_P − i X_U Y_j Z_R), with update, parity and remainder sets read off from B; for Bravyi–Kitaev the weight is log₂M + 1 (5 for M = 16, 7 for M = 64), against up to M for the other two. Being Clifford, the encodings leave the number of Pauli terms, the 1-norm λ and the spectrum unchanged; only the weights change. For H₂ to N₂ in STO-3G, BK changes the mean Hamiltonian weight by between +12% (H₂) and −19% (N₂) and lowers the maximum from M to 7–13. Verified against operators built from the definition, anticommutators, and FCI and HF energies.
status: in-progress
kind: theory
level: intermediate
tags: [qubit-mapping, parity-mapping, bravyi-kitaev, jordan-wigner, pauli-weight, clifford, fenwick-tree]
prerequisites: [jordan-wigner-mapping, molecular-hamiltonian-in-the-mo-basis]
related: [qubit-tapering, trotter-error-in-qpe-energies, variational-quantum-eigensolver, sample-based-quantum-diagonalization, controlled-operations]
order: 20
date: 2026-11-17
---

## Overview

Jordan–Wigner stores each occupation number $n_j$ in its own qubit ([[jordan-wigner-mapping]]). Occupations are then local, but the fermionic sign $(-1)^{\sum_{k<j}n_k}$ needs a string of $Z$s on every lower qubit, so an operator on orbital $j$ acts on up to $M$ qubits. The opposite extreme stores parities, so the sign is local but changing one occupation must update many qubits. The Bravyi–Kitaev encoding stores partial sums arranged so that both costs are $O(\log M)$. This note treats all three as one construction and measures what changes for molecular Hamiltonians.

**Conventions.** $M$ spin orbitals, interleaved $(0\alpha,0\beta,1\alpha,\dots)$ as in [[molecular-hamiltonian-in-the-mo-basis]]. Occupation vector $\mathbf n\in\{0,1\}^M$. All arithmetic on bit vectors is mod 2. Qubit indices start at 0.

## Encodings as binary matrices

An encoding is an invertible binary matrix $B$; the qubit register holds $|\mathbf b\rangle=|B\mathbf n\rangle$.

| encoding | qubit $j$ stores | $B_{jk}=1$ for |
|---|---|---|
| Jordan–Wigner | $n_j$ | $k=j$ |
| parity | $\sum_{k\le j}n_k$ | $k\le j$ |
| Bravyi–Kitaev | $\sum_{k=j+1-\ell(j+1)}^{j}n_k$ | $j+1-\ell(j+1)\le k\le j$ |

Here $\ell(m)$ is the lowest set bit of $m$ ($\ell(6)=2$, $\ell(8)=8$), so qubit $j$ holds a block of $\ell(j+1)$ occupations ending at $j$. This is a Fenwick (binary indexed) tree. For $M=8$:

$$
B_{\text{BK}}=\begin{pmatrix}
1&&&&&&&\\ 1&1&&&&&&\\ &&1&&&&&\\ 1&1&1&1&&&&\\ &&&&1&&&\\ &&&&1&1&&\\ &&&&&&1&\\ 1&1&1&1&1&1&1&1
\end{pmatrix}
$$

For $M=2^k$ it is built recursively: $B_{2m}=\begin{pmatrix}B_m&0\\A_m&B_m\end{pmatrix}$, where $A_m$ is zero except for a last row of ones. This is the recursion of Seeley, Richard and Love (2012), written here with qubit $j$ as row $j$; their paper orders indices in the opposite direction (orientation to verify against the paper). The Fenwick definition works for any $M$, not only powers of two.

**Every encoding is a Clifford rotation of Jordan–Wigner.** The map $U:|\mathbf n\rangle\mapsto|B\mathbf n\rangle$ is a permutation of basis states built from CNOT gates ([[controlled-operations]]). An operator in encoding $B$ is $U\,O_{\text{JW}}\,U^\dagger$. Writing a Pauli string as $i^{n_Y}X^{\mathbf x}Z^{\mathbf z}$, conjugation gives

$$
U\,X^{\mathbf x}U^\dagger=X^{B\mathbf x},\qquad U\,Z^{\mathbf z}U^\dagger=Z^{B^{-T}\mathbf z},
$$

since $X^{\mathbf x}$ shifts $\mathbf n\to\mathbf n+\mathbf x$ and $Z^{\mathbf z}$ multiplies by $(-1)^{\mathbf z\cdot\mathbf n}$. Each Pauli string therefore maps to a single Pauli string, with a phase fixed by $XZ=-iY$. The verification script uses exactly this to transform Hamiltonians.

## Ladder operators: update, parity and remainder sets

$a_j$ must (i) flip $n_j$, (ii) multiply by $(-1)^{\sum_{k<j}n_k}$, and (iii) act only when $n_j=1$. In an encoding $B$ each requirement picks a set of qubits:

- **Update set** $U(j)=\{k\ne j: B_{kj}=1\}$. These are the other qubits whose stored sums contain $n_j$; flipping $n_j$ means applying $X$ to $j$ and to all of $U(j)$.
- **Parity set** $P(j)$. These are the qubits whose stored values add up to $\sum_{k<j}n_k$: the support of $B^{-T}\mathbf e_{<j}$, where $\mathbf e_{<j}$ has ones below $j$. Then $Z_{P(j)}=(-1)^{\sum_{k<j}n_k}$.
- **Flip set** $F(j)\subseteq P(j)$. These are the lower qubits whose stored values together with $b_j$ give $n_j$, that is $n_j=b_j+\sum_{k\in F(j)}b_k$. So $(-1)^{\hat n_j}=Z_jZ_{F(j)}$.
- **Remainder set** $R(j)=P(j)\setminus F(j)$.

With Majorana operators $c_j=a_j+a_j^\dagger$ and $d_j=i(a_j^\dagger-a_j)$:

$$
c_j=X_{U(j)}X_jZ_{P(j)},\qquad d_j=i\,c_j(-1)^{\hat n_j}=X_{U(j)}\,(iX_jZ_j)\,Z_{P(j)}Z_{F(j)}=X_{U(j)}Y_jZ_{R(j)} .
$$

The second step uses $iXZ=Y$ and $Z_PZ_F=Z_{P\setminus F}$ for $F\subseteq P$. Hence

$$
a_j^\dagger=\tfrac12\big(X_{U(j)}X_jZ_{P(j)}-i\,X_{U(j)}Y_jZ_{R(j)}\big),\qquad
a_j=\tfrac12\big(X_{U(j)}X_jZ_{P(j)}+i\,X_{U(j)}Y_jZ_{R(j)}\big),
$$

the form given by Seeley, Richard and Love.

**Special cases.**
- Jordan–Wigner: $U=\varnothing$, $P=\{0,\dots,j-1\}$, $F=\varnothing$.
- Parity: $U=\{j+1,\dots,M-1\}$, $P=F=\{j-1\}$, so $a_j=\tfrac12 X_{>j}(X_jZ_{j-1}+iY_j)$.

!!! example "Bravyi–Kitaev sets for $M=8$"

    | $j$ | $U(j)$ | $P(j)$ | $F(j)$ | $R(j)$ |
    |---|---|---|---|---|
    | 0 | 1, 3, 7 | – | – | – |
    | 1 | 3, 7 | 0 | 0 | – |
    | 2 | 3, 7 | 1 | – | 1 |
    | 3 | 7 | 1, 2 | 1, 2 | – |
    | 4 | 5, 7 | 3 | – | 3 |
    | 5 | 7 | 3, 4 | 4 | 3 |
    | 6 | 7 | 3, 5 | – | 3, 5 |
    | 7 | – | 3, 5, 6 | 3, 5, 6 | – |

    Every $|U|+|P|+1$ here equals 4. For $M=8$, 12, 16 and 64 the script checks three things:
    - the set formula equals $U a_j^{\text{JW}}U^\dagger$ term by term;
    - both equal the operator defined directly on encoded basis states, $|B\mathbf n\rangle\mapsto(-1)^{\sum_{k<j}n_k}|B(\mathbf n-\mathbf e_j)\rangle$;
    - $\{a_p,a_q^\dagger\}=\delta_{pq}$ and $\{a_p,a_q\}=0$ hold to machine precision in all three encodings.

**Weights.** The largest Pauli weight of $a_j$ over $j$ is 16 / 16 / 5 for JW / parity / BK at $M=16$, and 64 / 64 / 7 at $M=64$, that is $\log_2M+1$ for BK.

## Molecular Hamiltonians in the three encodings

Because $U$ is Clifford, it permutes Pauli strings one to one. The **number of terms, the multiset of $|c_k|$, the 1-norm $\lambda$ and the spectrum are all identical** in the three encodings; only which qubits each string touches changes. Hartree–Fock remains a basis state, $|B\mathbf n_{\text{HF}}\rangle$. For H₂, $|1100\rangle$ becomes $|1000\rangle$ in both the parity and BK encodings.

STO-3G, RHF orbitals (point-group adapted), identity excluded from the weights:

| system | $M$ | terms | $\lambda$ ($E_h$) | JW mean / max | parity mean / max | BK mean / max |
|---|---:|---:|---:|---|---|---|
| H₂, 0.735 Å | 4 | 15 | 1.894 | 2.29 / 4 | 2.43 / 4 | 2.57 / 4 |
| H₄ chain, 1.0 Å | 8 | 185 | 7.145 | 4.61 / 8 | 4.72 / 8 | 4.59 / 7 |
| LiH, 1.6 Å | 12 | 631 | 12.341 | 6.17 / 12 | 6.40 / 12 | 5.63 / 10 |
| H₂O | 14 | 1086 | 71.998 | 7.06 / 14 | 7.24 / 14 | 6.24 / 10 |
| H₈ chain, 1.0 Å | 16 | 2913 | 33.500 | 8.14 / 16 | 8.22 / 16 | 7.08 / 10 |
| N₂, 1.098 Å | 20 | 2239 | 114.707 | 9.47 / 20 | 9.62 / 20 | 7.65 / 13 |

Checks:
- For H₂, H₄ and LiH the full $2^M$ spectra agree to $10^{-13}$ across encodings.
- The $N$-electron ground state is the FCI energy in each encoding (LiH: $-7.8823243789$), with $N$ read from the encoded number operator.
- $\langle B\mathbf n_{\text{HF}}|\hat H|B\mathbf n_{\text{HF}}\rangle=E_{\text{RHF}}$.

**Reading the table.**
- **For small molecules the gain is modest.** Relative to JW, BK's mean weight is 12% higher for H₂, about equal for H₄, and 9–19% lower from LiH to N₂. The maximum weight drops from $M$ to between 7 and 13. Parity is slightly heavier than JW throughout.
- **The scaling argument is asymptotic.** BK's advantage grows like $M/\log M$ in operator weight. Whether it gives shorter circuits depends on how the circuit is compiled. Tranter et al. (2018), across 86 molecules, found BK circuits equal to or shorter than JW ones, with the clearest gains under limited circuit optimization.
- **Weight is not the only cost.** The term count, $\lambda$ and the Trotter-error commutators do not depend on the encoding, so phase-estimation cost estimates based on $\lambda$ ([[qpe-cost-and-resource-estimates]]) are unaffected. The Trotter error itself is unchanged too, because it is a property of the operator, not of the qubit labels ([[trotter-error-in-qpe-energies]]). What changes is the gate cost of each exponential $e^{-i\theta P_k}$, which grows with the weight of $P_k$.

## Which encoding to use

- **Jordan–Wigner** keeps bit strings equal to determinants. That is what [[sample-based-quantum-diagonalization]] samples, and it is what fermionic-swap and LUCJ-type circuits on linear connectivity are built around. In another encoding a measured $\mathbf b$ must be decoded as $\mathbf n=B^{-1}\mathbf b$, which is cheap classically but must not be forgotten.
- **Parity** makes the $N_\alpha$ and $N$ parities single-qubit $Z$ operators when the spin orbitals are ordered in blocks, which allows removing two qubits for free ([[qubit-tapering]]).
- **Bravyi–Kitaev** gives the lowest operator weight for larger $M$, and with it shorter Trotter-step circuits.

## Source

- S. B. Bravyi and A. Yu. Kitaev, "Fermionic quantum computation", *Ann. Phys.* **298**, 210 (2002), doi:10.1006/aphy.2002.6254, arXiv:quant-ph/0003137.
- J. T. Seeley, M. J. Richard and P. J. Love, "The Bravyi-Kitaev transformation for quantum computation of electronic structure", *J. Chem. Phys.* **137**, 224109 (2012), doi:10.1063/1.4768229 (update, parity, flip and remainder sets; recursive $B$ matrix; H₂ example).
- A. Tranter, P. J. Love, F. Mintert and P. V. Coveney, "A comparison of the Bravyi–Kitaev and Jordan–Wigner transformations for the quantum simulation of quantum chemistry", *J. Chem. Theory Comput.* **14**, 5617 (2018), doi:10.1021/acs.jctc.8b00450.
- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), Secs. 4.1.2–4.1.3 (review).
- All numbers are computed in `qcchem/part6_ch2_mappings.py` (sections A–B).
