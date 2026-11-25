Vector analysis in three dimensions: scalars and vectors, and the three first-derivative operators (gradient, divergence and curl) with the integral theorems that go with them. Then the second derivatives, above all the Laplacian, and how all of this looks in spherical and cylindrical coordinates. The reference is Chapters 1–2 of Arfken and Weber.

## What this chapter is about

Fields (a potential, a density, an electric field, a current) are functions of position. The del operator $\nabla$ turns them into new fields:

- **the gradient** $\nabla\varphi$ points uphill on a scalar field;
- **the divergence** $\nabla\cdot\mathbf V$ measures the outflow of a vector field from a point;
- **the curl** $\nabla\times\mathbf V$ measures its circulation around a point.

Gauss's and Stokes's theorems convert these local quantities into fluxes and circulations over surfaces and curves. Applying $\nabla$ twice gives the Laplacian, the operator of kinetic energy, electrostatics, diffusion and waves.

## Why it matters

- **The kinetic-energy operator is $-\tfrac12\nabla^2$.** Its spherical form, with the angular part $-\hat L^2/r^2$, is why central-field problems separate into radial equations and spherical harmonics.
- **$\nabla^2(1/r) = -4\pi\delta(\mathbf r)$** makes $1/|\mathbf r - \mathbf r'|$ the Green's function of electrostatics. Hartree potentials, Coulomb integrals and solvation models rest on it.
- **Continuity equations** for charge and probability come from the divergence theorem, and the probability current is a divergence-free field in stationary states.
- **Magnetic properties need the curl.** $\mathbf B = \nabla\times\mathbf A$, the symmetric gauge $\mathbf A = \tfrac12\mathbf B\times\mathbf r$, and gauge freedom $\mathbf A\to\mathbf A + \nabla\chi$ all come from the identities of this chapter.
- **Nuclear gradients and Hessians** are the same gradient in $3N$ dimensions.

## The main ideas, in order

1. **Scalars and vectors** defined by their behaviour under rotation; dot, cross and triple products; the Levi-Civita identity; pseudovectors.
2. **The gradient.** Directional derivatives, normals to level surfaces, line integrals and conservative fields.
3. **The divergence and Gauss's theorem.** Flux, the continuity equation, $\nabla\cdot(\mathbf r/r^3) = 4\pi\delta$, Green's theorems.
4. **The curl and Stokes's theorem.** Circulation, rigid rotation, irrotational fields, and what changes when the region has a hole.
5. **Second derivatives.** curl grad = 0, div curl = 0, curl curl, the Laplacian, product rules, scalar and vector potentials, Poisson's equation.
6. **Curvilinear coordinates.** Scale factors and the operators in cylindrical and spherical coordinates.

## How to read it

**Path.**

1. [[scalars-and-vectors]]
2. [[scalar-and-vector-fields-and-the-gradient]]
3. [[divergence-and-gauss-theorem]]
4. [[curl-and-stokes-theorem]]
5. [[vector-identities-and-the-laplacian]]
6. [[curvilinear-coordinates]]

**Needs.** Chapter 1 (matrices and determinants, for rotations and the cross product) and Chapter 2 (partial derivatives, multiple integrals, Jacobians).

**Leads to.**

- Electromagnetism (Part 1, Chapter 2).
- Separation of variables and the special functions (Chapter 6).
- The hydrogen atom and angular momentum (Part 2).
- Current densities and magnetic properties (Part 4, Chapter 16).

**Planned sections:** Tensor analysis and general curvilinear coordinates; Differential forms.
