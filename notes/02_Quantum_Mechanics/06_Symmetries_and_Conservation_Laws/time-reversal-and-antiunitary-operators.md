---
id: time-reversal-and-antiunitary-operators
title: Time reversal and antiunitary operators
summary: Time reversal reverses motion, and it must be antiunitary: Θ = UK, unitary times complex conjugation. Covers why (a unitary Θ would reverse the sign of energy), the transformation x → x, p → −p, J → −J, the reality of nondegenerate wave functions of spinless systems, the operator Θ = exp(−iπJ_y/ħ)K and its action Θ|j,m⟩ = (−1)^{j−m}|j,−m⟩, Θ² = (−1)^{2j}, the constraint on expectation values of tensor operators (no permanent electric dipole moment), Kramers degeneracy for odd numbers of spin-1/2 particles, and its removal by a magnetic field.
status: in-progress
kind: theory
level: advanced
tags: [time-reversal, antiunitary, antilinear, complex-conjugation, kramers-degeneracy, electric-dipole-moment, discrete-symmetry, sakurai]
prerequisites: [symmetry-conservation-and-degeneracy, wigner-rotation-matrices, spin-one-half]
related: [parity-and-parity-selection-rules, spherical-tensor-operators, minimal-coupling-and-aharonov-bohm, hf-solution-classification, ghf]
order: 45
date: 2026-11-15
---

## What time reversal means

Classically, if $\mathbf x(t)$ solves Newton's equations in a potential, so does $\mathbf x(-t)$: the film run backwards is also a possible motion, with every velocity reversed. In a magnetic field this fails, because the Lorentz force is odd in the velocity, unless the field is reversed too. "Time reversal" in quantum mechanics is the corresponding operation on states: **reversal of motion**, not a backward running of time.

The short treatment in [[symmetry-conservation-and-degeneracy]] defines $\Theta\Psi = \Psi^*$ for a spinless particle and proves Kramers' theorem. This note gives the general theory.

## Why Θ must be antiunitary

Let $|\alpha\rangle$ evolve for a short time $\delta t$, then be time reversed; or be time reversed first and evolve backwards by $\delta t$. If time reversal is a symmetry, the two must agree:

$$
\Big(1 - \frac{iH\delta t}{\hbar}\Big)\Theta|\alpha\rangle = \Theta\Big(1 - \frac{iH(-\delta t)}{\hbar}\Big)|\alpha\rangle \quad\Rightarrow\quad -iH\Theta = \Theta iH .
$$

If $\Theta$ were linear the $i$ could be cancelled, giving $H\Theta = -\Theta H$. Then $\Theta|n\rangle$ would have energy $-E_n$ for every eigenstate, which is absurd for a free particle (whose energies are bounded below). So $\Theta$ cannot be linear. It must be **antilinear**, $\Theta(c_1|\alpha\rangle + c_2|\beta\rangle) = c_1^*\Theta|\alpha\rangle + c_2^*\Theta|\beta\rangle$, so that $\Theta i = -i\Theta$ and the condition becomes

$$
\Theta H = H\Theta .
$$

Wigner showed that a symmetry preserving all transition probabilities $|\langle\beta|\alpha\rangle|^2$ is, up to phases, either unitary or **antiunitary**:

$$
\langle\tilde\beta|\tilde\alpha\rangle = \langle\beta|\alpha\rangle^* ,\qquad |\tilde\alpha\rangle = \Theta|\alpha\rangle .
$$

Every antiunitary operator can be written

$$
\Theta = UK ,
$$

with $U$ unitary and $K$ complex conjugation of the components in a fixed basis, $K\sum_ac_a|a\rangle = \sum_ac_a^*|a\rangle$. $K$ depends on the basis; the product $UK$ does not, once $U$ is adjusted.

**Notation.** Bra-ket notation is built for linear operators. With an antiunitary $\Theta$, an expression such as $\langle\beta|\Theta|\alpha\rangle$ must be read as $\langle\beta|\cdot(\Theta|\alpha\rangle)$; letting $\Theta$ act to the left is not allowed. For a linear operator $A$ the useful identity is

$$
\langle\beta|A|\alpha\rangle = \langle\tilde\alpha|\Theta A^\dagger\Theta^{-1}|\tilde\beta\rangle .
$$

## Transformation of operators

An observable is called even or odd under time reversal according as $\Theta A\Theta^{-1} = \pm A$. Since the expectation value of a position measurement should be unchanged and that of momentum reversed,

$$
\Theta\mathbf x\Theta^{-1} = \mathbf x ,\qquad \Theta\mathbf p\Theta^{-1} = -\mathbf p ,\qquad \Theta\mathbf J\Theta^{-1} = -\mathbf J .
$$

These are consistent with $[x_i,p_j] = i\hbar\delta_{ij}$ only because $\Theta$ conjugates the $i$; a unitary operator with these properties could not exist. In the position representation of a spinless particle, $K$ alone does the job: $\Theta\psi(\mathbf x) = \psi^*(\mathbf x)$, and a momentum eigenfunction $e^{i\mathbf p\cdot\mathbf x/\hbar}$ becomes $e^{-i\mathbf p\cdot\mathbf x/\hbar}$.

**Real wave functions.** If $\Theta H = H\Theta$ and $|n\rangle$ is a nondegenerate eigenstate, $\Theta|n\rangle$ has the same energy and must be proportional to $|n\rangle$. For a spinless particle this means $\psi_n^* = e^{i\delta}\psi_n$: the wave function is real up to an overall phase. This is why nondegenerate bound states in a real potential can always be taken real. Degenerate states need not be (a plane wave is complex, but degenerate with its conjugate). A numerical check: the eigenvectors of a random real symmetric matrix are real; adding an imaginary antisymmetric part, the matrix form of a $\mathbf p\cdot\mathbf A$ term, makes them irreducibly complex.

For orbital angular momentum, $Y_l^{m*} = (-1)^mY_l^{-m}$, so $\Theta|l,m\rangle = (-1)^m|l,-m\rangle$ with $K$ acting on wave functions.

## Spin and the general angular momentum state

With spin, complex conjugation in the $S_z$ basis leaves $S_x$ and $S_z$ unchanged and reverses only $S_y$ (whose matrix is imaginary). A further rotation by $\pi$ about $y$ reverses $S_x$ and $S_z$. Hence

$$
\boxed{\,\Theta = \eta\,e^{-i\pi J_y/\hbar}\,K\,}\qquad|\eta| = 1 ,
$$

with $K$ acting on the standard basis $|j,m\rangle$, in which $J_y$ is imaginary and $e^{-i\pi J_y/\hbar}$ is real. Numerically, $\Theta\mathbf J\Theta^{-1} = -\mathbf J$ holds for $j = \tfrac12$ to 2. Using $d^{(j)}_{m'm}(\pi) = (-1)^{j-m}\delta_{m',-m}$ ([[wigner-rotation-matrices]]),

$$
\Theta|j,m\rangle = \eta\,(-1)^{j-m}\,|j,-m\rangle .
$$

The phase $\eta$ is conventional. For integer $j$, $\eta = (-1)^j$ gives $\Theta|j,m\rangle = (-1)^m|j,-m\rangle$, matching the orbital case. For spin $\tfrac12$ with $\eta = 1$, $\Theta = -i\sigma_yK$, which maps $(c_+,c_-)$ to $(-c_-^*,\ c_+^*)$, Griffiths' convention.

**$\Theta^2$.** Applying $\Theta$ twice, $\Theta^2 = |\eta|^2e^{-2\pi iJ_y/\hbar}$ on states of angular momentum $j$, which is $(-1)^{2j}$:

$$
\Theta^2 = +1\ \ (j\text{ integer}) ,\qquad \Theta^2 = -1\ \ (j\text{ half-integer}) .
$$

For a system of several particles this is the parity of the number of spin-$\tfrac12$ particles: $\Theta^2 = (-1)^{N}$ for $N$ electrons.

## Consequences

**Kramers degeneracy.** If $\Theta H = H\Theta$ and $\Theta^2 = -1$, then $|n\rangle$ and $\Theta|n\rangle$ have the same energy and are orthogonal. Antiunitarity gives $\langle\Theta\alpha|\Theta\beta\rangle = \langle\beta|\alpha\rangle$; with $|\alpha\rangle = |n\rangle$ and $|\beta\rangle = \Theta|n\rangle$ this reads $\langle\Theta n|\Theta^2n\rangle = \langle\Theta n|n\rangle$, and since $\Theta^2n = -n$ the overlap equals minus itself and vanishes. Every level of a time-reversal-invariant system with an odd number of electrons is at least doubly degenerate, however low its spatial symmetry and whatever the spin-orbit coupling.

!!! example "Kramers pairs in random spin Hamiltonians"

    $N$ spins $\tfrac12$ coupled by random two-spin terms $\sum J^{ab}_{pq}\sigma^a_p\sigma^b_q$ (even under $\Theta$, since each $\sigma$ is odd), with $\Theta = \prod_p(-i\sigma_y^{(p)})K$:

    | $N$ | $\Theta^2$ | spectrum all doubly degenerate? | with a field $0.3\sum_p\sigma_z^{(p)}$ |
    |---|---|---|---|
    | 2 | $+1$ | no | no |
    | 3 | $-1$ | yes | no |
    | 4 | $+1$ | no | no |
    | 5 | $-1$ | yes | no |

    For $N = 3$ the levels are $-9.043$ (twice), $-1.365$ (twice), $2.694$ (twice), $7.713$ (twice). A magnetic field term is odd under $\Theta$ and splits every pair.

**Magnetic fields.** Terms such as $\mathbf S\cdot\mathbf B$ or $\mathbf p\cdot\mathbf A + \mathbf A\cdot\mathbf p$ with an external field are odd under $\Theta$ (the field, produced by currents outside the system, is not reversed). They break time-reversal symmetry, lift Kramers degeneracy and allow complex nondegenerate wave functions ([[minimal-coupling-and-aharonov-bohm]]). An electrostatic potential $e\phi(\mathbf x)$ is even and changes nothing.

**Expectation values of tensor operators.** Let $T^{(k)}_q$ be a Hermitian spherical tensor ([[spherical-tensor-operators]]) with $\Theta T^{(k)}_0\Theta^{-1} = \pm T^{(k)}_0$, and let the states $|\alpha,j,m\rangle$ transform as above with $\alpha$ unchanged. Time reversal gives

$$
\langle\alpha,j,m|T^{(k)}_0|\alpha,j,m\rangle = \pm\langle\alpha,j,-m|T^{(k)}_0|\alpha,j,-m\rangle ,
$$

while the Wigner-Eckart theorem gives the same two matrix elements in the ratio of $\langle jk;m0|jm\rangle$ and $\langle jk;-m0|j,-m\rangle$, which differ by $(-1)^k$ (checked with SymPy). Unless $\pm(-1)^k = +1$ the expectation value vanishes. The electric dipole operator $e\mathbf x$ is even under $\Theta$ with $k = 1$: a state of definite $j$ and $m$ in a time-reversal-invariant system has **no permanent electric dipole moment**. The magnetic moment is odd with $k = 1$ and is allowed. Parity gives the same conclusion for the electric dipole independently; a measured permanent electric dipole moment of an elementary particle would violate both symmetries.

**What time reversal does not give.** Unlike a unitary symmetry, $\Theta$ does not commute with $H$ in a way that yields a conserved quantum number: $\Theta$ is not an observable, and there is no "time-reversal parity" of a state. Its consequences are degeneracies, reality conditions and selection rules of the kind above.

In electronic structure the same structure decides which broken-symmetry Hartree-Fock solutions are possible, since the Fock operator can lose time-reversal symmetry when complex orbitals are allowed ([[hf-solution-classification]], [[ghf]]).

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 4.4, pp. 271-285: motivation (4.105)-(4.112); antiunitary operators, $\Theta = UK$ and Wigner's theorem (4.4.1, Eqs. (4.113)-(4.124)); the time-reversal operator, $\Theta H = H\Theta$ (4.134), transformation of $\mathbf x$, $\mathbf p$ and $\mathbf J$ (4.135)-(4.156) (4.4.2); wave functions, reality of nondegenerate eigenfunctions and $Y_l^m$ (4.157)-(4.163) (4.4.3); spin, $\Theta = \eta e^{-i\pi J_y/\hbar}K$, $\Theta^2 = \pm1$ and the phase conventions (4.164)-(4.181), expectation values of tensor operators (4.182)-(4.187) (4.4.4); electric and magnetic fields and Kramers degeneracy (4.188)-(4.194) (4.4.5).

The random-Hamiltonian checks and the remark on Hartree-Fock are my additions, computed in `sakurai/companions_ch2_ch4.py` (section E). Wigner's theorem on unitary and antiunitary symmetries is quoted, not proved, as in Sakurai.
