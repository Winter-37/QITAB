Rayleigh–Schrödinger perturbation theory and the single-particle Green's function: the two general tools that return as Møller–Plesset theory (Part 4, Chapter 10) and as propagators (Part 4, Chapter 17).

## What this chapter is about

Perturbation theory applies when the Hamiltonian is a solvable part plus a small correction, $\hat H=\hat H^{(0)}+\lambda\hat V$. The exact energies and states are expanded as power series in $\lambda$. Each order is expressed through the known unperturbed states, for example

$$
E_n^{(1)}=\langle n^{(0)}|\hat V|n^{(0)}\rangle,
\qquad
E_n^{(2)}=\sum_{m\ne n}\frac{|\langle m^{(0)}|\hat V|n^{(0)}\rangle|^2}{E_n^{(0)}-E_m^{(0)}} .
$$

When unperturbed levels are degenerate the denominators vanish. The cure is to first diagonalize $\hat V$ within the degenerate subspace. The theory is applied to the hydrogen atom:

- in an electric field (the Stark effect);
- with relativistic and spin–orbit corrections (fine structure);
- in a magnetic field (the Zeeman effect);
- with nuclear spin (hyperfine splitting).

The chapter ends with Green's functions, the resolvent $(E-\hat H)^{-1}$. It solves inhomogeneous equations, has its poles at the eigenvalues, and obeys a Dyson-type equation when $\hat H$ is split into two parts.

## Why it matters

- **It complements the variational principle.** Perturbation theory needs no trial function and gives a systematic hierarchy of corrections. In return it gives no upper bound, and the series can diverge.
- **It is the basis of a whole family of correlation methods.** Møller–Plesset theory is Rayleigh–Schrödinger theory with the Fock operator as $\hat H^{(0)}$. MP2 is the second-order formula above, written in orbitals. CASPT2 and NEVPT2 apply the same idea to a multiconfigurational reference.
- **Response properties are perturbation coefficients.** Polarizabilities, magnetizabilities and force constants are second derivatives of the energy with respect to a field or displacement. The Stark effect is the simplest example, with the hydrogen polarizability as a second-order energy.
- **Small effects organize spectra.** Fine and hyperfine structure show how a hierarchy of small couplings splits levels in stages, and which quantum numbers stay good at each stage.
- **Green's functions are the bridge to many-body theory.** The poles-and-residues view of $(E-\hat H)^{-1}$ is exactly how ionization energies and excitation energies are extracted from propagators in Part 4.

## Where it is used later

- [[mp2|MP2]] and [[perturbation-theory-second-quantization|perturbation theory in second quantization]] (Part 4, Chapter 10).
- [[rspt-wigner-rule-and-hylleraas-functional|The $2n+1$ rule and the Hylleraas functional]] (Part 4).
- [[molecular-properties-and-response|Molecular properties as energy derivatives]] (Part 4, Chapter 16).
- [[one-particle-greens-function|The one-particle Green's function]] (Part 4, Chapter 17).
- Time-dependent perturbation theory (Chapter 11) and the Born series (Chapter 10).

## The main ideas, in order

1. **Nondegenerate theory.** Energies through fourth order with intermediate normalization, and the two-state model as a check on convergence.
2. **Degenerate theory.** Diagonalize the perturbation in the degenerate subspace to find the "good" zeroth-order states.
3. **Applications to hydrogen.** The quadratic Stark effect from parity; fine structure depending only on $n$ and $j$; Zeeman splitting in weak, strong and intermediate fields; the 21 cm hyperfine line.
4. **Green's functions.** The resolvent, its spectral representation, and the Dyson-type integral equation.

## How to read it

**Path.** [[rayleigh-schrodinger-perturbation-theory]], then [[degenerate-perturbation-theory]], worked in full on [[helium-excited-states-perturbation|the 1s2s and 1s2p states of helium]], and its applications to hydrogen: [[stark-effect]], [[hydrogen-fine-structure]], [[zeeman-effect]], [[hyperfine-splitting-hydrogen]]. [[greens-functions-single-particle]] closes the chapter.

**Needs.** Chapter 3 (formalism), Chapter 4 (hydrogen, spin, addition of angular momenta), and parity from Chapter 6.

**Leads to.** Chapter 10 (Born series), Chapter 11 (time-dependent perturbation theory), Part 4, Chapters 10, 16 and 17.

**Planned sections:** none here. Time-dependent perturbation theory is in Chapter 11: [[time-dependent-perturbation-theory]].
