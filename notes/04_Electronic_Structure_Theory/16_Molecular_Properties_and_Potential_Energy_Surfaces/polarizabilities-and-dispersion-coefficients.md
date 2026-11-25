---
id: polarizabilities-and-dispersion-coefficients
title: Polarizabilities and dispersion coefficients - the Unsöld picture, size and conjugation, the two-state model, induction and dispersion energies, and C6 from polarizabilities at imaginary frequencies (Casimir-Polder)
summary: The static polarizability is roughly the dipole variance divided by an average excitation energy (Unsöld), so it grows with molecular size. In a conjugated chain it grows superlinearly (particle in a box, α ∝ L⁴ for fixed n), and a two-state model shows the three levers: smaller gap, larger transition moment, frequency near resonance. Second-order perturbation theory for two separated molecules splits the interaction into induction (classical, from permanent moments and α) and dispersion, which needs both spectra at once. London's average-energy estimate gives C₆ ≈ (3/2)ΔE_AΔE_B/(ΔE_A + ΔE_B)·α_Aα_B. The Casimir-Polder identity makes it exact: C₆ = (3/π)∫α_A(iu)α_B(iu)du, evaluated with a handful of Gauss-Legendre points. Checked: H-H C₆ = 6.49902 from exact oscillator strengths (exact 6.49903), He-He C₆ at TDHF level, and the particle-in-a-box formula, where NRS's Eq. (8.129) has a sign misprint.
status: in-progress
kind: theory
level: intermediate
tags: [polarizability, unsold-approximation, dispersion, c6-coefficient, casimir-polder, london-formula, induction-energy, imaginary-frequency, hyperpolarizability, kerr-effect]
prerequisites: [exact-state-response-functions, damped-response-and-absorption-cross-sections, dispersion-oscillator-strengths-and-sum-rules]
related: [molecular-properties-and-response, linear-response-for-variational-wave-functions, infinite-square-well, stark-effect, basis-set-superposition-error, exchange-correlation-functionals]
conventions: [atomic-units]
key: cp
order: 50
date: 2026-11-24
---

Atomic units ($4\pi\varepsilon_0 = 1$). $\alpha_{\alpha\beta}(-\omega;\omega)$ is the polarizability of [[exact-state-response-functions]]. $\bar\alpha = \tfrac13\mathrm{tr}\,\boldsymbol\alpha$ is the isotropic average, and $f_n$ are oscillator strengths with excitation energies $\omega_n$ ([[dispersion-oscillator-strengths-and-sum-rules]]).

## What sets the size of α

**Unsöld approximation.** Replace every excitation energy in the static sum over states by one average $\Delta E$ and close the sum:

$$
\bar\alpha \approx \frac{2}{3\Delta E}\sum_n{}'|\langle0|\hat{\boldsymbol\mu}|n\rangle|^2 = \frac{2\big(\langle\hat\mu^2\rangle - \langle\hat\mu\rangle^2\big)}{3\Delta E}\ \xrightarrow{\ \text{nonpolar}\ }\ \frac{2\langle r^2\rangle}{3\Delta E}.
\label{unsold}
$$

The polarizability is a dipole *variance* over an energy gap. Larger electron clouds polarize more, which explains the trend gas (F₂, Cl₂) → liquid (Br₂) → solid (I₂) through stronger dispersion forces. For hydrogen ($\langle r^2\rangle = 3$), the exact $\alpha = 9/2$ needs $\Delta E = 4/9\,E_h$. The ionization energy $\tfrac12$, a common choice, gives 4.

**Additivity.** Size dependence suggests $\boldsymbol\alpha\approx\sum_K\boldsymbol\alpha^K$ over atoms. Free-atom values work poorly. *Dressed-atom* values fitted to molecular data reach median errors below 3%, and are smaller than free-atom ones: bonding contracts the density ("minimum polarizability"). NRS show TDHF/aug-cc-pVDZ data for n-alkanes (per-CH₂ contribution nearly constant) and trans-polyenes, where the chain component grows much faster.

**Conjugation: particle in a box.** For an electron in a 1D box of length $L$, $\langle n|x|k\rangle = -8Lnk/[\pi^2(n^2-k^2)^2]$ for $n+k$ odd (zero otherwise). With $E_k-E_n = \pi^2(k^2-n^2)/(2L^2)$,

$$
\alpha_{xx}^{(n)} = \frac{64L^4}{\pi^6}\sum_{k\ne n}\frac{n^2k^2\big[(-1)^{n+k}-1\big]^2}{(k^2-n^2)^5},\qquad \alpha_{xx}^{(1)} = \frac{(15-\pi^2)L^4}{12\pi^4}.
\label{box}
$$

- **Sign misprint in NRS.** NRS's Eq. (8.129) has $(n^2-k^2)^5$ in the denominator, which makes every term negative for $n = 1$.
- **Closed form.** The ground-state value on the right is checked numerically below.
- **Scaling.** At fixed $n$, $\alpha\propto L^4$. In a real chain the occupied quantum number grows with length, which partly cancels this. TDHF polyene data grow roughly as $N^{1.67}$, alkanes nearly linearly: delocalized π electrons behave more like the box.

**Two-state model.**

$$
\alpha_{\alpha\beta}(-\omega;\omega) = \frac{2\omega_{10}}{\omega_{10}^2-\omega^2}\mu^{01}_\alpha\mu^{10}_\beta.
$$

There are three levers: a smaller gap $\omega_{10}$ (longer conjugation), a larger transition moment (donor-acceptor substitution), and $\omega$ closer to resonance (until absorption takes over). The same logic guides the design of large hyperpolarizabilities.

## Intermolecular forces

**Setup.** Two nonoverlapping molecules $A$ and $B$, unperturbed states $|mn\rangle = |m\rangle_A|n\rangle_B$. The perturbation is the Coulomb interaction between the two charge distributions, expanded in multipoles about centres a distance $R$ apart:

$$
\hat H_{\rm int} = \frac{q_Aq_B}{R} + \frac{(q_B\hat\mu^A_\alpha - q_A\hat\mu^B_\alpha)R_\alpha}{R^3} - \frac{(3R_\alpha R_\beta - R^2\delta_{\alpha\beta})\hat\mu^A_\alpha\hat\mu^B_\beta}{R^5} + \cdots
$$

**First order.** $\langle00|\hat H_{\rm int}|00\rangle$ is the electrostatic energy of the permanent moments.

**Second order.** It splits by which molecule is excited:

$$
E^{(2)} = E^A_{\rm ind} + E^B_{\rm ind} + E_{\rm disp},\qquad
E^B_{\rm ind} = -\tfrac12F^A_\alpha(B)\,\alpha^B_{\alpha\beta}(0)\,F^A_\beta(B),\qquad
E_{\rm disp} = -\sum_{m\ne0,n\ne0}\frac{|\langle00|\hat H_{\rm int}|mn\rangle|^2}{\omega^A_m + \omega^B_n}.
$$

- **Induction.** $F^A(B)$ is the field of $A$'s permanent charge and dipole at $B$. This is a classical energy, $-\tfrac12\mathbf F\cdot\boldsymbol\mu_{\rm ind}$, with only $\alpha$ quantum mechanical. It decays as $R^{-4}$ for a charge and $R^{-6}$ for a dipole.
- **Dispersion.** Both molecules are excited at once. It exists between nonpolar molecules and has no classical analogue: the correlated fluctuations of two dipoles.

**Dispersion with the dipole-dipole term.** For atoms or freely rotating molecules the angular factors average to

$$
E_{\rm disp} = -\frac{C_6}{R^6},\qquad C_6 = \frac32\sum_{m,n}{}'\frac{f^A_mf^B_n}{\omega^A_m\omega^B_n(\omega^A_m+\omega^B_n)}.
\label{c6sos}
$$

The joint denominator $\omega^A_m+\omega^B_n$ prevents writing this as a product of single-molecule properties.

**London's estimate.** With one average excitation energy per molecule, $1/(\omega_m+\omega_n)\to1/(\Delta E_A+\Delta E_B)$ and the sums give polarizabilities:

$$
C_6\approx\frac32\frac{\Delta E_A\Delta E_B}{\Delta E_A+\Delta E_B}\,\alpha_A\alpha_B.
$$

This is accurate only if $\Delta E$ is chosen well. With ionization energies, it overestimates H-H ($7.59$ against $6.50$).

**Casimir-Polder: exact factorization.** The identity

$$
\frac1{a+b} = \frac2\pi\int_0^\infty\frac{ab}{(a^2+u^2)(b^2+u^2)}\,du\qquad(a,b>0)
$$

separates the denominator. Each factor $\sum_m f_m/(\omega_m^2+u^2)$ is the polarizability at the **imaginary frequency** $iu$ (the damped polarizability of [[damped-response-and-absorption-cross-sections]] at $\omega = 0$ with damping $u$):

$$
C_6 = \frac3\pi\int_0^\infty\bar\alpha_A(iu)\,\bar\alpha_B(iu)\,du,\qquad \bar\alpha(iu) = \sum_n{}'\frac{f_n}{\omega_n^2+u^2}.
\label{cp}
$$

**Why it works in practice.**

- $\bar\alpha(iu)$ is real, positive, smooth and monotonically decreasing (no poles on the imaginary axis).
- A Gauss-Legendre rule after mapping $u\in[0,\infty)$ to $(-1,1)$ converges in about 8-10 points. NRS show the same for benzene at B3LYP level.
- Each point is one complex linear-response solve, with no excited states needed.
- This is how $C_6$ coefficients for dispersion corrections are computed from first principles.
- Higher terms $C_8$, $C_{10}$ come from multipole polarizabilities in the same way.

## Nonlinear polarizabilities with static fields

**Orientational terms.** In processes involving a static field (Pockels, Kerr, field-induced SHG), dipolar molecules in a sample partly align along the field. That adds orientational terms with $1/kT$ to the molecular hyperpolarizabilities. For field-induced SHG, NRS Eq. (8.146) gives

$$
\chi_{\rm NL} = \frac{\mathcal N}{15}\left\{\frac{\mu_\alpha\beta_\alpha(-2\omega;\omega,\omega)}{kT} + \big[2\gamma_{\alpha\alpha\beta\beta} + \gamma_{\alpha\beta\beta\alpha}\big](-2\omega;\omega,\omega,0)\right\},
$$

with $\mathcal N$ the number density and $\beta_\alpha = \sum_\beta(\beta_{\alpha\beta\beta}+\beta_{\beta\alpha\beta}+\beta_{\beta\beta\alpha})$ the vector part of $\beta$. Plotting against $1/kT$ separates $\mu\beta$ (slope) from $\gamma$ (intercept).

**Kerr constant.** It has terms in $1/kT$ and $1/(kT)^2$ built from $\gamma$, $\mu\beta$, the anisotropies of $\alpha(\omega)$ and $\alpha(0)$, and $\alpha(\omega)\mu\mu$ (NRS Eq. 8.147).

## Worked examples

!!! example "Hydrogen: α, Unsöld and C₆ from exact oscillator strengths (computed for this note)"
    Oscillator strengths from the radial-grid calculation of [[dispersion-oscillator-strengths-and-sum-rules]] (200-bohr box, 4000 and 8000 points, Richardson in $h^2$).

    | | 4000 pts | 8000 pts | extrapolated | exact |
    |---|---:|---:|---:|---:|
    | $\alpha$ | 4.50854 | 4.50214 | 4.50000 | 9/2 |
    | $C_6$(H-H), double sum Eq. [[#c6sos]] | 6.51710 | 6.50354 | 6.49902 | 6.49903 |

    - **Casimir-Polder quadrature.** Eq. [[#cp]] on the 8000-point grid with $u = 0.3(1+t)/(1-t)$ gives 6.469877 (4 points), 6.502918 (6), and 6.503545 (8, 10, 12, 16). That is the double-sum value to $10^{-6}$ with 8 points.
    - **Unsöld and London.** The Unsöld $\Delta E$ reproducing $\alpha$ is $4/9$. London's formula gives $\tfrac34\Delta E\alpha^2 = 6.750$ with it, and 7.594 with $\Delta E = $ IP.

!!! example "Helium, TDHF/aug-cc-pVTZ (computed for this note)"
    All TDHF roots from the Hermitian form $(\mathbf A-\mathbf B)^{1/2}(\mathbf A+\mathbf B)(\mathbf A-\mathbf B)^{1/2}$, with oscillator strengths from the length form.

    - **Sums.** $\sum f = 1.9992$ (TRK: 2) and $\alpha(0) = 1.3160$.
    - **C₆.** $C_6$(He-He) $= 1.377$ (12-point quadrature).
    - **Comparison.** The accurate correlated $C_6$ for He-He is about 1.46 (literature value, to verify). TDHF misses most of the correlation contribution, as it does for $\alpha$.

!!! example "Particle in a box (computed for this note)"
    Ground state ($n = 1$), $L = 4$ bohr: Eq. [[#box]] (sum to $k = 4000$) gives 1.12360. The sum over states with explicit matrix elements gives 1.12360, and the exact field derivative of the lowest eigenvalue on a 4000-point grid gives 1.12356. The closed form $(15-\pi^2)L^4/(12\pi^4) = 1.12360$; at $L = 8$ it is $16\times$ larger, 17.97753.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.3.1, Eqs. (8.123)–(8.130), Figs. 8.7–8.8 (described); Sec. 8.3.1.1, Eqs. (8.131)–(8.145), Fig. 8.9 (described); Sec. 8.3.2, Eqs. (8.146)–(8.147). The ground-state box closed form and the sign correction of Eq. (8.129) were established numerically here. The exact H-H value 6.49903 is the standard literature value (Pauling and Beach) and was reproduced to $10^{-5}$ above. The calculations are in `Claude outputs/part4_response_batchB1.py`, section A.
