---
id: lie-groups-and-lie-algebras
title: Lie groups and Lie algebras - matrix groups, generators and structure constants, the exponential map and where it fails, Casimir operators, and the unitary group of orbital rotations
summary: A matrix Lie group such as U(n), SU(n), SO(n) or SL(n, R) is described near the identity by its Lie algebra, the matrices X with exp(tX) in the group for all t. The algebra is closed under the commutator, because the group commutator of exp(tX) and exp(tY) is exp(t²[X, Y] + O(t³)). Its structure constants fix the group locally, and a Casimir operator built from the generators is constant on every irrep. Groups with the same algebra can differ globally: SU(2) and SO(3) share su(2) ≅ so(3), but a 2π rotation is −1 in one and +1 in the other. The exponential map covers compact connected groups but not SL(2, R), where diag(−2, −½) is not an exponential. In second quantization the singlet excitation operators E_pq obey the commutation relations of the n × n matrix units, so exp(−κ̂) represents the orbital rotation exp(−κ). They commute with the total spin, which makes the N-electron, spin-S space a single irrep of U(n) whose dimension is the CSF count. All relations are checked numerically, including the commutators in a 64-dimensional Fock space.
status: in-progress
kind: theory
level: intermediate
tags: [lie-group, lie-algebra, generators, structure-constants, exponential-map, casimir-operator, adjoint-representation, su2, so3, unitary-group, sl2r, orbital-rotation, excitation-operators, unitary-group-approach, guga, schur-weyl]
prerequisites: [groups-representations-and-characters, unitary-matrices-exponential-logarithm, baker-campbell-hausdorff, rotations-su2-so3-and-euler-angles]
related: [orbital-rotations, symmetric-group-and-young-diagrams, spin-operators, genealogical-coupling, functions-of-matrices, orbital-angular-momentum, schwinger-oscillator-model, variational-and-unitary-coupled-cluster, lucj-ansatz]
key: gl-n
order: 50
date: 2026-11-26
---

The previous sections of this chapter treat finite groups. Here the group elements depend smoothly on continuous parameters. Only **matrix Lie groups** are considered: closed subgroups of the invertible complex matrices $GL(n,\mathbb C)$. This covers every group used in this notebook.

$[X,Y]=XY-YX$ is the commutator. $e^X$ is the matrix exponential ([[functions-of-matrices]]).

## Groups and their algebras

**The Lie algebra.** The **Lie algebra** $\mathfrak g$ of a matrix group $G$ is the set of matrices $X$ such that $e^{tX}\in G$ for every real $t$. It is the tangent space of $G$ at the identity, a real vector space whose dimension is the number of parameters of the group.

| group | defined by | algebra | defined by | dimension |
|---|---|---|---|---|
| $U(n)$ | $U^\dagger U=1$ | $\mathfrak u(n)$ | $X^\dagger=-X$ | $n^2$ |
| $SU(n)$ | also $\det U=1$ | $\mathfrak{su}(n)$ | also $\operatorname{tr}X=0$ | $n^2-1$ |
| $O(n)$, $SO(n)$ | $R^{\mathsf T}R=1$, $\det R=\pm1$ or $1$ | $\mathfrak{so}(n)$ | $X^{\mathsf T}=-X$ real | $n(n-1)/2$ |
| $SL(n,\mathbb R)$ | real, $\det=1$ | $\mathfrak{sl}(n,\mathbb R)$ | real, $\operatorname{tr}X=0$ | $n^2-1$ |

Each algebra condition is the derivative at $t=0$ of the group condition. For example, $(e^{tX})^\dagger e^{tX}=1$ gives $X^\dagger+X=0$, and $\det e^X=e^{\operatorname{tr}X}$ turns $\det=1$ into $\operatorname{tr}=0$ ([[unitary-matrices-exponential-logarithm]]).

**Physics convention.** Physicists usually write $X=-iT$ with Hermitian **generators** $T$, so that $U=e^{-i\theta T}$. Arfken and Weber write group elements as exponentials of $i$ times Hermitian generators, a sign difference only.

**Closure under the commutator.** Expand the group commutator with the Baker–Campbell–Hausdorff series ([[baker-campbell-hausdorff]]):

$$
e^{tX}e^{tY}e^{-tX}e^{-tY}=\exp\!\big(t^2[X,Y]+O(t^3)\big).
\label{group-commutator}
$$

The left side lies in $G$ for every $t$, so $[X,Y]\in\mathfrak g$. The algebra is closed under the commutator, which is the defining property of a **Lie algebra**.

For random $4\times4$ anti-Hermitian $X$ and $Y$, $\|\log(\cdot)/t^2-[X,Y]\|$ is 1.42, 0.144 and 0.0144 at $t=10^{-1}$, $10^{-2}$ and $10^{-3}$. It falls linearly in $t$, as the $O(t^3)$ term requires. $[X,Y]$ is anti-Hermitian and traceless, so it lies in $\mathfrak{su}(4)$ even when $X$ and $Y$ do not.

**Structure constants.** In a basis of Hermitian generators,

$$
[T_a,T_b]=i\sum_cf_{abc}\,T_c
\label{structure}
$$

(Arfken and Weber, Eq. (4.14)). The $f_{abc}$ are the **structure constants**, antisymmetric in $a$ and $b$. The Jacobi identity $[T_a,[T_b,T_c]]+\text{cyclic}=0$ constrains them further.

Near the identity, the structure constants fix the group multiplication completely: BCH expresses $\log(e^Xe^Y)$ through nested commutators alone. The global shape of the group is not fixed, as the next example shows.

## su(2), so(3), and one algebra for two groups

**Two realizations of one algebra.**

- **Spin ½.** $T_a=\sigma_a/2$ gives $[T_a,T_b]=i\epsilon_{abc}T_c$, so $f_{abc}=\epsilon_{abc}$.
- **Rotations.** The three $3\times3$ matrices $(L_a)_{bc}=-i\epsilon_{abc}$ generate $SO(3)$ and obey the same relations.

Both statements are verified numerically. So $\mathfrak{su}(2)\cong\mathfrak{so}(3)$. The angular momentum commutation relations are this one algebra ([[rotations-su2-so3-and-euler-angles]]).

**The adjoint representation.** Every algebra acts on itself by $\operatorname{ad}_X(Y)=[X,Y]$. In a basis, $(\operatorname{ad}T_a)_{cb}$ is the coefficient of $T_c$ in $[T_a,T_b]$, which is $i f_{abc}$. For $\mathfrak{su}(2)$ these matrices are exactly the $L_a$. The vector representation of $SO(3)$ is the adjoint representation of $SU(2)$.

**The groups differ.** The rotation by $2\pi$ about the axis $(1,2,2)/3$ is $e^{-2\pi i\,\mathbf n\cdot\boldsymbol\sigma/2}=-1$ in $SU(2)$, but $e^{-2\pi i\,\mathbf n\cdot\mathbf L}=+1$ in $SO(3)$. $SU(2)$ covers $SO(3)$ twice. The algebra cannot see this, but the representations can: half-integer spins are representations of $SU(2)$ only.

**Casimir operators.** $C=\sum_aT_aT_a$ (for an orthonormal basis of a compact algebra) commutes with every generator. By Schur's lemma it is a multiple of the identity on each irrep, and its value labels the irrep (Arfken and Weber, Sec. 4.3). For $\mathfrak{su}(2)$, $C=\mathbf J^2$: it is $\tfrac34$ on spin ½ and $2$ on spin 1, which is $j(j+1)$ in both cases.

Any Hamiltonian that commutes with the generators commutes with $C$. Its levels then form whole multiplets, the continuous-group version of the degeneracy argument in [[projection-operators-and-symmetry-adapted-functions]].

## The exponential map and where it fails

**Compact connected groups.** For $U(n)$, $SU(n)$ and $SO(n)$, every element is an exponential. A unitary matrix is diagonalized by a unitary, $U=V\operatorname{diag}(e^{i\theta_k})V^\dagger$, so $U=e^X$ with $X=V\operatorname{diag}(i\theta_k)V^\dagger$ anti-Hermitian. Numerically, `logm` of a random $5\times5$ unitary is anti-Hermitian, and `logm` of a random $4\times4$ rotation is real and antisymmetric.

**$O(n)$ has two components.** Exponentials of real antisymmetric matrices give only $\det R=+1$. A reflection, which changes the sign of one orbital, is not of the form $e^{\boldsymbol\kappa}$. For orbital optimization this is harmless. Changing the sign of one orbital only changes the sign of the determinant, and changing the signs of two orbitals is a rotation by $\pi$. So real orbital rotations are parametrized as $e^{-\boldsymbol\kappa}$ with $\boldsymbol\kappa$ real antisymmetric (HJO Sec. 3.1.4; [[orbital-rotations]]).

**Non-compact groups can miss elements.** $M=\operatorname{diag}(-2,-\tfrac12)\in SL(2,\mathbb R)$ is not $e^X$ for any real traceless $X$. Such an $X$ has eigenvalues $\pm\mu$, with $\mu$ real or imaginary. Then $e^X$ has eigenvalues $e^{\pm\mu}$, either two positive numbers or a conjugate pair on the unit circle, and never $\{-2,-\tfrac12\}$.

The numerical logarithm confirms this: it is $\operatorname{diag}(\ln2+i\pi,\,-\ln2+i\pi)$, which is not real. Yet $M=e^{\pi J}e^{\operatorname{diag}(\ln2,-\ln2)}$ with $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, a product of two exponentials. A connected group is generated by exponentials even when not every element is one.

## The unitary group in second quantization

**$E_{pq}$ represents the matrix units.** With $n$ spatial orbitals, the singlet excitation operators $E_{pq}=\sum_\sigma a^\dagger_{p\sigma}a_{q\sigma}$ satisfy

$$
[E_{pq},E_{rs}]=\delta_{qr}E_{ps}-\delta_{ps}E_{rq}
\label{gl-n}
$$

(HJO Eq. (2.3.35)). These are the commutation relations of the $n\times n$ matrix units $e_{pq}$, the matrices with a single 1 at position $pq$. So $e_{pq}\mapsto E_{pq}$ is a representation of $\mathfrak{gl}(n)$ on Fock space. HJO call the $E_{pq}$ the generators of the unitary group.

**Rotations.** Exponentiating the representation gives the representation of the group. For anti-Hermitian $\boldsymbol\kappa$, $\hat\kappa=\sum_{pq}\kappa_{pq}E_{pq}$ is anti-Hermitian, and

$$
e^{-\hat\kappa}\,a^\dagger_{p\sigma}\,e^{\hat\kappa}=\sum_qa^\dagger_{q\sigma}\big[e^{-\boldsymbol\kappa}\big]_{qp}
\label{rotation}
$$

(HJO Eqs. (3.2.1)-(3.2.6), (3.2.16)). The operator $e^{-\hat\kappa}$ on Fock space is the representative of the orbital rotation $U=e^{-\boldsymbol\kappa}$. The derivation by nested commutators is in [[orbital-rotations]].

**Closure.** One-body operators are closed under commutators, because Eq. [[#gl-n]] produces only one-body operators. That is why an orbital rotation, however large, stays an orbital rotation, and can be compiled into $O(n^2)$ two-orbital Givens rotations. Commutators of two-body operators produce three-body and higher terms. Exponentials of two-body generators, as in unitary coupled cluster or LUCJ, have no such small closed algebra ([[variational-and-unitary-coupled-cluster]], [[lucj-ansatz]]).

**Spin commutes with orbital rotations.** The spin operators $\hat S_\pm$ and $\hat S_z$ are built from the same creation and annihilation operators, and they commute with every $E_{pq}$. Hence $[E_{pq},\hat S^2]=0$, and orbital rotations never mix spin states. This is the second-quantized form of the Schur–Weyl duality between $U(n)$ acting on orbitals and $SU(2)$ acting on spins ([[symmetric-group-and-young-diagrams]]).

**The CSF space is one irrep.** The space of $N$ electrons with spin $S$ and fixed $M_S$ carries a single irrep of $U(n)$. Its Young diagram has two columns, of lengths $N/2+S$ and $N/2-S$, and its dimension is the number of CSFs. Two consequences:

- **The Gelfand–Tsetlin basis.** A basis of this irrep labelled by the subgroup chain $U(n)\supset U(n-1)\supset\cdots$ is the CSF basis of the unitary group approach (GUGA).
- **Coupling coefficients.** The Hamiltonian is a quadratic polynomial in the $E_{pq}$ (HJO Eq. (2.2.18)). Its matrix elements in that basis are the matrix elements of generators and their products, which the unitary group approach evaluates by graphical rules.

!!! example "Fock-space checks, 3 orbitals and 6 spin orbitals"
    The creation and annihilation operators are built as $64\times64$ Jordan–Wigner matrices, with the anticommutators exact.

    - **Generators.** Eq. [[#gl-n]] holds for all $3^4$ index combinations, with error 0.
    - **Spin.** $[E_{pq},\hat S^2]$ and $[E_{pq},\hat S_z]$ vanish, with error 0.
    - **Rotation.** For a random real antisymmetric $\boldsymbol\kappa$, Eq. [[#rotation]] holds to $1.5\times10^{-15}$.
    - **The two-electron sector.** With $M_S=0$ it has 9 states. $\hat S^2$ has eigenvalues 0 (six times) and 2 (three times). These are the $U(3)$ irreps $[2]$ (dimension 6, spatially symmetric, singlets) and $[1,1]$ (dimension 3, spatially antisymmetric, triplets), with dimensions from the hook-content formula.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005):

- Sec. 4.2, pp. 246-260: generators of continuous groups, structure constants (Eq. (4.14)) and the Jacobi constraint (Eqs. (4.16)-(4.19)), SU(2) and SO(3) generators with the same structure constants, the 2-to-1 relation, SU(3) and its eight generators.
- Sec. 4.3, pp. 264-266: rank, Casimir operators, and the degeneracy of Hamiltonians that commute with them.

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000):

- Sec. 2.3.5, Eq. (2.3.35): the generators of the unitary group.
- Sec. 2.2.1, Eq. (2.2.18): the Hamiltonian in terms of the $E_{pq}$.
- Secs. 3.1.1-3.1.4, pp. 80-84: exponential representations of unitary, special unitary and orthogonal matrices.
- Sec. 3.2, Eqs. (3.2.1)-(3.2.6) and (3.2.16): exponential transformations of creation operators.

Which parts are from where:

- **Derived here.** The $SL(2,\mathbb R)$ counterexample and the remark on $\det=-1$ orbital transformations.
- **General knowledge, not from these books.** The Gelfand–Tsetlin and GUGA remarks.

Every number is computed in `Claude outputs/part0_math_batchH.py`, section F.
