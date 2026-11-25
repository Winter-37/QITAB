---
id: concentration-inequalities-and-sampling
title: Concentration inequalities and how many samples an estimate needs
summary: How fast an average of repeated measurements approaches its expectation. Covers Chebyshev's inequality, the law of large numbers with its 1/n variance bound, the Chernoff bound for majority voting (error ≤ e^{−2ε²n}), and their application to estimating a Pauli expectation value from measurement shots, with exact and simulated comparisons. The statistical error falls as 1/√n, so each extra digit of precision costs a factor of 100 in shots.
status: in-progress
kind: theory
level: intermediate
tags: [chebyshev-inequality, law-of-large-numbers, chernoff-bound, hoeffding-inequality, shot-noise, sampling, standard-error, estimator, nielsen-chuang]
prerequisites: [probability-and-random-variables]
related: [variational-quantum-eigensolver, sample-based-quantum-diagonalization, density-operators-and-mixed-states, generalized-statistical-interpretation]
order: 20
date: 2026-11-17
---

## The question

Quantum mechanics predicts probabilities, and an experiment or a quantum computer delivers samples. If each run returns $X_i$, independently, with the same distribution as $X$, the natural estimator of $E(X)$ is the sample mean

$$
S_n = \frac1n\sum_{i=1}^nX_i ,\qquad E(S_n) = E(X) ,\qquad \mathrm{var}(S_n) = \frac{\mathrm{var}(X)}{n} .
$$

The variance formula follows because the variances of independent variables add ([[probability-and-random-variables]]). So the typical error, the standard deviation of $S_n$, is $\sigma/\sqrt n$. The inequalities below turn this into guarantees: how likely is an error larger than $\epsilon$?

## Chebyshev's inequality

For any random variable with finite variance and any $\lambda>0$,

$$
\boxed{\,p\big(|X - E(X)|\ge\lambda\sigma\big)\le\frac{1}{\lambda^2}\,}
$$

Proof: apply Markov's inequality $p(Y\ge a)\le E(Y)/a$ (for $Y\ge0$, since $E(Y)\ge a\,p(Y\ge a)$) to $Y = (X - E(X))^2$ with $a = \lambda^2\sigma^2$. The bound uses only the variance and holds for every distribution, which makes it weak for any particular one: for a Poisson variable with mean 3, the probability of lying two standard deviations or more from the mean is 0.034, against the bound 0.25.

## The law of large numbers

**Theorem.** If $X_1,X_2,\dots$ are independent with the distribution of $X$, and $E(X^2)<\infty$, then for every $\epsilon>0$

$$
p\big(|S_n - E(X)|>\epsilon\big)\le\frac{\mathrm{var}(X)}{n\epsilon^2}\ \xrightarrow{\ n\to\infty\ }\ 0 .
$$

This is Chebyshev's inequality applied to $S_n$, whose variance is $\mathrm{var}(X)/n$. It justifies interpreting probabilities as long-run frequencies, and expectation values as averages over many identically prepared systems.

## The Chernoff bound

Suppose an algorithm answers a yes/no question correctly with probability $\tfrac12 + \epsilon$, and we run it $n$ times and take the majority. Let $X_i = 1$ for a correct run, 0 otherwise. The majority is wrong if $\sum X_i\le n/2$, and

$$
\boxed{\,p\Big(\sum_{i=1}^nX_i\le\frac n2\Big)\le e^{-2\epsilon^2n}\,}
$$

**Proof.** A particular sequence with at most $n/2$ correct runs has probability at most $(\tfrac12 - \epsilon)^{n/2}(\tfrac12 + \epsilon)^{n/2} = (1 - 4\epsilon^2)^{n/2}/2^n$, since replacing correct runs by incorrect ones only lowers the probability. There are at most $2^n$ such sequences, so the total is at most $(1 - 4\epsilon^2)^{n/2}\le e^{-2\epsilon^2n}$, using $1 - x\le e^{-x}$.

The error falls exponentially with $n$, much faster than the $1/n$ of the law of large numbers, because a specific distribution (bounded, independent) is assumed.

| $\epsilon$ | $n$ | exact $p(\text{majority wrong})$ | bound $e^{-2\epsilon^2n}$ |
|---|---|---|---|
| 0.25 | 10 | $7.8\times10^{-2}$ | $2.9\times10^{-1}$ |
| 0.25 | 50 | $1.2\times10^{-4}$ | $1.9\times10^{-3}$ |
| 0.25 | 100 | $6.6\times10^{-8}$ | $3.7\times10^{-6}$ |
| 0.1 | 100 | $2.7\times10^{-2}$ | $1.4\times10^{-1}$ |
| 0.1 | 500 | $3.8\times10^{-6}$ | $4.5\times10^{-5}$ |
| 0.05 | 1000 | $8.5\times10^{-4}$ | $6.7\times10^{-3}$ |

(The exact value is the binomial tail, counting a tie as an error.) For $\epsilon = \tfrac14$, an error probability below $10^{-20}$ needs $n = 369$ by the bound and 299 in fact: "a few hundred repetitions", which is why a probabilistic algorithm with any fixed advantage over guessing is as good as a deterministic one.

## Estimating an expectation value from shots

Measuring a Pauli operator $P$ (or any observable with eigenvalues $\pm1$) on a state with $\langle P\rangle = m$ gives $+1$ with probability $(1 + m)/2$ and $-1$ otherwise, so each shot has mean $m$ and variance $1 - m^2$. The estimate from $n$ shots has standard error

$$
\Delta m = \sqrt{\frac{1 - m^2}{n}}\le\frac{1}{\sqrt n} .
$$

!!! example "Shot noise for $m = 0.3$"

    Each $n$ was repeated 20000 times in simulation.

    | $n$ | observed std of the estimate | $\sqrt{(1-m^2)/n}$ | observed $p(\lvert\text{err}\rvert>0.05)$ | Chebyshev bound | Gaussian estimate |
    |---|---|---|---|---|---|
    | 100 | 0.0962 | 0.0954 | 0.601 | 1 (useless) | 0.600 |
    | 1000 | 0.0303 | 0.0302 | 0.097 | 0.364 | 0.097 |
    | 10000 | 0.0096 | 0.0095 | 0.0000 | 0.036 | 0.0000 |

    The $1/\sqrt n$ law holds precisely. The Gaussian estimate, $p\approx2\,\Phi_{\rm tail}(\epsilon/\Delta m)$, is accurate once $n$ is moderately large; it rests on the central limit theorem, which is not proved in the books used here.

**How many shots?** To reach error $\epsilon$ with confidence $1 - \delta$ (worst case, variance 1):

| target | Chebyshev $1/(\delta\epsilon^2)$ | Hoeffding $2\ln(2/\delta)/\epsilon^2$ | Gaussian $(z_{\delta/2}/\epsilon)^2$ |
|---|---|---|---|
| $\epsilon = 0.01$, $\delta = 0.05$ | $2.0\times10^5$ | $7.4\times10^4$ | $3.8\times10^4$ |
| $\epsilon = 0.001$, $\delta = 0.05$ | $2.0\times10^7$ | $7.4\times10^6$ | $3.8\times10^6$ |

All three scale as $1/\epsilon^2$: one more digit costs a hundred times more shots. Hoeffding's inequality, $p(|S_n - E|\ge\epsilon)\le2e^{-2n\epsilon^2/(b-a)^2}$ for variables confined to $[a,b]$, generalizes the Chernoff bound and is the usual rigorous tool; it is not in the three books used for Part 0. (Reference, quoted from memory and to verify: W. Hoeffding, J. Am. Stat. Assoc. 58, 13 (1963).)

For an energy $E = \sum_kc_k\langle P_k\rangle$ measured term by term with $n_k$ shots each, the variances add: $\mathrm{var}(E)\approx\sum_kc_k^2(1 - \langle P_k\rangle^2)/n_k$. Reaching chemical accuracy (about $1.6\times10^{-3}$ hartree) for a Hamiltonian with many terms and coefficients of order one therefore requires millions of shots, which is a central cost of [[variational-quantum-eigensolver]] methods. Methods that use samples to select configurations and then diagonalize classically, such as [[sample-based-quantum-diagonalization]], face a different sampling question: how many shots are needed to see the important configurations at all.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010): Appendix 1, p. 609 (Chebyshev's inequality (A1.6), Exercise A1.6); Box 3.4, p. 154 (Theorem 3.3, the Chernoff bound, Eqs. (3.2)-(3.6), and the remark that a few hundred repetitions bring the error below $10^{-20}$); Box 12.3, p. 541 (Theorem 12.3, the law of large numbers, Eqs. (12.34)-(12.38)).

Markov's inequality, Hoeffding's inequality, the central-limit estimate and the shot-count application are additions beyond the books; all numbers are computed in `mathematics/part0_batch5.py` (section G).
