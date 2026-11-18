---
id: dft-versus-hartree-fock
title: Kohn–Sham DFT versus Hartree–Fock - strengths and failures
summary: KS-DFT costs about as much as Hartree–Fock but includes correlation. Compared directly, with computed examples - atomization energy of H₂O (B3LYP recovers 93% of D₀, HF 59%); orbital energies (−ε_HOMO is 5-6 eV below the ionization energy for LDA/PBE, while ΔSCF works); self-interaction error (H atom, and a stretched H₂⁺ that is 2 eV too stable at 10 bohr); the restricted-to-unrestricted instability of stretched H₂ (3.15 bohr for LSDA, 2.20 bohr for HF); dispersion (no He₂ binding with BLYP or B3LYP); non-variational energies; excited states.
status: in-progress
kind: comparison
level: intermediate
tags: [dft, hartree-fock, self-interaction, koopmans, dispersion, ionization-energy, comparison]
prerequisites: [kohn-sham-dft, exchange-correlation-functionals, rhf, uhf]
related: [koopmans-theorem, h2-dissociation-rhf-uhf, hf-solution-classification, zero-point-energy-and-thermochemistry, electronic-structure-methods-at-a-glance, basis-set-superposition-error]
order: 30
date: 2026-11-17
---

## Same machinery, different physics

The KS operator is the Fock operator with $-\sum_j\hat K_j$ replaced by $v_{xc}$ ([[kohn-sham-dft]]), so a KS calculation is an SCF calculation of the same size. The difference is what the single determinant represents:

| | Hartree–Fock | Kohn–Sham DFT |
|---|---|---|
| determinant | best single-determinant approximation to $\Psi$ | exact density of a fictitious noninteracting system |
| exchange | exact, nonlocal operator | approximate, local potential (plus a fraction of exact exchange in hybrids) |
| correlation | none | approximate, in $E_{xc}$ |
| energy | upper bound (variational) | not an upper bound with approximate $E_{xc}$ |
| systematic improvement | yes (post-HF hierarchy) | no; new functionals must be tested one by one |
| orbital energies | Koopmans: $-\varepsilon_i\approx$ IPs | only $-\varepsilon_{\text{HOMO}}$ = IP, and only for the exact functional |
| self-interaction | cancels exactly ($J_{ii} = K_{ii}$) | cancels only approximately |
| cost | $\hat K$ is the bottleneck | numerical $v_{xc}$ quadrature; pure functionals avoid $\hat K$ entirely |

Both are size-consistent (GGAs included). Spin contamination in unrestricted KS is usually smaller than in UHF.

## Where DFT wins: correlation at mean-field cost

!!! example "Atomization of water (6-31G*, Cartesian $d$)"
    Optimized geometries, analytic harmonic frequencies (unscaled), UHF/UKS atoms:

    | | $D_e$ (eV) | $E_{\text{ZPE}}$ (eV) | $D_0$ (eV) | harmonic wavenumbers (cm$^{-1}$) |
    |---|---:|---:|---:|---|
    | HF | 6.268 | 0.625 | 5.643 | 1826, 4070, 4188 |
    | B3LYP | 9.464 | 0.576 | 8.888 | 1713, 3727, 3849 |
    | experiment (Levine) | | | 9.51 | |

    HF misses 41% of the atomization energy; B3LYP with the same small basis misses 7%, at essentially the same cost. B3LYP harmonic wavenumbers are also much closer to the experimental harmonic values (1649, 3832, 3943 cm$^{-1}$, Levine Fig. 15.16) than HF's ([[harmonic-vibrational-analysis]], [[zero-point-energy-and-thermochemistry]]).

## Where DFT fails

**Orbital energies are not ionization energies.** For approximate functionals $v_{xc}$ decays too fast at large $r$, so the outermost orbital is underbound.

!!! example "Ionization energy of water (aug-cc-pVTZ, B3LYP geometry)"
    | Method | $-\varepsilon_{\text{HOMO}}$ (eV) | $\Delta$SCF IP (eV) |
    |---|---:|---:|
    | HF | 13.88 | 10.97 |
    | LSDA (SVWN5) | 7.39 | 13.17 |
    | PBE | 7.24 | 12.78 |
    | B3LYP | 8.82 | 12.79 |
    | PBE0 | 9.08 | 12.60 |
    | CCSD(T) (vertical, $\Delta$) | | 12.67 |

    - **Orbital energies.** Koopmans' HF value is a fair estimate ([[koopmans-theorem]]), whereas LSDA and PBE HOMO energies are 5-6 eV too high. Exact exchange in the hybrids helps only partly.
    - **Energy differences.** $\Delta$SCF with any functional lands within 0.5 eV of CCSD(T), and HF's $\Delta$SCF is 1.7 eV too low because the cation's correlation is missing.

**Self-interaction.** For a one-electron system the Hartree energy $J[\rho]$ must be cancelled exactly by $E_{xc}$. Approximate functionals do not achieve this.

!!! example "The hydrogen atom and H₂⁺ (one electron)"
    H atom, aug-cc-pV5Z, unrestricted. HF is exact for one electron: $E = -0.499\,995\,E_h$, $J = 0.3125 = 5/16$.

    | Functional | $E$ ($E_h$) | $J + E_{xc}$ ($E_h$; exact 0) |
    |---|---:|---:|
    | LSDA exchange only | −0.457 073 | +0.0413 |
    | LSDA (SVWN5) | −0.478 665 | +0.0203 |
    | BLYP | −0.497 908 | +0.0013 |
    | PBE | −0.499 985 | −0.0006 |
    | B3LYP | −0.502 438 | −0.0028 |

    PBE's near-exact energy is a cancellation of errors. B3LYP lies below the exact energy. For the exact 1s density, LSDA exchange is $-0.2680\,E_h$ against the exact $-0.3125$.

    H₂⁺ dissociation, $E(R) - E(\text{H})$ in eV (aug-cc-pVTZ; HF exact):

    | $R$ (bohr) | 2 | 4 | 6 | 8 | 10 |
    |---|---:|---:|---:|---:|---:|
    | exact (HF) | −2.789 | −1.249 | −0.324 | −0.070 | −0.015 |
    | PBE | −2.970 | −2.177 | −1.944 | −2.075 | −2.219 |
    | B3LYP | −2.927 | −1.996 | −1.634 | −1.699 | −1.808 |

    With PBE and B3LYP the stretched ion is 2 eV too stable and the curve even turns down again, because approximate functionals make a fractionally occupied, delocalized electron too stable: the exact energy is linear in a fractional electron number, while semilocal functionals give a convex curve (delocalization error, the many-electron form of self-interaction error). Symmetric radical cations (He₂⁺, F₂⁺) and charge-transfer complexes suffer the same error.

**Static correlation and symmetry breaking.** Stretched H₂ has the same problem in DFT as in HF ([[h2-dissociation-rhf-uhf]]): the restricted solution dissociates wrongly, and an unrestricted (broken-symmetry) solution appears beyond a critical distance.

!!! example "Where the unrestricted solution appears (H₂, STO-3G)"
    The UHF/UKS solution started from a symmetry-broken guess first falls below the restricted one at $R = 2.20$ bohr for HF and $R = 3.15$ bohr for LSDA. Gunnarsson and Lundqvist found 3.2 bohr for LSDA in a 1s basis (Levine). At 6 bohr the LSDA broken-symmetry solution has $\langle S^2\rangle = 0.997$: an equal mixture of singlet and triplet, with the correct energy of two H atoms but the wrong spin.

**Dispersion.** Semilocal functionals cannot describe London dispersion, which is a correlation between distant electrons.

!!! example "He₂ interaction energy (aug-cc-pVTZ, counterpoise-corrected, $\mu E_h$)"
    | $R$ (bohr) | 4.5 | 5.0 | 5.6 | 6.0 | 7.0 |
    |---|---:|---:|---:|---:|---:|
    | HF | 418 | 125 | 29 | 11 | 0.9 |
    | BLYP | 499 | 239 | 137 | 100 | 41 |
    | B3LYP | 327 | 131 | 73 | 56 | 24 |
    | PBE | 65 | −108 | −100 | −71 | −22 |
    | CCSD(T) | 226 | 18 | −26 | −26 | −13 |

    BLYP and B3LYP give no binding, as Levine states. PBE binds, but about four times too strongly and at too short a distance compared with CCSD(T) in the same basis. Dispersion corrections (DFT-D3, VV10; [[exchange-correlation-functionals]]) are the standard fix.

**Other known weaknesses** (Levine): most functionals give only fair barrier heights (kinetics-fitted ones such as BMK and MPW1K are better); KS-DFT cannot match CCSD(T) where CCSD(T) is affordable; and it is a ground-state theory. Linear-response TDDFT gives vertical excitation energies typically within 0.1-0.5 eV (CIS: 1-2 eV) for valence single excitations, but fails for charge-transfer states and long conjugated chains.

## Practical consequences

- Use DFT for structures, frequencies and reaction energies of large molecules, with a dispersion correction; use wave-function methods to calibrate it on smaller models.
- Report the functional precisely (including the VWN variant for B3LYP), the grid, and the dispersion correction.
- Basis sets: DFT converges faster than correlated wave-function methods; triple-zeta is usually converged, and Pople sets often do better than cc sets of similar size (Levine).
- Treat KS orbital energies, especially virtual ones, as qualitative.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 16.5, pp. 558-572: KS versus Fock operator; Koopmans and the HOMO; LSDA spin-DFT and the Gunnarsson–Lundqvist H₂ result; spin contamination; basis sets; TDDFT; failings (non-variational energy, self-interaction and symmetric radical cations, no systematic improvement, van der Waals: BLYP/B3LYP do not bind He₂, Ne₂; barrier heights). Sec. 15.13 (experimental $D_0$ of water) and Fig. 15.16. Calculations in `part4_dft.py`, sections E-I (PySCF 2.15.1).
