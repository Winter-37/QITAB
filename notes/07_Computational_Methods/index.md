The numerical and programming techniques behind the methods of Parts 4 and 6.

## What this part is about

Every method in this notebook ends in a computation:

- diagonalizing large matrices;
- solving linear and nonlinear equations iteratively;
- optimizing many parameters;
- organizing code that runs on many cores.

This part collects those algorithms and practices in one place.

## Why it is here

The method chapters state *what* is computed. Whether the computation is feasible depends on *how*:

- **Davidson and Krylov solvers** make large CI and response calculations possible.
- **DIIS and quasi-Newton methods** make SCF and coupled-cluster iterations converge.
- **Low-rank decompositions** reduce memory and cost.

Keeping these in their own part avoids repeating them in every method note.

## How to read it

As a reference, when a method note points here. All chapters are planned.
