---
id: linear-response-for-variational-wave-functions
title: Linear response for variational wave functions - exponential parametrization, the electronic Hessian E[2] and metric S[2] for SCF, CI and MCSCF, paired eigenvalues, stability, and why there is no excited-state wave function
summary: For SCF, CI and MCSCF references the time-dependent state is written as a unitary rotation exp(−iκ)…|0⟩ of the optimized reference. The Ehrenfest equations for the time-transformed rotation operators then give one response equation, (E[2] − ωS[2])κ⁽¹⁾ = −iV[1], and the linear response function −Ω[1]†(E[2] − ωS[2])⁻¹V[1]. E[2] is the electronic Hessian, with the CIS matrix as its A block. S[2] is diag(1, −1) for SCF and a projected metric for CI and MCSCF. The generalized eigenproblem gives paired eigenvalues ±λ, and a common transformation brings E[2] and S[2] to diagonal form. That turns the response function into a sum over states with λ as excitation energies, and makes negative Hessian eigenvalues instabilities. Recomputed: NRS's helium aug-cc-pVDZ matrices and CIS, TDHF and CI excitation energies, and the beryllium 6-31G triplet instability.
status: in-progress
kind: theory
level: advanced
tags: [linear-response, rpa, tdhf, electronic-hessian, exponential-parametrization, cis, tamm-dancoff, stability, mcscf-response, ci-response]
prerequisites: [quasienergy-and-time-dependent-variational-principle, polarization-propagator-rpa, orbital-rotations, scf-second-order-and-stability]
related: [residue-analysis-of-response-functions, cphf-closed-shell, mcscf-second-order-optimization, state-averaged-mcscf-and-configuration-rotations, ci-optimization-newton-and-davidson, damped-response-and-absorption-cross-sections, tddft-linear-response, rhf-instabilities-and-multiple-solutions]
conventions: [ia-letters, spin-orbitals, spatial-orbitals, antisymmetrized-integrals, chemists-integrals, atomic-units]
key: rpa
order: 100
date: 2026-11-24
---

Atomic units. $i,j$ occupied (NRS: inactive), $a,b$ virtual (NRS: secondary, $s,t$), $p,q$ general; spin orbitals unless stated. $\hat q^\dagger_n$ is an excitation operator ($\hat a^\dagger_a\hat a_i$ for SCF), and $n$ runs over a nonredundant set. Each block vector is written as (excitation part, de-excitation part). $\langle pq||rs\rangle$ are antisymmetrized physicists' integrals and $(pq|rs)$ chemists' integrals.

## Parametrizing the time-dependent reference

**Single determinant.** With the optimized determinant $|0\rangle$,

$$
|\tilde\psi(t)\rangle = e^{-i\hat\kappa(t)}|0\rangle,\qquad \hat\kappa(t) = \sum_{ai}\big[\kappa_{ai}(t)\hat a^\dagger_a\hat a_i + \kappa^*_{ai}(t)\hat a^\dagger_i\hat a_a\big].
$$

$\hat\kappa$ is Hermitian, so the transformation is unitary. It transforms every creation operator as $e^{-i\hat\kappa}\hat a^\dagger_pe^{i\hat\kappa} = \sum_r\hat a^\dagger_r[e^{-i\boldsymbol\kappa}]_{rp}$, so $e^{-i\hat\kappa}|0\rangle$ is again a single determinant, built from rotated orbitals ([[orbital-rotations]]). Occupied-occupied and virtual-virtual rotations only change the phase and are left out.

**A determinant that looks multiconfigurational.** For two electrons in four spin orbitals, $|0\rangle = |\chi_1\chi_2\rangle$, with only the rotations $\kappa_{31}$ and $\kappa_{42}$:

$$
e^{-i\hat\kappa}|0\rangle = \cos|\kappa_{31}|\cos|\kappa_{42}|\,|0\rangle - i\tfrac{\kappa_{31}}{|\kappa_{31}|}\sin|\kappa_{31}|\cos|\kappa_{42}|\,|0^3_1\rangle - i\tfrac{\kappa_{42}}{|\kappa_{42}|}\cos|\kappa_{31}|\sin|\kappa_{42}|\,|0^4_2\rangle - \tfrac{\kappa_{31}\kappa_{42}}{|\kappa_{31}\kappa_{42}|}\sin|\kappa_{31}|\sin|\kappa_{42}|\,|0^{34}_{12}\rangle.
$$

The double excitation enters at second order in $\kappa$, and its coefficient is fixed by the singles: the whole is the single determinant $|\tilde\chi_1\tilde\chi_2\rangle$ with $\tilde\chi_1 = \cos|\kappa_{31}|\chi_1 - i(\kappa_{31}/|\kappa_{31}|)\sin|\kappa_{31}|\chi_3$ and similarly $\tilde\chi_2$. The range of the map is the set of determinants, not a linear space.

**Spin adaptation (closed shell, singlet perturbations).** Restrict to singlet rotations with $\hat E^\dagger_{ai} = \hat a^\dagger_{a\alpha}\hat a_{i\alpha} + \hat a^\dagger_{a\beta}\hat a_{i\beta}$ (spatial orbitals). Triplet ($M_S = 0$) rotations use $\hat T^\dagger_{ai} = \hat a^\dagger_{a\alpha}\hat a_{i\alpha} - \hat a^\dagger_{a\beta}\hat a_{i\beta}$. These operators are not normalized: $\langle0|[\hat E_{ai},\hat E^\dagger_{ai}]|0\rangle = 2$. NRS's numbers carry this factor 2.

**CI.** The CI eigenvectors $|n\rangle$ satisfy $\hat H_0 = \sum_nE_n|n\rangle\langle n|$ within the CI space, so the exact-state parametrization of [[exact-state-response-functions]] carries over. When the eigenvectors are not available (direct CI), use a redundant parametrization over the configurations $|\Phi_n\rangle$,

$$
\hat R(t) = \sum_n\big[R_n(t)|\Phi_n\rangle\langle0| + R_n^*(t)|0\rangle\langle\Phi_n|\big],
$$

which includes $n = 0$ (a phase change) to avoid solving for all eigenvectors.

**MCSCF.** Here $|\tilde\psi\rangle = e^{-i\hat\kappa}e^{-i\hat R}|0\rangle$, with configurations rotated first. In the other order $\hat R$ would refer to $e^{-i\hat\kappa}|0\rangle$ and depend on $\boldsymbol\kappa$. The orbital rotations are inactive-active, inactive-secondary and active-secondary; active-active rotations are covered by the configurations.

## Gradient and Hessian (SCF)

Expanding $E(\boldsymbol\kappa) = \langle0|e^{i\hat\kappa}\hat H_0e^{-i\hat\kappa}|0\rangle$ by BCH:

$$
\mathbf E^{[1]} = i\begin{pmatrix}\langle0^a_i|\hat H_0|0\rangle\\ -\langle0|\hat H_0|0^a_i\rangle\end{pmatrix},\qquad
\mathbf E^{[2]} = \begin{pmatrix}\mathbf A & \mathbf B\\ \mathbf B^* & \mathbf A^*\end{pmatrix},
$$

$$
A_{ai,bj} = \langle0^a_i|\hat H_0|0^b_j\rangle - E_0\delta_{ab}\delta_{ij} = F_{ab}\delta_{ij} - F_{ji}\delta_{ab} - \langle aj||bi\rangle,\qquad
B_{ai,bj} = -\langle0^{ab}_{ij}|\hat H_0|0\rangle = -\langle ab||ij\rangle.
\label{ab}
$$

- **Gradient.** $\mathbf E^{[1]}$ vanishes at convergence (Brillouin).
- **$\mathbf A$.** It is the CIS Hamiltonian minus $E_0$. Its diagonal in canonical orbitals is $\varepsilon_a - \varepsilon_i - \langle ai||ai\rangle$, so orbital-energy differences are corrected by the Coulomb-exchange attraction.
- **$\mathbf B$.** It couples to doubles through the second-order part of the exponential. Dropping it is the Tamm-Dancoff approximation (CIS).
- **Sign of $\mathbf B$.** NRS's $\mathbf B$ is minus the "modern" $\mathbf B$ used in [[polarization-propagator-rpa]] and [[scf-second-order-and-stability]]. The difference is the phase convention $\kappa\to i\kappa$ of the generator. NRS's $\mathbf A - \mathbf B$ is the modern $\mathbf A + \mathbf B$, the Hessian for real orbital rotations. Eigenvalues are unaffected.

## Equations of motion

**Which operators.** The time dependence of $\boldsymbol\kappa$ is fixed by requiring the Ehrenfest theorem for a set of operators equal in number to the parameters. The natural choice is the **time-transformed** operators $\hat t_n = e^{-i\hat\kappa}\hat q_ne^{i\hat\kappa}$, which excite between the *current* occupied and virtual orbitals.

**Why time-transformed.** With them, the Ehrenfest theorem also holds for the occupied-occupied and virtual-virtual parts of any one-electron operator, so it holds for every one-electron operator. That preserves exact relations that follow from it, such as the length-velocity relation

$$
\omega\langle\langle\hat r_\alpha;\hat r_\beta\rangle\rangle_\omega = i\langle\langle\hat p_\alpha;\hat r_\beta\rangle\rangle_\omega,\qquad \langle\langle\hat p_\alpha;\hat l_\beta\rangle\rangle_0 = -\varepsilon_{\alpha\beta\gamma}\langle0|\hat r_\gamma|0\rangle.
$$

(These additionally need $[\hat{\mathbf r},\hat H_0] = i\hat{\mathbf p}$, i.e. a complete basis.) The untransformed $\hat q_n$ would not do this. For MCSCF the transformed set is $\{e^{-i\hat\kappa}\hat q^\dagger e^{i\hat\kappa},\ e^{-i\hat\kappa}e^{-i\hat R}\hat Q^\dagger e^{i\hat R}e^{i\hat\kappa}\}$ plus adjoints, with $\hat Q^\dagger_n = |\Phi_n\rangle\langle0|$.

**Expansion.** Collecting orders in $\boldsymbol\kappa$ and in the field defines generalized matrices:

- the Hessians $\mathbf E^{[k+1]}$ from $\hat H_0$;
- the overlaps $\mathbf S^{[k+2]}$ from the time derivative of the transformed operators;
- the property gradients $\mathbf V^{[k+1]}$ from the perturbation.

At first order, with $\boldsymbol\kappa^{(1)}(\omega) = (\kappa^{(1)}_n(\omega),\ [\kappa^{(1)}_n(-\omega)]^*)$:

$$
\big(\mathbf E^{[2]} - \omega\mathbf S^{[2]}\big)\boldsymbol\kappa^{(1)}(\omega) = -i\mathbf V^{\omega,[1]},\qquad \mathbf S^{[2]} = \begin{pmatrix}\mathbf 1 & 0\\ 0 & -\mathbf 1\end{pmatrix},\qquad \mathbf V^{\omega,[1]} = \begin{pmatrix}\langle0|[\hat q_n,\hat V^\omega]|0\rangle\\ \langle0|[\hat q^\dagger_n,\hat V^\omega]|0\rangle\end{pmatrix}.
$$

**Linear response function.** Inserting into $\langle\hat\Omega\rangle = \langle0|e^{i\hat\kappa}\hat\Omega e^{-i\hat\kappa}|0\rangle$:

$$
\langle\langle\hat\Omega;\hat V^\omega\rangle\rangle = -[\boldsymbol\Omega^{[1]}]^\dagger\big(\mathbf E^{[2]} - \omega\mathbf S^{[2]}\big)^{-1}\mathbf V^{\omega,[1]},
\label{rpa}
$$

the RPA (TDHF) linear response function, with $\boldsymbol\Omega^{[1]}$ built like $\mathbf V^{[1]}$.

- **Quasienergy route.** The same equation follows from $\delta Q_T = 0$ with electron-transfer instead of state-transfer amplitudes ([[quasienergy-and-time-dependent-variational-principle]]).
- **Static limit.** At $\omega = 0$ Eq. [[#rpa]] is the coupled Hartree-Fock polarizability ([[cphf-closed-shell]]).
- **Kohn-Sham.** The same structure with an exchange-correlation kernel gives TDDFT ([[tddft-linear-response]]).

**CI.** With the redundant $\hat R$ the matrices are

$$
A_{nm} = \langle\Phi_n|\hat H_0|\Phi_m\rangle - E_{CI}\delta_{nm},\quad B = 0,\qquad
\mathbf S^{[2]} = \begin{pmatrix}\delta_{nm} - c_nc^*_m & 0\\ 0 & -(\delta_{nm} - c^*_nc_m)\end{pmatrix},
$$

with $c_n$ the reference CI coefficients. $\mathbf A$ has one zero eigenvalue, whose eigenvector is the reference itself (the redundant phase direction). Its other eigenvalues are the CI excitation energies. The metric projects out the reference direction. No orbital response is included unless added with a Lagrangian ([[variational-perturbation-theory-and-the-2n-plus-1-rule]]).

**MCSCF.** $\mathbf E^{[2]}$ is the MCSCF Hessian with orbital, configuration and mixed blocks ([[mcscf-second-order-optimization]]). The metric becomes

$$
\mathbf S^{[2]} = \begin{pmatrix}\boldsymbol\Sigma & \boldsymbol\Delta\\ -\boldsymbol\Delta^* & -\boldsymbol\Sigma^*\end{pmatrix},
$$

with $\boldsymbol\Sigma$ Hermitian and $\boldsymbol\Delta$ antisymmetric. Both are built from $\langle0|[\hat X_n,\hat Y^\dagger_m]|0\rangle$ and $\langle0|[\hat X_n,\hat Y_m]|0\rangle$, where $\hat X,\hat Y\in\{\hat q,\hat Q\}$.

## Paired eigenvalues and the spectral form

**Generalized eigenproblem.** Solve $\mathbf E^{[2]}\mathbf X_e = \lambda_e\mathbf S^{[2]}\mathbf X_e$. The block structure makes the eigenvalues come in pairs: if $\mathbf X_e = (\mathbf Z_e, \mathbf Y^*_e)$ has eigenvalue $\lambda_e$, then $\mathbf X_{-e} = (\mathbf Y_e, \mathbf Z^*_e)$ has $-\lambda_e$. With the normalization

$$
\mathbf X^\dagger\mathbf E^{[2]}\mathbf X = \begin{pmatrix}\boldsymbol\lambda & 0\\ 0 & \boldsymbol\lambda\end{pmatrix},\qquad \mathbf X^\dagger\mathbf S^{[2]}\mathbf X = \begin{pmatrix}\mathbf 1 & 0\\ 0 & -\mathbf 1\end{pmatrix},
\label{diag}
$$

one non-unitary $\mathbf X$ diagonalizes both Hermitian matrices. Proof for distinct eigenvalues: $\mathbf X_f^\dagger\mathbf E^{[2]}\mathbf X_e$ equals both $\lambda_e\mathbf X^\dagger_f\mathbf S^{[2]}\mathbf X_e$ and $\lambda_f$ times the same overlap, so the overlap vanishes. Degenerate subspaces are diagonalized separately. Which member of a pair counts as "positive" is decided by the sign of $\mathbf X^\dagger\mathbf S^{[2]}\mathbf X$.

**Spectral form.** Using $(\mathbf E - \omega\mathbf S)^{-1} = \mathbf X[\mathbf X^\dagger(\mathbf E - \omega\mathbf S)\mathbf X]^{-1}\mathbf X^\dagger$,

$$
\langle\langle\hat\Omega;\hat V^\omega\rangle\rangle = -[\boldsymbol\Omega^{[1]}]^\dagger\sum_{e>0}\left(\frac{\mathbf X_e\mathbf X_e^\dagger}{\lambda_e - \omega} + \frac{\mathbf X_{-e}\mathbf X_{-e}^\dagger}{\lambda_e + \omega}\right)\mathbf V^{\omega,[1]},
$$

the sum-over-states formula with $\lambda_e$ as excitation energies and $[\boldsymbol\Omega^{[1]}]^\dagger\mathbf X_e$ as transition moments ([[residue-analysis-of-response-functions]]).

**Real eigenvalues and stability.**

- **Reality.** The $\lambda_e$ are real if $\mathbf E^{[2]}$ is sufficiently diagonally dominant. For a $2\times2$ case $\mathbf E^{[2]} = \begin{pmatrix}a & b\\ b^* & a\end{pmatrix}$ the pair is $\pm\sqrt{a^2 - |b|^2}$, imaginary if $|b| > a$.
- **Counting.** A congruence transformation such as Eq. [[#diag]] keeps the number of negative eigenvalues (Sylvester), so the number of negative $\lambda$'s equals half the number of negative eigenvalues of $\mathbf E^{[2]}$.
- **Real references.** $\mathbf E^{[2]}$ is unitarily equivalent to $\mathrm{diag}(\mathbf A+\mathbf B,\ \mathbf A-\mathbf B)$. A ground-state calculation is stable only if both blocks are positive definite. Otherwise the reference is not a minimum, and some excitation energies are imaginary or negative.

## No excited-state wave function

It is tempting to read $\mathbf X_e$ as an excited state, $\hat O^\dagger_e|0\rangle$ with $\hat O^\dagger_e = \sum_{ai}(Z_{ai}\hat a^\dagger_a\hat a_i + Y^*_{ai}\hat a^\dagger_i\hat a_a)$. But the de-excitation partner gives $\hat O_e|0\rangle = \sum_{ai}Y_{ai}|0^a_i\rangle\ne0$. The "killer condition" $\hat O_e|0\rangle = 0$ fails whenever $\mathbf Y\ne0$, i.e. whenever $\mathbf B\ne0$. So RPA delivers energies, transition moments and, through quadratic response, excited-state properties, but not an excited-state wave function. CIS ($\mathbf Y = 0$) and CI do give one.

## Worked examples

!!! example "Helium, aug-cc-pVDZ (NRS Sec. 7.1; recomputed for this note)"
    HF orbital energies $-0.9171$ (1s), $0.1744$ (2s), $0.5304$ (2p), $1.7135$ (3s), $3.0249$ (3p) $E_h$. Integrals (chemists'): $(22|11) = 0.3297$, $(21|12) = 0.0313$, $(32|11) = 0.1508$, $(31|12) = 0.0714$.

    **Response matrices.** The $s$-type singlet block ($1s\to2s$, $1s\to3s$), with NRS's unnormalized $\hat E^\dagger_{ai}$:

    $$
    \mathbf A = \begin{pmatrix}1.6490 & -0.0161\\ -0.0161 & 4.4119\end{pmatrix},\qquad \mathbf B = \begin{pmatrix}-0.0627 & -0.1428\\ -0.1428 & -0.4182\end{pmatrix}.
    $$

    **Excitation energies.**

    | Level | $1s\to2s$ ($E_h$) | eV |
    |---|---:|---:|
    | orbital-energy difference | 1.0915 | 29.70 |
    | CIS ($\tfrac12$ lowest eigenvalue of $\mathbf A$) | 0.8245 | 22.43 |
    | TDHF ($\lambda$ of Eq. [[#diag]]; second root 2.1944) | 0.8221 | 22.37 |
    | CI in the 1s, 2s active space | 0.8001 | 21.77 |

    - **TDHF eigenvectors.** $\mathbf Z = \begin{pmatrix}0.7074 & -0.0063\\ 0.0074 & 0.7081\end{pmatrix}$, $\mathbf Y = \begin{pmatrix}0.0139 & 0.0168\\ 0.0172 & 0.0336\end{pmatrix}$. The leading elements are near $1/\sqrt2$ because of the factor 2 in $\mathbf S^{[2]}$.
    - **CI.** Three CSFs (closed-shell $1s^2$, open-shell singlet $1s2s$, closed-shell $2s^2$) give $H_{CI} = \begin{pmatrix}-2.8557 & 0 & 0.0313\\ 0 & -2.0312 & 0.1864\\ 0.0313 & 0.1864 & -0.6571\end{pmatrix}$. The zero is Brillouin's theorem. Eigenvalues: $-2.8562, -2.0560, -0.6319$. The correlation energy is only $-0.5\,\mathrm{m}E_h$, but the excitation energy drops by 0.66 eV relative to CIS.
    - **CI Hessian.** The redundant $\mathbf A = \mathbf H_{CI} - E_{CI}\mathbf 1$ has eigenvalues $0,\ 0.8001,\ 2.2243$. The zero is the reference direction; the metric $\mathbf 1 - \mathbf c\mathbf c^{\mathsf T}$ has eigenvalues 0, 1, 1.
    - **PySCF check.** Full PySCF TDHF in this basis puts the lowest singlet at 22.369 eV.

!!! example "Beryllium, 6-31G: a triplet instability (NRS Tables 7.3-7.4; recomputed for this note)"
    HF orbital energies $-4.7069$ (1s), $-0.3013$ (2s), $0.0824$ (2p), $0.4398$ (3s), $0.4649$ (3p). Blocks for $2s\to2p_z, 3p_z$ (NRS normalization and sign; off-diagonal signs depend on the orbital phases):

    | | $\mathbf A$ | $\mathbf B$ |
    |---|---|---|
    | singlet | $\begin{pmatrix}0.4087 & 0.0440\\ 0.0440 & 0.9606\end{pmatrix}$ | $\begin{pmatrix}-0.1261 & 0.0570\\ 0.0570 & -0.0634\end{pmatrix}$ |
    | triplet | $\begin{pmatrix}0.1565 & 0.1579\\ 0.1579 & 0.8339\end{pmatrix}$ | $\begin{pmatrix}0.1261 & -0.0570\\ -0.0570 & 0.0634\end{pmatrix}$ |

    - **Off-diagonal elements.** $A^{\rm s}_{2s\,2p,2s\,3p} = -2(2p\,3p|2s\,2s) + 4(2p\,2s|2s\,3p)$ and $A^{\rm t} = -2(2p\,3p|2s\,2s)$. In the triplet the exchange integrals cancel completely, and the large Coulomb coupling $0.1579$ survives.
    - **Triplet instability.** The triplet $\mathbf A - \mathbf B$ (NRS sign) has eigenvalues $-0.0274$ and $0.8284$. The negative one means the RHF ground state is unstable toward mixing in triplet character (RHF→UHF). PySCF's stability analysis finds the lowest RHF→UHF Hessian eigenvalue at $-0.0137$, the same number with unit-normalized operators.
    - **Imaginary excitation energy.** $\omega^2$ for the lowest triplet is $-0.00184\,E_h^2$, so its TDHF energy is imaginary, as NRS report ("—" in Table 7.3).
    - **The singlet is fine.** Both $\mathbf A\pm\mathbf B$ are positive. TDHF puts $2p\,{}^1P$ at 5.158 eV (NRS 5.16; experiment 5.28).
    - **Practical trap.** PySCF's iterative triplet TDHF solver silently skips the imaginary root and reports 11.77 eV as the lowest triplet. CIS gives 1.653 eV.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 7.1, Eqs. (7.1)–(7.49) (parametrizations, Figs. 7.1–7.3, He Hessian Eqs. (7.27)–(7.30), CI Eqs. (7.35)–(7.41)); Sec. 7.2.1, Eqs. (7.61)–(7.82) (Ehrenfest equations, equivalence relations, Table 7.2 on neon described); Sec. 7.3.1–7.3.4, Eqs. (7.91)–(7.135), Tables 7.3–7.4; Sec. 7.4, Eqs. (7.153)–(7.158). The CI and SCF matrices were recomputed with PySCF 2.15.1 in `Claude outputs/part4_response_batchA.py`, section G. The sign relation between NRS's B and the convention of [[polarization-propagator-rpa]] was established by comparing Eq. (7.23) with PySCF's matrices.
