What a chemical bond is in quantum-mechanical terms, and how bonds are read back out of a computed wave function.

## What this chapter is about

A molecular wave function has no "bond" operator. The chemist's bonds, lone pairs, bond orders and atomic charges are interpretations of a many-electron function or of its density. This chapter collects the main interpretations and tests each against calculations:

- the two zeroth-order pictures of the electron-pair bond, valence bond and molecular orbital, and why they meet once each is improved;
- what the virial theorem says about the kinetic and potential energy changes when a bond forms;
- how a delocalized closed-shell determinant can be rewritten, without changing it, as localized bonds, lone pairs and hybrids;
- bond orders, atomic charges and the electrostatic potential computed from the density matrix, and how much each depends on arbitrary choices.

## Why it matters

- **Interpretation is not unique.** Canonical and localized orbitals, or Mulliken and ESP charges, can tell different stories about the same wave function. Knowing which quantities are observables (the density, the dipole, the electrostatic potential) and which are conventions (charges, bond orders, orbitals) protects against over-reading a calculation.
- **The pictures have computational consequences.** The MO–VB equivalence is the simplest case of configuration interaction and of generalized valence bond. Localized orbitals are the starting point of low-scaling correlation methods. The virial theorem is a check on any approximate wave function.

## Where it is used later

- [[mcscf-and-gvb]] and [[h2-minimal-basis-correlation-analysis]] (Part 4) take the MO/VB comparison further.
- [[population-analysis]] (Part 4, Chapter 3) gives the density-matrix machinery used here.
- [[molecular-orbitals-of-polyatomic-molecules]] (Chapter 4) supplies the canonical MOs that are localized here.

## The main ideas, in order

1. **MO versus VB.** Equal-weight ionic terms in the MO function, none in Heitler–London; ionic–covalent resonance and MO-CI coincide.
2. **Virial theorem.** At $R_e$ the kinetic energy is higher and the potential energy lower than in the atoms; at large $R$ the reverse.
3. **Localized MOs.** Unitary invariance of a determinant; Edmiston–Ruedenberg, Boys and Pipek–Mezey; equivalent orbitals and hybrids; banana bonds.
4. **Bond orders and charges.** Overlap populations, Mayer bond orders, the electrostatic potential, and charge schemes from Mulliken to Hirshfeld.

## How to read it

**Path.** [[mo-and-valence-bond-theories]], [[virial-theorem-and-chemical-bonding]], [[localized-molecular-orbitals]], [[bond-orders-and-atomic-charges]].

**Needs.** Part 2: [[hydrogen-molecule-ion-variational]] and [[hydrogen-molecule-heitler-london]]. Part 4: Slater determinants (Chapter 2), RHF and population analysis (Chapter 3), the virial theorem (Chapter 1). The last two sections use the canonical MOs of Chapter 4 of this part, which can be read first or alongside.

**Leads to.** Chapter 4 of this part (MO theory), and in Part 4 the correlation chapters (9, 13).

**Core (first pass).** [[mo-and-valence-bond-theories]], [[localized-molecular-orbitals]]. **Deep.** [[virial-theorem-and-chemical-bonding]], [[bond-orders-and-atomic-charges]].

**Checkpoint.** Show that $(a+b)(a+b) + \gamma(a-b)(a-b)$ equals the covalent function plus $\delta$ times the ionic one with $\delta = (1+\gamma)/(1-\gamma)$. Then explain why the LCAO with exponent 1 lowers the kinetic energy of H₂⁺ while the exact wave function raises it.

**Planned sections:** Bond energies and additivity; Hyperconjugation and the ethane barrier; Natural bond orbitals.
