---
id: electronic-and-nuclear-contributions-to-response
title: Electronic and nuclear contributions to response functions - the vibronic sum over states, pure vibrational terms [μ²], [μα], [μ³], and zero-point vibrational averaging
summary: In the Born–Oppenheimer approximation a polarizability is a sum over vibronic states. Splitting that sum into excitations within the electronic ground state and excitations to excited electronic states gives two contributions. The pure vibrational part [μ²] is built from vibrational transition moments of the geometry-dependent dipole μ(R). The zero-point vibrationally averaged part ⟨0|α_e(R)|0⟩ is the electronic polarizability averaged over the vibrational ground state. Hyperpolarizabilities split the same way into [μα] + [μ³] and [α²] + [μβ] + [μ²α] + [μ⁴]. Because vibrational frequencies are far below optical ones, pure vibrational terms are large for static fields and small at optical frequencies. Recomputed: for hydrogen fluoride, the exact vibronic static α equals α_e + Δα_zpva + α_v to five digits; the vibrational β nearly cancels the electronic one.
status: in-progress
kind: theory
level: advanced
tags: [vibrational-polarizability, pure-vibrational, zero-point-vibrational-averaging, born-oppenheimer, vibronic-states, hyperpolarizability, bishop-kirtman, nonlinear-optics]
prerequisites: [exact-state-response-functions, born-oppenheimer-approximation, polarizabilities-and-dispersion-coefficients, harmonic-vibrational-analysis]
related: [zero-point-vibrational-corrections-to-properties, pure-vibrational-contributions-and-nuclear-relaxation, infrared-intensities, dispersion-oscillator-strengths-and-sum-rules, vibronic-band-shapes-franck-condon-and-herzberg-teller]
conventions: [atomic-units]
key: alpha-split
order: 160
date: 2026-11-25
---

Atomic units. $|K,k\rangle = |K\rangle_e|k\rangle_K$ is a Born–Oppenheimer vibronic state: electronic state $K$, vibrational state $k$ on the surface of $K$. $|0,0\rangle$ is the vibronic ground state, $\omega_{Kk,00} = E_{Kk} - E_{00}$. For an electronic quantity $P$ evaluated at fixed nuclei, $P(\mathbf R) = \langle0|\hat P|0\rangle_e(\mathbf R)$ and $(P)_{kl} = \langle k|P(\mathbf R)|l\rangle$. The dipole operator contains electrons and nuclei, $\hat{\boldsymbol\mu} = \sum_i\hat{\boldsymbol\mu}(i) + \sum_NZ_N\mathbf R_N$ (NRS Eq. 6.13). $\sum_{-\sigma,1}$ denotes the sum over permutations of the pairs $(-\omega_\sigma,\alpha)$, $(\omega_1,\beta)$.

## The Born–Oppenheimer starting point

**Adiabatic expansion.** The exact molecular wave function can be expanded in electronic eigenfunctions at fixed nuclei, $\Psi(\mathbf r,\mathbf R) = \sum_K\Phi_K(\mathbf R)\psi_K(\mathbf r;\mathbf R)$ (NRS Eq. 6.4). Inserting it into the Schrödinger equation and projecting gives nuclear equations coupled through

$$
C_{KL}(\mathbf R) = \langle\psi_K|\hat T_N|\psi_L\rangle - \sum_N\frac{1}{m_N}\langle\psi_K|\nabla_N|\psi_L\rangle\cdot\nabla_N
$$

(NRS Eqs. 6.9–6.10, footnote 3; see [[born-oppenheimer-approximation]]).

- **Adiabatic approximation.** Dropping $K\neq L$ couplings gives this approximation. The nuclei move on $V_K(\mathbf R)$ plus the diagonal correction $C_{KK}$, which depends on the nuclear masses and is different for each isotopologue.
- **Clamped-nucleus surface.** Dropping $C_{KK}$ as well gives the mass-independent surface $V_K(\mathbf R)$, with $[\hat T_N + V_K(\mathbf R)]\Phi^K_k = E^K_k\Phi^K_k$ (NRS Eq. 6.8).

Near conical intersections the neglected couplings are large and the separation fails. Everything below assumes well-separated electronic states.

## Splitting the vibronic polarizability

**The vibronic sum over states.** For a molecule in $|0,0\rangle$, the exact-state polarizability of [[exact-state-response-functions]] becomes a sum over vibronic states (no damping, NRS Eq. 6.12):

$$
\alpha_{\alpha\beta}(-\omega_\sigma;\omega_1) = \sum_{-\sigma,1}\sum_{(K,k)\neq(0,0)}\frac{\langle0,0|\hat\mu_\alpha|K,k\rangle\langle k,K|\hat\mu_\beta|0,0\rangle}{\omega_{Kk,00} - \omega_1}.
$$

Split the sum into $K = 0$ (vibrational excitations within the electronic ground state) and $K\neq0$ (NRS Eq. 6.14).

**The $K = 0$ terms.** The electronic integration gives $\langle0,0|\hat\mu_\alpha|0,k\rangle = \langle0|\mu_\alpha(\mathbf R)|k\rangle$, a vibrational transition moment of the geometry-dependent dipole moment (NRS Eq. 6.15). This is the **pure vibrational** polarizability:

$$
\alpha^{\rm v}_{\alpha\beta}(-\omega_\sigma;\omega_1) = \sum_{-\sigma,1}\sum_{k\neq0}\frac{(\mu_\alpha)_{0k}(\mu_\beta)_{k0}}{\omega_{k0} - \omega_1}\equiv[\mu^2].
\label{mu2}
$$

It vanishes if $\mu(\mathbf R)$ does not depend on geometry. Its poles are the vibrational transitions, the IR spectrum of [[infrared-intensities]].

**The $K\neq0$ terms.** If the electronic gaps are large compared with vibrational spacings, $\omega_{Kk,00}\approx\omega_{K0}(\mathbf R)$. The vibrational sum over $k$ then closes to the identity, and what remains is the electronic polarizability averaged over the vibrational ground state (NRS Eq. 6.17):

$$
\alpha^{\rm zpva}_{\alpha\beta} = \sum_{-\sigma,1}\sum_{K\neq0}\frac{\langle0,0|\hat\mu_\alpha|K\rangle\langle K|\hat\mu_\beta|0,0\rangle}{\omega_{K0} - \omega_1} = \langle0|\alpha^{\rm e}_{\alpha\beta}(\mathbf R)|0\rangle .
$$

The nuclear part of $\hat{\boldsymbol\mu}$ drops out here, because it is a constant in the electronic integral and $\langle0|K\rangle_e = 0$.

**The partition.** Writing $\langle0|\alpha^{\rm e}(\mathbf R)|0\rangle = \alpha^{\rm e}(\mathbf R_e) + \Delta\alpha^{\rm zpva}$ gives the standard partition (NRS Eq. 6.18):

$$
\alpha = \alpha^{\rm e}(\mathbf R_e) + \Delta\alpha^{\rm zpva} + \alpha^{\rm v}.
\label{alpha-split}
$$

The two corrections are evaluated in [[zero-point-vibrational-corrections-to-properties]] and [[pure-vibrational-contributions-and-nuclear-relaxation]].

## Hyperpolarizabilities

**First hyperpolarizability.** Start from the sum-over-states $\beta$ written with fluctuation operators $\bar\mu = \hat\mu - \langle0,0|\hat\mu|0,0\rangle$, which is free of secular divergences (NRS Eq. 6.19). The pure vibrational terms are those in which at least one intermediate state belongs to the electronic ground state (NRS Eq. 6.20).

- **Closing the sum.** For the terms with one electronically excited intermediate, set $\omega_{Kk,00}\approx\omega_{K0}$ and close the sum over its vibrational states. Each such pair of electronic transition moments becomes an electronic polarizability $\alpha^{\rm e}(\mathbf R)$ inside a vibrational matrix element (NRS Eq. 6.21).
- **Static electronic polarizability.** Using the static $\alpha^{\rm e}$ there, with all real matrix elements, gives

$$
\beta^{\rm v} = [\mu\alpha] + [\mu^3],\qquad
[\mu\alpha] = \sum_{-\sigma,1,2}\sum_{k\neq0}\frac{(\mu_\alpha)_{0k}(\alpha_{\beta\gamma})_{k0}\,\omega_{k0}}{\omega_{k0}^2 - \omega_\sigma^2},\qquad
[\mu^3] = \sum_{-\sigma,1,2}\sum_{k,l\neq0}\frac{(\mu_\alpha)_{0k}(\bar\mu_\beta)_{kl}(\mu_\gamma)_{l0}}{(\omega_{k0} - \omega_\sigma)(\omega_{l0} - \omega_2)}
\label{beta-v}
$$

(NRS Eqs. 6.22–6.25).

- **Why the static approximation is mild.** It replaces a dispersive $\alpha^{\rm e}$ at several optical frequencies by one static value. Away from electronic resonances dispersion is modest, and the permutations mix positive and negative frequencies.

**Second hyperpolarizability.** In the same way $\gamma^{\rm v} = [\alpha^2] + [\mu\beta] + [\mu^2\alpha] + [\mu^4]$ (NRS Eq. 6.26, Table 6.1).

## General consequences

**Lower-order responses.** Pure vibrational terms are built from lower-order responses ($\mu$, $\alpha$, $\beta$) and their geometry dependence. If these vanish, as the magnetic moment of a closed-shell state does, there is no pure vibrational term. Pure vibrational corrections therefore matter much more for electric properties than for mixed magnetic ones.

**Frequency dependence.** Vibrational frequencies (≲ 4000 cm⁻¹, ≲ 0.02 au) lie far below optical frequencies (589 nm is 0.077 au). In each denominator $\omega_{k0}^2 - \omega^2$ the optical frequency then dominates:

- **At optical frequencies.** $\alpha^{\rm v}$ is small and negative, of order $|\mu'|^2/\omega^2$.
- **For static fields.** The same term is $|\mu'|^2/\omega_{k0}^2$, which can rival the electronic part.
- **Mixed processes.** Processes with at least one static field, or whose frequencies combine to zero somewhere, keep large vibrational parts. Examples are the dc-Kerr effect $\gamma(-\omega;\omega,0,0)$, EFISHG $\gamma(-2\omega;\omega,\omega,0)$ and the Pockels effect $\beta(-\omega;\omega,0)$, as well as optical rectification. Pure optical SHG and THG are nearly free of them.

**Comparing with experiment.** Experimental static polarizabilities and hyperpolarizabilities (from dielectric constants or static-field measurements) always include $\alpha^{\rm v}$ and $\beta^{\rm v}$. They cannot be compared with purely electronic calculations.

## Worked example

!!! example "Hydrogen fluoride along its bond (recomputed for this note)"
    **Setup.** HF/aug-cc-pVTZ energies $E(r,F)$ on 49 bond lengths (0.62–1.58 Å) × 5 field strengths ($F_z = 0, \pm0.0025, \pm0.005$ au, along the bond). The electronic $\mu$, $\alpha_{zz}$, $\beta_{zzz}$ at each $r$ come from five-point field differences. Exact vibrational states on each field-dependent curve come from a sinc discrete-variable representation (500 points, reduced mass of ¹H¹⁹F). Only the bond direction is treated, so rotations and the perpendicular components are ignored.

    | quantity (au) | value |
    |---|---:|
    | $\alpha^{\rm e}_{zz}(r_e)$, $r_e = 0.89912$ Å | 5.5329 |
    | $\Delta\alpha^{\rm zpva} = \langle0|\alpha^{\rm e}(r)|0\rangle - \alpha^{\rm e}(r_e)$ | 0.1912 |
    | $\alpha^{\rm v}(0;0)$, exact sum over 40 vibrational states, Eq. [[#mu2]] | 0.2420 |
    | sum, Eq. [[#alpha-split]] | 5.9661 |
    | $-\partial^2E_{\rm vib,0}(F)/\partial F^2$ (exact vibronic ground state in the field) | 5.9661 |

    **The partition is exact.** The decomposition reproduces the vibronic polarizability to $10^{-5}$: within Born–Oppenheimer and the static limit, Eq. [[#alpha-split]] involves no approximation.

    **Size.** The vibrational parts add 8% to the static $\alpha$.

    **At 589 nm** the same sum gives $\alpha^{\rm v} = -0.0169$ au: ten times smaller and of the opposite sign.

    **Hyperpolarizability.** The static $\beta_{zzz}$ shows the cancellation dramatically:

    - $\beta^{\rm e}(r_e) = -8.71$ au;
    - the exact vibronic value (third field derivative of $E_{\rm vib,0}$) is $+0.67$ au;
    - the vibrational contribution, $+9.38$ au, almost exactly cancels the electronic one.

    The split into nuclear-relaxation and curvature parts is in [[pure-vibrational-contributions-and-nuclear-relaxation]].

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 6.1, Eqs. (6.1)–(6.10), Fig. 6.1 (described); Sec. 6.2, Eqs. (6.11)–(6.26), Table 6.1. The calculations are in `Claude outputs/part4_response_batchC.py`, section A.
