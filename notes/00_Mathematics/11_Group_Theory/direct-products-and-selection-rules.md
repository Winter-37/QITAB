---
id: direct-products-and-selection-rules
title: Direct products and selection rules - product representations, the vanishing-integral theorem, symmetric and antisymmetric squares, and the states of a degenerate configuration
summary: Products of functions that transform as Γ and Γ′ transform as the direct product Γ ⊗ Γ′, whose character is χ^Γ χ^Γ′ and which decomposes with the usual multiplicity formula. An integral over all space is unchanged by every symmetry operation, so only its totally symmetric part survives. Hence ⟨a|Ô|b⟩ = 0 unless Γ_a* ⊗ Γ_O ⊗ Γ_b contains A₁, which is the general selection rule. For two identical particles the product space splits into a symmetric and an antisymmetric square with characters ½[χ(g)² ± χ(g²)]. With spin this decides which spatial states of a degenerate configuration are singlets and which are triplets: e² in C₃ᵥ gives ¹A₁, ¹E and ³A₂, and π² gives ³Σ⁻, ¹Δ and ¹Σ⁺ as in O₂. Checked on H₂O, where twelve CIS states show dipole components only along the axis their symmetry allows (A₂ states dark to 10⁻¹⁴), and only 26 % of the MO integrals (pq|rs) are allowed by symmetry.
status: in-progress
kind: theory
level: intermediate
tags: [group-theory, direct-product, clebsch-gordan-series, selection-rules, vanishing-integral, symmetric-square, antisymmetric-square, term-symbols, transition-dipole, c2v, c3v, water, cis, integral-sparsity]
prerequisites: [groups-representations-and-characters, projection-operators-and-symmetry-adapted-functions, tensor-products-and-partial-trace]
related: [parity-and-parity-selection-rules, rotational-selection-rules-and-wigner-eckart, addition-of-angular-momenta, diatomic-electronic-terms, periodic-table-and-term-symbols, exchange-symmetry-spin-and-symmetrization-principle, molecular-symmetry-and-point-groups, spin-adapted-configurations]
key: selection
order: 30
date: 2026-11-26
---

Notation follows [[projection-operators-and-symmetry-adapted-functions]]: $\hat O_g$ acts on functions, $\rho^\Gamma$ and $\chi^\Gamma$ are irrep matrices and characters, and $A_1$ (or $\Gamma_1$) is the totally symmetric irrep, $\chi=1$ for every $g$. Characters of point groups are real, so complex conjugation is dropped where that is harmless.

## Product representations

**The product transforms as $\Gamma\otimes\Gamma'$.** If $\{\phi_k\}$ transforms as $\Gamma$ and $\{\psi_m\}$ as $\Gamma'$, the $d_\Gamma d_{\Gamma'}$ products $\phi_k\psi_m$ transform with the Kronecker product matrices ([[tensor-products-and-partial-trace]]):

$$
\hat O_g(\phi_k\psi_m)=\sum_{k'm'}\phi_{k'}\psi_{m'}\big[\rho^\Gamma(g)\otimes\rho^{\Gamma'}(g)\big]_{k'm',km},\qquad\chi^{\Gamma\otimes\Gamma'}(g)=\chi^\Gamma(g)\,\chi^{\Gamma'}(g).
\label{product}
$$

This holds because $\hat O_g$ acts on each factor separately, $(\hat O_g\phi\psi)(\mathbf r)=\phi(R^{-1}\mathbf r)\psi(R^{-1}\mathbf r)$. The trace of a Kronecker product is the product of the traces.

**The Clebsch–Gordan series.** The product is generally reducible. It contains $\Gamma''$

$$
n_{\Gamma''}=\frac1{|G|}\sum_g\chi^{\Gamma''}(g)^*\chi^\Gamma(g)\chi^{\Gamma'}(g)
\label{cg-series}
$$

times. For a rotation group this is the coupling of angular momenta, $j_1\otimes j_2=|j_1-j_2|\oplus\dots\oplus(j_1+j_2)$ ([[addition-of-angular-momenta]]).

Some rules for reading a character table follow:

- one-dimensional irreps multiply like their characters;
- $A_1\otimes\Gamma=\Gamma$;
- $\Gamma\otimes\Gamma$ contains $A_1$ exactly once for an irrep with real characters;
- in $C_{2v}$ every irrep squared is $A_1$, and $B_1\otimes B_2=A_2$.

For $D_{2h}$ and its subgroups, numbering the irreps as bit strings turns the product into a bitwise XOR of the labels, which is how programs such as PySCF store orbital symmetry.

## The vanishing-integral theorem

**An integral keeps only its symmetric part.** An integral over all space does not change under an orthogonal change of variables: $\int(\hat O_gf)\,d\mathbf r=\int f\,d\mathbf r$. Averaging over the group,

$$
\int f\,d\mathbf r=\int\Big(\frac1{|G|}\sum_g\hat O_gf\Big)d\mathbf r=\int\hat P^{A_1}f\,d\mathbf r .
$$

So only the totally symmetric component of the integrand contributes. If $f$ belongs to any irrep $\Gamma\ne A_1$, then $\hat P^{A_1}f=0$ and the integral vanishes.

**Matrix elements.** In $\langle\phi^a_k|\hat O|\phi^b_m\rangle$, take $\hat O$ to be an operator that transforms as $\Gamma_O$ (the dipole components transform as $x$, $y$, $z$). The integrand then transforms as $\Gamma_a^*\otimes\Gamma_O\otimes\Gamma_b$. Therefore

$$
\langle\phi^a|\hat O|\phi^b\rangle=0\quad\text{unless}\quad n_{A_1}\big(\Gamma_a^*\otimes\Gamma_O\otimes\Gamma_b\big)=\frac1{|G|}\sum_g\chi^{\Gamma_a}(g)^*\chi^{\Gamma_O}(g)\chi^{\Gamma_b}(g)>0 .
\label{selection}
$$

Equivalently, $\Gamma_a$ must occur in $\Gamma_O\otimes\Gamma_b$. Three cases:

- **Totally symmetric operator.** For $\hat O$ totally symmetric (the Hamiltonian, the overlap), the rule reduces to $\Gamma_a=\Gamma_b$, the block structure of [[projection-operators-and-symmetry-adapted-functions]].
- **Parity.** For inversion it gives the parity rule ([[parity-and-parity-selection-rules]]).
- **Continuous groups.** For the rotation group, the full statement including the dependence on the partner labels $k$, $m$ is the Wigner–Eckart theorem ([[rotational-selection-rules-and-wigner-eckart]]).

**What it does not say.** The theorem says which integrals are zero, not how large the others are. An allowed transition can be weak.

A forbidden one is zero only within the approximations that define the symmetry:

- **Clamped nuclei at a symmetric geometry.** Vibrations that lower the symmetry lend intensity (Herzberg–Teller coupling).
- **A spin-free Hamiltonian.** Spin–orbit coupling mixes spin states.
- **The electric-dipole approximation.** Magnetic-dipole and quadrupole terms follow other rules.

## Symmetric and antisymmetric squares

**The two squares.** For two identical copies of the same space, the product splits under the swap $\hat P_{12}$ of the two factors into a symmetric part $(1+\hat P_{12})/2$ and an antisymmetric part $(1-\hat P_{12})/2$. Both are invariant under the group. Their characters follow from $\operatorname{tr}\big[\hat P_{12}(A\otimes A)\big]=\operatorname{tr}A^2$:

$$
\chi^{[\Gamma^2]}(g)=\tfrac12\big[\chi^\Gamma(g)^2+\chi^\Gamma(g^2)\big],\qquad\chi^{\{\Gamma^2\}}(g)=\tfrac12\big[\chi^\Gamma(g)^2-\chi^\Gamma(g^2)\big].
\label{squares}
$$

Their dimensions are $d(d+1)/2$ and $d(d-1)/2$.

**With spin.** For two electrons in a degenerate set of orbitals transforming as $\Gamma$, the total wave function must be antisymmetric ([[exchange-symmetry-spin-and-symmetrization-principle]]). The two-electron spin functions are a symmetric triplet and an antisymmetric singlet. So:

- **Singlets** pair with spatial states in the symmetric square;
- **Triplets** pair with spatial states in the antisymmetric square.

This is how the terms of a configuration with a partly filled degenerate shell are found without writing out determinants.

!!! example "e² in C₃ᵥ and π² of a linear molecule"
    **$C_{3v}$.** The squares of the classes are $E^2=E$, $C_3^2\in2C_3$ and $\sigma_v^2=E$. With $\chi^E=(2,-1,0)$:

    | | $E$ | $2C_3$ | $3\sigma_v$ | decomposition |
    |---|---:|---:|---:|---|
    | $E\otimes E$ | 4 | 1 | 0 | $A_1+A_2+E$ |
    | symmetric square | 3 | 0 | 1 | $A_1+E$ |
    | antisymmetric square | 1 | 1 | $-1$ | $A_2$ |

    So a configuration $e^2$ gives $^1A_1$, $^1E$ and $^3A_2$. That is three singlet functions and three triplet functions ($^3A_2$ with $M_S=-1,0,1$), matching the $\binom42=6$ determinants of two electrons in four spin orbitals. The antisymmetric combination built explicitly from the $(x, y)$ representation is $x_1y_2-y_1x_2$. It has characters $(1,1,-1)$, the same as the rotation $R_z$.

    **Linear molecule.** In $C_{4v}$, a subgroup that keeps the $\pi_x,\pi_y$ pair as $E$, the squares give:

    - symmetric: $A_1+B_1+B_2$, which is $^1\Sigma^+$ plus the two components of $^1\Delta$;
    - antisymmetric: $A_2$, which is $^3\Sigma^-$.

    This is the $\pi_g^2$ configuration of O₂: ground state $^3\Sigma_g^-$, then $^1\Delta_g$ and $^1\Sigma_g^+$ ([[diatomic-electronic-terms]]). The atomic $p^2$ terms $^3P$, $^1D$, $^1S$ follow the same way in the rotation group ([[periodic-table-and-term-symbols]]).

## Worked example: water

!!! example "Dipole selection rules and integral sparsity in H₂O"
    H₂O lies in the $yz$ plane with $C_2$ along $z$, as PySCF orients it. In $C_{2v}$ the coordinates transform as $x\to B_1$ (out of plane), $y\to B_2$ and $z\to A_1$. The ground state is $^1A_1$, with RHF/aug-cc-pVDZ occupied orbitals $1a_1\,2a_1\,1b_2\,3a_1\,1b_1$.

    By Eq. [[#selection]], a transition from $A_1$ to a state $\Gamma$ is allowed with polarization $\mu_x$ for $B_1$, $\mu_y$ for $B_2$ and $\mu_z$ for $A_1$. It is forbidden for $A_2$, since none of $x,y,z$ transforms as $A_2$.

    **CIS states.** The twelve lowest singlet CIS (Tamm–Dancoff) states, with the symmetry of each state taken from its excitations. Every amplitude of a state has the same symmetry.

    | state | $E$ (eV) | symmetry | $\mu_x$ | $\mu_y$ | $\mu_z$ (a.u.) |
    |---:|---:|---|---:|---:|---:|
    | 1 | 8.68 | $B_1$ | 0.489 | 0 | 0 |
    | 2 | 10.36 | $A_2$ | $2\times10^{-15}$ | 0 | 0 |
    | 3 | 11.00 | $A_1$ | 0 | $8\times10^{-16}$ | 0.635 |
    | 4 | 12.14 | $B_1$ | 0.132 | 0 | 0 |
    | 5 | 12.66 | $B_2$ | 0 | 0.310 | $4\times10^{-15}$ |
    | 6 | 12.88 | $A_1$ | 0 | $2\times10^{-15}$ | 0.032 |
    | 7 | 13.22 | $A_2$ | $4\times10^{-17}$ | 0 | 0 |
    | 8 | 13.26 | $B_1$ | 0.043 | 0 | 0 |
    | 9 | 14.37 | $B_2$ | 0 | 0.661 | $2\times10^{-14}$ |
    | 10 | 14.42 | $B_1$ | 0.076 | 0 | 0 |
    | 11 | 14.48 | $A_2$ | $5\times10^{-15}$ | 0 | 0 |
    | 12 | 14.75 | $A_1$ | 0 | $9\times10^{-15}$ | 0.191 |

    - **Selection rules.** Every forbidden component is zero to rounding. The allowed ones vary by a factor of 20, which symmetry does not predict.
    - **Absolute values.** CIS energies are only qualitative here. The lowest state, $1b_1\to4a_1$ ($^1B_1$, polarized out of plane), is the known first band of water near 7.4 eV.

    **Sparsity of the MO integrals.** In the symmetry-adapted MO basis (41 orbitals: 18 $a_1$, 4 $a_2$, 7 $b_1$, 12 $b_2$), $(pq|rs)$ can be nonzero only if $\Gamma_p\otimes\Gamma_q\otimes\Gamma_r\otimes\Gamma_s=A_1$.

    - **Allowed fraction.** It is 0.2621 of the $41^4$ integrals. This is exactly the fraction predicted from the orbital counts, close to $1/|G|=1/4$.
    - **Forbidden integrals.** The largest is $2.8\times10^{-13}$.
    - **Use.** Programs skip the forbidden integrals and store the rest in symmetry blocks. CI and SQD Hamiltonians likewise connect only determinants of the same total symmetry.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005):

- Sec. 3.2, pp. 181-182: the direct (Kronecker) product of matrices.
- Sec. 4.4, pp. 266-277: the rotation-group analogue, angular-momentum coupling and the Clebsch–Gordan series.
- Sec. 4.7, pp. 291-301: classes and characters of discrete groups.

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Appendix 2: the decomposition formula used in Eq. [[#cg-series]].

Which parts are derived here:

- **Derived.** The vanishing-integral argument, the symmetric- and antisymmetric-square characters, and the term analysis of $e^2$ and $\pi^2$, all checked numerically.
- **General knowledge, not from these books.** The remarks on Herzberg–Teller and spin–orbit intensity borrowing, the XOR labelling of $D_{2h}$ irreps, and the 7.4 eV experimental band position.

Every number is computed with PySCF in `Claude outputs/part0_math_batchH.py`, section D.
