---
id: groups-representations-and-characters
title: Groups, representations and characters
summary: The finite-group theory behind symmetry labels and selection rules. Covers group axioms, subgroups, Lagrange's theorem, cosets, conjugacy classes, matrix representations, equivalence and irreducibility, Schur's lemma, the fundamental orthogonality theorem, characters and their orthogonality, the irreducibility test, decomposition of a representation into irreducibles, and the regular representation. Worked fully on S₃ (isomorphic to the point group C₃ᵥ) and on the one-qubit Pauli group, with every relation checked numerically.
status: in-progress
kind: theory
level: intermediate
tags: [group-theory, finite-groups, lagrange-theorem, cosets, conjugacy-classes, representations, irreducible-representation, schur-lemma, characters, character-table, regular-representation, symmetric-group, pauli-group, point-groups, nielsen-chuang]
prerequisites: [matrices-and-determinants, spectral-decomposition-and-normal-operators]
related: [fourier-transforms-and-the-dirac-delta, symmetry-conservation-and-degeneracy, rotations-su2-so3-and-euler-angles, wigner-rotation-matrices, spherical-tensor-operators]
order: 10
date: 2026-11-17
---

## Groups

A **group** $(G,\cdot)$ is a set with an associative product, an identity $e$ ($eg = ge = g$) and an inverse for every element ($gg^{-1} = g^{-1}g = e$), closed under the product. The **order** $|G|$ is the number of elements. $G$ is **Abelian** if all elements commute.

Examples: the integers modulo $n$ under addition, $\mathbb Z_n$ (Abelian, order $n$); the permutations of three objects, $S_3$ (order 6, not Abelian); the symmetry operations of a molecule (point groups); the rotations SO(3) and SU(2) of [[rotations-su2-so3-and-euler-angles]], which are infinite (Lie) groups.

**Subgroups and Lagrange's theorem.** A subset that is itself a group under the same product is a subgroup. For finite $G$:

$$
H\ \text{a subgroup of}\ G\quad\Longrightarrow\quad|H|\ \text{divides}\ |G| .
$$

The proof uses **cosets**: the sets $gH = \{gh: h\in H\}$ all have $|H|$ elements, and two cosets are either identical or disjoint, so they partition $G$ into $|G|/|H|$ pieces. Consequences: the **order** of an element (the smallest $r$ with $g^r = e$) divides $|G|$, since $g$ generates a cyclic subgroup of order $r$; and a group of prime order is cyclic.

**Conjugacy classes.** Elements $x$ and $g^{-1}xg$ are **conjugate**. The **conjugacy class** of $x$ is $\{g^{-1}xg: g\in G\}$. Classes partition the group. In an Abelian group every element is its own class. For symmetry operations, conjugate elements are "the same kind of operation" seen in a rotated frame: all three reflections of an equilateral triangle form one class, the two rotations by $\pm120^\circ$ another.

!!! example "$S_3$"

    Six permutations of $(0,1,2)$. Conjugacy classes: $\{e\}$, the three transpositions, the two cyclic permutations, sizes 1, 3, 2. The even permutations form a subgroup $A_3$ of order 3 (the rotations of the triangle), with two cosets, as Lagrange requires. $S_3$ is isomorphic to $C_{3v}$, the point group of NH₃: transpositions correspond to the three vertical mirror planes and three-cycles to the $C_3$ rotations.

## Representations

A **representation** of $G$ assigns to each element a matrix $\rho(g)$ such that $\rho(g_1g_2) = \rho(g_1)\rho(g_2)$ (a homomorphism into matrices); its **dimension** $d_\rho$ is the size of the matrices. It is **faithful** if distinct elements get distinct matrices. Representations arise whenever a group acts on a vector space: the symmetry operations of a molecule act on its orbitals, rotations act on states of angular momentum $j$ through the Wigner matrices of [[wigner-rotation-matrices]].

Any representation of a finite group is equivalent to a unitary one (average an inner product over the group), so representations can be taken unitary.

**Equivalence and reducibility.** Two representations are **equivalent** if $\rho'(g) = S\rho(g)S^{-1}$ for one fixed invertible $S$ and all $g$: they differ only by a change of basis. A representation is **reducible** if it is equivalent to a block-diagonal one, $\rho(g)\simeq\rho_1(g)\oplus\rho_2(g)$, for all $g$ at once; otherwise **irreducible** (an irrep). Every representation of a finite group decomposes into irreducible ones.

**Schur's lemma.** If $S\rho_1(g) = \rho_2(g)S$ for all $g$, with $\rho_1$ and $\rho_2$ irreducible, then either $S = 0$ or $S$ is square and invertible (so the irreps are equivalent). A corollary: a matrix that commutes with every matrix of an irrep is a multiple of the identity. Applied to a Hamiltonian that commutes with a symmetry group, this is why the energy is the same throughout each irreducible subspace: degeneracies are dimensions of irreps ([[symmetry-conservation-and-degeneracy]]).

## The fundamental theorem and characters

**Theorem.** A finite group has exactly as many inequivalent irreducible representations as it has conjugacy classes, $r$. For two of them, $\rho^p$ and $\rho^q$,

$$
\frac{d_p}{|G|}\sum_{g\in G}\big[\rho^p(g)^{-1}\big]_{ij}\,\rho^q(g)_{kl} = \delta_{pq}\,\delta_{il}\,\delta_{jk} ,
$$

and the dimensions satisfy $\sum_pd_p^2 = |G|$, with each $d_p$ dividing $|G|$.

The **character** of a representation is $\chi(g) = \mathrm{tr}\,\rho(g)$. It is the same for equivalent representations and for all elements of a class, satisfies $\chi(g^{-1}) = \chi(g)^*$, and $\chi(e) = d$. Writing $\chi^p_i$ for the character of irrep $p$ on class $i$, of size $r_i$, the theorem gives the **orthogonality relations**

$$
\sum_{i=1}^rr_i\,\chi^{p\,*}_i\chi^q_i = |G|\,\delta_{pq} ,\qquad \sum_p\chi^{p\,*}_i\chi^p_j = \frac{|G|}{r_i}\,\delta_{ij} .
$$

Two practical consequences:

- **Irreducibility test.** A representation with character $\chi$ is irreducible if and only if $\frac{1}{|G|}\sum_g|\chi(g)|^2 = 1$.
- **Decomposition.** A representation with character $\chi$ contains irrep $p$ exactly

$$
c_p = \frac{1}{|G|}\sum_ir_i\,\chi^{p\,*}_i\,\chi_i
$$

times. Characters alone, without the matrices, decide how a representation splits.

!!! example "Character table of $S_3\cong C_{3v}$"

    The irreps are the trivial one, the sign of the permutation, and a two-dimensional one (the action on the plane of the triangle; built here by restricting the $3\times3$ permutation matrices to the plane orthogonal to $(1,1,1)$, and checked to be a homomorphism). In chemical notation:

    | irrep | $E$ (1) | $2C_3$ (2) | $3\sigma_v$ (3) |
    |---|---|---|---|
    | $A_1$ (trivial) | 1 | 1 | 1 |
    | $A_2$ (sign) | 1 | 1 | $-1$ |
    | $E$ | 2 | $-1$ | 0 |

    Checks: three classes, three irreps; $1^2 + 1^2 + 2^2 = 6$; rows are orthogonal with weights $(1,2,3)$ and norm 6; columns are orthogonal with norms $6, 3, 2 = |G|/r_i$. The irreducibility test gives 1 for $E$, and 2 for the $3\times3$ permutation representation, which decomposes by the formula above as $A_1\oplus E$: three equivalent hydrogen $1s$ orbitals of NH₃ span one totally symmetric combination and a degenerate pair.

!!! example "The one-qubit Pauli group"

    $G_1 = \{\pm1,\pm i\}\times\{I,X,Y,Z\}$ has 16 elements and is closed under multiplication, but not Abelian. Its 10 conjugacy classes are the four multiples of $I$ (each alone, since they commute with everything) and six pairs $\{X,-X\}$, $\{iX,-iX\}$ and so on (conjugating $X$ by $Z$ flips its sign). Hence 10 irreps, and $\sum d_p^2 = 16$ with ten terms forces eight one-dimensional irreps and two two-dimensional ones. The defining representation by the Pauli matrices passes the irreducibility test: $\frac{1}{16}\sum|\mathrm{tr}\,g|^2 = \frac{4\times4}{16} = 1$. The other two-dimensional irrep is its complex conjugate.

## The regular representation and Fourier transforms

Label basis vectors by group elements and let $g$ act by $|h\rangle\to|gh\rangle$. This **regular representation** has dimension $|G|$ and is faithful; its character is $|G|$ on the identity and 0 elsewhere. By the decomposition formula it contains each irrep $p$ exactly $d_p$ times, which proves $\sum_pd_p^2 = |G|$ (for $S_3$: multiplicities 1, 1, 2).

For the cyclic group $\mathbb Z_N$ every irrep is one-dimensional, $\chi_k(j) = e^{2\pi ijk/N}$, and the Fourier transform over the group, $\hat f(\rho)\propto\sum_gf(g)\rho(g)$, becomes the discrete Fourier transform of [[fourier-transforms-and-the-dirac-delta]]. Character orthogonality is the unitarity of the DFT matrix. Fourier transforms over non-Abelian groups such as $S_3$ are defined the same way with matrix-valued irreps.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Appendix 2, pp. 610-616: basic definitions, Lagrange's theorem (Theorem A2.1), conjugacy classes and the Pauli group (A2.1); generators, cyclic groups and cosets (A2.1.1-A2.1.3); representations, characters and their properties, equivalence and reducibility, Schur's lemma (Lemma A2.2), the irreducibility criterion (Theorem A2.3, Eq. (A2.2)) (A2.2.1); the fundamental theorem (Theorem A2.4, Eq. (A2.3)) and character orthogonality (A2.4), with Exercise A2.16 on $S_3$ (A2.2.2); the regular representation and the decomposition theorem (Theorem A2.5, Eqs. (A2.5)-(A2.6)) (A2.2.3); Fourier transforms on groups, Eq. (A2.9) (A2.3). Page numbers are those printed in the book.

The chemical labels for $C_{3v}$, the NH₃ illustration and the counting argument for the Pauli group's irreps are my additions; every number is computed in `mathematics/part0_batch5.py` (section J).
