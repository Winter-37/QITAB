---
id: interaction-picture-and-dyson-series
title: The interaction picture and the Dyson series
summary: For H = H0 + V(t), the interaction picture removes the trivial evolution under H0 so that states move only under V. The evolution operator then obeys an integral equation whose iteration is the Dyson series, a time-ordered expansion in powers of V. Its matrix elements between H0 eigenstates are the transition amplitudes of time-dependent perturbation theory. The order-by-order convergence is checked numerically on a three-level system.
status: in-progress
kind: derivation
level: advanced
tags: [interaction-picture, dirac-picture, dyson-series, time-ordering, time-evolution-operator, transition-amplitude, pictures, sakurai]
prerequisites: [heisenberg-picture-and-time-translation, two-level-systems-and-rabi-oscillations]
related: [time-dependent-perturbation-theory, fermi-golden-rule-and-decay-width, rayleigh-schrodinger-perturbation-theory, born-approximation-and-lippmann-schwinger]
order: 20
date: 2026-11-15
---

## The problem

Let $H = H_0 + V(t)$, where $H_0$ is time-independent with known eigenstates, $H_0|n\rangle = E_n|n\rangle$, and $V(t)$ may depend on time explicitly. Because $H$ depends on time there are no stationary states; the question is how an initial eigenstate $|i\rangle$ of $H_0$ spreads into the others. The evolution under $H_0$ alone is known and uninteresting, so it pays to remove it.

## The interaction picture

Define the interaction-picture state and operators (with $t_0 = 0$ as the reference time) by

$$
|\alpha,t\rangle_I = e^{iH_0t/\hbar}\,|\alpha,t\rangle_S ,\qquad A_I(t) = e^{iH_0t/\hbar}\,A_S\,e^{-iH_0t/\hbar} .
$$

Expectation values are unchanged, $\,_I\langle\alpha,t|A_I|\alpha,t\rangle_I = \,_S\langle\alpha,t|A_S|\alpha,t\rangle_S$. Differentiating the first definition and using the Schrödinger equation,

$$
\boxed{\,i\hbar\frac{\partial}{\partial t}|\alpha,t\rangle_I = V_I(t)\,|\alpha,t\rangle_I ,\qquad V_I(t) = e^{iH_0t/\hbar}\,V(t)\,e^{-iH_0t/\hbar}\,}
$$

while the operators obey a Heisenberg-like equation with $H_0$ alone, $dA_I/dt = (1/i\hbar)[A_I,H_0]$ for $A_S$ without explicit time dependence.

| | Schrödinger | interaction (Dirac) | Heisenberg |
|---|---|---|---|
| state | evolves with $H$ | evolves with $V_I$ | fixed |
| operators | fixed | evolve with $H_0$ | evolve with $H$ |

The interaction picture is intermediate between the two pictures of [[heisenberg-picture-and-time-translation]]: if $V = 0$ it is the Heisenberg picture, and all of the state's motion is due to $V$.

**Amplitude equations.** Expanding $|\alpha,t\rangle_I = \sum_nc_n(t)|n\rangle$ and projecting on $\langle n|$,

$$
i\hbar\,\dot c_n(t) = \sum_mV_{nm}(t)\,e^{i\omega_{nm}t}\,c_m(t) ,\qquad \omega_{nm} = \frac{E_n - E_m}{\hbar} ,\quad V_{nm} = \langle n|V(t)|m\rangle .
$$

These are exact coupled equations. The $c_n$ are the same coefficients as in $|\alpha,t\rangle_S = \sum_nc_n(t)e^{-iE_nt/\hbar}|n\rangle$, and for two levels they are the equations of [[two-level-systems-and-rabi-oscillations]].

## The evolution operator and the Dyson series

Define $U_I(t,t_0)$ by $|\alpha,t\rangle_I = U_I(t,t_0)|\alpha,t_0\rangle_I$. It satisfies

$$
i\hbar\frac{d}{dt}U_I(t,t_0) = V_I(t)\,U_I(t,t_0) ,\qquad U_I(t_0,t_0) = 1 ,
$$

which is equivalent to the integral equation

$$
U_I(t,t_0) = 1 - \frac{i}{\hbar}\int_{t_0}^tV_I(t')\,U_I(t',t_0)\,dt' .
$$

Iterating (substituting the equation into its own right-hand side) gives the **Dyson series**:

$$
\boxed{\,U_I(t,t_0) = 1 - \frac{i}{\hbar}\int_{t_0}^tdt'\,V_I(t') + \Big(\!-\frac{i}{\hbar}\Big)^2\int_{t_0}^tdt'\int_{t_0}^{t'}dt''\,V_I(t')V_I(t'') + \cdots\,}
$$

In the $n$-th term the operators are ordered with later times to the left, $t'>t''>\cdots$. This ordering matters because $V_I$ at different times need not commute; it is the reason the answer is not simply $\exp[-(i/\hbar)\int V_I\,dt]$. Introducing the time-ordering symbol $T$, which arranges any product with later times to the left, the $n$-th term can be extended to the full cube $t_0<t',t'',\dots<t$ at the cost of $1/n!$, and the series is written compactly as

$$
U_I(t,t_0) = T\exp\Big[-\frac{i}{\hbar}\int_{t_0}^tV_I(t')\,dt'\Big] .
$$

**Transition amplitudes.** The Schrödinger-picture evolution operator is $U(t,t_0) = e^{-iH_0t/\hbar}\,U_I(t,t_0)\,e^{iH_0t_0/\hbar}$. Between eigenstates of $H_0$ the two differ only by phases, so

$$
c_n(t) = \langle n|U_I(t,t_0)|i\rangle ,\qquad |\langle n|U_I(t,t_0)|i\rangle|^2 = |\langle n|U(t,t_0)|i\rangle|^2 ,
$$

and the successive terms of the series give the first-order, second-order, ... amplitudes of [[time-dependent-perturbation-theory]]. Each term has a simple reading: free propagation under $H_0$ interrupted by one, two, ... actions of $V$, summed over all intermediate states and all times of interaction. This is the time-dependent counterpart of the Born series ([[born-approximation-and-lippmann-schwinger]]) and the starting point of diagrammatic many-body perturbation theory (Part 4, Chapters 10 and 17).

Two cautions. The initial and final states must be eigenstates of $H_0$ for the simple identification above; otherwise expand them in $H_0$ eigenstates first. And a truncated series is not unitary: probabilities computed at finite order do not sum to one, the defect being of the next order.

!!! example "Order-by-order check on a three-level system"

    $H_0 = \mathrm{diag}(0,\,1,\,2.7)$ and $V(t) = \lambda\,e^{-t^2}\,W$ with a fixed real symmetric $3\times3$ matrix $W$ (entries of order one), $\hbar = 1$, from $t = -6$ to $6$. $U_I$ is computed by integrating the Schrödinger equation, and the first two Dyson terms by quadrature. The error is the largest element of the difference.

    | $\lambda$ | $\max|U_I - U^{(\le1)}|$ | divided by $\lambda^2$ | $\max|U_I - U^{(\le2)}|$ | divided by $\lambda^3$ |
    |---|---|---|---|---|
    | 0.4 | 0.220 | 1.38 | 0.0615 | 0.96 |
    | 0.2 | 0.0587 | 1.47 | 0.00807 | 1.01 |
    | 0.1 | 0.0150 | 1.50 | 0.00102 | 1.02 |
    | 0.05 | 0.00378 | 1.51 | 0.000129 | 1.03 |

    The first-order error scales as $\lambda^2$ and the second-order error as $\lambda^3$, as it must if each term of the series is correct.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.5.1-5.5.2, pp. 320-323 (interaction picture, Table 5.2, amplitude equations); Sec. 5.7.1, pp. 337-339 (Dyson series (5.265)); Sec. 5.7.2, pp. 339-340 (transition probability, Eqs. (5.270)-(5.278)).

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018) does not use the interaction picture by name; the multi-level amplitude equations appear in Problem 11.24 and the time-ordered exponential (Dyson's formula) in Problem 11.23, Eqs. (11.108)-(11.112). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

The numerical check is my own, computed in `griffiths/ch11_dynamics.py` (section B).
