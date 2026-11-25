---
id: electromagnetic-waves-and-polarization
title: Electromagnetic waves and polarization - plane waves, transversality, linear, elliptic and circular polarization, the handedness convention, and decomposition into circular components
summary: Away from sources, E, B and the Coulomb-gauge vector potential satisfy the wave equation. Monochromatic plane waves have k = ω/c, with E, B and k mutually perpendicular and |E| = c|B|. The polarization is set by the relative phase of the two transverse components: in phase gives linear, π/2 out of phase gives elliptic, and equal amplitudes give circular, written with the complex unit vectors e± = e_x ± ie_y. Two handedness conventions exist. Following IUPAC (as NRS do), a wave is right-handed if the field traces a right-handed helix when frozen in time, and the receiver then sees it turn clockwise. Linear light is the sum of two opposite circular waves, so a medium in which they travel at different speeds rotates the plane of polarization (optical activity). Checked numerically: the helicity of e±, their phase under frame rotation, and the linear-to-circular decomposition.
status: in-progress
kind: theory
level: introductory
tags: [plane-wave, polarization, circular-polarization, elliptic-polarization, handedness, helicity, wave-vector, transversality, optical-activity]
prerequisites: [maxwell-equations-and-helmholtz-decomposition, electromagnetic-potentials-and-gauge-freedom]
related: [charged-particle-in-an-electromagnetic-field, optical-activity-ecd-and-mcd, vibrational-optical-activity, electromagnetic-waves-in-linear-media]
conventions: [si-units]
key: decomp
order: 40
date: 2026-11-25
---

SI units. Physical fields are the real parts of the complex expressions. $\mathbf e_x$, $\mathbf e_y$, $\mathbf e_z$ are Cartesian unit vectors, and the wave travels along $\mathbf e_z$ where a direction is needed.

## Plane waves

**Source-free equations.** Without sources, $\Box^2\mathbf E = \mathbf 0$ and $\Box^2\mathbf B = \mathbf 0$. Both fields are solenoidal, so in the Coulomb gauge no scalar potential is needed and $\Box^2\mathbf A = \mathbf 0$ (NRS Eqs. 3.67–3.69). A solution is $\Psi = \Psi_0\exp[i(\mathbf k\cdot\mathbf r - \omega t + \delta)]$ with $k = \omega/c$ (NRS Eqs. 3.70–3.72).

**Terminology.**

- **Wavefronts.** The surfaces of constant phase are planes perpendicular to $\mathbf k$, moving at speed $c$ along $\mathbf k$.
- **Period and wavelength.** The period is $T = 2\pi/\omega$ and the wavelength $\lambda = cT$.
- **Wavenumber.** $\tilde\nu = 1/\lambda$ (NRS Eq. 3.73).

**Monochromatic fields.** For $\mathbf E = \tilde{\mathbf E}_0e^{i(\mathbf k\cdot\mathbf r - \omega t)}$, $\mathbf B = \tilde{\mathbf B}_0e^{i(\mathbf k\cdot\mathbf r - \omega t)}$, with phases absorbed into the complex amplitudes (NRS Eqs. 3.74–3.76):

$$
\mathbf k\cdot\mathbf E = 0,\qquad \mathbf k\cdot\mathbf B = 0,\qquad \mathbf k\times\mathbf E = \omega\mathbf B\quad\Rightarrow\quad |\mathbf E| = c|\mathbf B| .
$$

$(\mathbf k, \mathbf E, \mathbf B)$ form a right-handed set: with $\mathbf k\parallel\mathbf e_z$ and $\mathbf E\parallel\mathbf e_x$, $\mathbf B\parallel\mathbf e_y$. The magnetic field is $c$ times weaker in SI units, which is why electric-dipole coupling dominates ([[multipolar-gauge-and-the-electric-dipole-approximation]]).

## Polarization

**General transverse wave.** For a wave along $z$ (NRS Eq. 3.77),

$$
\mathbf E = E_{0x}\cos(kz - \omega t + \delta_x)\,\mathbf e_x + E_{0y}\cos(kz - \omega t + \delta_y)\,\mathbf e_y .
$$

**Polarization types.**

- **Linear.** $\delta_y - \delta_x = m\pi$: the field oscillates at a fixed angle $\theta$ to the $x$ axis, $\mathbf E = E_0(\cos\theta\,\mathbf e_x + \sin\theta\,\mathbf e_y)\cos(kz - \omega t + \delta)$, with $\mathbf B$ at $\theta + \pi/2$ (NRS Eqs. 3.78–3.80).
- **Elliptic.** $\delta_y - \delta_x = \pi/2 + m\pi$: the tip of $\mathbf E$ traces the ellipse $E_x^2/E_{0x}^2 + E_y^2/E_{0y}^2 = 1$ in a fixed plane (NRS Eqs. 3.81–3.82). An arbitrary phase difference gives an ellipse rotated with respect to the axes.
- **Circular.** Additionally $E_{0x} = E_{0y} = E_0$, which gives (NRS Eqs. 3.83–3.84)

$$
\mathbf E_{\rm cp} = \mathrm{Re}\big\{E_0\,\mathbf e_\pm\,e^{i(kz - \omega t + \delta_x)}\big\},\qquad \mathbf e_\pm = \mathbf e_x\pm i\mathbf e_y,
$$

with the sign $+$ for even $m$ and $-$ for odd $m$.

**Behaviour under rotation.** If the Cartesian axes are rotated by $\phi$ about $z$, the complex unit vectors built from the rotated axes are $\mathbf e'_\pm = e^{\mp i\phi}\mathbf e_\pm$ (NRS Eq. 3.85). Circular components carry a definite phase under rotation, the classical counterpart of angular momentum $\pm\hbar$ per photon.

## Handedness

**Two conventions.** Two opposite conventions are in use, depending on whether one follows the field in space or in time.

- **The spatial convention.** NRS adopt the IUPAC (spatial) convention (NRS Eq. 3.86). Take $\mathbf e_-$ (odd $m$) at a fixed instant: $\mathbf E(z) = E_0(\cos kz\,\mathbf e_x + \sin kz\,\mathbf e_y)$, which as a function of $z$ is a right-handed helix.
- **What the receiver sees.** At fixed $z$ the same wave turns from $\mathbf e_x$ toward $-\mathbf e_y$ in time, which is clockwise for a receiver looking toward the source.
- **The rule.** In this convention $\mathbf e_-$ is right-handed and $\mathbf e_+$ left-handed. A right-handed wave is clockwise seen by the receiver: point the right thumb toward the source, and the fingers curl with the field.
- **The temporal convention.** It names the same waves the other way round, from the point of view of the source.

**Photon helicity.** The IUPAC convention agrees with quantum-mechanical helicity, where a particle is right-handed if its spin points along its momentum. Photons have spin 1, with $m_s = +1$ left-handed and $m_s = -1$ right-handed (positive and negative helicity). There is no $m_s = 0$ component because the field is transverse (NRS Sec. 3.1.5).

**Check before comparing signs.** When comparing chiroptical signs across papers, check the convention first: a CD spectrum quoted in the other convention has the opposite sign of $\Delta\epsilon = \epsilon_L - \epsilon_R$ for the same data.

## Circular decomposition

**Circular amplitudes.** In the basis $\mathbf e_\pm$, $\mathbf E = \mathrm{Re}\{(\tilde E_{0+}\mathbf e_+ + \tilde E_{0-}\mathbf e_-)e^{i(kz - \omega t)}\}$ with $\tilde E_{0\pm} = \tfrac12(\tilde E_{0x}\mp i\tilde E_{0y})$ (NRS Eqs. 3.87–3.88).

**Linear light as a superposition.** A linearly polarized wave at angle $\theta$ is a superposition of two opposite circular waves of equal amplitude (NRS Eq. 3.89):

$$
\cos\theta\,\mathbf e_x + \sin\theta\,\mathbf e_y = \tfrac12\big(e^{i\theta}\mathbf e_- + e^{-i\theta}\mathbf e_+\big).
\label{decomp}
$$

**Consequences.**

- **Optical rotation.** If the two circular components acquire different phases in a medium, $\theta$ changes along the path: optical rotation, the subject of [[optical-activity-ecd-and-mcd]].
- **The general ellipse.** With amplitudes $E_{0+}\neq E_{0-}$ and phase difference $\alpha = \delta_- - \delta_+$, the wave is elliptic with its major axis rotated by $\alpha/2$ (NRS Eq. 3.90). This is the elliptical light produced by circular dichroism.

## Worked example

!!! example "Numerical checks (computed for this note)"
    **Helicity.** For $\mathbf E = \mathrm{Re}(\mathbf e_\pm e^{ikz})$ at $t = 0$, the sign of $(\mathbf E\times\partial_z\mathbf E)\cdot\mathbf e_z$ gives the handedness of the spatial helix. At $z = 0$, the sense of rotation in time as seen from $+z$ (the receiver) gives the temporal behaviour.

    - $\mathbf e_+$: a left-handed helix, counterclockwise for the receiver.
    - $\mathbf e_-$: a right-handed helix, clockwise for the receiver.

    This matches the IUPAC assignment above.

    **Rotation.** For $\phi = 0.37$ rad, $\mathbf e'_x + i\mathbf e'_y = e^{-i\phi}(\mathbf e_x + i\mathbf e_y)$ and $\mathbf e'_x - i\mathbf e'_y = e^{+i\phi}(\mathbf e_x - i\mathbf e_y)$, as in NRS Eq. 3.85.

    **Decomposition.** Eq. [[#decomp]] holds for $\theta = 0.6$ rad to machine precision.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.1.5, Eqs. (3.67)–(3.90), Figs. 3.3–3.4 (described). S. E. Braslavsky, *Pure Appl. Chem.* **79**, 293–465, cited by NRS (dated 2009 there) for the IUPAC handedness convention (not read; year to verify). The remark on comparing CD signs is general knowledge. The checks are in `Claude outputs/part1_fields_batchD.py`, section D.
