---
id: qubit-tapering
title: Qubit tapering - removing qubits with Z₂ symmetries
summary: If a Z-type Pauli string τ commutes with every term of the qubit Hamiltonian, the Clifford U = (X_q + τ)/√2 turns τ into a single-qubit X_q, and that qubit can be replaced by an eigenvalue ±1 and removed. Spin-parity and abelian point-group symmetries give 3 to 5 independent τ for small molecules, found here as a GF(2) kernel. Tapering in the Hartree–Fock sector gives H₂ 4→1, H₄ 8→5, LiH 12→8, H₂O 14→10 and N₂ 20→15 qubits. In every case where energies were checked (all but N₂), the lowest N-electron state of the tapered Hamiltonian is exactly the FCI energy, and the HF bits with the pivot qubits deleted give E_RHF. One-qubit H₂: −0.3211 I − 0.7959 Z + 0.1809 X. Point-group symmetries only appear with symmetry-adapted orbitals: a non-adapted N₂ run has 4 generators, 2951 terms and λ = 118.6 Eh, against 5, 2239 and 114.7. The two-qubit reduction of the parity mapping is the special case where the parity τ are already single Z.
status: in-progress
kind: algorithm
level: intermediate
tags: [qubit-tapering, z2-symmetry, clifford, point-group-symmetry, parity-mapping, qubit-reduction, stabilizer]
prerequisites: [jordan-wigner-mapping, parity-and-bravyi-kitaev-mappings, groups-representations-and-characters]
related: [molecular-hamiltonian-in-the-mo-basis, frozen-core-and-active-space-hamiltonians, variational-quantum-eigensolver, sample-based-quantum-diagonalization, symmetry-conservation-and-degeneracy]
order: 30
date: 2026-11-17
---

## Overview

The qubit Hamiltonian acts on all $2^M$ occupation states, but the electronic ground state lies in one symmetry sector: fixed electron numbers $N_\alpha$ and $N_\beta$, and one irreducible representation of the molecular point group ([[symmetry-conservation-and-degeneracy]]). Each **$\mathbb Z_2$ symmetry**, a Pauli string with eigenvalues $\pm1$ that commutes with $\hat H$, can be used to remove one qubit exactly (Bravyi, Gambetta, Mezzacapo and Temme 2017). This note gives the construction, the algorithm for finding the symmetries, and the result for small molecules. Freezing orbitals ([[frozen-core-and-active-space-hamiltonians]]) changes the physics; tapering is exact.

**Conventions.** Jordan–Wigner with interleaved spin orbitals ([[jordan-wigner-mapping]]). A Pauli string is written $X^{\mathbf x}Z^{\mathbf z}$ up to phase, with $\mathbf x,\mathbf z\in\{0,1\}^M$. Two strings commute iff $\mathbf x\cdot\mathbf z'+\mathbf z\cdot\mathbf x'=0$ (mod 2).

## Where the symmetries come from

In Jordan–Wigner, $Z_j=(-1)^{\hat n_j}$, so a product of $Z$s over a set $S$ of spin orbitals is $(-1)^{\sum_{j\in S}\hat n_j}$, the parity of the number of electrons in $S$. It commutes with $\hat H$ whenever every term conserves that parity:

- $S$ = all $\alpha$ spin orbitals: $(-1)^{\hat N_\alpha}$, conserved because $\hat H$ conserves $N_\alpha$. Likewise for $\beta$.
- $S$ = all spin orbitals whose spatial orbital is odd under a symmetry operation $g$ of an abelian point group (character $-1$). This product is the eigenvalue of $g$ acting on the determinant, and it is conserved because $\hat H$ is invariant under $g$.

**Counting.** D₂h has three generators, so there are at most $2+3=5$ independent $\mathbb Z_2$ symmetries; C₂v gives at most 4. Fewer appear when some generator acts trivially on all the orbitals present. In the H₄ chain all orbitals are $\sigma$, so only inversion survives and there are 3.

**Finding them without symmetry labels.** A $Z$-type string $Z^{\mathbf z}$ commutes with term $k$ iff $\mathbf x_k\cdot\mathbf z=0$. Stacking the $X$-parts of all terms into a matrix $A$ (one row per term), the symmetries are the GF(2) kernel of $A$. Bring a basis of the kernel to reduced row-echelon form. Then generator $\tau_i$ has a **pivot qubit** $q_i$ on which it alone carries $Z$. This is what the verification script does. Kernel elements with $X$ parts also exist in principle, but the $Z$-type ones are the ones used here.

## The Clifford rotation

For each generator define

$$
U_i=\tfrac1{\sqrt2}\big(X_{q_i}+\tau_i\big).
$$

$X_{q_i}$ and $\tau_i$ anticommute (they overlap only on $q_i$, as $X$ against $Z$), so $U_i^2=\tfrac12(1+1+\{X_{q_i},\tau_i\})=1$: $U_i$ is Hermitian and unitary. It swaps the two:

$$
U_i\,\tau_i\,U_i=X_{q_i},\qquad U_i\,X_{q_i}\,U_i=\tau_i .
$$

Every Hamiltonian term $P$ commutes with $\tau_i$. After the rotation, $U_iPU_i$ commutes with $X_{q_i}$, so it carries only $I$ or $X$ on qubit $q_i$. The $U_i$ for different generators commute, because pivots appear in only one generator and all $\tau$ are $Z$-type. So $U=\prod_iU_i$ maps every $\tau_i$ to $X_{q_i}$ at once.

**Tapering.** In $U\hat HU$, replace each $X_{q_i}$ by its eigenvalue $s_i=\pm1$, the eigenvalue of $\tau_i$ in the sector wanted, and delete qubit $q_i$. The result acts on $M-k$ qubits, and its spectrum is the spectrum of $\hat H$ restricted to the sector $\{\tau_i=s_i\}$.

**Choosing the sector.** For a ground state with the symmetry of Hartree–Fock, take $s_i=\langle\text{HF}|\tau_i|\text{HF}\rangle=(-1)^{\sum_{j\in\tau_i}n_j^{\text{HF}}}$. A sector fixes only parities, so it still contains other electron numbers (for example $N_\alpha\pm2$). The script tapers the number operator alongside $\hat H$ (it comes out diagonal) to confirm which state is the $N$-electron ground state. In every case checked here it was also the lowest state of the whole sector. Excited states of other irreducible representations live in other sectors and are reached by changing the $s_i$.

## Results

!!! example "H₂, STO-3G, 0.735 Å: 4 qubits to 1"
    The kernel has dimension 3. In row-echelon form the generators are:

    | generator | pivot qubit | eigenvalue on HF $|1100\rangle$ |
    |---|---|---|
    | $Z_0Z_3$ | 0 | $-1$ |
    | $Z_1Z_3$ | 1 | $-1$ |
    | $Z_2Z_3$ | 2 | $+1$ |

    They generate the same group as the physical symmetries:
    - the spin parities $Z_0Z_2=(-1)^{N_\alpha}$ and $Z_1Z_3=(-1)^{N_\beta}$;
    - the inversion parity $Z_2Z_3$, the occupation parity of $\sigma_u$.

    For example, $Z_0Z_3=(Z_0Z_2)(Z_2Z_3)$.

    The tapered Hamiltonian is

    $$
    \hat H_{\text{tap}}=-0.321124\,I-0.795875\,Z+0.180931\,X ,
    $$

    with lowest eigenvalue $-0.321124-\sqrt{0.795875^2+0.180931^2}=-1.137306\,E_h$, the FCI energy. The two states of the sector are $|1100\rangle$ and $|0011\rangle$. The off-diagonal element is the exchange integral $K_{12}$ ([[molecular-hamiltonian-in-the-mo-basis]]), and $\lambda$ falls from 1.894 to 0.977, because tapering merges terms.

STO-3G, symmetry-adapted RHF orbitals, Hartree–Fock sector:

| system | point group (abelian subgroup for orbital labels) | generators | qubits | terms | $\lambda$ ($E_h$) | lowest $N$-electron state |
|---|---|---:|---|---|---|---|
| H₂, 0.735 Å | D∞h (D₂h) | 3 | 4 → 1 | 15 → 3 | 1.894 → 0.977 | $-1.1373060358$ = FCI |
| H₄ chain, 1.0 Å | D∞h (D₂h) | 3 | 8 → 5 | 185 → 132 | 7.145 → 6.945 | $-2.1663874486$ = FCI |
| LiH, 1.6 Å | C∞v (C₂v) | 4 | 12 → 8 | 631 → 558 | 12.341 → 12.149 | $-7.8823243789$ = FCI |
| H₂O | C₂v | 4 | 14 → 10 | 1086 → 1035 | 71.998 → 71.597 | $-75.0125782411$ = FCI |
| N₂, 1.098 Å | D∞h (D₂h) | 5 | 20 → 15 | 2239 → 2229 | 114.707 → 114.707 | not computed ($2^{15}$ space with 2229 terms) |

- **Pauli terms and the 1-norm.** Tapering never increases $\lambda$: merged terms satisfy $|c_1\pm c_2|\le|c_1|+|c_2|$. For larger molecules few terms merge and $\lambda$ barely moves. The saving is in qubits, not in the cost of phase estimation.
- **The input state stays simple.** Deleting the pivot bits from the HF determinant gives a basis state of the tapered register whose energy is $E_{\text{RHF}}$, checked for H₂, H₄, LiH and H₂O. (Each $U_i$ maps $|\mathbf n\rangle$ to a product of $|\pm\rangle$ on $q_i$ and the unchanged other bits.)
- **Decoding.** Each deleted bit is recovered from the others: $(-1)^{n_{q_i}+\sum_{j\in\tau_i,j\ne q_i}n_j}=s_i$. A sampled bit string of the tapered register therefore still identifies a unique determinant, which matters for [[sample-based-quantum-diagonalization]].

**Symmetry-adapted orbitals are required.** The point-group symmetries appear as $Z$ strings only if every orbital belongs to one irreducible representation. For N₂ the occupied $\pi$ pair is degenerate. An SCF run without symmetry returns an arbitrary rotation within that pair, which mixes irreducible representations. That run gives:
- 4 generators instead of 5;
- 2951 Pauli terms instead of 2239;
- $\lambda=118.61\,E_h$ instead of $114.71$.

For LiH and H₂O the non-adapted runs happened to give the same term count, the same $\lambda$ and the same 4 generators. With degenerate orbitals that is luck, not something to rely on. Requesting symmetry in the SCF (PySCF `symmetry=True`) fixes the orbitals and also makes $\lambda$ and the term count reproducible (compare the N₂ range in [[molecular-hamiltonian-in-the-mo-basis]]).

## The two-qubit reduction of the parity mapping

Order the spin orbitals in blocks (all $\alpha$, then all $\beta$) and use the parity encoding ([[parity-and-bravyi-kitaev-mappings]]). Then qubit $M/2-1$ stores $\sum_{k<M/2}n_k=N_\alpha$ (mod 2), and qubit $M-1$ stores $N$ (mod 2). Both symmetries are already single-qubit $Z$s, so no Clifford rotation is needed: replace $Z_{M/2-1}\to(-1)^{N_\alpha}$ and $Z_{M-1}\to(-1)^{N}$ and delete the two qubits.

| system | qubits | terms | ground state |
|---|---|---|---|
| H₂ | 4 → 2 | 15 → 5 | $-1.1373060358$ = FCI |
| H₄ chain | 8 → 6 | 185 → 165 | $-2.1663874486$ = FCI |
| LiH | 12 → 10 | 631 → 631 | $-7.8823243789$ = FCI |

For H₂ this gives

$$
\hat H=-0.332404\,II+0.397937\,(ZI-IZ)-0.011280\,ZZ+0.180931\,XX .
$$

With the interleaved ordering, qubit $M/2-1$ stores the parity of the first $M/2$ spin orbitals instead, which is not conserved in general (checked for H₄ and LiH; for H₂ it happens to be the $\sigma_g$ occupation parity, which is conserved). The reduction is the special case of tapering with the two spin-parity generators. General tapering also removes the point-group qubits and works in any encoding.

## Practical points

- **Every operator must be transformed the same way.** An observable is tapered with the same $U$ and the same $s_i$, so this works only for operators that commute with all the $\tau_i$, such as $\hat H$, $\hat N$, $\hat S_z$, or the totally symmetric components of the dipole. A transition operator between different irreducible representations connects different sectors and cannot be written on one tapered register.
- **Ansätze must respect the symmetry.** A circuit that breaks a $\tau_i$ cannot be expressed on the tapered register. Particle- and symmetry-conserving ansätze taper cleanly ([[variational-quantum-eigensolver]]).
- **Tapering removes qubits, not cost.** $\lambda$ and the number of terms change little for larger molecules, as the table shows.

## Source

- S. Bravyi, J. M. Gambetta, A. Mezzacapo and K. Temme, "Tapering off qubits to simulate fermionic Hamiltonians", arXiv:1701.08213 (2017): $\mathbb Z_2$ symmetries, the Clifford $U=(X_q+\tau)/\sqrt2$ construction, and the parity-mapping two-qubit reduction.
- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), Sec. 4.3 (review of qubit reduction).
- Point groups and characters: [[groups-representations-and-characters]].
- All numbers are computed in `qcchem/part6_ch2_mappings.py` (sections C–D).
