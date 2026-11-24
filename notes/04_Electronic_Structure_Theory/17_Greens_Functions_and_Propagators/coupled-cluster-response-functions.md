---
id: coupled-cluster-response-functions
title: Coupled-cluster response functions - the time-dependent quasienergy Lagrangian, Λ equations, first-order properties, the linear response equation with the CC Jacobian, and the pole structure of non-variational methods
summary: Time-dependent CC defines the quasienergy by projection, Q(t) = ⟨HF|H e^T|HF⟩, and the amplitudes by projected equations. Neither is variational, so a time-averaged Lagrangian with multipliers λ(t) is made stationary instead. At zeroth order this gives the ground-state amplitude and Λ equations. The first-order property is ⟨HF|(1 + Λ)e^{−T}V e^T|HF⟩, an expectation value with an asymmetric (orbital-unrelaxed) density. The linear response function needs only first-order amplitudes from (A − ω1)t⁽¹⁾ = −ξ, so its poles are the eigenvalues of the CC Jacobian (the EOM-CC energies). Orbital-relaxed CC, MP2 and CCSD(T) would add uncorrelated Hartree-Fock poles. Checked: the Λ-based CCSD dipole of water equals the finite-field derivative of the CCSD energy with frozen HF orbitals to 3 × 10⁻⁸.
status: in-progress
kind: theory
level: advanced
tags: [coupled-cluster, response-theory, lagrangian, lambda-equations, cc-jacobian, unrelaxed-density, polarizability, eom-cc]
prerequisites: [quasienergy-and-time-dependent-variational-principle, coupled-cluster-optimization-and-lagrangian, eom-ccsd-and-size-extensivity]
related: [lagrangian-for-nonvariational-energies, variational-perturbation-theory-and-the-2n-plus-1-rule, linear-response-for-variational-wave-functions, residue-analysis-of-response-functions, coupled-cluster-second-quantization]
conventions: [ia-letters, atomic-units]
key: ccresp
order: 110
date: 2026-11-24
---

Atomic units. $|{\rm HF}\rangle$ is the reference determinant, $\hat T = \sum_nt_n\hat\tau^\dagger_n$ the cluster operator with excitation operators $\hat\tau^\dagger_n$ ($n$ = singles, doubles, …), and $\langle n| = \langle{\rm HF}|\hat\tau_n$ the excited bras. $|{\rm CC}\rangle = e^{\hat T^{(0)}}|{\rm HF}\rangle$. Orbitals are the field-free HF orbitals throughout ("unrelaxed" CC response).

## Why CC needs a Lagrangian

**Ground state.** The CC energy and amplitudes come from projections, $E = \langle{\rm HF}|\hat H_0e^{\hat T}|{\rm HF}\rangle$ and $\Omega_n = \langle n|e^{-\hat T}\hat H_0e^{\hat T}|{\rm HF}\rangle = 0$ (using $\langle{\rm HF}|\hat T = 0$). The energy is not stationary in the amplitudes and not an expectation value. So the Hellmann-Feynman theorem does not hold, and nothing guarantees a real energy.

**Time-dependent CC.** With $e^{\hat T(t)}|{\rm HF}\rangle$ as the phase-isolated state, the quasienergy and amplitude equations become

$$
Q(t) = \langle{\rm HF}|\big(\hat H - i\partial_t\big)e^{\hat T(t)}|{\rm HF}\rangle = \langle{\rm HF}|\hat He^{\hat T(t)}|{\rm HF}\rangle,\qquad \langle n|e^{-\hat T}\big(\hat H - i\partial_t\big)e^{\hat T}|{\rm HF}\rangle = 0.
$$

The time derivative drops from $Q$ because $\partial_te^{\hat T}|{\rm HF}\rangle = \dot{\hat T}e^{\hat T}|{\rm HF}\rangle$ has no $|{\rm HF}\rangle$ component. Following the variational treatment of [[quasienergy-and-time-dependent-variational-principle]], the constraints are added with time-dependent multipliers:

$$
L(t) = Q(t) + \sum_n\lambda_n(t)\,\langle n|e^{-\hat T}\big(\hat H - i\partial_t\big)e^{\hat T}|{\rm HF}\rangle,\qquad \delta L_T = 0.
\label{lag}
$$

$L_T$ is the time average. Stationarity in $\lambda$ gives back the amplitude equations; stationarity in $t$ fixes the multipliers. Variational and non-variational methods now share one recipe: differentiate a stationary time-averaged function.

## Zeroth order: amplitudes and Λ

**Equations.** Stationarity with respect to $\lambda^{(0)}_n$ gives the ground-state amplitude equations $\Omega_n = 0$. Stationarity with respect to $t^{(0)}_n$ gives the $\Lambda$ equations

$$
0 = \eta_n + \sum_k\lambda^{(0)}_kA_{kn},\qquad \eta_n = \langle{\rm HF}|\hat H_0\hat\tau^\dagger_n|{\rm CC}\rangle,\qquad A_{kn} = \langle k|e^{-\hat T}[\hat H_0,\hat\tau^\dagger_n]|{\rm CC}\rangle,
\label{lambda}
$$

i.e. $\boldsymbol\lambda^{(0)} = -\boldsymbol\eta\mathbf A^{-1}$.

**The CC Jacobian.** $\mathbf A$ is the CC Jacobian, $A_{kn} = \partial\Omega_k/\partial t_n$. In the derivation, all excitation operators commute with $\hat T$, so $\partial e^{\hat T}/\partial t_n = \hat\tau^\dagger_ne^{\hat T}$. This is the same linear system for the multipliers as in [[coupled-cluster-optimization-and-lagrangian]], and $\boldsymbol\lambda$ is the left ground-state eigenvector of the similarity-transformed Hamiltonian ([[eom-ccsd-and-size-extensivity]]).

## First-order properties

Because $L_T$ is stationary in all amplitudes and multipliers, the first field derivative is purely explicit:

$$
\langle\hat V\rangle^{(0)} = \frac{\partial L_T}{\partial F^{\omega_1}} = \Big[\langle{\rm HF}|\hat Ve^{\hat T}|{\rm HF}\rangle + \sum_n\lambda^{(0)}_n\langle n|e^{-\hat T}\hat Ve^{\hat T}|{\rm HF}\rangle\Big]\delta_{\omega_1}.
\label{prop}
$$

This is $\langle{\rm HF}|(1+\hat\Lambda)e^{-\hat T}\hat Ve^{\hat T}|{\rm HF}\rangle$, a "CC expectation value" with an asymmetric one-particle density. It is nonzero only for a static field. For an observable one takes the real part.

**No orbital relaxation.** Eq. [[#prop]] is the derivative of the CC energy computed with orbitals that do **not** respond to the field. The derivative with relaxed orbitals needs one more set of multipliers for the HF conditions, as in [[lagrangian-for-nonvariational-energies]]. The worked example shows the size of the difference.

## Linear response

**Second derivative.** Differentiating $L_T$ twice, the terms with second-order amplitudes and multipliers vanish by stationarity. The $2n+2$ rule for the multipliers removes the first-order multipliers as well: they multiply the derivative of the first-order amplitude equation, which is zero. Symmetrized over $(\alpha,\omega_1)\leftrightarrow(\beta,\omega_2)$, the result is

$$
\langle\langle\hat V^{\omega_1}_\alpha;\hat V^{\omega_2}_\beta\rangle\rangle = \sum_{\alpha\beta}\Big[\frac{\partial^2L_T}{\partial F^{\omega_1}_\alpha\partial t^{(1)}_n}\frac{\partial t^{(1)}_n}{\partial F^{\omega_2}_\beta} + \tfrac12\frac{\partial t^{(1)}_m}{\partial F^{\omega_1}_\alpha}\frac{\partial^2L_T}{\partial t^{(1)}_m\partial t^{(1)}_n}\frac{\partial t^{(1)}_n}{\partial F^{\omega_2}_\beta}\Big].
\label{ccresp}
$$

The symmetrization is needed explicitly because the CC expression is not symmetric by itself.

**First-order amplitudes.** They come from differentiating the multiplier stationarity condition once:

$$
\big(\mathbf A - \omega_2\mathbf 1\big)\frac{\partial\mathbf t^{(1)}}{\partial F^{\omega_2}_\beta} = -\boldsymbol\xi^\beta,\qquad \xi^\beta_m = \langle m|e^{-\hat T}\hat V^{\omega_2}_\beta|{\rm CC}\rangle.
\label{ccle}
$$

The $-\omega_2\mathbf 1$ comes from the $-i\partial_t$ term of Eq. [[#lag]]. In $\langle m|e^{-\hat T}(-i\partial_t)e^{\hat T}|{\rm HF}\rangle = -i\dot t_m$ only the amplitude's own time factor survives, since $[\hat T,\dot{\hat T}] = 0$. For a Fourier amplitude $\propto e^{-i\omega_2t}$ this gives $-\omega_2$.

**Second-derivative blocks.**

$$
\frac{\partial^2L_T}{\partial F_\alpha\partial t_n} = \langle{\rm HF}|\hat V_\alpha\hat\tau^\dagger_n|{\rm CC}\rangle + \sum_k\lambda^{(0)}_k\langle k|e^{-\hat T}[\hat V_\alpha,\hat\tau^\dagger_n]|{\rm CC}\rangle,
$$

$$
\frac{\partial^2L_T}{\partial t_m\partial t_n} = \langle{\rm HF}|\hat H_0\hat\tau^\dagger_m\hat\tau^\dagger_n|{\rm CC}\rangle + \sum_k\lambda^{(0)}_k\langle k|e^{-\hat T}[[\hat H_0,\hat\tau^\dagger_m],\hat\tau^\dagger_n]|{\rm CC}\rangle.
$$

## Pole structure

**Poles.** All frequency dependence of Eq. [[#ccresp]] sits in $(\mathbf A - \omega\mathbf 1)^{-1}$, so the poles are the eigenvalues of the Jacobian: the EOM-CC excitation energies. They are size-intensive for local excitations ([[eom-ccsd-and-size-extensivity]]).

**Residues.** Because $\mathbf A$ is not symmetric, left and right eigenvectors differ. Transition strengths combine a left and a right transition moment, and are not squares of one quantity.

**Why "unrelaxed".** If the orbitals were also allowed to respond (orbital-relaxed CC), or for MP2 and CCSD(T), the response function would also contain the TDHF poles of the orbital response. These are uncorrelated excitation energies with no physical meaning in a correlated spectrum, and they distort the dispersion. That is why frequency-dependent CC response is formulated unrelaxed.

**Pragmatic combination.** NRS mention combining a static correlated property, computed as a relaxed energy derivative (e.g. MP2), with the frequency dependence from a cheaper method (e.g. TDHF), $\alpha(\omega)\approx\alpha^{\rm MP2}(0) + [\alpha^{\rm HF}(\omega)-\alpha^{\rm HF}(0)]$.

## Worked example

!!! example "Water, 6-31G: the CCSD first-order property is an unrelaxed derivative (computed for this note)"
    O at the origin, H at $(0,\pm0.757,0.587)$ Å, field along $z$ (electron energy $+Fz$), so $dE/dF = \mathrm{tr}(\mathbf D\mathbf z)$ for the electronic part. CCSD with PySCF 2.15.1. The frozen-orbital energies use the field-free HF orbitals with the field in the one-electron Hamiltonian (non-canonical CCSD).

    | Quantity | value |
    |---|---:|
    | $dE_{CC}/dF$, frozen HF orbitals, finite field ($h = 10^{-4}$) | 1.22619692 |
    | $\mathrm{tr}(\mathbf D_\Lambda\mathbf z)$, Eq. [[#prop]] | 1.22619689 |
    | the same density with $\Lambda = 0$ (not a derivative) | 1.20259543 |
    | $\mathrm{tr}(\mathbf D_{HF}\mathbf z)$ | 1.18298281 |
    | $dE_{CC}/dF$, relaxed orbitals (SCF in each field) | 1.22399326 |

    - **Λ is essential.** Without it, the expression is not the derivative of anything: it misses 0.024.
    - **Orbital relaxation.** The relaxed derivative differs by $-0.0022$. That is the price of leaving out the orbital response, and of avoiding the HF poles.

## Limitations

- **Real part.** The projected quasienergy is not guaranteed real. Properties are taken as the real part, or the response is defined from $\mathrm{Re}\,L_T$.
- **Higher orders.** Quadratic and cubic CC response follow by further differentiation of Eq. [[#lag]] with $2n+1$ and $2n+2$ rules. NRS do not derive them; their reference for the Fourier-component formalism is Christiansen, Jørgensen and Hättig, Int. J. Quantum Chem. 68, 1 (1998) (as cited by NRS, to verify).
- **Cost.** Each frequency needs one non-symmetric linear solve of the size of the amplitude space for each perturbation.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 7.1.4, Eqs. (7.50)–(7.60); Sec. 7.2.2, Eqs. (7.86)–(7.90); Sec. 7.3 (introduction, pole structure of MP2 and CCSD(T)); Sec. 7.3.5, Eqs. (7.136)–(7.152); Appendix H, Eqs. (H.19)–(H.25). The water calculation is in `Claude outputs/part4_response_batchA.py`, section I.
