---
id: feynman-path-integral
title: Propagators and the Feynman path integral
summary: The propagator K(x, t; x₀, t₀) = ⟨x|U(t, t₀)|x₀⟩ as a transition amplitude, its composition property, and Feynman's reformulation of quantum mechanics as a sum over all paths weighted by exp(iS/ħ). Derives the short-time kernel and the path integral, shows that it reproduces the Schrödinger equation, explains the classical limit by stationary phase, and connects imaginary time to the partition function. Tested numerically: a discretized imaginary-time path integral for the oscillator converges to the exact Z and Mehler kernel with error ∝ 1/P².
status: in-progress
kind: derivation
level: advanced
tags: [path-integral, propagator, transition-amplitude, composition-property, classical-action, stationary-phase, imaginary-time, partition-function, trotter, feynman, sakurai]
prerequisites: [heisenberg-picture-and-time-translation, free-particle-and-wave-packets, density-operators-and-mixed-states]
related: [harmonic-oscillator-ladder-operators, wkb-approximation, greens-functions-single-particle, interaction-picture-and-dyson-series, baker-campbell-hausdorff]
order: 70
date: 2026-11-15
---

## The propagator

For a time-independent Hamiltonian with eigenstates $|a'\rangle$, a state evolves as $|\alpha,t\rangle = \sum_{a'}|a'\rangle\langle a'|\alpha,t_0\rangle e^{-iE_{a'}(t-t_0)/\hbar}$. In the position representation

$$
\psi(\mathbf x'',t) = \int d^3x'\,K(\mathbf x'',t;\mathbf x',t_0)\,\psi(\mathbf x',t_0) ,\qquad K(\mathbf x'',t;\mathbf x',t_0) = \sum_{a'}\langle\mathbf x''|a'\rangle\langle a'|\mathbf x'\rangle\,e^{-iE_{a'}(t-t_0)/\hbar} .
$$

The **propagator** $K$ depends only on the Hamiltonian, not on the initial state. It solves the Schrödinger equation in $(\mathbf x'',t)$ and tends to $\delta^3(\mathbf x'' - \mathbf x')$ as $t\to t_0$. For a free particle in one dimension,

$$
K(x'',t;x',t_0) = \sqrt{\frac{m}{2\pi i\hbar(t-t_0)}}\,\exp\Big[\frac{im(x'' - x')^2}{2\hbar(t-t_0)}\Big] ,
$$

and for the oscillator it is the Mehler kernel of [[heisenberg-picture-and-time-translation]].

**As a transition amplitude.** In terms of Heisenberg-picture position eigenkets, $|\mathbf x',t'\rangle = U^\dagger(t')|\mathbf x'\rangle$,

$$
K(\mathbf x'',t'';\mathbf x',t') = \langle\mathbf x'',t''|\mathbf x',t'\rangle ,
$$

the amplitude for a particle localized at $\mathbf x'$ at time $t'$ to be found at $\mathbf x''$ at time $t''$. Inserting a complete set of position states at an intermediate time gives the **composition property**

$$
\langle\mathbf x'',t''|\mathbf x',t'\rangle = \int d^3x'''\,\langle\mathbf x'',t''|\mathbf x''',t'''\rangle\langle\mathbf x''',t'''|\mathbf x',t'\rangle ,\qquad t''>t'''>t' .
$$

The particle must be somewhere at the intermediate time, and the amplitudes for all intermediate positions add.

**Imaginary time.** Setting $\mathbf x'' = \mathbf x'$, integrating, and putting $t - t_0 = -i\hbar\beta$,

$$
\int d^3x'\,K(\mathbf x',-i\hbar\beta;\mathbf x',0) = \sum_{a'}e^{-\beta E_{a'}} = Z ,
$$

the partition function. More generally $K(\mathbf x'',-i\hbar\beta;\mathbf x',0) = \langle\mathbf x''|e^{-\beta H}|\mathbf x'\rangle$ is the unnormalized thermal density matrix of [[density-operators-and-mixed-states]]. Quantum dynamics in real time and statistical mechanics in imaginary time are governed by the same object.

## Paths and the action

Divide the interval from $t_1$ to $t_N$ into $N-1$ steps of length $\Delta t$ and apply the composition property at every intermediate time:

$$
\langle x_N,t_N|x_1,t_1\rangle = \int dx_{N-1}\cdots dx_2\;\langle x_N,t_N|x_{N-1},t_{N-1}\rangle\cdots\langle x_2,t_2|x_1,t_1\rangle .
$$

Each set $(x_1,x_2,\dots,x_N)$ is a path in the $xt$ plane, and the integral runs over all of them, not only the classical one. Following a remark of Dirac, Feynman proposed that each short step contributes a phase given by the classical action,

$$
S(n,n-1) = \int_{t_{n-1}}^{t_n}L_{\rm cl}(x,\dot x)\,dt ,\qquad L_{\rm cl} = \tfrac12m\dot x^2 - V(x) .
$$

For a short step the path may be taken straight, so $S(n,n-1)\approx\Delta t\,[\tfrac12m((x_n - x_{n-1})/\Delta t)^2 - V(\bar x)]$, and the normalization is fixed by requiring the $V = 0$ case to reproduce the free propagator:

$$
\langle x_n,t_n|x_{n-1},t_{n-1}\rangle = \sqrt{\frac{m}{2\pi i\hbar\Delta t}}\,\exp\Big[\frac{i}{\hbar}S(n,n-1)\Big] .
$$

Taking $N\to\infty$,

$$
\boxed{\,\langle x_N,t_N|x_1,t_1\rangle = \lim_{N\to\infty}\Big(\frac{m}{2\pi i\hbar\Delta t}\Big)^{(N-1)/2}\int dx_{N-1}\cdots dx_2\;\exp\Big[\frac{i}{\hbar}\sum_{n=2}^NS(n,n-1)\Big]\equiv\int_{x_1}^{x_N}\mathcal D[x(t)]\;e^{iS[x(t)]/\hbar}\,}
$$

This is **Feynman's path integral**: the amplitude is a sum over all paths with fixed end points, each weighted by $e^{iS/\hbar}$ with $S$ its classical action. No operators appear.

**Equivalence with the Schrödinger equation.** Apply the short-time kernel to a wave function for one step $\Delta t$ and set $\xi = x - x'$:

$$
\psi(x,t+\Delta t) = \sqrt{\frac{m}{2\pi i\hbar\Delta t}}\int d\xi\,\exp\Big(\frac{im\xi^2}{2\hbar\Delta t} - \frac{iV\Delta t}{\hbar}\Big)\psi(x - \xi,t) .
$$

The Gaussian restricts $\xi$ to $O(\sqrt{\hbar\Delta t/m})$. Expanding $\psi(x-\xi)$ to second order in $\xi$ and the potential factor to first order in $\Delta t$, and using $\langle\xi^2\rangle = i\hbar\Delta t/m$ for this Gaussian, gives $\psi + \Delta t\,\partial\psi/\partial t = \psi - (i\Delta t/\hbar)\big[-\tfrac{\hbar^2}{2m}\partial^2\psi/\partial x^2 + V\psi\big]$, the Schrödinger equation. The path integral is a complete formulation of quantum mechanics, equivalent to the operator one.

## The classical limit

When $\hbar$ is small compared with the actions involved, $e^{iS/\hbar}$ oscillates wildly from path to path and neighbouring paths cancel. The exception is a path at which $S$ is **stationary**, $\delta S = 0$: there the phase changes only to second order in a deformation, and a whole tube of nearby paths adds in phase. Stationarity of the action is Hamilton's principle, so as $\hbar\to0$ the amplitude is dominated by the classical trajectory. This is the stationary-phase approximation, and its next correction reproduces the WKB wave function $e^{iS/\hbar}/\sqrt{p}$ of [[wkb-approximation]].

!!! example "Second variation of the action for the oscillator"

    For $L = \tfrac12\dot x^2 - \tfrac12x^2$ ($m = \omega = 1$), from $x_1 = 0.7$ at $t = 0$ to $x_2 = -0.2$ at $t = T$, the classical action $[(x_1^2 + x_2^2)\cos T - 2x_1x_2]/(2\sin T)$ agrees with direct quadrature. Deforming the classical path by $\varepsilon\sin(\pi t/T)$ changes the action by exactly $\varepsilon^2(\pi^2/T^2 - 1)T/4$, with no linear term:

    | $T$ | $\varepsilon$ | $S - S_{\rm cl}$ |
    |---|---|---|
    | 1.9 | 0.2 | $+0.03295$ |
    | 1.9 | 0.1 | $+0.00824$ |
    | 1.9 | 0.05 | $+0.00206$ |
    | 4.0 | 0.1 | $-0.00383$ |

    For $T<\pi/\omega$ the classical path is a minimum of the action. For $T>\pi/\omega$ (beyond the first focal point, where all paths from $x_1$ reconverge) this deformation lowers the action, so the classical path is a saddle. Hamilton's principle requires only that the action be stationary, which is also all the stationary-phase argument needs.

## Imaginary time: a numerical path integral

With $t\to-i\hbar\tau$ the weight $e^{iS/\hbar}$ becomes $e^{-S_E/\hbar}$, with the Euclidean action $S_E = \int_0^{\hbar\beta}[\tfrac12m\dot x^2 + V(x)]\,d\tau$, which is real and positive. Splitting $e^{-\beta H}$ into $P$ factors and using $e^{-\epsilon(T+V)}\approx e^{-\epsilon V/2}e^{-\epsilon T}e^{-\epsilon V/2}$ (error $O(\epsilon^3)$ per factor, from [[baker-campbell-hausdorff]]),

$$
\langle x''|e^{-\beta H}|x'\rangle\approx\int dx_1\cdots dx_{P-1}\prod_{n=1}^P\sqrt{\frac{m}{2\pi\hbar^2\epsilon}}\exp\Big[-\frac{m(x_n - x_{n-1})^2}{2\hbar^2\epsilon} - \frac\epsilon2\big(V(x_n) + V(x_{n-1})\big)\Big] ,\qquad \epsilon = \beta/P ,
$$

with $x_0 = x'$, $x_P = x''$. A quantum particle at temperature $T$ becomes a classical closed chain ("ring polymer") of $P$ beads joined by springs. This is the basis of path-integral Monte Carlo and path-integral molecular dynamics for nuclear quantum effects.

!!! example "Harmonic oscillator, $\hbar = m = \omega = 1$"

    The integrals over intermediate beads are done by matrix multiplication on a grid of 801 points on $[-8,8]$. The exact results are $Z = 1/[2\sinh(\beta/2)]$ and the Mehler kernel.

    | $P$ | $Z_P$, $\beta = 1$ | relative error | $Z_P$, $\beta = 4$ | relative error |
    |---|---|---|---|---|
    | 1 | 1.000000 | $+4.2\times10^{-2}$ | 0.250000 | $+8.1\times10^{-1}$ |
    | 2 | 0.970143 | $+1.1\times10^{-2}$ | 0.176777 | $+2.8\times10^{-1}$ |
    | 4 | 0.962209 | $+2.8\times10^{-3}$ | 0.149071 | $+8.1\times10^{-2}$ |
    | 8 | 0.960193 | $+7.0\times10^{-4}$ | 0.140792 | $+2.1\times10^{-2}$ |
    | 16 | 0.959686 | $+1.8\times10^{-4}$ | 0.138602 | $+5.4\times10^{-3}$ |
    | 32 | 0.959560 | $+4.4\times10^{-5}$ | 0.138046 | $+1.3\times10^{-3}$ |
    | 64 | 0.959528 | $+1.1\times10^{-5}$ | 0.137907 | $+3.4\times10^{-4}$ |
    | exact | 0.959517 | | 0.137860 | |

    Each doubling of $P$ cuts the error by four: the symmetric splitting is accurate to $O(1/P^2)$. Lower temperatures need more beads. The off-diagonal element $\langle0.5|e^{-\beta H}|-0.3\rangle$ converges the same way (at $\beta = 4$, $P = 64$: 0.064099 against Mehler's 0.064068). At $\beta = 12$, $P = 128$, $-\ln Z/\beta = 0.49982$, approaching the ground-state energy $\tfrac12$, and $\rho(0,0)/Z = 0.5645$ approaches $|\psi_0(0)|^2 = 1/\sqrt\pi = 0.5642$: at low temperature the chain samples the ground state.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 2.6, pp. 109-121: propagators in wave mechanics, the free-particle propagator (2.280), the oscillator, and the connection with the partition function (2.6.1, Eqs. (2.266)-(2.290)); the propagator as a transition amplitude and the composition property (2.292) (2.6.2); path integrals as a sum over paths and Hamilton's principle (2.6.3, Eqs. (2.294)-(2.304)); Feynman's formulation, the short-time kernel (2.310), the path integral (2.313) and its equivalence with the Schrödinger equation (2.314)-(2.320) (2.6.4). Feynman's paper, as cited by Sakurai: R. P. Feynman, Rev. Mod. Phys. 20, 367 (1948). Sakurai's Problem 2.44 asks for the oscillator propagator by the path integral.

Sakurai states Hamilton's principle as minimization of the action; the oscillator example shows it is stationarity in general (my addition). The ring-polymer picture, the symmetric splitting and all numbers are my own, computed in `sakurai/companions_ch2_ch4.py` (section G).
