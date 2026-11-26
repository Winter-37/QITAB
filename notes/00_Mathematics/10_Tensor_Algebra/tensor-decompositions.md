---
id: tensor-decompositions
title: Tensor decompositions - the CP format and border rank, Tucker and the higher-order SVD, and tensor trains (matrix product states) built by successive SVDs
summary: Three ways to generalize the low-rank SVD to arrays with three or more indices. CP writes a tensor as a sum of R outer products. It is the most compact format, but its rank is hard to compute and a best rank-R approximation need not exist: the W tensor has rank 3, yet rank-2 tensors approach it arbitrarily closely, with diverging terms. Tucker compresses each index separately and keeps a small core; the higher-order SVD takes the factors from the SVDs of the unfoldings, and its squared error is at most the sum of the discarded squared singular values, within a factor d of optimal. The tensor train (matrix product state) writes each entry as a product of matrices, one per index. Successive SVDs build it, the ranks are the ranks of the sequential unfoldings (Schmidt ranks for a quantum state), and the squared error equals the sum of everything discarded. Worked examples: W-tensor border rank, real rank-2 versus rank-3 2×2×2 tensors, HOSVD versus HOOI, and the compression of a 14-site Heisenberg ground state against a random state.
status: in-progress
kind: theory
level: advanced
tags: [tensor-decomposition, cp-decomposition, parafac, tensor-rank, border-rank, tucker, hosvd, hooi, tensor-train, matrix-product-state, mps, tt-svd, bond-dimension, entanglement, dmrg, tensor-hypercontraction, low-rank-approximation]
prerequisites: [polar-and-singular-value-decompositions, tensor-products-and-partial-trace, schmidt-decomposition-and-purification]
related: [density-fitting-and-cholesky-decomposition, natural-orbitals, dmrg, full-ci, qpe-cost-and-resource-estimates, matrix-and-tensor-identities]
key: tt
order: 40
date: 2026-11-26
---

$\mathcal T\in\mathbb R^{n_1\times\cdots\times n_d}$ is an order-$d$ tensor with entries $T_{i_1\cdots i_d}$, here simply a $d$-index array. $\|\mathcal T\|^2=\sum T_{i_1\cdots i_d}^2$ is the Frobenius norm. $a\circ b\circ c$ is the outer product, $(a\circ b\circ c)_{ijk}=a_ib_jc_k$.

The **mode-$k$ unfolding** $T_{(k)}$ is the $n_k\times\prod_{j\ne k}n_j$ matrix with rows labelled by $i_k$. The **sequential unfolding** $T^{\langle k\rangle}$ is the $(n_1\cdots n_k)\times(n_{k+1}\cdots n_d)$ matrix that groups the first $k$ indices into rows. The **mode-$k$ product** $\mathcal T\times_kU$ contracts index $k$ with the columns of $U$.

For a matrix ($d=2$) the SVD gives the best rank-$r$ approximation, with squared error equal to the sum of the discarded $\sigma_i^2$ (Eckart–Young, [[polar-and-singular-value-decompositions]]). No single decomposition keeps all of these properties for $d\ge3$. Each format below keeps some of them.

## CP: sums of rank-one terms

$$
\mathcal T=\sum_{r=1}^R\lambda_r\,a_r\circ b_r\circ c_r .
\label{cp}
$$

The smallest such $R$ is the **rank** of $\mathcal T$. It is also called the CP, CANDECOMP or PARAFAC rank. Storage is $R(n_1+n_2+n_3)$, far less than $n_1n_2n_3$.

**How it differs from matrix rank.**

- **The rank can exceed every dimension.** A $2\times2\times2$ tensor can have rank 3.
- **The rank depends on the field.** Over the complex numbers a generic $2\times2\times2$ tensor has rank 2. Over the reals, ranks 2 and 3 both occur on sets of positive volume. They are told apart by the sign of the Cayley hyperdeterminant: positive gives rank 2, negative gives rank 3. Of 4000 tensors with Gaussian random entries, 78.8 % had rank 2 and 21.1 % had rank 3. Alternating least squares (below) reaches no rank-2 error below 0.52, for $\|\mathcal T\|=1.87$, on a tensor with negative hyperdeterminant.
- **Computing the rank is NP-hard** in general (Kolda and Bader). In practice $R$ is chosen by trial.
- **A best rank-$R$ approximation may not exist.** The set of tensors of rank $\le R$ is not closed (de Silva and Lim). This is the most important difference for numerical work.

**Border rank: the W tensor.** With $a=(1,0)$ and $b=(0,1)$, let

$$
\mathcal W=a\circ a\circ b+a\circ b\circ a+b\circ a\circ a .
$$

It has rank 3, and each of its three unfoldings has rank 2. For any $\epsilon>0$,

$$
\frac1\epsilon\big[(a+\epsilon b)^{\circ3}-a^{\circ3}\big]=\mathcal W+\epsilon\,(a\circ b\circ b+b\circ a\circ b+b\circ b\circ a)+\epsilon^2\,b^{\circ3}
$$

has rank 2 and differs from $\mathcal W$ by $O(\epsilon)$. The error is $1.73\times10^{-1}$, $1.73\times10^{-2}$ and $1.73\times10^{-3}$ at $\epsilon=10^{-1}$, $10^{-2}$ and $10^{-3}$. The two terms have norm $1/\epsilon$ and cancel almost completely. So $\mathcal W$ has **border rank** 2: it is a limit of rank-2 tensors that is not itself of rank 2.

A rank-2 fit therefore has no minimizer. Alternating least squares lowers the error from $6\times10^{-2}$ after 50 sweeps to $1.6\times10^{-2}$ after 500 and $5\times10^{-3}$ after 5000, while its factors keep growing. A rank-3 fit is exact ($10^{-15}$). Diverging, nearly cancelling components are the signature of this degeneracy in practice. Normalized, $\mathcal W$ is the three-qubit W state, which also has no tripartite Schmidt form ([[schmidt-decomposition-and-purification]]).

**Alternating least squares.** Fixing all factors but one makes the fit linear in that one. For mode 1 it is the least-squares problem $T_{(1)}\approx A\,(C\odot B)^{\mathsf T}$, where $\odot$ is the column-wise Kronecker (Khatri–Rao) product. One sweep updates $A$, $B$ and $C$ in turn. Each step lowers the error, but convergence can be very slow. If an essentially unique CP exists, which is common for $d\ge3$ (Kruskal's condition, reviewed by Kolda and Bader), ALS recovers it up to scaling and order. Matrix factorizations, by contrast, are unique only up to an arbitrary invertible matrix.

**In electronic structure.** Tensor hypercontraction writes the electron-repulsion integrals as $(pq|rs)\approx\sum_{PQ}X_{pP}X_{qP}Z_{PQ}X_{rQ}X_{sQ}$ (Hohenstein, Parrish and Martínez). This is a CP-type structure with grid points $P$, and it lowers the scaling of MP2 and coupled cluster. It is also the basis of the cheapest current block encodings of molecular Hamiltonians ([[qpe-cost-and-resource-estimates]]). Density fitting and Cholesky decomposition are the simpler matrix factorization of the same tensor ([[density-fitting-and-cholesky-decomposition]]).

## Tucker and the higher-order SVD

$$
\mathcal T\approx\mathcal G\times_1U_1\times_2U_2\times_3U_3,\qquad U_k\in\mathbb R^{n_k\times r_k}\ \text{orthonormal},\quad\mathcal G\in\mathbb R^{r_1\times r_2\times r_3}.
\label{tucker}
$$

Each index is compressed separately, into its own $r_k$-dimensional subspace, and the core $\mathcal G$ couples the subspaces. $(r_1,r_2,r_3)$ is the **multilinear rank**, and $r_k=\operatorname{rank}T_{(k)}$ for an exact decomposition. Unlike CP rank, multilinear rank is computable, and the set of tensors with multilinear rank $\le(r_1,\dots,r_d)$ is closed, so a best approximation always exists. The cost is the core, $\prod r_k$ numbers, which grows exponentially with $d$.

**HOSVD** (De Lathauwer, De Moor and Vandewalle).

1. Take $U_k$ as the leading $r_k$ left singular vectors of $T_{(k)}$, for each $k$.
2. Project: $\mathcal G=\mathcal T\times_1U_1^{\mathsf T}\times_2U_2^{\mathsf T}\times_3U_3^{\mathsf T}$.

Without truncation the core is **all-orthogonal**: $G_{(k)}G_{(k)}^{\mathsf T}=\operatorname{diag}(\sigma^{(k)}_1{}^2,\sigma^{(k)}_2{}^2,\dots)$, the squared singular values of $T_{(k)}$. With truncation, the truncated HOSVD $\hat{\mathcal T}$ satisfies

$$
\|\mathcal T-\hat{\mathcal T}\|^2\le\sum_{k=1}^d\sum_{i>r_k}\sigma_i^{(k)2}\le d\,\min_{\operatorname{rank}\le(r_k)}\|\mathcal T-\mathcal X\|^2 .
\label{hosvd-bound}
$$

The first inequality holds because the error splits into the parts removed by each projection. Each part is at most what that projection removes from $\mathcal T$ itself. For the second, any $\mathcal X$ with mode-$k$ rank $r_k$ has error at least $\sum_{i>r_k}\sigma_i^{(k)2}$, by Eckart–Young applied to $T_{(k)}$. So HOSVD is quasi-optimal, but not optimal. **HOOI** (higher-order orthogonal iteration) improves it: each $U_k$ is recomputed in turn from the SVD of $\mathcal T$ projected on the other factors.

!!! example "Truncated HOSVD of a 12 × 10 × 8 tensor"
    Exact multilinear rank $(4,4,4)$ plus noise of size $10^{-3}$ per entry. The mode singular values show the rank at once: mode 1 gives 4.47, 3.69, 3.35, 2.69, then 0.012.

    | ranks kept | HOSVD error² | bound, sum of discarded | HOOI error² |
    |---|---:|---:|---:|
    | $(4,4,4)$ | $8.71\times10^{-4}$ | $1.77\times10^{-3}$ | $8.71\times10^{-4}$ |
    | $(3,3,3)$ | 17.28 | 19.99 | 14.72 |
    | $(2,3,4)$ | 25.06 | 25.91 | 21.42 |

    - **Correct rank.** At $(4,4,4)$ only noise is removed and HOSVD is already optimal.
    - **Rank too small.** HOOI gains 15 % in squared error, within the factor $d=3$ the bound allows.
    - **Core.** All-orthogonality holds to $6\times10^{-15}$.
    - **Storage.** 184 numbers instead of 960.

**In electronic structure.** Choosing natural orbitals for each index of a wave-function tensor is a Tucker compression ([[natural-orbitals]]). Multiconfiguration time-dependent Hartree wave functions in quantum dynamics are Tucker tensors with time-dependent factors. Both are exponential in $d$ through the core, which is what the next format avoids.

## Tensor trains and matrix product states

$$
T_{i_1i_2\cdots i_d}=A^{(1)}[i_1]\,A^{(2)}[i_2]\cdots A^{(d)}[i_d],\qquad A^{(k)}[i_k]\in\mathbb R^{r_{k-1}\times r_k},\quad r_0=r_d=1 .
\label{tt}
$$

Each entry is a product of $d$ small matrices, one chosen by each index. Storage is at most $d\,n\,r^2$, which is linear in $d$. Numerical analysts call this a **tensor train** (Oseledets). Physicists call it a **matrix product state** with **bond dimensions** $r_k$, often written $\chi$ or $D$ (Schollwöck).

**TT-SVD** (Oseledets, Algorithm 1).

1. Reshape $\mathcal T$ to an $n_1\times(n_2\cdots n_d)$ matrix and take its SVD.
2. Keep $r_1$ left singular vectors as $A^{(1)}$. Carry $\Sigma V^{\mathsf T}$ forward and reshape it to $(r_1n_2)\times(n_3\cdots n_d)$.
3. Repeat: SVD, keep $r_k$ vectors as $A^{(k)}$, carry the rest forward. The last remainder is $A^{(d)}$.

**Three properties.**

- **Ranks.** Without truncation, $r_k=\operatorname{rank}T^{\langle k\rangle}$ exactly, the rank of the sequential unfolding at cut $k$.
- **Error.** The left factors are orthonormal, so the pieces discarded at successive cuts are mutually orthogonal. The squared error is therefore exactly the sum of all discarded $\sigma^2$. That sum is in turn at most $\sum_k\varepsilon_k^2$, where $\varepsilon_k$ is the best rank-$r_k$ error of $T^{\langle k\rangle}$ for the original tensor (Oseledets, Theorem 2.2).
- **Closedness.** As for Tucker, sets of bounded TT rank are closed, so best approximations exist. The degeneracy of CP does not occur.

**Quantum states.** For an $N$-qubit state, $T^{\langle k\rangle}$ is the coefficient matrix of the bipartition (sites $1\ldots k$ | rest). Its singular values are the **Schmidt coefficients** across that cut ([[schmidt-decomposition-and-purification]]). So:

- the bond dimension at cut $k$ is the Schmidt rank there;
- truncating a bond discards the smallest Schmidt coefficients;
- the state is cheap exactly when every cut is weakly entangled.

A random state is close to maximally entangled across every cut and needs $r_k=\min(2^k,2^{N-k})$. Ground states of local one-dimensional Hamiltonians are far less entangled. That is why DMRG, which optimizes an MPS variationally, works for them (Schollwöck, Secs. 3-4). GHZ and W states have bond dimension 2 at every cut (checked for 8 qubits), although for three qubits the W state has CP rank 3 and no best rank-2 approximation.

!!! example "Compressing the ground state of a 14-site Heisenberg chain"
    $H=\sum_{i=1}^{13}\mathbf S_i\cdot\mathbf S_{i+1}$ (spin ½, open ends). Exact diagonalization gives $E_0=-6.0267246619$. This chain is gapless, a comparatively hard case for an MPS.

    - **Schmidt spectrum at the middle cut.** The coefficients fall fast: 0.703 (twice), 0.069 (twice), 0.022 (four times), $1.8\times10^{-3}$, $6.0\times10^{-4}$, …
    - **Entanglement entropy** $-\sum\lambda^2\ln\lambda^2$. The ground state has 0.76. A random state has 4.34. The maximum, $7\ln2$, is 4.85.

    Fidelity loss $1-|\langle\psi|\tilde\psi\rangle|/\|\tilde\psi\|$ after TT-SVD truncation to bond dimension $\chi$:

    | $\chi$ | parameters | ground state | random state | ground-state $E-E_0$ |
    |---:|---:|---:|---:|---:|
    | 4 | 360 | $3.8\times10^{-3}$ | 0.88 | $1.7\times10^{-2}$ |
    | 8 | 1 192 | $1.9\times10^{-5}$ | 0.76 | $1.1\times10^{-4}$ |
    | 16 | 3 752 | $6.2\times10^{-8}$ | 0.57 | $3.2\times10^{-7}$ |
    | 32 | 10 920 | $4.1\times10^{-11}$ | 0.30 | |
    | 64 | 27 304 | 0 | 0.054 | |

    - **Ground state.** With 3752 numbers instead of $2^{14}=16384$, it is reproduced to $6\times10^{-8}$.
    - **Random state.** It needs the full bond dimension, $2^7$.
    - **Energy.** The error is quadratic in the wave-function error, as for any variational state, although this truncation is not itself variationally optimized.

    In a test on a random TT tensor with ranks 3 and added noise, the squared truncation error equals the sum of the discarded $\sigma^2$ to 10 digits ($9.2339287123\times10^{-5}$). It lies below $\sum_k\varepsilon_k^2=2.88\times10^{-4}$.

**In quantum chemistry.** The FCI coefficient tensor $C_{n_1n_2\cdots n_K}$ has one index per spatial orbital. Each index takes 4 values (empty, $\alpha$, $\beta$, double), and an MPS of it is the DMRG wave function ([[dmrg]]). Two differences from spin chains matter:

- **Order.** The orbitals have no natural one-dimensional order, so the ordering changes the bond dimensions needed.
- **Entanglement.** Entanglement between orbitals, not spatial locality, is what the bond dimension pays for.

## Which format, when

| format | storage | rank computable | best approximation exists | algorithm |
|---|---|---|---|---|
| CP | $R\sum n_k$ | no (NP-hard) | not always | ALS, nonlinear least squares |
| Tucker | $\prod r_k+\sum n_kr_k$ | yes, $\operatorname{rank}T_{(k)}$ | yes | HOSVD, HOOI |
| tensor train / MPS | $\sum n_kr_{k-1}r_k$ | yes, $\operatorname{rank}T^{\langle k\rangle}$ | yes | TT-SVD, DMRG sweeps |

- **Tucker** suits a few indices of large dimension.
- **Tensor trains** suit many indices of small dimension, such as qubits, orbitals and grid dimensions, provided that a linear ordering with weakly entangled cuts exists.
- **CP** is the most compact when it works. Fit it with a rank check, and watch for growing components.

## Source

- Kolda and Bader, "Tensor Decompositions and Applications", *SIAM Review* **51**, 455-500 (2009), doi:10.1137/07070111X. Unfoldings, the mode product, CP rank and its field dependence, ALS, uniqueness, Tucker and HOSVD.
- de Silva and Lim, "Tensor rank and the ill-posedness of the best low-rank approximation problem", *SIAM J. Matrix Anal. Appl.* **30**, 1084-1127 (2008), doi:10.1137/06066518X. Non-closedness of bounded-rank sets, border rank, the $2\times2\times2$ hyperdeterminant.
- De Lathauwer, De Moor and Vandewalle, "A multilinear singular value decomposition", *SIAM J. Matrix Anal. Appl.* **21**, 1253-1278 (2000), doi:10.1137/S0895479896305696. HOSVD, all-orthogonality and the truncation bound.
- Oseledets, "Tensor-Train Decomposition", *SIAM J. Sci. Comput.* **33**, 2295-2317 (2011), doi:10.1137/090752286. TT format, TT-SVD, rank and error theorems.
- Schollwöck, "The density-matrix renormalization group in the age of matrix product states", *Ann. Phys.* **326**, 96-192 (2011), doi:10.1016/j.aop.2010.09.012. MPS, Schmidt decomposition at each bond, entanglement and why DMRG works.
- Hohenstein, Parrish and Martínez, "Tensor hypercontraction density fitting. I. Quartic scaling second- and third-order Møller-Plesset perturbation theory", *J. Chem. Phys.* **137**, 044103 (2012), doi:10.1063/1.4732310.

The theorem and algorithm numbers cited from Oseledets are from memory and marked to verify; the Schollwöck section numbers were checked against the paper's contents. The bound in Eq. [[#hosvd-bound]] is derived here, and so is the orthogonality argument for the TT-SVD error. The MCTDH and natural-orbital remarks are general knowledge, not taken from these sources. Every number is computed in `Claude outputs/part0_math_batchH.py`, section A.
