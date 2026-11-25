---
id: error-analysis-and-propagation-of-uncertainty
title: Error analysis and propagation of uncertainty - systematic and random errors, the standard error of a mean, confidence intervals and Student's t, propagation through functions with and without correlations, weighted means, and parameter errors of least-squares fits
summary: A measured or computed number is incomplete without its uncertainty. Random errors average down as σ/√N; systematic errors do not, and must be estimated separately. For a function q(x₁, …, xₙ) of uncertain inputs, linearization gives σ_q² = gᵀCg, with g the gradient of q and C the covariance matrix of the inputs. For uncorrelated inputs this is the sum of squared contributions, and relative errors add in quadrature for products and quotients. Correlations can greatly reduce (or increase) the error of a difference. Linearization fails for large relative errors, where the mean is also biased by ½f''σ². Monte Carlo propagation handles that case. Repeated measurements combine in a weighted mean with weights 1/σᵢ², and a χ² test checks their consistency. A least-squares fit gives parameter covariances (AᵀWA)⁻¹. Worked examples: propagation checked by Monte Carlo, correlated energy differences, a weighted mean, and a straight-line fit and an Arrhenius fit with their errors.
status: in-progress
kind: theory
level: introductory
tags: [error-analysis, uncertainty, propagation-of-uncertainty, standard-error, confidence-interval, student-t, covariance, correlation, weighted-mean, chi-squared, least-squares-fit, monte-carlo, systematic-error, significant-figures]
prerequisites: [probability-and-random-variables, multivariable-taylor-expansion]
related: [concentration-inequalities-and-sampling, floating-point-and-numerical-error, error-mitigation-for-vqe]
key: prop
order: 15
date: 2026-11-25
---

$x_i$ are input quantities with standard uncertainties $\sigma_i$ and covariance matrix $C_{ij} = \mathrm{cov}(x_i, x_j)$, so $C_{ii} = \sigma_i^2$. Correlation coefficients are $\rho_{ij} = C_{ij}/(\sigma_i\sigma_j)$. Results are reported as value $\pm$ one standard uncertainty unless stated.

## Kinds of error

**Random and systematic errors.**

- **Random errors** scatter repeated results about their mean and shrink when results are averaged.
- **Systematic errors** shift all results in the same way and do not average out: a miscalibrated instrument, a basis-set error, a missing relativistic correction.

**Accuracy and precision.** Accuracy is closeness to the true value; precision is reproducibility. A calculation can be perfectly precise and inaccurate. Most of the error budget of a quantum-chemical number is systematic: basis set, correlation treatment, geometry. Statistical errors appear in stochastic methods such as quantum Monte Carlo, sampling on quantum hardware ([[concentration-inequalities-and-sampling]]) and molecular dynamics averages.

## The mean and its error

**Sample statistics.** For $N$ independent measurements $x_j$ of one quantity:

$$
\bar x = \frac1N\sum_jx_j,\qquad s^2 = \frac1{N - 1}\sum_j(x_j - \bar x)^2,\qquad \sigma_{\bar x} = \frac s{\sqrt N} .
$$

$s$ estimates the spread of single measurements. $N - 1$ appears because one degree of freedom was used to compute $\bar x$, which makes $s^2$ unbiased. The standard error $\sigma_{\bar x}$ is the uncertainty of the mean, from the variance of a sum of independent variables ([[probability-and-random-variables]]). Halving it needs four times as many measurements.

**Confidence intervals.** For normally distributed data, $\bar x\pm t_{N-1}\,\sigma_{\bar x}$ is a confidence interval. Student's $t$ factor corrects for $s$ being itself an estimate from few data (Arfken Sec. 19.6). For 95% confidence, $t = 2.064$ at $N = 25$ and $1.960$ for $N\to\infty$.

**Correlated samples.** Successive samples from a Markov chain (MC, MD) are correlated. The naive standard error is then too small, by $\sqrt{2\tau_{\rm int}}$ with $\tau_{\rm int}$ the integrated autocorrelation time. Blocking analysis estimates it.

**Reporting.** Quote the uncertainty to one or two significant figures and the value to the same decimal place: $4.505\pm0.025$, or $4.505(25)$, not $4.50492\pm0.02494$.

## Propagation through a function

**The linear formula.** Expand $q(\mathbf x)$ to first order about the means ([[multivariable-taylor-expansion]]): $\delta q = \sum_i(\partial q/\partial x_i)\delta x_i = \mathbf g^{\rm T}\delta\mathbf x$. Taking the variance (Arfken Sec. 19.6):

$$
\sigma_q^2 = \mathbf g^{\rm T}\mathbf C\,\mathbf g = \sum_i\Big(\frac{\partial q}{\partial x_i}\Big)^2\sigma_i^2 + 2\sum_{i<j}\frac{\partial q}{\partial x_i}\frac{\partial q}{\partial x_j}C_{ij} .
\label{prop}
$$

**Special cases (uncorrelated inputs).**

| $q$ | $\sigma_q$ |
|---|---|
| $x\pm y$ | $\sqrt{\sigma_x^2 + \sigma_y^2}$ |
| $xy$ or $x/y$ | $|q|\sqrt{(\sigma_x/x)^2 + (\sigma_y/y)^2}$ |
| $x^n$ | $|q|\,|n|\,\sigma_x/|x|$ |
| $\ln x$ | $\sigma_x/x$ |
| $e^{ax}$ | $|q|\,|a|\sigma_x$ |

Absolute errors add in quadrature for sums, relative errors for products. Errors add in quadrature, not linearly, because independent errors partly cancel. The largest contribution usually dominates: one input with three times the relative error of the others contributes nine times as much variance.

**Correlations matter.** For $q = x - y$ with equal $\sigma$ and correlation $\rho$, $\sigma_q = \sigma\sqrt{2(1 - \rho)}$. Two energies computed with the same method and basis share most of their error, so their difference is far more precise than either. This is why relative energies are trusted more than total energies, and why a reaction energy can be accurate when the absolute energies are not.

**When linearization fails.** Eq. [[#prop]] needs the relative errors small enough that $q$ is nearly linear over $\pm\sigma$. Otherwise:

- the second-order Taylor term biases the mean, $\langle q\rangle\approx q(\bar x) + \tfrac12q''\sigma^2$;
- the distribution of $q$ is skewed.

Monte Carlo propagation handles any $q$: sample the inputs from their distribution, compute $q$ for each sample, and take the mean and spread.

## Combining measurements

**Weighted mean.** For independent results $x_i\pm\sigma_i$ of one quantity, the minimum-variance combination is

$$
\bar x_w = \frac{\sum_iw_ix_i}{\sum_iw_i},\qquad w_i = \frac1{\sigma_i^2},\qquad \sigma_{\bar x_w} = \Big(\sum_iw_i\Big)^{-1/2} .
$$

**Consistency check.** $\chi^2 = \sum_iw_i(x_i - \bar x_w)^2$ should be about $N - 1$. A much larger value means the quoted errors are underestimated, or a systematic error is present (Arfken Sec. 19.6).

## Least-squares fits

**Linear least squares.** For a model linear in its parameters, $y = \mathbf A\mathbf p$ (a straight line: rows $(1, x_j)$), with data errors $\sigma_j$ and weights $\mathbf W = \mathrm{diag}(1/\sigma_j^2)$:

$$
\hat{\mathbf p} = (\mathbf A^{\rm T}\mathbf W\mathbf A)^{-1}\mathbf A^{\rm T}\mathbf W\mathbf y,\qquad \mathrm{cov}(\hat{\mathbf p}) = (\mathbf A^{\rm T}\mathbf W\mathbf A)^{-1} .
\label{fit}
$$

The covariance is Eq. [[#prop]] applied to the linear map from $\mathbf y$ to $\hat{\mathbf p}$.

**Correlated parameters.** Fitted parameters are usually correlated. Slope and intercept of a line through data at positive $x$ are anticorrelated. The correlation must be kept when the parameters are used together, through the off-diagonal elements in Eq. [[#prop]]. If the $\sigma_j$ are unknown, they are estimated from the residuals as $s^2 = \chi^2_{\min}/(N - n_p)$.

**Nonlinear models.** These are linearized about the best fit; the Jacobian takes the place of $\mathbf A$. Linearizing transformations (fitting $\ln k$ against $1/T$) change the error weights. The transformed errors must be propagated, $\sigma_{\ln k} = \sigma_k/k$.

## Worked examples

!!! example "Propagation, correlation and fits with numbers (computed for this note)"
    **Mean of 25 measurements** (drawn from a normal distribution, $\sigma = 0.5$): $\bar x = 9.9874$, $s = 0.4578$, $\sigma_{\bar x} = 0.0916$. The 95% interval is $9.987\pm2.064\times0.092 = 9.99\pm0.19$.

    **Product and quotient.** $q = xy/z$ with $x = 2.00\pm0.02$, $y = 3.00\pm0.06$, $z = 1.50\pm0.015$. Relative errors 1%, 2%, 1% combine to 2.45%: $q = 4.000\pm0.098$. Monte Carlo with $10^6$ samples gives $4.0004\pm0.0981$.

    **Nonlinearity.** $E = x^2/2$ with $x = 1\pm\sigma$:

    | $\sigma$ | linear $\sigma_E$ | Monte Carlo $\sigma_E$ | mean shift (MC) | $\tfrac12E''\sigma^2$ |
    |---:|---:|---:|---:|---:|
    | 0.01 | 0.0100 | 0.0100 | 0.00006 | 0.00005 |
    | 0.2 | 0.2000 | 0.2020 | 0.0201 | 0.0200 |

    **Correlated difference.** Two energies with $\sigma = 0.010$ each: uncorrelated, $\sigma_{\rm diff} = 0.0141$; with $\rho = 0.9$, $\sigma_{\rm diff} = 0.0045$.

    **Weighted mean.** $4.52\pm0.05$, $4.61\pm0.10$ and $4.49\pm0.03$ combine to $4.505\pm0.025$. $\chi^2 = 1.44$ for 2 degrees of freedom, which is consistent.

    **Straight line.** Eleven points $x = 0..10$, $y = 1.2 + 0.45x$ plus noise of $\sigma = 0.3$. Eq. [[#fit]] gives $a = 1.20\pm0.17$ and $b = 0.419\pm0.029$, with correlation $-0.85$. Refitting $2\times10^4$ fresh noise realizations gives a spread of $b$ of 0.02862, against the predicted 0.02860.

    **Arrhenius.** $\ln k$ at five temperatures (300–380 K) with $\sigma_{\ln k} = 0.05$ and true $E_a = 50.00$ kJ/mol. The fit gives $E_a = 50.6\pm0.8$ kJ/mol and $\ln A = 27.8\pm0.3$: within one standard error of the truth, as expected about two times in three.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 19.6 (statistics: error propagation, fitting curves to data, the χ² distribution, the Student t distribution). Monte Carlo propagation, blocking analysis and the remarks on quantum-chemical error budgets are general knowledge. The data in the examples are synthetic (seeded random numbers). Calculations in `Claude outputs/part0_math_batchE.py`, section G.
