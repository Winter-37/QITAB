---
id: x-ray-absorption
title: X-ray absorption (NEXAFS) - core-excited states, relaxation, orientation from linear dichroism and the magic angle, static exchange, and core-valence-separated damped response
summary: Near-edge X-ray absorption excites a localized core electron into valence or Rydberg orbitals. The core hole is a nearly unscreened extra nuclear charge (Z+1 picture), so the valence density relaxes strongly toward it. This relaxation, about 20 eV for the O 1s hole in water, is a strong correlation effect from the ground-state point of view. It makes CIS useless and forces either state-specific orbitals (ΔSCF, static exchange) or a response method with double excitations (CCSD) or an adapted functional. Core-valence separation removes the valence continuum in which core states are embedded, and damped response gives the spectrum directly. Linear dichroism of oriented monolayers gives the molecular orientation through cos²(D,F), with a magic angle of 54.7°. Recomputed: the water O K-edge by Koopmans, ΔSCF, CVS-CIS and ΔSCF core excitation.
status: in-progress
kind: theory
level: intermediate
tags: [x-ray-absorption, nexafs, xanes, core-excitation, core-valence-separation, cvs, static-exchange, stex, delta-scf, orbital-relaxation, z-plus-1, magic-angle, complex-polarization-propagator]
prerequisites: [electronic-absorption-and-emission, damped-response-and-absorption-cross-sections, koopmans-theorem]
related: [tddft-linear-response, polarization-propagator-rpa, coupled-cluster-response-functions, multiphoton-absorption]
conventions: [atomic-units]
key: dichro
order: 130
date: 2026-11-24
---

Atomic units; energies in eV where stated ($1\,E_h = 27.211386$ eV). $c$ labels core orbitals, $i,j$ occupied, $a,b$ virtual. $\mathbf D = \langle f|\hat{\boldsymbol\mu}|0\rangle$ is the absorption (transition) dipole and $\mathbf F$ the X-ray electric field vector.

## The experiment

Soft X-rays (below about 2 keV) excite 1s electrons (K edges) of second-row elements, and 2s, 2p₁/₂, 2p₃/₂ electrons of third-row elements (L₁, L₂, L₃ edges, split by spin–orbit coupling). The fine structure near an edge, mostly below the ionization threshold, is NEXAFS (synonym XANES). The oscillations far above the edge are EXAFS.

**Source and detection.** The source is a synchrotron: tunable, highly polarized and collimated. The absorption is detected indirectly through the decay of the core hole. Either a valence electron fills the hole and emits a fluorescence photon, or the energy is released as an Auger electron. For C, N and O the Auger yield dominates, so NEXAFS is usually measured as electron yield (NRS Figs. 8.20–8.21).

## What makes core excitations different

**Localization and relaxation.** The core hole is atomic and localized. To the valence electrons it looks like almost a full extra unit of nuclear charge. This is the equivalent-core or $Z+1$ approximation: a carbon with a 1s hole resembles nitrogen. Two consequences follow:

- **Localization breaks symmetry.** In ethylene the C 1s hole sits on one carbon, and the inversion symmetry of the molecule is lost.
- **Strong relaxation.** The valence density flows toward the hole (NRS Fig. 8.23), and the core orbital itself contracts: the C 1s radial maximum moves from 0.176 to 0.168 $a_0$ in C₂H₄⁺, close to the hydrogenic $Z = 6$ value 0.167 (NRS Fig. 8.22). Koopmans core ionization energies are therefore far too high.

**The two difficulties for response theory** (NRS Sec. 8.5.5.1):

1. **Finding the states.** Core-excited states lie hundreds of eV up, embedded in a continuum of valence-ionized states. Bottom-up eigensolvers (Davidson for the lowest roots) cannot reach them.
2. **Relaxation is correlation.** In a CI expansion over ground-state orbitals, relaxing the valence density around the hole needs at least double excitations: the core excitation plus a valence excitation that polarizes. CIS and adiabatic TDDFT with standard functionals lack them.

## Orientation from linear dichroism

**Intensity and orientation.** In the dipole approximation a transition's intensity under linearly polarized light is $I\propto|\mathbf D\cdot\mathbf F|^2\propto\cos^2(\mathbf D,\mathbf F)$ (NRS Eqs. 8.191–8.192). For 1s → σ* and 1s → π* transitions, $\mathbf D$ points along the σ* bond axis or the π* lobe, so the intensity reports the orientation of that bond.

**Monolayers.** A self-assembled monolayer on a surface (normal $z$) has azimuthally random domains. Averaging over the azimuth $\phi_D$, with $\mathbf F$ in the $xz$ plane at polar angle $\theta_F$ (NRS Eqs. 8.193–8.194), gives

$$
I(\theta_D,\theta_F)\propto\tfrac12\sin^2\theta_D\sin^2\theta_F + \cos^2\theta_D\cos^2\theta_F .
\label{dichro}
$$

- **Normal incidence.** $\theta_F = 90^\circ$ ($\mathbf F$ parallel to the surface).
- **Grazing incidence.** $\theta_F$ is small. The ratio of intensities at two incidence angles gives $\theta_D$.
- **Magic angle.** At $\theta_F = \arctan\sqrt2 = 54.7356^\circ$, $\tan^2\theta_F = 2$ and $I = \tfrac13$ for every $\theta_D$. Symmetrically, molecules tilted at $\theta_D = 54.7^\circ$ show no dichroism. Their spectrum then cannot be distinguished from a disordered film, so grazing angles are chosen away from 54.7° (NRS uses 30°, Fig. 8.26).

## Static exchange (STEX)

**Idea.** Do one SCF for the core-ionized molecule, then CIS from the core orbital with these relaxed orbitals (NRS Eq. 8.195):

$$
|\epsilon\rangle = \sum_{c}^{\rm core}\sum_a^{\rm virt}C^c_a\,\hat a^\dagger_a\hat a_c|\mathrm{ref}\rangle,
$$

with $|\mathrm{ref}\rangle$ built from orbitals of the ion. Originally STEX was an effective one-particle Hamiltonian for the excited electron in the static field of the ion. With more than one core orbital (p shells), "CIS in ion orbitals" is the better description.

**Advantages.**

- **Cheap.** A single ion SCF plus one diagonalization gives hundreds to thousands of core-excited states, with their wave functions available for interpretation.
- **Relaxation included.** The relaxation is built into the orbitals.
- **Orthogonal states.** Unlike pure state-specific methods, the excited states remain orthogonal to each other.

**Costs.**

- **One atom at a time.** The relaxation is specific to one atom, so each inequivalent atom needs its own calculation, and the spectra are summed.
- **Nonorthogonal transition moments.** Transition moments couple the ground state (ground-state orbitals) with excited states (ion orbitals). They need cofactor expansions, about one matrix inversion per state (NRS Eq. 8.196).
- **No correlation** beyond the relaxation.

**Example (described).** For the carbon K-edge of 1,1-difluoroethylene, ground-state CIS misses the first peak by 11.1 eV, about the relaxation energy, and gets the profile wrong. STEX resolves the CH₂ (lower, weaker) and CF₂ (higher, stronger) π* resonances (NRS Fig. 8.27).

## Core-valence separation and damped response

**The complex polarization propagator view.** Instead of searching for states, compute the observable: the absorption cross section from the imaginary part of the damped polarizability at X-ray frequencies, $\alpha^{\rm I}_{\alpha\beta}(\omega) = -\mathrm{Im}\langle\langle\hat\mu_\alpha;\hat\mu_\beta\rangle\rangle_{\omega+i\gamma}$ (NRS Eq. 8.197; [[damped-response-and-absorption-cross-sections]]). Its advantages:

- **Ground state only.** Only the ground state is optimized; the states stay orthogonal and the sum rules hold.
- **All edges together.** All atoms of one edge are treated together (full channel interaction).
- **No eigenvalues needed.** The resolvent is solved at each frequency.

**Core-valence separation (CVS).** Core and valence excitations differ in energy by hundreds of eV, so their coupling can be neglected. In the excitation manifold, keep only operators that move an electron out of the core orbitals of interest:

$$
\{\hat a^\dagger_a\hat a_i\}\;\longrightarrow\;\{\hat a^\dagger_a\hat a_c\},\qquad c\in\text{core}.
$$

The core-excited states then become the lowest roots of a small eigenvalue problem, and standard eigensolvers work again. CVS also removes the unphysical mixing with the valence-ionization continuum.

**Method requirements** (NRS Sec. 8.5.5.4):

- **Wave-function methods** need at least doubles for the relaxation. CCSD captures about 90% of it, and CCSDR(3) corrects the energies with triples (NRS Figs. 8.27–8.28).
- **TDDFT has three problems.**
  1. **Charge-transfer character.** The excitation runs from a compact core orbital to a diffuse virtual one with small overlap, like a valence charge-transfer excitation. Range-separated functionals with the correct asymptotic $-1/r$ (CAM-B3LYP with a modified long-range parameter) help.
  2. **Self-interaction error.** It is large for localized core orbitals. If nearly constant across the core orbitals of interest, it is removed by a single energy shift. NRS shift CAM-B3LYP by −10.2 eV and CCSD by −3.0 eV in Fig. 8.28, after which the two profiles agree closely.
  3. **No relaxation.** Adiabatic TDDFT has only single excitations, so the relaxation must come from the functional and is never complete.

## Worked example

!!! example "Water O K-edge (recomputed for this note)"
    HF, uncontracted aug-cc-pwCVTZ on O (core flexibility), aug-cc-pVTZ on H. Geometry $r_{\rm OH} = 0.9572$ Å, $\angle = 104.5^\circ$; $E_{\rm HF} = -76.060845\,E_h$.

    **Ionization.**

    | quantity | eV |
    |---|---:|
    | Koopmans O 1s IP, $-\varepsilon_{1s}$ | 559.65 |
    | ΔSCF O 1s IP (UHF ion with the 1s hole kept by MOM) | 538.97 |
    | relaxation energy, Koopmans − ΔSCF | 20.68 |

    The experimental gas-phase O 1s IP is about 539.9 eV (to verify). ΔSCF lacks correlation and the scalar-relativistic shift of a few tenths of an eV. NRS quote about 17 eV for the relaxation energy at the water oxygen K-edge (Sec. 8.5.5.3); the ΔSCF−Koopmans difference here is larger, so their definition may differ.

    **Excitation.** CVS-CIS from O 1s with ground-state orbitals (singlet, length-gauge oscillator strengths):

    | state | eV | $f$ |
    |---:|---:|---:|
    | 1 | 551.23 | 0.040 |
    | 2 | 551.87 | 0.075 |
    | 3 | 555.72 | 0.034 |
    | 4 | 556.12 | 0.016 |

    ΔSCF core excitation 1s → LUMO with MOM: mixed-spin determinant 533.64 eV, triplet 533.37 eV, spin-purified singlet $2E_{\rm mixed} - E_{\rm T}$ = **533.90 eV**. The experimental first band (O 1s → 4a₁/3s) is near 534 eV (to verify).

    **The lesson in numbers.**

    - **CIS with frozen orbitals.** It is 17 eV too high, close to the relaxation energy. Relaxation, not the excitation pattern, dominates the error.
    - **State-specific orbitals.** They recover the band to within a few tenths of an eV.
    - **Below the ionization edge.** The ΔSCF excitation lies 5 eV below the ΔSCF IP: the first band is a bound pre-edge state.

    **Magic angle.** At $\theta_F = 54.7356^\circ$, Eq. [[#dichro]] gives $I = 0.333333$ for $\theta_D = 0^\circ, 30^\circ, 60^\circ, 90^\circ$.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.5.5, Eqs. (8.191)–(8.197), Figs. 8.20–8.28 (described). The water calculations, including the ΔSCF singlet purification $2E_{\rm mixed} - E_{\rm T}$, are in `Claude outputs/part4_response_batchB2.py`, section E. The purification formula is the standard Ziegler–Rauk sum method, not from NRS.
