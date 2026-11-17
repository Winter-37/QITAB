---
id: emission-absorption-and-spontaneous-emission
title: Emission and absorption of radiation
summary: An atom in a classical light wave, in the electric dipole approximation. Derives the rates of absorption and stimulated emission for monochromatic and for incoherent light, Einstein's A and B coefficients and the spontaneous emission rate A = ω³|℘|²/(3πε₀ħc³), and from it the lifetime of an excited state. Worked for a charged oscillator and for hydrogen (2p lifetime 1.60 ns, with the n = 3 states), with the dipole selection rules, oscillator strengths and the sum rule.
status: in-progress
kind: derivation
level: intermediate
tags: [radiation, absorption, stimulated-emission, spontaneous-emission, einstein-coefficients, electric-dipole-approximation, lifetime, selection-rules, oscillator-strength, hydrogen, griffiths, sakurai]
prerequisites: [time-dependent-perturbation-theory, fermi-golden-rule-and-decay-width, hydrogen-atom]
related: [two-level-systems-and-rabi-oscillations, rotational-selection-rules-and-wigner-eckart, parity-and-parity-selection-rules, minimal-coupling-and-aharonov-bohm, hyperfine-splitting-hydrogen]
order: 50
date: 2026-11-15
---

## An atom in a light wave

Visible light has a wavelength of about 5000 Å, an atom a size of about 1 Å. Over the atom the field is therefore nearly uniform, and for an electron bound by a much stronger internal field the magnetic force is negligible. In this **electric dipole approximation** a wave polarized along $z$ acts through

$$
H'(t) = -q\,E_0\,z\,\cos\omega t ,\qquad H'_{ba} = -\wp\,E_0\cos\omega t ,\qquad \wp\equiv q\,\langle\psi_b|z|\psi_a\rangle ,
$$

where $\wp$ is the matrix element of the $z$ component of the dipole moment $q\mathbf r$. Diagonal elements vanish for states of definite parity. This is the sinusoidal perturbation of [[time-dependent-perturbation-theory]] with $V_{ba} = -\wp E_0$:

$$
P_{a\to b}(t) = P_{b\to a}(t) = \Big(\frac{|\wp|E_0}{\hbar}\Big)^2\frac{\sin^2[(\omega_0 - \omega)t/2]}{(\omega_0 - \omega)^2} ,\qquad \omega_0 = \frac{E_b - E_a}{\hbar} .
$$

Three processes must be distinguished.

- **Absorption:** the atom goes up, taking $\hbar\omega_0$ from the field.
- **Stimulated emission:** an atom in the upper state is driven down by the field, with the same probability, adding $\hbar\omega_0$ to the field. One photon in, two out: the principle of the laser.
- **Spontaneous emission:** an excited atom decays with no applied field. A classical field cannot produce this; it is found below by Einstein's argument.

## Incoherent light

Real light sources are not monochromatic. The energy density of the wave is $u = \tfrac12\epsilon_0E_0^2$; for a spread of frequencies let $\rho(\omega)\,d\omega$ be the energy density in $d\omega$. Summing probabilities (not amplitudes, since the components are incoherent),

$$
P_{b\to a}(t) = \frac{2|\wp|^2}{\epsilon_0\hbar^2}\int_0^\infty\rho(\omega)\,\frac{\sin^2[(\omega_0 - \omega)t/2]}{(\omega_0 - \omega)^2}\,d\omega\approx\frac{\pi|\wp|^2}{\epsilon_0\hbar^2}\,\rho(\omega_0)\,t ,
$$

exactly the step that leads to the golden rule ([[fermi-golden-rule-and-decay-width]]): the flopping is washed out and the **rate** is constant. For unpolarized light arriving from all directions, $|\wp|^2$ is replaced by the average of $|\hat{\mathbf n}\cdot\boldsymbol\wp|^2$ over polarization directions $\hat{\mathbf n}$, which is $|\boldsymbol\wp|^2/3$:

$$
\boxed{\,R_{b\to a} = R_{a\to b} = \frac{\pi}{3\epsilon_0\hbar^2}\,|\boldsymbol\wp|^2\,\rho(\omega_0) ,\qquad \boldsymbol\wp = q\,\langle\psi_b|\mathbf r|\psi_a\rangle\,}
$$

## Einstein's A and B coefficients

Consider $N_a$ atoms in the lower state and $N_b$ in the upper, in thermal equilibrium with radiation at temperature $T$. Let $A$ be the spontaneous emission rate, and $B_{ba}\rho(\omega_0)$, $B_{ab}\rho(\omega_0)$ the stimulated emission and absorption rates. In equilibrium

$$
\frac{dN_b}{dt} = -N_bA - N_bB_{ba}\,\rho(\omega_0) + N_aB_{ab}\,\rho(\omega_0) = 0 \quad\Rightarrow\quad \rho(\omega_0) = \frac{A}{(N_a/N_b)B_{ab} - B_{ba}} .
$$

With the Boltzmann ratio $N_a/N_b = e^{\hbar\omega_0/k_BT}$, this must coincide with Planck's formula

$$
\rho(\omega) = \frac{\hbar}{\pi^2c^3}\,\frac{\omega^3}{e^{\hbar\omega/k_BT} - 1} ,
$$

which requires

$$
B_{ab} = B_{ba} ,\qquad A = \frac{\hbar\omega_0^3}{\pi^2c^3}\,B_{ba} .
$$

The first was found above from quantum mechanics, with $B = \pi|\boldsymbol\wp|^2/(3\epsilon_0\hbar^2)$. The second then gives the **spontaneous emission rate**:

$$
\boxed{\,A = \frac{\omega_0^3\,|\boldsymbol\wp|^2}{3\pi\epsilon_0\hbar c^3}\,}
$$

**Remarks.**

- The ratio of stimulated to spontaneous emission in thermal radiation is $1/(e^{\hbar\omega/k_BT} - 1)$, the mean number of photons per mode. At 300 K the two are equal at $\nu = k_BT\ln2/h = 4.3\times10^{12}$ Hz, in the far infrared. Below that frequency stimulated emission dominates; for optical transitions at room temperature it is utterly negligible.
- Spontaneous emission is, in quantum electrodynamics, emission stimulated by the zero-point field: $A/B$ is the energy density corresponding to one photon per mode, $\hbar\omega\times\omega^2/(\pi^2c^3)$.
- $A\propto\omega^3$: high-frequency transitions are fast, which is why population inversion is easier to maintain at microwave than at X-ray frequencies.

## Lifetime of an excited state

If spontaneous emission is the only process, $dN_b/dt = -AN_b$ and

$$
N_b(t) = N_b(0)\,e^{-t/\tau} ,\qquad \tau = \frac1A .
$$

When several decay channels are open the rates add, $\tau = 1/(A_1 + A_2 + \cdots)$. The level acquires the natural width $\Gamma = \hbar/\tau$ ([[fermi-golden-rule-and-decay-width]]).

!!! example "Charged harmonic oscillator"

    A charge $q$ on a spring, in the state $|n\rangle$. Since $\langle n'|x|n\rangle = \sqrt{n\hbar/2m\omega}\;\delta_{n',n-1}$ for downward transitions, the only decay is $n\to n-1$, with

    $$
    A = \frac{nq^2\omega^2}{6\pi\epsilon_0mc^3} ,\qquad \tau_n = \frac{6\pi\epsilon_0mc^3}{nq^2\omega^2} .
    $$

    The radiated power is $A\hbar\omega = (q^2\omega^2/6\pi\epsilon_0mc^3)(E - \tfrac12\hbar\omega)$, which is the classical Larmor result for an oscillator of energy $E$ with the zero-point energy removed: the ground state does not radiate. For an electron oscillating at an optical frequency (500 nm) and $n = 1$, $A = 8.9\times10^7\ \text{s}^{-1}$, a lifetime of 11 ns.

!!! example "Hydrogen"

    For $2p\to1s$ the dipole matrix element is the same for each $m$: $|\langle100|\mathbf r|21m\rangle|^2 = (2^{15}/3^{10})\,a^2 = 0.5549\,a^2$ with $a$ the Bohr radius, and $\hbar\omega_0 = \tfrac34(13.606\ \text{eV}) = 10.204$ eV. Then

    $$
    A_{2p\to1s} = 6.27\times10^8\ \text{s}^{-1} ,\qquad \tau_{2p} = 1.60\ \text{ns} .
    $$

    In general, summing over the final $m'$, the rate from any state of the level $(n,l)$ to the level $(n',l')$ with $l' = l\pm1$ is

    $$
    A = \frac{\omega_0^3e^2}{3\pi\epsilon_0\hbar c^3}\,\frac{\max(l,l')}{2l+1}\,\Big|\int_0^\infty R_{n'l'}(r)\,R_{nl}(r)\,r^3\,dr\Big|^2 .
    $$

    | transition | $A$ (s$^{-1}$) | | state | lifetime |
    |---|---|---|---|---|
    | $2p\to1s$ | $6.27\times10^8$ | | $2p$ | 1.60 ns |
    | $3s\to2p$ | $6.32\times10^6$ | | $3s$ | 158 ns |
    | $3p\to1s$ | $1.67\times10^8$ | | $3p$ | 5.27 ns |
    | $3p\to2s$ | $2.25\times10^7$ | | $3d$ | 15.5 ns |
    | $3d\to2p$ | $6.47\times10^7$ | | $2s$ | no dipole decay |

    The natural width of $2p$ is $\hbar A = 4.1\times10^{-7}$ eV, a fraction $4\times10^{-8}$ of the transition energy. (Computed for an infinitely heavy nucleus; the reduced mass changes the rates by about 0.05 percent. I have not compared these against a spectroscopic database in this session.)

## Selection rules

The rate vanishes unless $\langle n'l'm'|\mathbf r|nlm\rangle\ne0$, and for states of definite angular momentum this requires

$$
\Delta l = \pm1 ,\qquad \Delta m = 0,\ \pm1 .
$$

The derivations are in [[rotational-selection-rules-and-wigner-eckart]] ($\mathbf r$ is a vector operator) and [[parity-and-parity-selection-rules]] ($\mathbf r$ is odd, so $l$ must change parity). Physically the photon carries one unit of angular momentum. Not every transition to a lower level is therefore **allowed**:

- Hydrogen $2s$ cannot decay to $1s$ by dipole radiation. It is **metastable**, and decays mainly by emitting two photons, with a lifetime many orders of magnitude longer than that of $2p$ (about a tenth of a second; value quoted from memory).
- "Forbidden" transitions proceed through the next terms in the expansion of the field over the atom (magnetic dipole, electric quadrupole), slower by a factor of order $(a/\lambda)^2$. The 21 cm line of [[hyperfine-splitting-hydrogen]] is a magnetic dipole transition at a very low frequency, with a lifetime of the order of $10^7$ years.

## Oscillator strengths

A convenient dimensionless measure of the strength of a transition $i\to n$ is the oscillator strength

$$
f_{ni} = \frac{2m\omega_{ni}}{\hbar}\,|\langle n|x|i\rangle|^2 ,\qquad \sum_nf_{ni} = 1 ,
$$

the sum over all states being the Thomas-Reiche-Kuhn sum rule, which follows from $[x,[x,H_0]] = -\hbar^2/m$. For the oscillator ground state the single transition $0\to1$ has $f = 1$ and exhausts the rule. For hydrogen $1s\to2p$, $f = 2\times\tfrac38\times0.5549 = 0.4162$ in atomic units: this one line carries 42 percent of the total absorption strength of the ground state.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.2, Eqs. (11.38)-(11.54); Sec. 11.3, Eqs. (11.55)-(11.78), Example 11.1 (oscillator); Problems 11.10 (thermal stimulated emission), 11.13 (lifetimes of the $n = 2$ states), 11.14-11.15 (selection rules from commutators), 11.31 (forbidden transitions), 11.32 (hydrogen rate formula (11.132)), 11.33 (21 cm line). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.8, pp. 347-355: absorption and stimulated emission from the $\mathbf A\cdot\mathbf p$ coupling, the electric dipole approximation, oscillator strength and the Thomas-Reiche-Kuhn sum rule (5.330)-(5.331), spontaneous emission (5.352). Sakurai starts from the vector-potential coupling of [[minimal-coupling-and-aharonov-bohm]], which reduces to $-q\mathbf E\cdot\mathbf r$ in the dipole approximation.

The hydrogen rates and lifetimes were computed here from numerical radial integrals with CODATA constants, in `griffiths/ch11_dynamics.py` (section D). The $2s$ two-photon lifetime and the 21 cm lifetime are quoted from memory and are to be verified.
