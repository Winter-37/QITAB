---
id: harmonic-vibrational-analysis
title: Harmonic vibrational analysis - normal modes from the Hessian
summary: Harmonic frequencies of a polyatomic molecule are the square roots of the eigenvalues of the mass-weighted Cartesian Hessian at a stationary point, ν̃ = 5140.487√λ cm⁻¹ for λ in E_h a₀⁻² u⁻¹. The six (five) translational and rotational modes are projected out; imaginary frequencies mark saddle points; harmonic frequencies exceed observed fundamentals, which is why scale factors are used. Worked example: H₂O at HF/6-31G*, reproducing Levine's 1826, 4070, 4188 cm⁻¹ and his scaled values.
status: in-progress
kind: algorithm
level: intermediate
tags: [vibrational-frequencies, normal-modes, hessian, mass-weighted, scale-factors, infrared]
prerequisites: [geometry-optimization, analytic-gradients-and-force-constants, diatomic-vibration-and-anharmonicity]
related: [rhf-analytic-hessian, zero-point-energy-and-thermochemistry, stationary-points-and-reaction-paths, energy-and-unit-conversions, matrix-eigenvalue-problem]
order: 30
date: 2026-11-17
---

## Normal modes

Near a minimum $\mathbf X_e$ of the Born–Oppenheimer surface, expand the energy to second order in the $3N$ Cartesian displacements $\xi_i = X_i - X_{e,i}$:

$$
U \approx U_e + \tfrac12\sum_{ij}H_{ij}\xi_i\xi_j,\qquad H_{ij} = \Big(\frac{\partial^2U}{\partial X_i\partial X_j}\Big)_e ,
$$

the linear term vanishing at a stationary point. The kinetic energy is $\tfrac12\sum_im_i\dot\xi_i^2$. In **mass-weighted coordinates** $q_i = \sqrt{m_i}\,\xi_i$ both become simple,

$$
T = \tfrac12\sum_i\dot q_i^2,\qquad U - U_e = \tfrac12\sum_{ij}F_{ij}q_iq_j,\qquad F_{ij} = \frac{H_{ij}}{\sqrt{m_im_j}},
$$

and an orthogonal transformation $Q_k = \sum_iL_{ik}q_i$ that diagonalizes $\mathbf F$,

$$
\mathbf F\mathbf L_k = \lambda_k\mathbf L_k ,
$$

separates the motion into $3N$ independent oscillators $\ddot Q_k = -\lambda_kQ_k$. Each $Q_k$ is a **normal coordinate** with harmonic frequency

$$
\nu_k = \frac{\sqrt{\lambda_k}}{2\pi},\qquad \tilde\nu_k = \frac{\sqrt{\lambda_k}}{2\pi c} .
$$

With $\lambda$ in $E_h\,a_0^{-2}\,\mathrm u^{-1}$, as a program returns it, $\tilde\nu = 5140.487\sqrt\lambda$ cm$^{-1}$ ([[energy-and-unit-conversions]]). In the harmonic approximation the vibrational energy is $\sum_k(v_k + \tfrac12)h\nu_k$ with independent $v_k = 0,1,2,\dots$

**Amplitudes.** In mode $k$ the Cartesian displacement of coordinate $i$ is proportional to $L_{ik}/\sqrt{m_i}$, so light atoms move more. In a diatomic the amplitudes are inversely proportional to the masses: in HF the H atom moves 19 times as far as F, in the opposite direction.

## Translations and rotations

Six eigenvalues of $\mathbf F$ (five for a linear molecule) are zero, because uniform translation and infinitesimal rotation do not change $U$. In mass-weighted coordinates these modes are spanned by

$$
\mathbf t_\alpha:\ (\mathbf t_\alpha)_{a\beta} = \sqrt{m_a}\,\delta_{\alpha\beta},\qquad
\mathbf r_\alpha:\ (\mathbf r_\alpha)_{a} = \sqrt{m_a}\,\big(\mathbf e_\alpha\times(\mathbf R_a - \mathbf R_{\text{cm}})\big),
$$

for atom $a$ and axis $\alpha$. Numerically the six eigenvalues come out small but nonzero (a few cm$^{-1}$, real or imaginary), because the geometry is not exactly stationary and the Hessian is computed to finite precision. The clean procedure is to orthonormalize these six vectors, form the projector $\mathbf P = \mathbf 1 - \sum\mathbf d\mathbf d^{\mathsf T}$, and diagonalize $\mathbf{PFP}$; the remaining $3N - 6$ eigenvalues are the vibrations.

## Reading the result

1. **Only at a stationary point.** Away from $\nabla U = 0$ the "frequencies" are not vibrational frequencies (the gradient term was dropped). Optimize with the same method and basis first.
2. **Character of the stationary point.** All $\lambda_k > 0$: a minimum. One negative eigenvalue (one imaginary frequency, printed as $i\tilde\nu$ or as a negative number): a first-order saddle point, a transition-state candidate. Two or more: a higher-order saddle point ([[stationary-points-and-reaction-paths]]).
3. **Harmonic versus fundamental.** Observed IR bands are fundamentals ($0\to1$), lower than harmonic frequencies by the anharmonicity ([[diatomic-vibration-and-anharmonicity]]). Hartree–Fock harmonic frequencies are typically several percent above observed harmonic frequencies as well, so both errors push the same way.
4. **Scale factors.** Multiplying computed harmonic frequencies by an empirical factor estimates fundamentals. For HF/6-31G* Levine quotes 0.895 (Scott and Radom, *J. Phys. Chem.* **100**, 16502 (1996)), with separate factors recommended for frequencies, zero-point energies and thermodynamic functions.

## Worked example

!!! example "Water at HF/6-31G*"
    Geometry optimized with PySCF and geomeTRIC (Cartesian $d$ functions, as in Gaussian's 6-31G*), analytic RHF Hessian, average atomic masses (O 15.999, H 1.008 u).

    - **Geometry.** $U_e = -76.010\,747\,E_h$ (Levine: $-76.010\,746$); $r(\text{OH}) = 0.9473$ Å, $\angle\text{HOH} = 105.50°$.
    - **Unprojected $\mathbf F$.** Nine eigenvalues; six correspond to $-1.3$, 0, 0, 0, 2.7 and 3.4 cm$^{-1}$ (translations and rotations), three to the vibrations.

    | Mode | HF/6-31G* harmonic | × 0.895 | Levine (scaled) | Expt. harmonic | Expt. fundamental |
    |---|---:|---:|---:|---:|---:|
    | bend $\nu_2$ | 1826.4 | 1635 | 1634 | 1649 | 1595 |
    | sym. stretch $\nu_1$ | 4070.1 | 3643 | 3643 | 3832 | 3657 |
    | asym. stretch $\nu_3$ | 4188.3 | 3749 | 3748 | 3943 | 3756 |

    (cm$^{-1}$; experimental values from Levine Fig. 15.16.) The unscaled HF values exceed the experimental harmonic ones by 6-11%, and the scaled values are within 3% of the fundamentals.

    The projected-Hessian diagonalization written for this note and PySCF's `thermo.harmonic_analysis` agree to $4\times10^{-6}$ cm$^{-1}$.

## Implementation

```python
from pyscf import gto, scf
from pyscf.geomopt.geometric_solver import optimize
from pyscf.hessian import thermo

mol = gto.M(atom="O 0 0 0.12; H 0 0.76 -0.47; H 0 -0.76 -0.47", basis="6-31g*", cart=True)
mol_eq = optimize(scf.RHF(mol))
mf = scf.RHF(mol_eq).run()
freq = thermo.harmonic_analysis(mol_eq, mf.Hessian().kernel())
print(freq["freq_wavenumber"])    # imaginary modes come out as complex numbers
```

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.12, pp. 496-498, Eqs. (15.74)-(15.77), Fig. 15.16 (experimental harmonic and fundamental wavenumbers of H₂O) and the HF/6-31G* water values and 0.895 scale factor; Sec. 15.13, p. 499 (HF/6-31G* water energy). The projection of translations and rotations is standard (not derived in Levine). Calculations in `part3_batchA.py`, section D (PySCF 2.15.1, geomeTRIC 1.1.1).
