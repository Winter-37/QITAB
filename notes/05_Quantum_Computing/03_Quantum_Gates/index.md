Unitary operations on qubits: single-qubit rotations, controlled gates, and the gate sets from which every computation can be built (Nielsen and Chuang, Chs. 1 and 4).

## What this chapter is about

A quantum computation is a sequence of gates, unitaries acting on one or two qubits at a time. This chapter covers three things:

- **Single-qubit gates.** What they are and what they do geometrically: rotations of the Bloch sphere, each decomposable into three rotations about two axes.
- **Controlled operations.** How they are assembled from CNOTs and single-qubit gates, from controlled-$U$ up to the Toffoli gate.
- **Universality.** Why a small fixed set suffices. CNOT plus single-qubit gates are exactly universal, and $\{H,S,T,\mathrm{CNOT}\}$ approximates any unitary.

## Why it matters

- **Every chemistry circuit is made of these pieces.** The UCC and LUCJ ansätze, Jordan–Wigner Pauli exponentials and phase estimation are all compiled into single-qubit rotations and CNOT ladders.
- **Gate counts are the cost.** Two-qubit gates dominate the error budget on present hardware, and $T$ gates dominate the cost on fault-tolerant hardware. Knowing that a controlled-$U$ costs two CNOTs and a Toffoli six is how circuit costs are estimated.
- **Universality is not efficiency.** Any unitary can be built, but generic $n$-qubit unitaries need exponentially many gates. Useful algorithms exploit structure, for chemistry the locality of the Hamiltonian.
- **Conventions hide in matrices.** Global phases, rotation-composition order and qubit ordering all change written matrices without changing the physics. Each is checked explicitly here.

## Where it is used later

- [[vqe-ansatze|VQE ansätze]] and [[lucj-ansatz|the LUCJ circuit]] (Part 6).
- [[jordan-wigner-mapping|Pauli-string exponentials]] (Part 6), built from CNOT ladders.
- Circuits, teleportation and algorithms (Chapters 4 and 5, planned).

## The main ideas, in order

1. **Single-qubit gates.** $X,Y,Z,H,S,T$; rotations $R_{\hat n}(\theta)=e^{-i\theta\hat n\cdot\boldsymbol\sigma/2}$ as Bloch-sphere rotations; the Z-Y decomposition $e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta)$; and the $AXBXC$ form.
2. **Controlled operations.** CNOT, CZ, phase kickback and SWAP; controlled-$U$ from two CNOTs; $C^2(U)$ and the Toffoli; Pauli propagation through CNOT; qubit ordering.
3. **Universality.** Two-level unitaries, Gray codes, the $H$–$T$ irrational rotation, the error measure $E(U,V)$, and Solovay–Kitaev.

## How to read it

**Path.** [[single-qubit-gates-and-rotations]], [[controlled-operations]], [[universal-gate-sets]].

**Needs.** Chapter 2 ([[qubits-and-the-bloch-sphere]], [[multi-qubit-states-and-bell-states]]). Rotations and SU(2) (Part 2, Chapter 6). Matrix exponentials (Part 0, Chapter 1).

**Leads to.** Chapter 4 (circuits, measurement, teleportation) and Chapter 5 (algorithms).

**Checkpoint.** Find the $Z$-$Y$ angles of $H$ and its $A,B,C$. Then verify by hand that the two-CNOT circuit gives controlled-$U$, and that $C^2(U)$ with $V^2=U$ leaves the target alone unless both controls are 1.

**Planned sections:** Clifford group and the Gottesman–Knill theorem; Native gate sets and compilation.
