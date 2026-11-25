The postulates in their simplest form: what $\Psi$ means, why it stays normalized, how expectation values and momentum enter, and where the uncertainty principle comes from (Griffiths Ch. 1).

## What this chapter is about

Quantum mechanics replaces a particle's trajectory $x(t)$ with a wave function $\Psi(x,t)$ that obeys the Schrödinger equation

$$
i\hbar\,\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + V(x)\,\Psi .
$$

This chapter answers the questions that come before any solving:

- What does $\Psi$ mean? By Born's rule, $|\Psi|^2$ is a probability density.
- Why is that interpretation consistent? Normalization is preserved in time.
- How are measurable quantities obtained? As expectation values.
- Why must momentum be the operator $-i\hbar\,\partial_x$?
- Why can't position and momentum both be sharp?

## Why it matters

Everything later is built on these rules. Several of them are used constantly without comment:

- **Born's rule** is why electron densities, populations and orbital pictures mean anything at all.
- **Expectation values as averages** are what quantum chemistry computes: energies, dipole moments, forces.
- **The probability current and conservation of norm** rest on the Hamiltonian being Hermitian, a requirement that returns in every approximate method.
- **Ehrenfest's theorem** shows when quantum averages follow classical laws and when they do not. This is the first glimpse of how molecular dynamics on a potential surface emerges.
- **The uncertainty principle** is presented here as a property of waves, before the operator proof of Chapter 3.

## Where it is used later

- The generalized statistical interpretation and the operator formalism of Chapter 3 restate these postulates in a basis-independent form.
- [[hellmann-feynman-and-virial-theorems|The Hellmann–Feynman theorem]] computes forces as expectation values (Part 4).
- [[momentum-operator-and-ehrenfest-theorem|Ehrenfest's theorem]] in one dimension becomes the generalized Ehrenfest theorem $d\langle Q\rangle/dt = (i/\hbar)\langle[\hat H,\hat Q]\rangle$ in Chapter 3. Commutators with $\hat H$ give conserved quantities.

## The main ideas, in order

1. **The wave function and Born's rule.** $|\Psi(x,t)|^2dx$ is the probability of finding the particle in $dx$. The three interpretations of measurement (realist, orthodox, agnostic) are compared, and collapse is introduced.
2. **Normalization is conserved.** The Schrödinger equation with a real potential keeps $\int|\Psi|^2dx$ fixed. The local form of this statement is the continuity equation with the probability current $J$.
3. **Expectation values and momentum.** Requiring $\langle p\rangle = m\,d\langle x\rangle/dt$ leads to the momentum operator $-i\hbar\,\partial_x$. Ehrenfest's theorem then gives Newton's law for averages.
4. **Uncertainty.** A wave cannot have both a sharp position and a sharp wavelength. With de Broglie's $p=h/\lambda$ this gives $\sigma_x\sigma_p\ge\hbar/2$, checked on three test states.

## How to read it

**Path.** [[wave-function-and-statistical-interpretation]], [[normalization-and-probability-current]], [[momentum-operator-and-ehrenfest-theorem]], [[de-broglie-and-heisenberg-uncertainty]].

**Needs.** Probability (Part 0, Chapter 8: [[probability-and-random-variables|random variables and expectation values]]) and the Fourier transform (Part 0, Chapter 4).

**Leads to.** Chapter 2 (solving the time-independent equation) and Chapter 3 (the general formalism).

**Planned sections:** none at present.
