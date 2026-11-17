Probability as quantum mechanics uses it: distributions and expectation values, and how many samples an estimate needs.

## What this chapter is about

The first note covers random variables, discrete and continuous distributions, expectation values, variance, joint and conditional probability, and independence. That is everything needed to read $|\Psi(x)|^2$ as a probability density and $\langle\hat Q\rangle$ as an average. The second note asks a practical question: if an expectation value is estimated from $n$ repeated measurements, how close is the estimate likely to be, and how fast does it improve?

## Why it matters

- **Quantum predictions are statistical.** The theory predicts distributions of outcomes, not single outcomes. Expectation values and standard deviations are the language of the statistical interpretation and of the uncertainty principle.
- **On a quantum computer, measurement cost is the computational cost.** An energy on quantum hardware is an average over shots. The error of the mean falls as $\sigma/\sqrt n$, so reaching precision $\epsilon$ takes roughly $n\approx\sigma^2/\epsilon^2$ shots. This scaling is a large part of the cost of variational algorithms.
- **Exponential tails make algorithms reliable.** Chernoff and Hoeffding bounds show that repeating a probabilistic algorithm and taking a majority vote drives the failure probability down exponentially. This is why a bounded error probability, such as 1/3, is acceptable in quantum complexity theory.

## Where it is used later

- [[wave-function-and-statistical-interpretation|The statistical interpretation]] and [[generalized-statistical-interpretation|the generalized statistical interpretation]] in Part 2.
- [[density-operators-and-mixed-states|Density operators]], which combine quantum and classical probability.
- Shot counts in [[variational-quantum-eigensolver|VQE]] and bitstring sampling in [[sample-based-quantum-diagonalization|SQD]].

## The main ideas, in order

1. **Distributions and moments.** $\langle x\rangle$, $\langle x^2\rangle$, and $\sigma^2=\langle x^2\rangle-\langle x\rangle^2$, for discrete and continuous variables.
2. **Joint and conditional probability.** Independence and the law of total probability.
3. **Concentration.** Chebyshev's inequality and the law of large numbers: the variance of a mean of $n$ independent samples is $\sigma^2/n$.
4. **Exponential bounds.** Chernoff and Hoeffding bounds for averages of bounded variables, applied to majority voting and to estimating a Pauli expectation value.

## How to read it

**Path.** [[probability-and-random-variables]], then [[concentration-inequalities-and-sampling]].

**Needs.** Nothing beyond calculus.

**Leads to.** The statistical interpretation (Part 2, Chapters 1 and 3), density operators (Part 2, Chapter 3), and measurement cost in quantum algorithms (Parts 5 and 6).

**Planned sections:** Monte Carlo estimators and importance sampling; Error analysis.
