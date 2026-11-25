---
id: probability-and-random-variables
title: Probability and random variables
summary: The probability needed to read quantum mechanics. Discrete and continuous distributions, expectation values, variance and standard deviation (with the shortcut σ² = ⟨x²⟩ − ⟨x⟩²), joint and conditional probabilities, independence, the law of total probability and Bayes' rule, and the binomial, Poisson and Gaussian distributions with their moments. Worked on Griffiths' examples (a room of ages, a falling rock) and on a small quantum state-discrimination problem.
status: in-progress
kind: theory
level: introductory
tags: [probability, random-variable, expectation-value, variance, standard-deviation, conditional-probability, bayes-rule, binomial-distribution, poisson-distribution, gaussian-distribution, griffiths, nielsen-chuang]
prerequisites: []
related: [concentration-inequalities-and-sampling, wave-function-and-statistical-interpretation, generalized-statistical-interpretation, density-operators-and-mixed-states, fourier-transforms-and-the-dirac-delta]
order: 10
date: 2026-11-17
---

## Discrete distributions

A **random variable** $X$ takes values $x$ with probabilities $p(x)\ge0$, $\sum_xp(x) = 1$. If $N(j)$ of $N$ people in a room have age $j$, then $p(j) = N(j)/N$. Three summaries of a distribution:

- the **most probable** value, where $p$ is largest;
- the **median**, with equal probability above and below;
- the **mean** or **expectation value**

$$
\langle j\rangle = E(j) = \sum_jj\,p(j) ,\qquad \langle f(j)\rangle = \sum_jf(j)\,p(j) .
$$

They need not coincide, and the mean need not be a value that ever occurs. In quantum mechanics "expectation value" means the average over many identically prepared systems, not the value expected in one measurement.

**Spread.** The average deviation $\langle j - \langle j\rangle\rangle$ is always zero, so one averages its square:

$$
\sigma^2 = \big\langle(j - \langle j\rangle)^2\big\rangle = \langle j^2\rangle - \langle j\rangle^2 .
$$

$\sigma^2$ is the **variance** and $\sigma$ the **standard deviation**. The second form follows by expanding the square, and it implies $\langle j^2\rangle\ge\langle j\rangle^2$, with equality only when every member has the same value.

!!! example "Ages in a room (Griffiths Sec. 1.3.1)"

    Fourteen people: one aged 14, one 15, three 16, two 22, two 24 and five 25. Then $\langle j\rangle = 21$, $\langle j^2\rangle = 459.57$, and both forms of the variance give $\sigma^2 = 18.57$, $\sigma = 4.31$. The most probable age is 25 and the median 23.

## Continuous distributions

For a continuous variable, $\rho(x)\,dx$ is the probability of a value between $x$ and $x + dx$, and the probability of an interval is $\int_a^b\rho\,dx$. $\rho$ is a probability **density**: it has units of $1/x$, can exceed 1, and $\rho(x)$ alone is not "the probability of $x$". The formulas carry over with sums replaced by integrals:

$$
\int\rho\,dx = 1 ,\qquad \langle f(x)\rangle = \int f(x)\rho(x)\,dx ,\qquad \sigma^2 = \langle x^2\rangle - \langle x\rangle^2 .
$$

!!! example "A falling rock (Griffiths Example 1.2)"

    A rock dropped from height $h$ is photographed at random times during its fall. Since $x = \tfrac12gt^2$ and the photographs are uniform in time, the distance fallen has density

    $$
    \rho(x) = \frac{1}{2\sqrt{hx}}\qquad(0\le x\le h) ,
    $$

    which is infinite at $x = 0$ (the rock starts slowly) but integrable. Then $\langle x\rangle = h/3$ and $\sigma = 2h/(3\sqrt5) = 0.2981h$, and the probability of a photograph more than one standard deviation from the mean is 0.393. This is the classical probability density that the WKB amplitude reproduces in quantum mechanics.

## Several random variables

For two variables, $p(x,y)$ is the joint probability. The **conditional probability** of $y$ given $x$ is

$$
p(y|x) = \frac{p(x,y)}{p(x)} ,\qquad p(x) = \sum_yp(x,y) .
$$

$X$ and $Y$ are **independent** if $p(x,y) = p(x)p(y)$ for all $x$, $y$, equivalently $p(y|x) = p(y)$. Then $E(XY) = E(X)E(Y)$ and the variances add: $\mathrm{var}(X + Y) = \mathrm{var}X + \mathrm{var}Y$. Expectation is linear whether or not the variables are independent; variance is additive only for independent (more precisely, uncorrelated) ones. Simulating two fair dice ($4\times10^5$ throws) gives $E(XY) = 12.255 = E(X)E(Y)$ and $\mathrm{var}(X + Y) = 5.84$, against $35/6 = 5.83$.

**Law of total probability and Bayes' rule.**

$$
p(y) = \sum_xp(y|x)\,p(x) ,\qquad p(x|y) = \frac{p(y|x)\,p(x)}{p(y)} .
$$

Bayes' rule turns the probability of an observation given a hypothesis into the probability of the hypothesis given the observation.

!!! example "Which state was prepared?"

    A source emits $|0\rangle$ or $|+\rangle = (|0\rangle + |1\rangle)/\sqrt2$ with probability $\tfrac12$ each, and $Z$ is measured. The likelihoods are $p(1|\,0) = 0$, $p(1|+) = \tfrac12$, $p(0|\,0) = 1$, $p(0|+) = \tfrac12$. By the law of total probability $p(0) = \tfrac34$, and Bayes gives

    $$
    p(+\,|\,1) = 1 ,\qquad p(0\,|\,0) = \frac{1\times\frac12}{\frac34} = \frac23 .
    $$

    Outcome 1 identifies the state with certainty; outcome 0 only makes $|0\rangle$ more likely. Because the two states are not orthogonal, no measurement can always tell them apart.

The same rule, with a small prior, explains why a test with 99 percent sensitivity and a 5 percent false-positive rate, applied to a condition present in 1 percent of cases, is right only 17 percent of the time when it reports a positive.

## Three standard distributions

| distribution | $p$ | mean | variance | arises as |
|---|---|---|---|---|
| binomial $B(n,q)$ | $\binom nkq^k(1-q)^{n-k}$ | $nq$ | $nq(1-q)$ | number of "successes" in $n$ independent trials, e.g. counts of an outcome in $n$ measurement shots |
| Poisson $\mathrm{Pois}(\mu)$ | $e^{-\mu}\mu^k/k!$ | $\mu$ | $\mu$ | rare events, $n\to\infty$ with $nq = \mu$ fixed; photon counts of a coherent state |
| Gaussian $N(\mu,s^2)$ | $\frac{1}{\sqrt{2\pi}s}e^{-(x-\mu)^2/2s^2}$ | $\mu$ | $s^2$ | sums of many independent contributions; the oscillator ground state $|\psi_0|^2$ |

The moments were checked by direct summation and integration ($B(20,0.3)$: mean 6, variance 4.2; $\mathrm{Pois}(2.5)$: 2.5, 2.5). For the Gaussian, the probabilities of falling within one, two and three standard deviations of the mean are 0.6827, 0.9545 and 0.9973. The Poisson distribution of a coherent state's photon number is derived in [[harmonic-oscillator-coherent-states]].

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 1.3.1, Eqs. (1.6)-(1.13) (discrete variables, the ages example, variance in two forms (1.11)-(1.12)); Sec. 1.3.2, Eqs. (1.14)-(1.19) and Example 1.2 (the falling rock); Problems 1.1, 1.2 and 1.3 (Gaussian distribution). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Appendix 1, pp. 608-609: random variables, conditional probability, independence, Bayes' rule (A1.2), law of total probability, expectation (A1.4), variance (A1.5).

The state-discrimination example, the table of distributions and the diagnostic-test illustration are my own; numbers are computed in `mathematics/part0_batch5.py` (section F).
