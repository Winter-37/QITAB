---
id: fourier-transforms-and-the-dirac-delta
title: Fourier transforms and the Dirac delta function
summary: The Fourier transform in the symmetric convention used by Griffiths, F(k) = (2π)^{-1/2} ∫ f(x) e^{-ikx} dx, with Plancherel's theorem, the Gaussian and box transforms, the uncertainty product σ_x σ_k ≥ 1/2, and the convolution theorem. The delta function as a limit of nascent functions, with δ(cx) = δ(x)/|c|, δ(g(x)) = Σ δ(x − x_i)/|g′(x_i)| and ∫e^{ikx}dk = 2πδ(x). The position-momentum overlap ⟨x|p⟩ = e^{ipx/ħ}/√(2πħ) as a Fourier kernel, and the discrete Fourier transform in the convention of quantum computing.
status: in-progress
kind: theory
level: introductory
tags: [fourier-transform, plancherel-theorem, dirac-delta, nascent-delta, convolution, gaussian-integral, discrete-fourier-transform, momentum-space, griffiths, sakurai, nielsen-chuang]
prerequisites: [fourier-series, orthonormal-functions-and-operators, dirac-notation]
related: [free-particle-and-wave-packets, delta-function-potential, position-momentum-and-energy-representations, generalized-uncertainty-principle, groups-representations-and-characters, probability-and-random-variables]
order: 60
date: 2026-11-17
---

## The transform pair

For a function $f(x)$ on the real line define

$$
\boxed{\,F(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty f(x)\,e^{-ikx}\,dx ,\qquad f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty F(k)\,e^{ikx}\,dk\,}
$$

$F$ is the Fourier transform of $f$ and $f$ the inverse transform of $F$; only the sign in the exponent differs. This symmetric convention, with $1/\sqrt{2\pi}$ on both sides, is Griffiths'. Other books put $1/2\pi$ on one side only, or use $e^{\mp2\pi i\nu x}$. Factors of $2\pi$ in formulas taken from different sources must be checked against the convention.

**Plancherel's theorem.** The inversion formula is the content of Plancherel's theorem, valid for square-integrable $f$; it can be obtained from the Fourier series on an interval of length $L$ by letting $L\to\infty$. It also gives the **Parseval** identity

$$
\int_{-\infty}^\infty|f(x)|^2\,dx = \int_{-\infty}^\infty|F(k)|^2\,dk ,
$$

so a normalized wave function has a normalized transform. In quantum mechanics this is why $\Phi(p,t)$, the momentum-space wave function, is as legitimate a description as $\Psi(x,t)$ ([[position-momentum-and-energy-representations]]).

**Basic properties** (direct from the definition):

| $f(x)$ | $F(k)$ |
|---|---|
| $f(x - a)$ | $e^{-ika}F(k)$ |
| $e^{ik_0x}f(x)$ | $F(k - k_0)$ |
| $f(ax)$ | $F(k/a)/|a|$ |
| $f'(x)$ | $ik\,F(k)$ |
| $x\,f(x)$ | $i\,F'(k)$ |
| $f^*(x)$ | $F^*(-k)$ |

The derivative rule is what turns $-i\hbar\,d/dx$ into multiplication by $\hbar k = p$ in momentum space.

## Two transforms worth knowing

**Gaussian.** Completing the square, $\int e^{-ax^2 + bx}dx = \sqrt{\pi/a}\,e^{b^2/4a}$ for $\mathrm{Re}\,a>0$ and any complex $b$, so

$$
f(x) = e^{-ax^2}\quad\Longrightarrow\quad F(k) = \frac{1}{\sqrt{2a}}\,e^{-k^2/4a} .
$$

A Gaussian transforms into a Gaussian, and the widths are inversely related. For the normalized packet $\psi = (2a/\pi)^{1/4}e^{-ax^2}$, $\sigma_x = 1/(2\sqrt a)$ and $\sigma_k = \sqrt a$, so $\sigma_x\sigma_k = \tfrac12$ exactly. (For $a = 0.7$: $\sigma_x = 0.597614$, $\sigma_k = 0.836660$, product $0.500000$ by numerical quadrature, and $\int|F|^2dk = 1.000000$.) For any other shape the product is larger: this is the uncertainty principle $\sigma_x\sigma_p\ge\hbar/2$ written for Fourier pairs ([[generalized-uncertainty-principle]]).

**Box.** $f = A$ for $|x|<a$, zero outside:

$$
F(k) = \sqrt{\frac2\pi}\,A\,\frac{\sin ka}{k} .
$$

A sharp edge produces a slowly decaying transform ($\sim1/k$), with zeros at $k = n\pi/a$. This is Griffiths' Example 2.6, a free particle released from a box.

**Convolution theorem.** With $(f*g)(x) = \int f(x')g(x - x')\,dx'$,

$$
\mathcal F[f*g](k) = \sqrt{2\pi}\,F(k)\,G(k) .
$$

(Checked numerically for $f = e^{-x^2}$, $g = e^{-|x|}$ at $k = 0.6$: both sides 0.950363.)

## The Dirac delta function

The delta function is defined by what it does under an integral:

$$
\int_{-\infty}^\infty f(x)\,\delta(x - a)\,dx = f(a)
$$

for every continuous $f$. It is not a function but a distribution (a linear map from functions to numbers). Two expressions containing delta functions are equal if they give the same result under every such integral. The completeness relation for any orthonormal basis produces one ([[orthonormal-functions-and-operators]]).

**Nascent delta functions.** Any family of peaks of unit area that narrow to zero width tends to $\delta(x)$:

| family $\delta_\epsilon(x)$ | $\int f\delta_\epsilon$ for $\epsilon = 0.3,\ 0.1,\ 0.03$ |
|---|---|
| Gaussian $\frac{1}{\sqrt{2\pi}\epsilon}e^{-x^2/2\epsilon^2}$ | 0.93092, 0.99175, 0.99925 |
| Lorentzian $\frac{1}{\pi}\frac{\epsilon}{x^2 + \epsilon^2}$ | 0.73701, 0.89914, 0.96812 |
| $\frac{\sin(x/\epsilon)}{\pi x}$ | 0.99787, 1.00000, 1.00000 |

(For $f(x) = \cos x\,e^{-x^2/3}$, $f(0) = 1$.) The Gaussian converges as $\epsilon^2$; the Lorentzian only as $\epsilon$, because its tails fall off slowly; the oscillating sinc family converges fastest here because $f$ is smooth. The Lorentzian is the limit met as $\mathrm{Im}[1/(x - i\epsilon)]/\pi$ in Green's functions and scattering, where $1/(x\mp i\epsilon) = \mathcal P(1/x)\pm i\pi\delta(x)$.

**Rules.**

$$
\delta(cx) = \frac{\delta(x)}{|c|} ,\qquad \delta\big(g(x)\big) = \sum_i\frac{\delta(x - x_i)}{|g'(x_i)|}\ \ (g(x_i) = 0,\ g'(x_i)\neq0) ,\qquad f(x)\,\delta(x - a) = f(a)\,\delta(x - a) .
$$

The absolute value matters for negative $c$. Checks with a narrow Gaussian: $\int f(x)\delta(-2.5x)\,dx = 0.399995$ against $f(0)/2.5 = 0.4$, and $\int f(x)\delta(x^2 - 1)\,dx = 0.38716$ against $[f(1) + f(-1)]/2 = 0.38714$. The step function $\theta(x)$ has $d\theta/dx = \delta(x)$.

**Fourier representation.** The transform of $\delta(x)$ is the constant $1/\sqrt{2\pi}$, and inverting it gives

$$
\delta(x) = \frac{1}{2\pi}\int_{-\infty}^\infty e^{ikx}\,dk .
$$

The integral does not converge as an ordinary integral; it means the limit of $\frac{1}{2\pi}\int_{-K}^Ke^{ikx}dk = \sin(Kx)/(\pi x)$, the sinc family above with $\epsilon = 1/K$. Griffiths remarks that the formula offends mathematicians because $\delta$ is not square-integrable, so Plancherel's theorem does not strictly apply.

## Position and momentum

In Dirac notation, with $\langle x|x'\rangle = \delta(x - x')$ and $\langle p|p'\rangle = \delta(p - p')$, the overlap of position and momentum eigenstates is

$$
\langle x|p\rangle = \frac{1}{\sqrt{2\pi\hbar}}\,e^{ipx/\hbar} ,
$$

the normalization fixed by $\int\langle x|p\rangle\langle p|x'\rangle\,dp = \delta(x - x')$. Inserting $\int|p\rangle\langle p|\,dp = 1$,

$$
\psi(x) = \frac{1}{\sqrt{2\pi\hbar}}\int\phi(p)\,e^{ipx/\hbar}\,dp ,\qquad \phi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int\psi(x)\,e^{-ipx/\hbar}\,dx ,
$$

the transform pair above with $k = p/\hbar$. Sakurai remarks that the formalism "knows" Fourier's inversion theorem: it follows from the completeness of the two bases.

## The discrete Fourier transform

For a vector $(x_0,\dots,x_{N-1})$, the discrete Fourier transform used in quantum computing is

$$
y_k = \frac{1}{\sqrt N}\sum_{j=0}^{N-1}x_j\,e^{2\pi ijk/N} ,\qquad F_{kj} = \frac{e^{2\pi ijk/N}}{\sqrt N} .
$$

The matrix $F$ is unitary (the discrete Parseval identity). The sign of the exponent is opposite to the continuous convention above and to NumPy's `fft`: with this definition $y = \sqrt N\,\mathtt{ifft}(x)$. Other checked properties ($N = 8$): $F^2$ is the parity permutation $j\to-j$ mod $N$, $F^4 = 1$ (so the eigenvalues are $\pm1,\pm i$), and a cyclic shift $x_j\to x_{j-1}$ multiplies $y_k$ by $e^{2\pi ik/N}$. Direct evaluation costs $N^2$ operations; the fast Fourier transform needs $O(N\log N)$; the quantum Fourier transform applies $F$ to the amplitudes of a state of $\log_2N$ qubits with $O(\log^2N)$ gates.

The rows of $F$ are the characters $e^{2\pi ijk/N}$ of the cyclic group $\mathbb Z_N$, and the DFT is the Fourier transform on that group ([[groups-representations-and-characters]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.4, Eqs. (2.101)-(2.104) (Plancherel's theorem, Eq. (2.103)), Example 2.6 (box), Problems 2.19 (proof of Plancherel's theorem from Fourier series), 2.21 (Gaussian packet; completing the square, Eq. (2.111)); Sec. 2.5.2, Eqs. (2.114)-(2.116) (delta function); Problems 2.23 ($\delta(cx)$, Eq. (2.145), and the step function), 2.26 (Fourier representation of $\delta$, Eq. (2.147)), 2.31 (delta as a limit of rectangles). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 1.7, pp. 47-53 (position eigenkets and $\delta$ normalization (1.233)-(1.234); $\langle x|p\rangle$ (1.264); the transform pair (1.266); the Gaussian wave packet (1.267)-(1.274)); Appendix F, pp. 535-541 (complex variables and contour integrals, for the $i\epsilon$ prescriptions).

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 5.1, Eq. (5.1), p. 217 (discrete Fourier transform); Appendix 2, Sec. A2.3, p. 615 (Fourier transforms on groups).

The table of properties, $\delta(g(x))$ and the nascent-delta comparison are standard results written in my own words; all numbers are computed in `mathematics/part0_batch5.py` (section C).
