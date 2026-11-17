---
id: density-operators-and-mixed-states
title: Density operators and mixed states
summary: How quantum mechanics describes an ensemble that is not in a single state. A mixed ensemble is fixed by ρ = Σ w_i |α_i⟩⟨α_i|, with ensemble averages tr(ρA). Covers the properties of ρ, the test tr ρ² = 1 for a pure state, the non-uniqueness of the mixture, the Bloch vector of a two-level system, the von Neumann equation of motion, the entropy −k tr(ρ ln ρ), the canonical ensemble ρ = e^{−βH}/Z as the state of maximum entropy, and the reduced density operator of an entangled subsystem.
status: in-progress
kind: theory
level: intermediate
tags: [density-operator, density-matrix, mixed-state, pure-state, ensemble-average, bloch-vector, purity, von-neumann-entropy, canonical-ensemble, partition-function, reduced-density-operator, entanglement, sakurai]
prerequisites: [generalized-statistical-interpretation, position-momentum-and-energy-representations]
related: [spin-one-half, addition-of-angular-momenta, heisenberg-picture-and-time-translation, one-particle-rdm, density-matrices-second-quantization, feynman-path-integral]
order: 80
date: 2026-11-15
---

## Pure and mixed ensembles

So far a system has been described by a state vector $|\alpha\rangle$. Every member of the ensemble that it describes is in the same state, and the ensemble is called **pure**. This is not the general situation. Silver atoms leaving an oven have spins pointing at random; a beam of particles may have been prepared partly in one state and partly in another; a molecule in contact with a heat bath occupies its levels with Boltzmann weights. Such an ensemble is **mixed**: a fraction $w_i$ of its members is in the state $|\alpha^{(i)}\rangle$, with

$$
w_i\ge0 ,\qquad \sum_iw_i = 1 .
$$

The states $|\alpha^{(i)}\rangle$ are normalized but need not be orthogonal, and their number is unrelated to the dimension of the space.

A mixture is not a superposition. A superposition $c_1|\alpha^{(1)}\rangle + c_2|\alpha^{(2)}\rangle$ is a single state with definite relative phases; a mixture has no relative phases at all. The weights $w_i$ express classical ignorance about which state a given member is in, on top of the quantum probabilities within each state.

## The density operator

The ensemble average of an observable $A$ is the weighted average of the quantum expectation values:

$$
[A]\equiv\sum_iw_i\,\langle\alpha^{(i)}|A|\alpha^{(i)}\rangle = \sum_{b',b''}\Big(\sum_iw_i\,\langle b''|\alpha^{(i)}\rangle\langle\alpha^{(i)}|b'\rangle\Big)\langle b'|A|b''\rangle ,
$$

after inserting a complete set $\{|b'\rangle\}$ twice. The bracket does not depend on $A$, which motivates the **density operator**

$$
\boxed{\,\rho = \sum_iw_i\,|\alpha^{(i)}\rangle\langle\alpha^{(i)}| ,\qquad [A] = \mathrm{tr}(\rho A)\,}
$$

Its matrix in a basis, $\langle b''|\rho|b'\rangle$, is the **density matrix**. Because the trace is basis independent, $[A]$ may be evaluated in whatever basis is convenient. Every measurable property of the ensemble follows from $\rho$: the probability of the outcome $a$ in a measurement of $A$ is $\mathrm{tr}(\rho P_a)$, with $P_a$ the projector onto the eigenspace of $a$.

**Properties.** From the definition:

- $\rho$ is Hermitian.
- $\mathrm{tr}\rho = 1$.
- $\rho$ is positive semidefinite: $\langle\phi|\rho|\phi\rangle = \sum_iw_i|\langle\phi|\alpha^{(i)}\rangle|^2\ge0$. Its eigenvalues $p_k$ therefore lie in $[0,1]$ and sum to one.

Conversely, any operator with these three properties is the density operator of some ensemble, for instance of the ensemble of its own eigenvectors with weights $p_k$.

**Pure or mixed?** For a pure ensemble $\rho = |\alpha\rangle\langle\alpha|$ is a projector, so $\rho^2 = \rho$ and its eigenvalues are 0 and 1. In general

$$
\mathrm{tr}\,\rho^2 = \sum_kp_k^2\le1 ,
$$

with equality only for a pure state. The **purity** $\mathrm{tr}\rho^2$ ranges from $1/N$ (the completely random ensemble $\rho = \mathbb 1/N$ in $N$ dimensions) to 1.

**Different mixtures, same $\rho$.** Distinct ensembles can have the same density operator, and are then indistinguishable by any measurement. An equal mixture of spin up and spin down along $z$ and an equal mixture of spin up and spin down along $x$ both give $\rho = \mathbb 1/2$: in each case there is no preferred direction. Only $\rho$, not the recipe that produced it, has physical meaning.

## Two-level systems: the Bloch vector

For a two-dimensional space the Hermitian, unit-trace operators are spanned by $\mathbb 1$ and the Pauli matrices $\sigma_x,\sigma_y,\sigma_z$ (as in [[spin-one-half]]), so every density matrix can be written

$$
\rho = \tfrac12\big(\mathbb 1 + \mathbf P\cdot\boldsymbol\sigma\big) ,\qquad \mathbf P = \mathrm{tr}(\rho\,\boldsymbol\sigma) ,\qquad \mathrm{tr}\rho^2 = \tfrac12\big(1 + |\mathbf P|^2\big) .
$$

Positivity requires $|\mathbf P|\le1$. Pure states lie on the surface of the unit ball (the Bloch sphere), mixed states inside it, and the completely random ensemble at the centre. For spin $\tfrac12$, $[\mathbf S] = \tfrac\hbar2\mathbf P$, so $\mathbf P$ is the polarization of the beam.

!!! example "A partially polarized beam"

    Take 75 percent of atoms in $|S_z;+\rangle$ and 25 percent in $|S_x;+\rangle = (|{+}\rangle + |{-}\rangle)/\sqrt2$:

    $$
    \rho = \tfrac34\begin{pmatrix}1&0\\0&0\end{pmatrix} + \tfrac14\begin{pmatrix}\tfrac12&\tfrac12\\ \tfrac12&\tfrac12\end{pmatrix} = \begin{pmatrix}\tfrac78&\tfrac18\\ \tfrac18&\tfrac18\end{pmatrix} .
    $$

    Then $\mathbf P = (\tfrac14,\,0,\,\tfrac34)$, so $[S_x] = \hbar/8$, $[S_y] = 0$, $[S_z] = 3\hbar/8$, and $|\mathbf P| = 0.7906$. The purity is $\tfrac12(1 + \tfrac{10}{16}) = 0.8125$ and the eigenvalues are $0.8953$ and $0.1047$. The same $\rho$ is produced by the mixture of its two eigenvectors (spin up and down along $\hat{\mathbf P}$) with those weights, which is a different preparation and an identical ensemble.

## Time evolution

If each member evolves under the same Hamiltonian, $|\alpha^{(i)},t\rangle = U(t)|\alpha^{(i)}\rangle$ while the weights stay fixed. Then $\rho(t) = U\rho(0)U^\dagger$ and

$$
\boxed{\,i\hbar\frac{\partial\rho}{\partial t} = [H,\rho]\,}
$$

the **von Neumann equation**. It has the opposite sign to the Heisenberg equation for an observable, because $\rho$ is built from states, not observables. It is the quantum analogue of Liouville's theorem for a classical phase-space density.

Unitary evolution leaves the eigenvalues of $\rho$ unchanged, so the purity and the entropy below are constant: unitary dynamics cannot turn a pure state into a mixed one or the reverse. For a spin in a magnetic field, $H = \tfrac12\hbar\,\boldsymbol\omega\cdot\boldsymbol\sigma$, the von Neumann equation becomes $d\mathbf P/dt = \boldsymbol\omega\times\mathbf P$: the Bloch vector precesses at fixed length, whether the state is pure or mixed. Both statements were checked numerically.

In the position representation $\rho(\mathbf x',\mathbf x'') = \langle\mathbf x'|\rho|\mathbf x''\rangle$, and the diagonal $\rho(\mathbf x',\mathbf x')$ is the probability density. For a pure state $\rho(\mathbf x',\mathbf x'') = \psi(\mathbf x')\psi^*(\mathbf x'')$.

## Entropy and the canonical ensemble

A measure of how mixed an ensemble is:

$$
\sigma = -\mathrm{tr}(\rho\ln\rho) = -\sum_kp_k\ln p_k .
$$

It vanishes for a pure ensemble and takes its maximum, $\ln N$, for the completely random one. Multiplied by Boltzmann's constant, $S = k\sigma$ is the entropy per member of statistical mechanics (the von Neumann entropy). For the beam above, $\sigma = 0.3353$; for the unpolarized beam, $\ln2 = 0.6931$.

**Thermal equilibrium.** Assume that nature maximizes $\sigma$ subject to a fixed ensemble average of the energy, $[H] = U$, and to $\mathrm{tr}\rho = 1$. Working in the energy basis with Lagrange multipliers, $\delta\sum_k(p_k\ln p_k + \beta p_kE_k + \gamma p_k) = 0$ gives $p_k\propto e^{-\beta E_k}$, that is

$$
\boxed{\,\rho = \frac{e^{-\beta H}}{Z} ,\qquad Z = \mathrm{tr}\,e^{-\beta H} = \sum_ke^{-\beta E_k}\,}
$$

with $\beta = 1/kT$ identified by comparison with thermodynamics. The completely random ensemble is the limit $\beta\to0$. A numerical search over 20000 random perturbations of the canonical weights that keep $\sum p_k$ and $\sum p_kE_k$ fixed (four levels, $\beta = 1.3$) found none with larger entropy.

!!! example "Spin in a magnetic field at temperature $T$"

    With $H = \omega S_z$,

    $$
    \rho = \frac1Z\begin{pmatrix}e^{-\beta\hbar\omega/2}&0\\0&e^{\beta\hbar\omega/2}\end{pmatrix} ,\qquad Z = 2\cosh\frac{\beta\hbar\omega}{2} ,\qquad [S_z] = -\frac\hbar2\tanh\frac{\beta\hbar\omega}{2} .
    $$

    | $\beta\hbar\omega$ | $[S_z]/\hbar$ | purity | $\sigma$ |
    |---|---|---|---|
    | 0.2 | $-0.0498$ | 0.505 | 0.688 |
    | 1.0 | $-0.2311$ | 0.607 | 0.582 |
    | 3.0 | $-0.4526$ | 0.910 | 0.191 |

    At high temperature the spin is nearly unpolarized; at low temperature it relaxes to the lower state ($[S_z]\to-\hbar/2$ for $\omega>0$). Multiplying $[S_z]$ by the magnetic moment per unit spin gives the paramagnetic magnetization and, for small $\beta\hbar\omega$, Curie's $1/T$ law.

## Subsystems and reduced density operators

Mixed states arise unavoidably when a system is part of a larger one. If $A$ and $B$ together are in the pure state $|\Psi\rangle$ of the product space, every measurement on $A$ alone is described by the **reduced density operator**

$$
\rho_A = \mathrm{tr}_B\,|\Psi\rangle\langle\Psi| ,\qquad \langle a'|\rho_A|a''\rangle = \sum_b\langle a',b|\Psi\rangle\langle\Psi|a'',b\rangle ,
$$

since $\langle\Psi|(O_A\otimes\mathbb 1_B)|\Psi\rangle = \mathrm{tr}(\rho_AO_A)$. If $|\Psi\rangle = |\phi_A\rangle|\chi_B\rangle$ is a product, $\rho_A$ is pure. Otherwise it is mixed, although the whole is pure, and the state is called **entangled**.

!!! example "Two spins"

    For $|\Psi\rangle = \cos\theta\,|{\uparrow\downarrow}\rangle - \sin\theta\,|{\downarrow\uparrow}\rangle$, tracing out the second spin gives $\rho_A = \mathrm{diag}(\cos^2\theta,\ \sin^2\theta)$:

    | $\theta$ | purity of $\rho_A$ | entropy of $\rho_A$ |
    |---|---|---|
    | 0 | 1 | 0 |
    | $\pi/8$ | 0.750 | 0.4165 |
    | $\pi/4$ (singlet) | 0.5 | $\ln2 = 0.6931$ |

    In the singlet of [[addition-of-angular-momenta]] each spin on its own is completely unpolarized, while the pair has total spin zero and its components are perfectly anticorrelated. The entropy of $\rho_A$ (which equals that of $\rho_B$) measures the entanglement.

The same construction, applied to many electrons and traced down to one or two of them, gives the reduced density matrices of Part 4 ([[one-particle-rdm]], [[density-matrices-second-quantization]]).

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.4, pp. 169-180: polarized and unpolarized beams (3.4.1); ensemble averages and the density operator, Eqs. (3.96)-(3.120), with the 75:25 mixture as Example 4, p. 174 (3.4.2); time evolution and the analogue of Liouville's theorem, Eqs. (3.121)-(3.123) (3.4.3); the position representation (3.4.4); entropy (3.127)-(3.133), maximization of entropy and the canonical ensemble (3.140)-(3.144), and the spin example (3.148)-(3.150) (3.4.5).

The Bloch-vector form, the reduced density operator and the two-spin example are not in Sakurai's Sec. 3.4 and are written in my own words; Sakurai uses the singlet's correlations in Sec. 3.10. All numbers are computed in `sakurai/companions_ch2_ch4.py` (section A).
