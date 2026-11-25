---
id: multiphoton-absorption
title: Multiphoton absorption - j-photon cross sections from residues, rotational averages, two- and three-state models for TPA, and parity rules for higher orders
summary: Simultaneous absorption of j photons is governed by the j-photon transition moment, the single residue of the jth-order response function. For randomly oriented molecules, rotational averaging turns the squared moments into the invariants of NRS Table 8.7, and the cross section scales as the product of photon frequencies times a line shape. Few-state models explain what makes a strong two-photon absorber (a large change of dipole moment along a bright transition, or a bright intermediate state near half the excitation energy). For centrosymmetric molecules, odd- and even-order processes reach u and g states respectively and are proportional to OPA and TPA, scaled by the excited-state polarizability. Recomputed: the Table 8.7 averages by Monte Carlo, the two-state angular factor, and 1 GM in atomic units.
status: in-progress
kind: theory
level: advanced
tags: [two-photon-absorption, multiphoton-absorption, tpa, goppert-mayer, rotational-average, few-state-model, quadratic-response, residue]
prerequisites: [residue-analysis-of-response-functions, electronic-absorption-and-emission]
related: [damped-response-and-absorption-cross-sections, exact-state-response-functions, raman-scattering, polarizabilities-and-dispersion-coefficients, rotations-su2-so3-and-euler-angles]
conventions: [atomic-units]
key: sigma-j
order: 120
date: 2026-11-24
---

Atomic units unless stated. $|0\rangle$ is the ground state and $|f\rangle$ the final state, with $\omega_{f0} = E_f - E_0$. The photon frequencies $\omega_1,\dots,\omega_j$ sum to $\omega_\sigma = \sum_k\omega_k$. $M^{(j)}_{0f,\alpha\beta\dots}$ is the $j$-photon transition moment, with one Cartesian index per photon. $\Delta\boldsymbol\mu = \boldsymbol\mu_f - \boldsymbol\mu_0$ is the change of the permanent dipole on excitation.

## Why multiphoton absorption

Göppert-Mayer predicted two-photon absorption (TPA) in her 1931 thesis; it was observed only with lasers in the early 1960s. The rate is quadratic in intensity, which gives the technique its four uses (NRS Sec. 8.5.4):

- **Biological imaging.** Near-infrared photons reach states that would otherwise need UV, so light penetrates deeper into tissue with less damage.
- **Focality.** Absorption is confined to the focal volume, where the intensity is high.
- **Photodynamic therapy.** Long-wavelength light excites reactive states.
- **Dark states.** States forbidden in one-photon absorption (OPA) become accessible.

**Selection rules by symmetry.** One photon transforms as $(x,y,z)$, two photons as the symmetric products $x^2, y^2, z^2, xy, xz, yz$, three photons as their products. In ethylene ($D_{2h}$), OPA reaches only $B_{1u}, B_{2u}, B_{3u}$; TPA reaches $A_g$ and the $B_{\cdot g}$ states. $A_u$ is dark to both and needs three photons polarized along $x$, $y$ and $z$.

## Cross sections

**Intensity expansion.** Absorption at intensity $I$ (NRS Eq. 8.172) is

$$
\sigma(\omega) = \sigma^{(1)}(\omega) + \sigma^{(2)}(\omega)I + \sigma^{(3)}(\omega)I^2 + \cdots,
$$

so $\sigma^{(j)}$ has SI units $\mathrm m^{2j}\,\mathrm s^{j-1}\,\mathrm J^{1-j}$. The conventional TPA unit is the Göppert-Mayer, $1\ \mathrm{GM} = 10^{-50}\ \mathrm{cm^4\,s\,photon^{-1}}$.

**Transition moments as residues.** As shown in [[residue-analysis-of-response-functions]], the two-photon moment is a single residue of the quadratic response function, and generally the $j$-photon moment is a single residue of the $j$th-order response function. Summing over intermediate states $n$, the two-photon moment is

$$
M^{(2)}_{0f,\alpha\beta} = \sum_n\left[\frac{\langle0|\hat\mu_\alpha|n\rangle\langle n|\hat\mu_\beta|f\rangle}{\omega_{n0} - \omega_1} + \frac{\langle0|\hat\mu_\beta|n\rangle\langle n|\hat\mu_\alpha|f\rangle}{\omega_{n0} - \omega_2}\right],\qquad \omega_1 + \omega_2 = \omega_{f0}.
\label{m2}
$$

The sum includes $n = 0$ and $n = f$, which enter through $\Delta\boldsymbol\mu$.

**Alternative route.** The $j$-photon absorption is also the imaginary part of a damped response function of order $2j-1$ ([[damped-response-and-absorption-cross-sections]]). For $j = 2$ this is the cubic response function, the imaginary part of $\gamma(-\omega;\omega,\omega,-\omega)$.

**Cross section.** With a normalized line shape $g(\omega_\sigma)$ (NRS Eqs. 8.173–8.177):

$$
\sigma^{j\rm PA} = (2\pi)^{j+1}\Big(\frac{e^2}{\hbar c}\Big)^j\Big[\prod_{i=1}^j\omega_i\Big]g(\omega_\sigma)\,\langle\delta^{j\rm PA}\rangle .
\label{sigma-j}
$$

For a single beam with all photons of energy $\omega = \omega_{f0}/j$, the photon loss rate is $j$ times the transition rate, which adds a factor $j$. The single-beam TPA cross section in cgs units is then $\sigma^{\rm TPA} = (4\pi^3\alpha a_0^5\omega^2/c)\langle\delta^{\rm TPA}\rangle g(\omega)$.

**Conversion pitfalls.** Published TPA values differ by factors of 2, 4 and $2\pi$ from these conventions: single or double beam, Lorentzian peak height $1/\pi\Gamma$ or another normalization, and $\Gamma$ as HWHM or FWHM. Beerepoot et al. (2015, cited by NRS) tabulate the conversions.

## Rotational averages

**Why averaging is needed.** In a liquid or gas the molecule-fixed moment must be projected on the lab polarization vectors $\mathbf e$ and averaged over orientations, $\langle|\sum M_{\alpha\beta\dots}e_\alpha e_\beta\cdots|^2\rangle$.

**Invariants.** For linearly polarized, parallel photons, the isotropic tensor averages of [[rotations-su2-so3-and-euler-angles]] give the invariants of NRS Table 8.7. Bars denote complex conjugates for variational methods; for nonvariational methods (CC), the left and right moments are used instead.

$$
\begin{aligned}
\langle\delta^{\rm OPA}\rangle &= \tfrac13\textstyle\sum_\alpha M_\alpha\bar M_\alpha,\\
\langle\delta^{\rm TPA}\rangle &= \tfrac1{15}\textstyle\sum_{\alpha\beta}\big(2M_{\alpha\beta}\bar M_{\alpha\beta} + M_{\alpha\alpha}\bar M_{\beta\beta}\big),\\
\langle\delta^{\rm 3PA}\rangle &= \tfrac1{35}\textstyle\sum_{\alpha\beta\gamma}\big(2M_{\alpha\beta\gamma}\bar M_{\alpha\beta\gamma} + 3M_{\alpha\alpha\beta}\bar M_{\beta\gamma\gamma}\big),\\
\langle\delta^{\rm 4PA}\rangle &= \tfrac1{315}\textstyle\sum\big(8M_{\alpha\beta\gamma\delta}\bar M_{\alpha\beta\gamma\delta} + 24M_{\alpha\alpha\beta\gamma}\bar M_{\beta\gamma\delta\delta} + 3M_{\alpha\alpha\beta\beta}\bar M_{\gamma\gamma\delta\delta}\big).
\end{aligned}
\label{avg}
$$

These hold for moments symmetric in their indices, as in the degenerate case $\omega_1 = \cdots = \omega_j$. Circular polarization and nonparallel beams give other combinations, and the ratio of circular to linear TPA identifies the symmetry of the final state.

## Few-state models for TPA

**Two-state model** (only $n = 0$ and $n = f$ in Eq. [[#m2]], degenerate photons $\omega = \omega_{f0}/2$; NRS Eq. 8.178):

$$
M^{(2)}_{0f,\alpha\beta} = \frac{2}{\omega_{f0}}\big(\mu^{0f}_\alpha\Delta\mu_\beta + \mu^{0f}_\beta\Delta\mu_\alpha\big)
\;\Rightarrow\;
\langle\delta^{\rm TPA}\rangle = \frac{16}{15\,\omega_{f0}^2}|\boldsymbol\mu_{0f}|^2|\Delta\boldsymbol\mu|^2\big(1 + 2\cos^2\theta\big),
\label{twostate}
$$

with $\theta$ the angle between $\boldsymbol\mu_{0f}$ and $\Delta\boldsymbol\mu$.

- **No dispersion.** The cross section $\propto\omega^2\langle\delta\rangle$ is independent of the photon frequency, as for OPA.
- **Design rules.** A strong two-state TPA needs a bright, charge-transfer transition ($|\boldsymbol\mu_{0f}|$ and $|\Delta\boldsymbol\mu|$ both large) with the two vectors parallel ($\theta = 0$ triples the value at $90^\circ$). This is the donor–π–acceptor design rule.
- **A trade-off.** A longer conjugated bridge increases $|\Delta\mu|$ but reduces orbital overlap and hence $|\mu_{0f}|$.
- **Limits.** The model is useless for centrosymmetric molecules, where $\Delta\boldsymbol\mu = 0$.

**Three-state model** (one intermediate $i$, NRS Eq. 8.180):

$$
M^{(2)}_{0f,\alpha\beta} = \frac{\mu^{0i}_\alpha\mu^{if}_\beta + \mu^{0i}_\beta\mu^{if}_\alpha}{\omega_{i0} - \omega_{f0}/2}
\;\Rightarrow\;
\langle\delta^{\rm TPA}\rangle = \frac{4}{15}\,\frac{|\boldsymbol\mu_{0i}|^2|\boldsymbol\mu_{if}|^2(1 + 2\cos^2\vartheta)}{(\omega_{i0} - \omega_{f0}/2)^2}.
\label{threestate}
$$

- **Dark final states.** Dipole-forbidden final states are reached through a bright intermediate state.
- **Resonance enhancement.** The cross section is enhanced when $\omega_{i0}$ approaches $\omega_{f0}/2$. Near that point the undamped residue diverges, and the finite lifetime of $|i\rangle$ must be included through damped (complex polarization propagator) response.

**Two discrepancies with NRS (my derivation; to verify).**

- **Eq. 8.179.** Inserting Eq. [[#twostate]] into the single-beam formula gives $\sigma = \frac{16\pi^3\alpha a_0^5}{15c}\frac{1}{\pi\Gamma}|\mu_{0f}|^2|\Delta\mu|^2(1+2\cos^2\theta)$. NRS Eq. 8.179 prints the prefactor without the $\tfrac1{15}$ of Table 8.7.
- **Eq. 8.181.** In the three-state cross section, NRS Eq. 8.181 shows the denominator $(\omega_{i0} - \omega_{f0}/2)$ to the first power. Squaring the transition moment gives the second power.

## Higher orders in centrosymmetric molecules

For a closed-shell centrosymmetric molecule the ground state is $g$. Dipole steps alternate $g\to u\to g\to\cdots$, so odd-order processes reach $u$ states and even-order processes reach $g$ states (NRS Eqs. 8.182–8.190).

**Odd orders.** Keep only the final state $f$ (assumed bright and isolated) among the $u$ intermediates. Then $M^{(3)}\approx M^{(1)}_{0f}\times\alpha_f$, where

$$
\alpha_f(\Omega) = \sum_l\frac{\langle f|\hat\mu|l\rangle\langle l|\hat\mu|f\rangle}{\omega_{l0} - \Omega}
$$

is an excited-state polarizability over $g$ states $l$, evaluated at the partial photon sum $\Omega$. Three-photon absorption is then OPA modulated by the excited-state polarizability, and it is enhanced when a $g$ state lies at two thirds of $\omega_{f0}$. Five-photon absorption is OPA times $\alpha_f^2$, or 3PA times $\alpha_f$ for one-photon-dark $u$ states (such as $A_u$ in $D_{2h}$).

**Even orders.** In the same way, 4PA ≈ TPA × excited-state polarizability over $u$ states, enhanced by a $u$ state at three quarters of $\omega_{f0}$.

**Example (described).** NRS show CAM-B3LYP/aug-cc-pVDZ one- to five-photon cross sections of *para*-dinitrobenzene (Fig. 8.19).

- **Two groups of states.** States 6–7 and 11–12 ($B_{2u}$, $B_{3u}$) are strong in odd orders; states 9–10 ($B_{1g}$, $A_g$) are strong in even orders.
- **An enhanced 4PA state.** State 10 ($2B_{1g}$, 6.20 eV) has only a moderate TPA but a strongly enhanced 4PA. The $B_{2u}$ state 5 at 4.62 eV sits near $\tfrac34\times6.20 = 4.65$ eV, the resonance the rule predicts.

## Worked example

!!! example "Checks of the formulas (recomputed for this note)"
    **Table 8.7 by Monte Carlo.** For random fully symmetric real tensors $M$ of rank 2, 3 and 4, I averaged $|M_{\alpha\beta\dots}e_\alpha e_\beta\cdots|^2$ over $2\times10^5$ uniformly random orientations of the lab $z$ axis and compared with Eq. [[#avg]]:

    | rank | Monte Carlo | formula |
    |---:|---:|---:|
    | 2 | 0.15393 | 0.15399 |
    | 3 | 1.52584 | 1.52657 |
    | 4 | 0.32063 | 0.32052 |

    The agreement is within the sampling error ($\sim10^{-3}$ relative).

    **Two-state angular factor.** With $M_{\alpha\beta} = u_\alpha v_\beta + u_\beta v_\alpha$ and unit vectors at angle $\theta$, Table 8.7 gives $\langle\delta\rangle = 0.80000, 0.53333, 0.26667$ for $\theta = 0^\circ, 45^\circ, 90^\circ$. This equals $\tfrac4{15}(1+2\cos^2\theta)$ exactly, the factor in Eq. [[#twostate]].

    **Unit.** $1\ \mathrm{GM} = 10^{-50}\ \mathrm{cm^4\,s} = 0.5272\ a_0^4\,t_{\rm au}$, with $a_0 = 5.2918\times10^{-9}$ cm and $t_{\rm au} = 2.4189\times10^{-17}$ s.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.5.4, Eqs. (8.172)–(8.190), Table 8.7, Fig. 8.19 (described). D. H. Friese, M. T. P. Beerepoot, and K. Ruud, *J. Chem. Phys.* **141**, 204103 (2014), and M. T. P. Beerepoot, D. H. Friese, N. H. List, J. Kongsted, and K. Ruud, *Phys. Chem. Chem. Phys.* **17**, 19306 (2015), both as cited by NRS (not read). The ratio of circular to linear TPA as a symmetry probe is general knowledge, not from NRS. The calculations are in `Claude outputs/part4_response_batchB2.py`, section D.
