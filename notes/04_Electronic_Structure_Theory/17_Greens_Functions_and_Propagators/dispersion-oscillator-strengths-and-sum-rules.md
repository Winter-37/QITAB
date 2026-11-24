---
id: dispersion-oscillator-strengths-and-sum-rules
title: Dispersion, oscillator strengths and sum rules - nonlinear optical processes, Cauchy moments, the universal dispersion of hyperpolarizabilities, and the Thomas-Reiche-Kuhn sum rule
summary: Which nonlinear optical process a hyperpolarizability describes is fixed by its frequency arguments; the factors K that relate the induced polarization amplitudes to β and γ follow from expanding the dipole in a static-plus-cosine field. Below the first excitation the polarizability is a power series in ω² whose coefficients are the Cauchy moments S(−2k−2) of the oscillator-strength distribution. To second order in the frequencies, β and γ depend on the process only through ω_L² = Σ ω_k², so one fit predicts all processes. The oscillator strength is the dimensionless transition strength. Its sum over all transitions equals the number of electrons (TRK), and S(−1), S(1) and S(−2) are ground-state expectation values or the static polarizability. Hydrogen Cauchy moments recomputed on a radial grid.
status: in-progress
kind: theory
level: advanced
tags: [dispersion, cauchy-moments, oscillator-strength, sum-rules, thomas-reiche-kuhn, hyperpolarizability, nonlinear-optics, second-harmonic-generation]
prerequisites: [exact-state-response-functions, emission-absorption-and-spontaneous-emission]
related: [polarization-propagator-rpa, stark-effect, residue-analysis-of-response-functions, damped-response-and-absorption-cross-sections, hydrogen-atom]
conventions: [atomic-units]
key: cauchy
order: 70
date: 2026-11-24
---

Atomic units. $\alpha$, $\beta$, $\gamma$ as defined in [[exact-state-response-functions]]; $\omega_{n0}$ excitation energies; $\mathbf R = \sum_i\mathbf r_i$ and $\mathbf P = \sum_i\mathbf p_i$ the total electronic position and momentum, so the electronic dipole is $\hat{\boldsymbol\mu} = -\mathbf R$.

## Which process: frequency arguments and the factors K

**A static plus an optical field.** For $F(t) = F^0 + F^\omega\cos\omega t$, expanding $\mu(t) = \mu^0 + \alpha F + \tfrac12\beta F^2 + \tfrac16\gamma F^3$ and using $\cos u\cos v = \tfrac12[\cos(u+v)+\cos(u-v)]$ sorts the induced dipole into components at $0, \omega, 2\omega, 3\omega$. Each component multiplies a $\beta$ or $\gamma$ with specific frequency arguments. Writing each amplitude as $\tfrac12K^{(2)}\beta F F$ or $\tfrac16K^{(3)}\gamma FFF$ defines factors that make every process reduce to the same static value:

| Process | Arguments | $K$ | $\omega_L^2$ |
|---|---|---:|---:|
| optical rectification | $\beta(0;\omega,-\omega)$ | 1/2 | $2\omega^2$ |
| Pockels effect | $\beta(-\omega;\omega,0)$ | 2 | $2\omega^2$ |
| second-harmonic generation | $\beta(-2\omega;\omega,\omega)$ | 1/2 | $6\omega^2$ |
| dc optical rectification | $\gamma(0;\omega,-\omega,0)$ | 3/2 | $2\omega^2$ |
| Kerr effect | $\gamma(-\omega;\omega,0,0)$ | 3 | $2\omega^2$ |
| intensity-dependent refractive index | $\gamma(-\omega;\omega,-\omega,\omega)$ | 3/4 | $4\omega^2$ |
| field-induced SHG | $\gamma(-2\omega;\omega,\omega,0)$ | 3/2 | $6\omega^2$ |
| third-harmonic generation | $\gamma(-3\omega;\omega,\omega,\omega)$ | 1/4 | $12\omega^2$ |

The last column is used below. Example: the $2\omega$ amplitude of $\tfrac12\beta F^2$ is $\tfrac14\beta(-2\omega;\omega,\omega)(F^\omega)^2$, so $K = \tfrac12$.

## Cauchy moments of the polarizability

**Series.** For real wave functions both terms of the polarizability have the same numerator, and

$$
\alpha_{\alpha\beta}(-\omega;\omega) = \sum_n{}'\frac{f^{\alpha\beta}_{n0}}{\omega_{n0}^2-\omega^2},\qquad f^{\alpha\beta}_{n0} = 2\omega_{n0}\langle0|\hat\mu_\alpha|n\rangle\langle n|\hat\mu_\beta|0\rangle.
$$

Expanding $1/(1-\omega^2/\omega_{n0}^2)$ geometrically (convergent below the first excitation energy),

$$
\alpha_{\alpha\beta}(-\omega;\omega) = \sum_{k=0}^\infty\omega^{2k}S(-2k-2),\qquad S(-k) = \sum_n{}'\frac{f^{\alpha\beta}_{n0}}{\omega_{n0}^k}.
\label{cauchy}
$$

The Cauchy moments $S(-k)$ are frequency independent. Only even powers of $\omega$ appear. For diagonal components all $S$ are positive, so $\alpha_{\alpha\alpha}$ rises with frequency below the first resonance (normal dispersion).

## Oscillator strengths

**Definition.** Comparing with the classical Lorentz oscillator, where $\alpha = \sum_i(e^2f_i/m)/(\omega_i^2-\omega^2)$ counts $f_i$ oscillators per resonance, gives the dimensionless oscillator strength. For a rotationally averaged sample:

$$
f_{n0} = \tfrac23\omega_{n0}\,|\langle0|\mathbf R|n\rangle|^2.
\label{f}
$$

**Length, velocity and mixed forms.** In a complete basis, $[\mathbf R,\hat H] = i\mathbf P$ gives $\omega_{n0}\langle0|\mathbf R|n\rangle = i\langle0|\mathbf P|n\rangle$. Hence

$$
f_{n0} = \frac{2}{3\omega_{n0}}|\langle0|\mathbf P|n\rangle|^2 = \tfrac{i}{3}\big[\langle0|\mathbf P|n\rangle\cdot\langle n|\mathbf R|0\rangle - \langle0|\mathbf R|n\rangle\cdot\langle n|\mathbf P|0\rangle\big].
$$

The three forms agree only in a complete basis, or for methods that keep the commutator relation (TDHF; [[polarization-propagator-rpa]]).

**Sum rules.** Each moment of the oscillator-strength distribution with $k = 1, 0, -1$ reduces, by completeness, to a ground-state quantity. Write $S(k) = \sum'_nf_{n0}\omega_{n0}^k$ (isotropic).

- **TRK, $k = 0$.** Use the mixed form, extend the sum to $n = 0$ (whose term vanishes), and close it:

$$
S(0) = \tfrac i3\langle0|\mathbf P\cdot\mathbf R - \mathbf R\cdot\mathbf P|0\rangle = \tfrac i3\sum_\alpha\langle0|[P_\alpha,R_\alpha]|0\rangle = N.
\label{trk}
$$

  Here $[P_\alpha,R_\alpha] = -iN$ for $N$ electrons. This is the Thomas-Reiche-Kuhn sum rule.
- **$k = -1$.** $f/\omega = \tfrac23|\langle0|\mathbf R|n\rangle|^2$, so $S(-1) = \tfrac23\big(\langle0|R^2|0\rangle - |\langle0|\mathbf R|0\rangle|^2\big)$, the fluctuation of the total electronic position.
- **$k = 1$.** With the velocity form, $S(1) = \tfrac23\langle0|P^2|0\rangle$, using $\langle0|\mathbf P|0\rangle = 0$ for a bound state.
- **$k = -2$.** $S(-2)$ is the static isotropic polarizability, the $k = 0$ term of Eq. [[#cauchy]].

**Approximate methods.** TRK holds for TDHF, CI and MCSCF linear response in a complete basis. In practice, a sum of computed oscillator strengths close to $N$ is a basis-set diagnostic. Band-integrated intensities are often more reliable than individual peaks when the basis cannot resolve a Rydberg series.

## Universal dispersion of hyperpolarizabilities

**Expansion.** In a diagonal component such as $\beta_{zzz}$ every term of the permutation sum has the same numerator, so the frequency dependence sits in $\sum_P[(\omega_{n0}-\omega_\sigma)(\omega_{p0}-\omega_2)]^{-1}$. Expanding each factor geometrically and keeping second order needs only the permutation sums over the $n+1$ frequencies $\{-\omega_\sigma,\omega_1,\ldots,\omega_n\}$, which add to zero:

$$
\sum_P1 = (n+1)!,\qquad \sum_P\omega_1 = 0,\qquad \sum_P\omega_1^2 = n!\,\omega_L^2,\qquad \sum_P\omega_1\omega_2 = -(n-1)!\,\omega_L^2,\qquad \omega_L^2 = \omega_\sigma^2 + \sum_k\omega_k^2.
$$

Every first-order term cancels, and every second-order term is proportional to $\omega_L^2$. Hence

$$
\beta_{zzz}(-\omega_\sigma;\omega_1,\omega_2) = \beta_{zzz}(0;0,0) + A\,\omega_L^2 + O(\omega^4),\qquad A = \sum_{np}{}'\frac{\mu_{0n}\bar\mu_{np}\mu_{p0}}{\omega_{n0}\omega_{p0}}\left(\frac2{\omega_{n0}^2} + \frac2{\omega_{p0}^2} + \frac1{\omega_{n0}\omega_{p0}}\right).
\label{universal}
$$

**Consequences.**

- $A$ is a molecular constant. One measured or computed process (Pockels, $\omega_L^2 = 2\omega^2$) predicts another (SHG, $\omega_L^2 = 6\omega^2$) to second order.
- The same holds for $\gamma$ with its own constant, and for the rotational averages $\bar\beta = \tfrac15\sum_\alpha(\beta_{z\alpha\alpha}+\beta_{\alpha z\alpha}+\beta_{\alpha\alpha z})$ and $\bar\gamma = \tfrac1{15}\sum_{\alpha\beta}(\gamma_{\alpha\alpha\beta\beta}+\gamma_{\alpha\beta\alpha\beta}+\gamma_{\alpha\beta\beta\alpha})$.
- NRS show TDHF data for HF ($\beta_{zzz}$ and $\gamma_{zzzz}$, t-aug-cc-pVTZ) collapsing onto one line against $\omega_L^2$, with visible deviations beyond $\omega_L^2\approx0.04$.
- Processes with larger $\omega_L^2$ (SHG, THG) disperse more strongly, because they approach two- and three-photon resonances sooner.

## Worked examples

!!! example "Hydrogen atom: Cauchy moments on a radial grid (computed for this note)"
    1s and the $l = 1$ radial Hamiltonian on a uniform grid in a 200-bohr box (Dirichlet ends), 4000 and 8000 points, Richardson-extrapolated in $h^2$. The discretized continuum is included automatically. With $z$-polarization, $f_{n0} = 2\omega_{n0}|\langle1s|z|np_0\rangle|^2$ equals the isotropic value.

    | | 4000 pts | 8000 pts | extrapolated | exact |
    |---|---:|---:|---:|---:|
    | $E_{1s}$ | −0.499688 | −0.499922 | | −0.5 |
    | $S(1)$ | 0.66501 | 0.66625 | 0.66667 | $\tfrac23\langle p^2\rangle = 2/3$ |
    | $S(0)$ | 0.99958 | 0.99990 | 1.00000 | 1 (TRK) |
    | $S(-1)$ | 2.00167 | 2.00042 | 2.00000 | $\tfrac23\langle r^2\rangle = 2$ |
    | $S(-2)$ | 4.50854 | 4.50214 | 4.50000 | $\alpha = 9/2$ |
    | $S(-4)$ | 26.68541 | 26.60884 | 26.58331 | |
    | $S(-6)$ | 173.16602 | 172.43224 | 172.18765 | |

    - **Dispersion.** $\alpha(\omega) = 4.5 + 26.58\,\omega^2 + 172.2\,\omega^4 + \cdots$ below the 1s→2p threshold.
    - **Bound states.** The bound $np$ states carry 56.5% of $S(0)$ and 3.665 of the 4.5 in $\alpha$ (81%, the figure quoted in [[stark-effect]]). The continuum carries the rest.

!!! example "Universal dispersion in a five-state model (computed for this note)"
    Model of [[exact-state-response-functions]], $\beta_{zzz}(0;0,0) = 2.463629$, $A = 7.267288$ from Eq. [[#universal]].

    | $\omega$ | SHG exact | $\beta_0 + 6A\omega^2$ | Pockels exact | $\beta_0 + 2A\omega^2$ |
    |---:|---:|---:|---:|---:|
    | 0.01 | 2.467996 | 2.467990 | 2.465084 | 2.465083 |
    | 0.02 | 2.481173 | 2.481071 | 2.469455 | 2.469443 |
    | 0.04 | 2.535058 | 2.533395 | 2.487067 | 2.486885 |

    Optical rectification $\beta(0;\omega,-\omega)$ equals the Pockels value at every $\omega$ (same $\omega_L^2$; in fact equal by permutation symmetry). The quartic remainder grows faster for SHG.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 5.2, Eqs. (5.66)–(5.77) and Table 5.1; Sec. 5.6, Eqs. (5.206)–(5.226), Figs. 5.13–5.14 (described); Sec. 5.7, Eqs. (5.227)–(5.236); Sec. 7.4, pp. 289–291 (helium oscillator-strength sums). The sum rules for $S(-1)$ and $S(1)$ are standard and derived here. The calculations are in `Claude outputs/part4_response_batchA.py`, section C.
