# Exercise Type 3: Gaussian Posterior & Evidence (Gaussian-Gaussian Conjugacy)

> **What the exam asks:** You are given a Gaussian likelihood (data model with unknown mean μ) and a Gaussian prior on μ. You must compute the posterior distribution over μ after seeing data, the evidence (marginal likelihood), and/or combine predictions from multiple models using Bayesian model averaging.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $\mu$ | Greek letter "mu" | The **unknown mean** — the parameter we're trying to estimate |
| $x$ | lowercase x | The **observation** — the data point we actually saw |
| $\sigma^2$ | "sigma squared" | A **variance** — how spread out a Gaussian distribution is |
| $\sigma_0^2$ | "sigma naught squared" | The **prior variance** — how uncertain we are about μ BEFORE seeing data |
| $\sigma^2_{post}$ | "sigma post squared" | The **posterior variance** — how uncertain we are about μ AFTER seeing data |
| $\mu_0$ | "mu naught" | The **prior mean** — what we believed μ was before seeing data |
| $\mu_{post}$ | "mu post" | The **posterior mean** — our updated estimate of μ after seeing data |
| $\sigma_\epsilon^2$ | "sigma epsilon squared" | The **observation noise variance** — how noisy our measurements are |
| $\mathcal{N}(x\|\mu, \sigma^2)$ | "Gaussian of x given mu and sigma squared" | The Gaussian (Normal) distribution for x, with mean μ and variance $\sigma^2$ |
| $\frac{1}{\sigma^2}$ | "one over sigma squared" | The **precision** — the inverse of variance. High precision = low uncertainty |

### The Gaussian Distribution Formula

$$\mathcal{N}(x|\mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**How to read this:** "The probability density of x given mean μ and variance $\sigma^2$." The exponential term gives the bell curve shape — highest when $x = \mu$, dropping off as x moves away.

**In the exam you don't need to expand this** — you just need to identify the mean and variance inside the $\mathcal{N}(\cdot|\cdot, \cdot)$ notation.

---

## Part 1: The Core Concepts — No Math

### What's Going On? (Plain English)

Imagine you're trying to figure out the true temperature μ of an oven. You have:

1. **A prior belief:** "I think the oven is around 200°C, give or take 10°C." This is your Gaussian prior: $\mathcal{N}(\mu|200, 10^2)$.
2. **A measurement:** You stick a thermometer in and it reads 210°C. But the thermometer is noisy. This is your likelihood: $\mathcal{N}(x=210|\mu, \sigma^2_{noise})$.
3. **An updated belief:** After seeing the measurement, you revise your estimate. This is your **posterior**.

**Bayesian inference with Gaussians is just the math of combining these two sources of information.**

### The Intuition Behind the Posterior

The posterior mean is a **weighted average** of the prior mean and the observation:

$$\mu_{post} = \text{(weight on prior)} \times \mu_0 + \text{(weight on data)} \times x$$

**Who gets more weight?** The one that's more certain (higher precision):
- If the prior is very certain (small $\sigma_0^2$) → posterior stays close to $\mu_0$
- If the observation is very certain (small $\sigma^2$) → posterior moves toward $x$

The posterior variance is **always smaller** than both the prior and the likelihood variance — because you now have TWO sources of information.

### The Intuition Behind the Evidence

The **evidence** $p(x)$ answers: "Before I saw the data, how likely was this particular observation under my model?"

For a Gaussian model with unknown mean, the evidence is a Gaussian centered at the **prior mean** with variance = **prior variance + likelihood variance**.

**Why the summed variance?** Because there are TWO sources of uncertainty:
1. We don't know μ (prior uncertainty = $\sigma_0^2$)
2. Even if we knew μ, the observation is noisy (likelihood uncertainty = $\sigma^2$)

These add up. The evidence is **broader** than the likelihood alone.

---

## Part 2: The Key Formulas (MEMORIZE)

### Setup

| Component | Formula | What You Know |
|-----------|---------|---------------|
| **Likelihood** | $p(x \mid \mu) = \mathcal{N}(x \mid \mu, \sigma^2)$ | $\sigma^2$ is given |
| **Prior** | $p(\mu) = \mathcal{N}(\mu \mid \mu_0, \sigma_0^2)$ | $\mu_0$ and $\sigma_0^2$ are given |

### Posterior: $p(\mu \mid x) = \mathcal{N}(\mu \mid \mu_{post}, \sigma^2_{post})$

| Formula | Expression | How to Remember |
|---------|------------|-----------------|
| **Posterior precision** | $\dfrac{1}{\sigma^2_{post}} = \dfrac{1}{\sigma^2_0} + \dfrac{1}{\sigma^2}$ | Precision = prior precision + likelihood precision |
| **Posterior variance** | $\sigma^2_{post} = \dfrac{1}{\frac{1}{\sigma^2_0} + \frac{1}{\sigma^2}} = \dfrac{\sigma^2_0 \cdot \sigma^2}{\sigma^2_0 + \sigma^2}$ | Inverse of the sum of precisions |
| **Posterior mean** | $\mu_{post} = \sigma^2_{post} \left( \dfrac{\mu_0}{\sigma^2_0} + \dfrac{x}{\sigma^2} \right)$ | Precision-weighted average |

### The Precision-Weighted Average (Rewritten)

$$\mu_{post} = \frac{\frac{\mu_0}{\sigma^2_0} + \frac{x}{\sigma^2}}{\frac{1}{\sigma^2_0} + \frac{1}{\sigma^2}}$$

**In plain English:** "Each source contributes in proportion to its precision. More precise sources get more weight."

**Shortcut when both variances = 1:** $\mu_{post} = (\mu_0 + x) / 2$ (simple average).

### Evidence: $p(x)$

$$p(x) = \mathcal{N}(x|\mu_0,\; \sigma^2_0 + \sigma^2)$$

**Mean = prior mean.** **Variance = prior variance + likelihood variance.**

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Posterior Precision = Sum of Precisions

Precision = $1/\sigma^2$. Just add them: $1/\sigma^2_{post} = 1/\sigma^2_0 + 1/\sigma^2$. Then flip: $\sigma^2_{post} = 1 / (\text{sum})$.

### TRICK 2: Posterior Mean = Precision-Weighted Average

Each source contributes: (its mean) × (its precision). Then divide by total precision.

**If both variances equal:** posterior mean = simple average $(\mu_0 + x) / 2$.

### TRICK 3: Evidence Variance = Sum of Variances

Evidence = $\mathcal{N}(x|\mu_0, \sigma^2_0 + \sigma^2)$. Mean stays at prior mean. Variances add.

### TRICK 4: Posterior Variance Always Decreases

$\sigma^2_{post}$ is always smaller than both $\sigma^2_0$ and $\sigma^2$. More information → more certainty.

---

## Part 4: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2023, Question 1a-b)

> Model $m_1$: $p(x|\mu, m_1) = \mathcal{N}(x|\mu, 1)$, $p(\mu|m_1) = \mathcal{N}(\mu|0, 1)$
>
> **1a:** We observe $x=1$. Determine $p(\mu|x=1, m_1)$.
>
> Options:
> - (a) $\mathcal{N}(\mu|0, 0.5)$
> - (b) $\mathcal{N}(\mu|1, 2)$
> - (c) $\mathcal{N}(\mu|0.5, 0.5)$
> - (d) $\mathcal{N}(\mu|0.5, 1)$

### STEP-BY-STEP SOLUTION

**Step 1: Compute posterior variance**

$$\frac{1}{\sigma^2_{post}} = \frac{1}{\sigma^2_0} + \frac{1}{\sigma^2} = \frac{1}{1} + \frac{1}{1} = 2$$

$$\sigma^2_{post} = \frac{1}{2} = 0.5$$

**Step 2: Compute posterior mean**

$$\mu_{post} = \sigma^2_{post} \left( \frac{\mu_0}{\sigma^2_0} + \frac{x}{\sigma^2} \right) = 0.5 \left( \frac{0}{1} + \frac{1}{1} \right) = 0.5 \cdot 1 = 0.5$$

**Answer: (c) $\mathcal{N}(\mu|0.5, 0.5)$** ✅

---

### Question 1b: Evidence

> Determine $p(x=1|m_1)$.
>
> Options:
> - (a) $\mathcal{N}(1|0, 2)$
> - (b) $2/\sqrt{2\pi}$
> - (c) $\mathcal{N}(0|1, 1)$
> - (d) $1/\sqrt{2\pi}$

### STEP-BY-STEP SOLUTION

$$p(x=1|m_1) = \mathcal{N}(x=1|\mu_0=0, \sigma^2_0 + \sigma^2 = 1+1 = 2) = \mathcal{N}(1|0, 2)$$

**Answer: (a) $\mathcal{N}(1|0, 2)$** ✅

---

### Tricks & Shortcuts

**TRICK 1: Posterior precision = sum of precisions**
- Precision = 1/variance
- Posterior precision = prior precision + likelihood precision
- Posterior variance = 1/(sum of precisions)

**TRICK 2: Posterior mean = precision-weighted average**
- More precise source gets more weight
- If both have same variance: mean = (μ₀ + x) / 2

**TRICK 3: Evidence = Gaussian with summed variances**
- $p(x) = \mathcal{N}(x|\mu_0, \sigma^2_0 + \sigma^2)$
- Mean = prior mean, variance = prior variance + likelihood variance

**TRICK 4: When both variances = 1**
- Posterior variance = 1/2
- Posterior mean = (prior_mean + observation) / 2

---

## Part 5: Practice Exercises

### Exercise 1 (2023, Question 1a)

> Model $m_1$: $p(x|\mu, m_1) = \mathcal{N}(x|\mu, 1)$, $p(\mu|m_1) = \mathcal{N}(\mu|0, 1)$
>
> We observe $x=1$. Determine $p(\mu|x=1, m_1)$.
>
> Options:
> - (a) $\mathcal{N}(\mu|0, 0.5)$
> - (b) $\mathcal{N}(\mu|1, 2)$
> - (c) $\mathcal{N}(\mu|0.5, 0.5)$
> - (d) $\mathcal{N}(\mu|0.5, 1)$

---

### Exercise 2 (2023, Question 1b)

> Same model. Determine $p(x=1|m_1)$.
>
> Options:
> - (a) $\mathcal{N}(1|0, 2)$
> - (b) $2/\sqrt{2\pi}$
> - (c) $\mathcal{N}(0|1, 1)$
> - (d) $1/\sqrt{2\pi}$

---

### Exercise 3 (2023, Question 1c)

> Model $m_1$: $p(x|\mu, m_1) = \mathcal{N}(x|\mu, 1)$, $p(\mu|m_1) = \mathcal{N}(\mu|0, 1)$
> Model $m_2$: $p(x|m_2) = \mathcal{N}(x|1, 1)$
> $p(m_1) = 2/3$, $p(m_2) = 1/3$
>
> Determine $p(x=2)$ by Bayesian model averaging.
>
> Options:
> - (a) $\frac{2}{3\sqrt{2\pi}} + \frac{1}{3}\mathcal{N}(2|0, 1)$
> - (b) $\frac{1}{3}\mathcal{N}(2|1, 2) + \frac{1}{3\sqrt{2\pi}}$
> - (c) $\frac{2}{3}\mathcal{N}(2|0, 2) + \frac{1}{3}\mathcal{N}(2|1, 1)$
> - (d) $\frac{1}{3\sqrt{2\pi}} + \frac{1}{3}\mathcal{N}(2|1, 1)$

### STEP-BY-STEP SOLUTION

**Step 1: Write the Bayesian model averaging formula**

$$p(x=2) = p(x=2|m_1) \cdot p(m_1) + p(x=2|m_2) \cdot p(m_2)$$

We need two ingredients: the evidence $p(x=2|m_1)$ and the evidence $p(x=2|m_2)$, then weight by their prior model probabilities.

---

**Step 2: Compute the evidence for model $m_1$**

Model $m_1$ has unknown parameter μ. The likelihood is $\mathcal{N}(x|\mu, 1)$ and the prior on μ is $\mathcal{N}(\mu|0, 1)$.

**Key formula — Gaussian evidence:**

When likelihood = $\mathcal{N}(x|\mu, \sigma^2)$ and prior = $\mathcal{N}(\mu|\mu_0, \sigma_0^2)$:

$$p(x|m_1) = \mathcal{N}(x|\mu_0,\; \sigma_0^2 + \sigma^2)$$

**How to read this:** The evidence is a Gaussian centered at the *prior mean* with variance = *prior variance + likelihood variance*.

From $m_1$:
- $\mu_0 = 0$ (prior mean)
- $\sigma_0^2 = 1$ (prior variance)
- $\sigma^2 = 1$ (likelihood variance)

$$p(x=2|m_1) = \mathcal{N}(x=2|\mu_0=0,\; 1+1=2) = \mathcal{N}(2|0, 2)$$

**Why is the variance 2?** Because we don't know μ — we averaged over all possible μ values (the prior), which adds uncertainty on top of the observation noise.

---

**Step 3: Compute the evidence for model $m_2$**

Model $m_2$ has NO unknown parameter — it directly specifies:

$$p(x|m_2) = \mathcal{N}(x|1, 1)$$

So we just evaluate at $x=2$:

$$p(x=2|m_2) = \mathcal{N}(2|1, 1)$$

**Key difference from $m_1$:** $m_2$ is fully specified (no parameter to integrate over), so its evidence is just the Gaussian evaluated at 2. $m_1$ has unknown μ, so its evidence is broader (variance 2 instead of 1).

---

**Step 4: Combine with model averaging**

$$p(x=2) = \underbrace{\mathcal{N}(2|0, 2)}_{m_1 \text{ evidence}} \cdot \underbrace{\frac{2}{3}}_{p(m_1)} + \underbrace{\mathcal{N}(2|1, 1)}_{m_2 \text{ evidence}} \cdot \underbrace{\frac{1}{3}}_{p(m_2)}$$

$$p(x=2) = \frac{2}{3}\mathcal{N}(2|0, 2) + \frac{1}{3}\mathcal{N}(2|1, 1)$$

---

**Step 5: Match the answer**

**(c)** matches exactly. ✓

**(a)** Has $\frac{2}{3\sqrt{2\pi}}$ — this looks like someone tried to evaluate $\mathcal{N}(2|0, 1)$ numerically but got it wrong. Also has $\mathcal{N}(2|0, 1)$ instead of $\mathcal{N}(2|0, 2)$. ELIMINATE.
**(b)** Has the model weights swapped ($1/3$ with the first term, $1/3\sqrt{2\pi}$ with the second). Also the second term is a number not a Gaussian. ELIMINATE.
**(d)** Same issues — wrong weights and wrong terms. ELIMINATE.

**Answer: (c) $\frac{2}{3}\mathcal{N}(2|0, 2) + \frac{1}{3}\mathcal{N}(2|1, 1)$** ✅

---

### KEY INTUITION

**Bayesian model averaging = weighted average of predictions**

Think of it like asking two weather forecasters:
- Forecaster $m_1$ says "20°C, but I'm uncertain (wide error bar)"
- Forecaster $m_2$ says "20°C, but I'm more confident (narrow error bar)"
- You trust forecaster $m_1$ twice as much (2/3 vs 1/3)

Your combined forecast = $2/3 \times m_1\text{'s prediction} + 1/3 \times m_2\text{'s prediction}$

**Why does $m_1$ have variance 2?** Because $m_1$ has an unknown parameter μ. It's uncertain about both the noise AND where μ is. $m_2$ has no unknown parameter — it's just one Gaussian with variance 1.

---

### Exercise 4 (Kalman-Style Posterior Variance Update)

> In a Kalman-style update, the posterior variance update is:
>
> Options:
> - (a) $\sigma_k^2 = (1-K_k)\cdot\sigma_{k-1}^2 + \sigma_\epsilon^2$
> - (b) $\sigma_k^2 = \sigma_{k-1}^2 + K_k\cdot(\sigma_\epsilon^2-\sigma_{k-1}^2)$
> - (c) $\sigma_k^2 = K_k\cdot\sigma_{k-1}^2$
> - (d) $\sigma_k^2 = (1-K_k)\cdot\sigma_{k-1}^2$

### STEP-BY-STEP SOLUTION

**Step 1: Understand the setup**

This is the Kalman filter applied to estimating a static parameter θ. At step k:
- Prior (before seeing $x_k$): $p(\theta|D_{k-1}) = \mathcal{N}(\theta|\mu_{k-1}, \sigma_{k-1}^2)$
- Likelihood: $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\epsilon^2)$
- Posterior (after seeing $x_k$): $p(\theta|D_k) = \mathcal{N}(\theta|\mu_k, \sigma_k^2)$

**Step 2: Use the Gaussian multiplication rule**

Posterior precision = prior precision + likelihood precision:

$$\frac{1}{\sigma_k^2} = \frac{1}{\sigma_{k-1}^2} + \frac{1}{\sigma_\epsilon^2}$$

**Step 3: Solve for $\sigma_k^2$**

$$\sigma_k^2 = \frac{1}{\frac{1}{\sigma_{k-1}^2} + \frac{1}{\sigma_\epsilon^2}} = \frac{\sigma_{k-1}^2 \cdot \sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$$

Now factor out $\sigma_{k-1}^2$:

$$\sigma_k^2 = \sigma_{k-1}^2 \cdot \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$$

**Step 4: Recognize the Kalman gain**

The Kalman gain is:

$$K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$$

So $1 - K_k = 1 - \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2} = \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$

**Step 5: Substitute**

$$\sigma_k^2 = \sigma_{k-1}^2 \cdot \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2} = \sigma_{k-1}^2 \cdot (1 - K_k) = (1 - K_k)\cdot\sigma_{k-1}^2$$

**Step 6: Match the answer**

**(a)** Adds $+\sigma_\epsilon^2$ at the end — this would make variance increase, which is wrong. ELIMINATE.
**(b)** A completely different form — doesn't match the derivation. ELIMINATE.
**(c)** Uses $K_k$ instead of $(1-K_k)$ — this would give the wrong factor. ELIMINATE.
**(d)** Matches exactly. ✓

**Answer: (d) $\sigma_k^2 = (1-K_k)\cdot\sigma_{k-1}^2$** ✅

### KEY INTUITION

- Since $0 < K_k < 1$, we have $0 < (1-K_k) < 1$
- So $\sigma_k^2 < \sigma_{k-1}^2$ — **posterior variance always decreases** with each new observation
- This makes sense: more data → more certainty → lower variance
- The Kalman gain $K_k$ controls how fast: high $K_k$ (trusting the observation more) → bigger variance reduction

---

### Answers

<details>
<summary>Exercise 1</summary>
**Answer: (c) 𝒩(μ|0.5, 0.5)** Posterior precision = 1/1 + 1/1 = 2, so variance = 1/2 = 0.5. Mean = 0.5 × (0/1 + 1/1) = 0.5
</details>

<details>
<summary>Exercise 2</summary>
**Answer: (a) 𝒩(1|0, 2)** Evidence = 𝒩(x|μ₀, σ²₀ + σ²) = 𝒩(1|0, 1+1) = 𝒩(1|0, 2)
</details>

<details>
<summary>Exercise 3</summary>
**Answer: (c)** p(x=2|m₁) = 𝒩(2|0, 2), p(x=2|m₂) = 𝒩(2|1, 1). Weighted sum: (2/3)𝒩(2|0, 2) + (1/3)𝒩(2|1, 1)
</details>

<details>
<summary>Exercise 4</summary>
**Answer: (d)** In the standard Kalman filter, σ²_k = (1-K_k)·σ²_{k-1}. The posterior variance decreases by the Kalman gain factor.
</details>
