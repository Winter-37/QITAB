The rules of quantum mechanics restated for information processing: states, unitary evolution, general measurements and composite systems, and the first proof that quantum correlations are not classical (Nielsen and Chuang, Ch. 2).

## What this chapter is about

Part 2 developed quantum mechanics around wave functions and observables. Quantum information needs the same theory in a sharper form, for three reasons:

- systems are finite-dimensional;
- operations are discrete unitaries applied on purpose;
- measurements are not only of observables but of any set of operators $\{M_m\}$ with $\sum_mM_m^\dagger M_m=I$.

This chapter states the four postulates in that form and draws out the measurement theory: projective measurements, POVMs, and the impossibility of distinguishing non-orthogonal states. It ends with Bell's inequality, which shows that no theory with pre-existing local values can reproduce quantum correlations.

## Why it matters

- **Everything in Part 5 rests on it.** Gates are Postulate 2, readout is Postulate 3, and registers are Postulate 4.
- **Measurement is the bottleneck of near-term algorithms.** A quantum computer returns samples, not amplitudes. Projective measurements and their statistics decide how many shots VQE needs and what SQD can extract.
- **Indistinguishability is a resource and a limit.** Non-orthogonal states cannot be told apart reliably. That limit protects quantum key distribution and forbids copying unknown states.
- **Entanglement is non-classical.** The CHSH violation, $2\sqrt2$ against a classical bound of 2, is the cleanest statement of what quantum correlations add.

## Where it is used later

- [[qubits-and-the-bloch-sphere|Qubits]] and [[multi-qubit-states-and-bell-states|Bell states]] (Chapter 2), and [[single-qubit-gates-and-rotations|gates]] (Chapter 3).
- [[variational-quantum-eigensolver|VQE]] and [[sample-based-quantum-diagonalization|SQD]] (Part 6), where measurement statistics set the cost.
- [[concentration-inequalities-and-sampling|Shot-count estimates]] (Part 0, Chapter 5).

## The main ideas, in order

1. **Postulates.** State space, unitary evolution, measurement operators and tensor products, plus their density-operator form. Any measurement is a unitary on system plus ancilla followed by a projective measurement.
2. **Measurements.** Projective measurements and POVMs. Non-orthogonal states cannot be distinguished, but they can be identified unambiguously some of the time.
3. **Bell inequalities.** EPR anticorrelation, the CHSH bound of 2, the quantum value $2\sqrt2$ and Tsirelson's proof that it is maximal, and Sakurai's three-direction form.

## How to read it

**Path.** [[quantum-postulates-for-information]], [[projective-and-povm-measurements]], then [[epr-and-bell-inequalities]] (which uses Bell states from Chapter 2; read [[multi-qubit-states-and-bell-states]] first if they are unfamiliar).

**Needs.** Part 2, Chapter 3 (Hilbert space, the statistical interpretation, density operators). Part 0, Chapter 7 (tensor products).

**Leads to.** Chapters 2 and 3; noise and error correction (Chapter 6).

**Checkpoint.** Show that a general measurement can be realized with an ancilla. Then reproduce the CHSH value $2\sqrt2$ for the singlet from $\langle(\mathbf a\cdot\boldsymbol\sigma)\otimes(\mathbf b\cdot\boldsymbol\sigma)\rangle=-\mathbf a\cdot\mathbf b$.

**Planned sections:** Quantum channels and the operator-sum representation; Distance measures (trace distance, fidelity); No-cloning theorem.
