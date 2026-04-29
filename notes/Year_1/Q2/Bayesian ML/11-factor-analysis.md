# Exercise Type 11: Factor Analysis & Marginal Gaussian

> **What the exam asks:** You are given a Factor Analysis model specification and must compute the joint distribution $p(x, z)$ and/or the marginal distribution $p(x)$ after "integrating out" the latent variable z.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $x$ or $x_n$ | "x" or "x sub n" | The observed data — what we can actually measure (high-dimensional) |
| $z$ or $z_n$ | "z" or "z sub n" | The **latent** (hidden) variable — what we CAN'T observe (low-dimensional) |
| $W$ or $\Lambda$ | Capital W or Lambda | The **weight/loading matrix** — connects latent variables to observations |
| $\epsilon$ or $v$ | Greek letter epsilon or letter v | The **noise** — random error in the observations |
| $\mathcal{N}$ | Capital N (script) | The **Gaussian** (Normal) distribution |
| $I$ | Capital i (identity) | The identity matrix — like the number 1 but for matrices |
| $\Psi$ | Greek letter Psi | The noise covariance matrix |
| $\Sigma$ | Capital Sigma | A covariance matrix |
| $W^T$ | "W transpose" | The matrix W with rows and columns swapped |
| $WW^T$ | "W times W transpose" | Matrix multiplication — gives the covariance contribution from W |
| $\mathbb{E}[\cdot]$ | "Expected value" | The average value you'd expect |
| $\text{Cov}[\cdot]$ | "Covariance" | How variables vary together |
| $\ll$ | "Much less than" | $M \ll N$ means M is much smaller than N |

### What Is Factor Analysis? (Plain English)

Imagine you have high-dimensional data (like a photo with thousands of pixels). But you believe the data is actually generated from a few hidden factors (like "brightness," "contrast," "sharpness").

**The Factor Analysis model says:**
1. There's a hidden low-dimensional variable $z$ (the "factors")
2. The observed data $x$ is created by: $x = Wz + \epsilon$
   - $Wz$: the hidden factors, transformed by weights, produce the main pattern
   - $\epsilon$: random noise adds some extra variation

**In plain English:** "The data we see is a linear combination of hidden factors plus some noise."

### The Model Specification

$$x = Wz + \epsilon$$
$$z \sim \mathcal{N}(0, I) \quad \text{(latent variable is standard Gaussian)}$$
$$\epsilon \sim \mathcal{N}(0, \Psi) \quad \text{(noise is Gaussian with covariance Ψ)}$$

**What this means:**
- $z$ has mean 0 and identity covariance (each factor is independent, unit variance)
- $\epsilon$ has mean 0 and covariance $\Psi$
- $x$ is a linear combination of Gaussians, so it's also Gaussian

---

## Part 1: Computing the Joint $p(x, z)$

### The Formula

$$p(x, z) = p(x|z) \cdot p(z)$$

**In plain English:** The joint = (how x is generated given z) × (how likely z is)

### The Pieces

- $p(x|z) = \mathcal{N}(x|Wz, \Psi)$ — given z, x is Gaussian with mean $Wz$ and covariance $\Psi$
- $p(z) = \mathcal{N}(z|0, I)$ — z is standard Gaussian

So:

$$p(x, z) = \mathcal{N}(x|Wz, \Psi) \cdot \mathcal{N}(z|0, I)$$

---

## Part 2: Computing the Marginal $p(x)$

### What Does "Marginal" Mean?

The marginal $p(x)$ is the distribution of $x$ when we DON'T know (or don't care about) $z$. We "integrate out" (average over) all possible values of $z$.

### The Result (MEMORIZE)

$$p(x) = \mathcal{N}(x|0, WW^T + \Psi)$$

**Mean = 0** (because both $z$ and $\epsilon$ have mean 0)

**Covariance = $WW^T + \Psi$** (covariance from the factors + covariance from the noise)

### Why $WW^T$ and Not $W^TW$?

- $x$ has dimension $N$ (high-dimensional observations)
- $z$ has dimension $M$ (low-dimensional latent)
- $W$ is $N \times M$ (N rows, M columns)
- $WW^T$ is $N \times N$ (correct dimension for x's covariance)
- $W^TW$ is $M \times M$ (wrong — that's the latent dimension)

---

## Part 2.5: The General Linear Gaussian Form

In many textbooks or more complex exam questions, the model might not be "standard." The marginal always follows the **Linear Gaussian Identity**.

### 1. Adding a Bias/Mean Term ($\mu$)
If the model is $x = Wz + \mu + \epsilon$ (where $\mu$ is the mean of the data):
- **Mean:** $p(x)$ will have mean $\mu$.
- **Result:** $p(x) = \mathcal{N}(x | \mu, WW^T + \Psi)$

### 2. General Latent Prior
If the latent variable is NOT standard Gaussian, e.g., $z \sim \mathcal{N}(\mu_z, \Sigma_z)$:
- **Mean:** $\mathbb{E}[x] = W\mu_z$
- **Covariance:** $\text{Cov}[x] = W\Sigma_z W^T + \Psi$
- **Result:** $p(x) = \mathcal{N}(x | W\mu_z, W\Sigma_z W^T + \Psi)$

### The "Master Formula"
For any model of the form:
$$z \sim \mathcal{N}(\mu, \Sigma)$$
$$x|z \sim \mathcal{N}(Az + b, \Psi)$$

The marginal is:
$$p(x) = \mathcal{N}(x | A\mu + b, A\Sigma A^T + \Psi)$$

---

## Part 3: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-A, Question 2a)

> Model: $x_n = Wz_n + \epsilon_n$, $z_n \sim \mathcal{N}(0,I)$, $\epsilon_n \sim \mathcal{N}(0,\Psi)$
>
> **Joint** $p(x_n, z_n)$?
>
> Options:
> - (a) $p(x_n,z_n) = \frac{\mathcal{N}(x_n|Wz_n,\epsilon_n)}{\mathcal{N}(z_n|0,I)}$
> - (b) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\Psi)$
> - (c) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\epsilon_n)\mathcal{N}(z_n|0,I)$
> - (d) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\Psi)\mathcal{N}(z_n|0,I)$

### STEP-BY-STEP SOLUTION

**Step 1: The joint is conditional × prior**

$$p(x_n, z_n) = p(x_n|z_n) \cdot p(z_n)$$

**Step 2: Identify the conditional**

$p(x_n|z_n) = \mathcal{N}(x_n|Wz_n, \Psi)$ — given $z_n$, $x_n$ has mean $Wz_n$ and covariance $\Psi$.

Note: The covariance is $\Psi$ (the noise covariance), NOT $\epsilon_n$ (which is the random variable itself).

**Step 3: Identify the prior**

$p(z_n) = \mathcal{N}(z_n|0, I)$

**Step 4: Multiply**

$$p(x_n, z_n) = \mathcal{N}(x_n|Wz_n, \Psi) \cdot \mathcal{N}(z_n|0, I)$$

**Step 5: Match the answer**

(d) matches exactly.

**(a)** Uses division — wrong operation. ELIMINATE.
**(b)** Missing the prior on $z_n$. ELIMINATE.
**(c)** Uses $\epsilon_n$ as the covariance parameter, but $\epsilon_n$ is the random variable, not the covariance matrix. ELIMINATE.

**Answer: (d)** ✅

---

### EXAM QUESTION 2 (2021-Part-A, Question 2b)

> Same model. **Marginal** $p(x_n)$?
>
> Options:
> - (a) $\mathcal{N}(x_n|0, WW^T + \Psi)$
> - (b) $\mathcal{N}(x_n|Wz_n, WW^T + \Psi)$
> - (c) $\mathcal{N}(x_n|0, W^TW + \Psi)$
> - (d) $\mathcal{N}(x_n|Wz_n, \epsilon_n)$

### STEP-BY-STEP SOLUTION

**Step 1: Apply the marginal formula**

$$p(x_n) = \mathcal{N}(x_n|0, WW^T + \Psi)$$

**Step 2: Match the answer**

(a) matches exactly.

**(b)** Mean is $Wz_n$ — this is the conditional $p(x_n|z_n)$, not the marginal. The marginal has mean 0 (z has been integrated out). ELIMINATE.

**(c)** Uses $W^TW$ — wrong dimensions. $W^TW$ is $M \times M$ (latent dimension), but $x_n$ has dimension $N$. ELIMINATE.

**(d)** Still conditional on $z_n$ and uses $\epsilon_n$ as parameter. ELIMINATE.

**Answer: (a)** ✅

---

### EXAM QUESTION 3 (2023, Question 4e)

> Factor Analysis: $x_n = \Lambda z_n + v_n$, $z_n \sim \mathcal{N}(0, I)$, $v_n \sim \mathcal{N}(0, \Psi)$
>
> **Evaluate** $p(x_n)$.
>
> Options:
> - (a) $\mathcal{N}(0, \Lambda\Lambda^T + \Psi)$
> - (b) $\mathcal{N}(0, \Lambda\Lambda^T + \Psi^T)$
> - (c) $\mathcal{N}(1, \Lambda + \Psi)$
> - (d) $\mathcal{N}(0, \Lambda + \Psi)$

### STEP-BY-STEP SOLUTION

Same pattern, just different notation: $\Lambda$ instead of $W$, $v$ instead of $\epsilon$.

$$p(x_n) = \mathcal{N}(x_n|0, \Lambda\Lambda^T + \Psi)$$

**(a)** Matches exactly. ✓

**(b)** Has $\Psi^T$ — $\Psi$ is already symmetric (it's a covariance matrix), so $\Psi^T = \Psi$. But the standard form is just $\Psi$. ELIMINATE.

**(c)** Mean is 1 — wrong, should be 0. Covariance is $\Lambda + \Psi$ — missing the $\Lambda^T$ and the matrix product structure. ELIMINATE.

**(d)** Covariance is $\Lambda + \Psi$ — same error, missing the product structure. ELIMINATE.

**Answer: (a)** ✅

---

### EXAM QUESTION 4 (2021-Part-A, Question 2c)

> We add prior $W \sim \mathcal{N}(0, I)$. Given data $X$ and unobserved latent $\{z_n\}$, how to train W?
>
> Options:
> - (a) Compute $p(W|\{x_n\},\{z_n\})$. Easy because joint is Gaussian.
> - (b) Compute $p(W|\{x_n\},\{z_n\})$. Hard because $\{z_n\}$ unobserved. Use variational.
> - (c) Compute $p(W|\{x_n\})$. Hard because both $\{z_n\}$ and W unobserved. Use variational.
> - (d) Compute $p(W|\{x_n\})$. Easy because joint is Gaussian.

### STEP-BY-STEP SOLUTION

**Step 1: What's observed and what's not?**

- Observed: $\{x_n\}$ (the data)
- Unobserved: $\{z_n\}$ (latent variables) AND $W$ (parameters we want to learn)

**Step 2: What do we need to compute?**

We want the posterior over W given ONLY the observed data: $p(W|\{x_n\})$.

But $\{z_n\}$ is also unobserved. So we need to marginalize over $\{z_n\}$ as well.

**Step 3: Is this easy or hard?**

This is HARD because both $\{z_n\}$ and $W$ are unknown. We can't just use Gaussian identities directly. We need an approximation — typically a **variational Bayesian approach**.

**Step 4: Match the answer**

**(a)** Assumes $\{z_n\}$ is observed — it's not. ELIMINATE.
**(b)** Computes $p(W|\{x_n\},\{z_n\})$ — this assumes $\{z_n\}$ is observed. ELIMINATE.
**(c)** Computes $p(W|\{x_n\})$, hard because both unobserved, use variational. ✓
**(d)** Says "easy" — it's not easy. ELIMINATE.

**Answer: (c)** ✅

---

## Part 4: Tricks & Shortcuts

### TRICK 1: Marginal Always Has Mean 0

If both $z$ and $\epsilon$ have mean 0, the marginal $p(x)$ has mean 0.

If an option has non-zero mean → wrong.

### TRICK 2: Covariance Is $WW^T + \Psi$

Remember: $WW^T$ (not $W^TW$), plus $\Psi$.

If an option has $W^TW$ → wrong (wrong dimensions).
If an option is missing $\Psi$ → wrong.

### TRICK 3: Joint = Conditional × Prior

$p(x, z) = p(x|z) \cdot p(z) = \mathcal{N}(x|Wz, \Psi) \cdot \mathcal{N}(z|0, I)$

### TRICK 4: Both W and z Unknown = Hard

If both are unobserved, you need variational methods.

---

## Part 5: Practice Exercises

### Exercise 1

> Model: $x_n = Wz_n + \epsilon_n$, $z_n \sim \mathcal{N}(0,I)$, $\epsilon_n \sim \mathcal{N}(0,\Psi)$
>
> **Joint** $p(x_n, z_n)$:
>
> Options:
> - (a) $p(x_n,z_n) = \frac{\mathcal{N}(x_n|Wz_n,\epsilon_n)}{\mathcal{N}(z_n|0,I)}$
> - (b) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\Psi)$
> - (c) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\epsilon_n)\mathcal{N}(z_n|0,I)$
> - (d) $p(x_n,z_n) = \mathcal{N}(x_n|Wz_n,\Psi)\mathcal{N}(z_n|0,I)$

---

### Exercise 2

> Same model. **Marginal** $p(x_n)$:
>
> Options:
> - (a) $\mathcal{N}(x_n|0, WW^T + \Psi)$
> - (b) $\mathcal{N}(x_n|Wz_n, WW^T + \Psi)$
> - (c) $\mathcal{N}(x_n|0, W^TW + \Psi)$
> - (d) $\mathcal{N}(x_n|Wz_n, \epsilon_n)$

---

### Exercise 3

> Model: $p(z) = \mathcal{N}(z|0, I)$, $p(x|z) = \mathcal{N}(x|Wz, \Sigma)$
>
> **Marginal** $p(x)$:
>
> Options:
> - (a) $\mathcal{N}(x|0, W^TW + \Sigma)$
> - (b) $\mathcal{N}(x|Wz, \Sigma)$
> - (c) $\mathcal{N}(x|0, W\Sigma W^T)$
> - (d) $\mathcal{N}(x|0, WW^T + \Sigma)$

---

### Exercise 4

> Factor Analysis: $x_n = \Lambda z_n + v_n$, $z_n \sim \mathcal{N}(0, I)$, $v_n \sim \mathcal{N}(0, \Psi)$
>
> $p(x_n)$:
>
> Options:
> - (a) $\mathcal{N}(0, \Lambda\Lambda^T + \Psi)$
> - (b) $\mathcal{N}(0, \Lambda\Lambda^T + \Psi^T)$
> - (c) $\mathcal{N}(1, \Lambda + \Psi)$
> - (d) $\mathcal{N}(0, \Lambda + \Psi)$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (d)**

Joint = conditional × prior = 𝒩(x|Wz, Ψ) × 𝒩(z|0, I).

(a) uses division.
(b) missing the prior.
(c) uses ε_n as parameter instead of Ψ.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (a)**

Marginal: 𝒩(x|0, WWᵀ + Ψ).

(b) still conditional on z.
(c) wrong dimensions (WᵀW is M×M).
(d) still conditional, wrong parameter.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (d)**

𝒩(x|0, WWᵀ + Σ).

(a) wrong dimensions.
(b) conditional on z.
(c) has WΣWᵀ instead of WWᵀ+Σ.
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (a)**

𝒩(0, ΛΛᵀ + Ψ).

(b) has Ψᵀ unnecessarily.
(c) wrong mean (1) and wrong covariance.
(d) missing the Λᵀ product structure.
</details>
