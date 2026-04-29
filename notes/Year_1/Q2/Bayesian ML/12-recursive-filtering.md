# Exercise Type 12: Recursive Bayesian Filtering (Kalman-Style Updates)

> **What the exam asks:** You observe a process sequentially and must recursively update your estimate of an unknown parameter θ (or latent state z) after each new observation.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $x_t$ or $x_k$ | "x sub t" or "x sub k" | The observation at time t (or step k) — what we actually see |
| $\theta$ | Greek letter theta | The unknown parameter we're trying to estimate |
| $z_t$ | "z sub t" | The latent (hidden) state at time t |
| $\epsilon_t$ | "epsilon sub t" | The observation noise at time t — random error |
| $\sigma_\epsilon^2$ | "sigma epsilon squared" | The variance of the observation noise |
| $\mu_k$ | "mu sub k" | The mean of our belief about θ after k observations |
| $\sigma_k^2$ | "sigma squared sub k" | The variance of our belief about θ after k observations (our uncertainty) |
| $D_k$ | "D sub k" | The dataset of the first k observations: $\{x_1, x_2, ..., x_k\}$ |
| $K_k$ | "K sub k" | The **Kalman gain** — how much we trust the new observation vs. our prior |
| $\propto$ | Proportional to symbol | "The shape is right, but the scale might not add to 1 yet" |
| $\rightarrow$ | Arrow | "approaches" — what happens as k gets very large |

### What Is Recursive Bayesian Filtering? (Plain English)

Imagine you're trying to figure out the true temperature θ of a room. You can't measure it perfectly — your thermometer has some noise. But you get a new reading every minute.

**Recursive filtering says:** "After each new reading, update your belief about θ using Bayes' rule. Your updated belief becomes the prior for the next step."

The key idea: **you don't need to reprocess all past data.** You just need:
1. Your current belief (the previous posterior)
2. The new observation

### The Observation Model

$$x_t = \theta + \epsilon_t \quad \text{where } \epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$$

**In plain English:** "The observation at time t equals the true value θ plus some random noise."

This means: $p(x_t|\theta) = \mathcal{N}(x_t|\theta, \sigma_\epsilon^2)$

**How to read this:** "Given θ, the observation $x_t$ is Gaussian distributed with mean θ and variance $\sigma_\epsilon^2$."

---

## Part 1: The Recursive Update

### The Core Formula

$$p(\theta|D_k) = p(\theta|x_k, D_{k-1}) \propto p(x_k|\theta) \cdot p(\theta|D_{k-1})$$

**In plain English:**

> Updated belief ∝ (how well θ explains the new observation) × (previous belief)

**Breaking it down:**
- $p(\theta|D_k)$ = posterior after k observations (our updated belief)
- $p(x_k|\theta)$ = likelihood (how well θ explains the k-th observation)
- $p(\theta|D_{k-1})$ = previous posterior (our belief before seeing the k-th observation — this becomes the new prior)

### The Kalman Filter Update Equations

For our specific model ($x_t = \theta + \epsilon_t$):

**Kalman Gain:**
$$K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$$

**Mean Update:**
$$\mu_k = \mu_{k-1} + K_k \cdot (x_k - \mu_{k-1})$$

**Variance Update:**
$$\sigma_k^2 = (1 - K_k) \cdot \sigma_{k-1}^2$$

### What Each Update Means

**Kalman Gain $K_k$:**
- If $K_k \approx 1$: we trust the new observation more (prior uncertainty is large compared to noise)
- If $K_k \approx 0$: we trust our prior more (noise is large compared to prior uncertainty)

**Mean Update:**
- $x_k - \mu_{k-1}$ = "prediction error" = (what we saw) - (what we expected)
- We adjust our mean by $K_k$ times the prediction error
- If the observation was higher than expected, we increase our estimate

**Variance Update:**
- $(1 - K_k)$ is between 0 and 1
- So the variance always **decreases** (or stays the same)
- Each new observation makes us more certain

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2022, Question 3a)

> Observation model: $x_t = \theta + \epsilon_t$, $\epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$
>
> **Which is the correct likelihood?**
>
> Options:
> - (a) $p(x_k|\theta) = \mathcal{N}(x_k|\mu_k, \sigma_\epsilon^2 + \sigma_\theta^2)$
> - (b) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\epsilon^2)$
> - (c) $p(x_k|\theta) = \mathcal{N}(x_k|0, \sigma_\epsilon^2 + \sigma_\theta^2)$
> - (d) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\theta^2)$

### STEP-BY-STEP SOLUTION

**Step 1: Understand the model**

$x_t = \theta + \epsilon_t$ means:
- Given θ, the observation $x_t$ equals θ plus noise
- The noise has variance $\sigma_\epsilon^2$

**Step 2: Write the likelihood**

Given θ, the distribution of $x_k$ is:

$$p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\epsilon^2)$$

Mean = θ (the true value), variance = $\sigma_\epsilon^2$ (the noise variance).

**Step 3: Match the answer**

(b) matches exactly.

**(a)** Mean is $\mu_k$ (the posterior mean) — but the likelihood is about how θ generates data, not about our belief. ELIMINATE.
**(c)** Mean is 0 — wrong, should be θ. ELIMINATE.
**(d)** Variance is $\sigma_\theta^2$ — wrong, should be $\sigma_\epsilon^2$ (the observation noise). ELIMINATE.

**Answer: (b)** ✅

---

### EXAM QUESTION 2 (2022, Question 3b)

> Complete the Kalman filter derivation. The correct update is:
>
> Options:
> - (a) $K_k = \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2 + \sigma_\epsilon^2$
> - (b) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = \sigma_{k-1}^2 + K_k(\sigma_\epsilon^2-\sigma_{k-1}^2)$
> - (c) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \frac{1}{2}\mu_{k-1} + \frac{1}{2}K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2 + \sigma_\epsilon^2$
> - (d) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2$

### STEP-BY-STEP SOLUTION

**Step 1: Derive the Kalman gain**

Using the Gaussian multiplication formula:

$$\frac{1}{\sigma_k^2} = \frac{1}{\sigma_{k-1}^2} + \frac{1}{\sigma_\epsilon^2}$$

Solving for $\sigma_k^2$:

$$\sigma_k^2 = \frac{\sigma_{k-1}^2 \cdot \sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2} = \sigma_{k-1}^2 \cdot \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2} = \sigma_{k-1}^2(1 - K_k)$$

Where:

$$K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$$

**Step 2: Derive the mean update**

$$\frac{\mu_k}{\sigma_k^2} = \frac{\mu_{k-1}}{\sigma_{k-1}^2} + \frac{x_k}{\sigma_\epsilon^2}$$

Standard Kalman filter result:

$$\mu_k = \mu_{k-1} + K_k(x_k - \mu_{k-1})$$

**Step 3: Match the answer**

**(a)** $K_k = \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$ — numerator is wrong. It should be $\sigma_{k-1}^2$ (prior variance), not $\sigma_\epsilon^2$ (noise variance). ELIMINATE.

**(b)** Variance update: $\sigma_k^2 = \sigma_{k-1}^2 + K_k(\sigma_\epsilon^2-\sigma_{k-1}^2)$ — this is NOT the standard form. ELIMINATE.

**(c)** Mean update has factors of 1/2 — this is wrong. ELIMINATE.

**(d)** $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$ ✓, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$ ✓, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2$ ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 3 (2022, Question 3c)

> What happens as $k \to \infty$ (number of observations goes to infinity)?
>
> Options:
> - (a) $\sigma_k^2 \rightarrow \sigma_{k-1}^2$ (stationarity)
> - (b) $\mu_k \approx \mu_{k-1}$ (stationarity)
> - (c) $\sigma_k^2 \rightarrow \sigma_\epsilon^2$
> - (d) $K_k \rightarrow 1$

### STEP-BY-STEP SOLUTION

**Step 1: What happens to the variance?**

$\sigma_k^2 = (1-K_k)\sigma_{k-1}^2$. As k increases, we get more and more data, so our uncertainty decreases.

$K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$. As $\sigma_{k-1}^2 \to 0$ (we become very certain), $K_k \to 0$.

So $\sigma_k^2 \to 0$ (not $\sigma_\epsilon^2$, not $\sigma_{k-1}^2$).

**(a)** Wrong — $\sigma_k^2 \to 0$, not $\sigma_{k-1}^2$. ELIMINATE.
**(c)** Wrong — $\sigma_k^2 \to 0$, not $\sigma_\epsilon^2$. ELIMINATE.
**(d)** Wrong — $K_k \to 0$, not 1. ELIMINATE.

**Step 2: What happens to the mean?**

As k → ∞, the mean converges to the true value of θ. Once converged, $\mu_k \approx \mu_{k-1}$ — it barely changes with each new observation because we're already very certain.

**(b)** Correct — as we accumulate infinite data, the estimate converges (becomes stationary).

**Answer: (b)** ✅

---

### EXAM QUESTION 4 (2021-Part-B, Question 5a)

> For a state space model, how to recursively update $p(z_t|x_{1:t})$?
>
> Options:
> - (a) $p(z_t|x_{1:t}) = p(x_t|z_t) \sum_{z_{t-1}} p(z_t|z_{t-1}) p(z_{t-1}|x_{1:t-1})$
> - (b) $p(z_t|x_{1:t}) \propto p(x_t|z_t) \sum_{z_{t-1}} p(z_t|z_{t-1}) p(z_{t-1}|x_{1:t-1})$
> - (c) $p(z_t|x_{1:t}) = \sum_{x_t} p(x_t|z_t) p(z_t|x_{1:t-1})$
> - (d) $p(z_t|x_{1:t}) \propto p(z_t, x_{1:t})$

### STEP-BY-STEP SOLUTION

**Step 1: The general recursive update**

$$p(z_t|x_{1:t}) \propto p(x_t|z_t) \cdot p(z_t|x_{1:t-1})$$

**Step 2: The prediction step**

We need $p(z_t|x_{1:t-1})$ — our prediction for the current state based on past observations:

$$p(z_t|x_{1:t-1}) = \sum_{z_{t-1}} p(z_t|z_{t-1}) \cdot p(z_{t-1}|x_{1:t-1})$$

This says: "To predict the current state, consider all possible previous states, weighted by how likely each previous state was."

**Step 3: Combine**

$$p(z_t|x_{1:t}) \propto p(x_t|z_t) \sum_{z_{t-1}} p(z_t|z_{t-1}) p(z_{t-1}|x_{1:t-1})$$

**Step 4: Match the answer**

(b) matches exactly. Note the **∝** (proportional to), not **=**.

**(a)** Uses = instead of ∝. The recursive update needs normalization. ELIMINATE.
**(c)** Sums over $x_t$ (observations) instead of $z_{t-1}$ (previous states). ELIMINATE.
**(d)** Too vague — doesn't show the actual recursive structure. ELIMINATE.

**Answer: (b)** ✅

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Kalman Gain Pattern

$$K_k = \frac{\text{prior variance}}{\text{prior variance} + \text{observation noise}}$$

If the numerator is the noise variance → wrong.

### TRICK 2: Variance Always Decreases

$\sigma_k^2 = (1-K_k)\sigma_{k-1}^2$. Since $(1-K_k) < 1$, the variance shrinks.

If an option adds something to the variance → wrong.

### TRICK 3: Look for the ∝ Symbol

The recursive update is proportional to, not equal to. Options without ∝ are often wrong.

### TRICK 4: As k → ∞

- $\sigma_k^2 \to 0$ (certainty)
- $K_k \to 0$ (new observations matter less)
- $\mu_k \to$ true value (converges)

---

## Part 4: Practice Exercises

### Exercise 1

> Observation model: $x_t = \theta + \epsilon_t$, $\epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$
>
> **Correct likelihood:**
>
> Options:
> - (a) $p(x_k|\theta) = \mathcal{N}(x_k|\mu_k, \sigma_\epsilon^2 + \sigma_\theta^2)$
> - (b) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\epsilon^2)$
> - (c) $p(x_k|\theta) = \mathcal{N}(x_k|0, \sigma_\epsilon^2 + \sigma_\theta^2)$
> - (d) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\theta^2)$

---

### Exercise 2

> **Correct Kalman filter update:**
>
> Options:
> - (a) $K_k = \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2 + \sigma_\epsilon^2$
> - (b) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = \sigma_{k-1}^2 + K_k(\sigma_\epsilon^2-\sigma_{k-1}^2)$
> - (c) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \frac{1}{2}\mu_{k-1} + \frac{1}{2}K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2 + \sigma_\epsilon^2$
> - (d) $K_k = \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2}$, $\mu_k = \mu_{k-1} + K_k(x_k-\mu_{k-1})$, $\sigma_k^2 = (1-K_k)\sigma_{k-1}^2$

---

### Exercise 3

> As $k \to \infty$:
>
> Options:
> - (a) $\sigma_k^2 \rightarrow \sigma_{k-1}^2$
> - (b) $\mu_k \approx \mu_{k-1}$ (stationarity)
> - (c) $\sigma_k^2 \rightarrow \sigma_\epsilon^2$
> - (d) $K_k \rightarrow 1$

---

### Exercise 4

> Recursive update for $p(z_t|x_{1:t})$:
>
> Options:
> - (a) $p(z_t|x_{1:t}) = p(x_t|z_t) \sum_{z_{t-1}} p(z_t|z_{t-1}) p(z_{t-1}|x_{1:t-1})$
> - (b) $p(z_t|x_{1:t}) \propto p(x_t|z_t) \sum_{z_{t-1}} p(z_t|z_{t-1}) p(z_{t-1}|x_{1:t-1})$
> - (c) $p(z_t|x_{1:t}) = \sum_{x_t} p(x_t|z_t) p(z_t|x_{1:t-1})$
> - (d) $p(z_t|x_{1:t}) \propto p(z_t, x_{1:t})$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (b)**

Given θ, x_k ~ 𝒩(θ, σ²_ε). The likelihood is centered at θ with observation noise variance.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (d)**

K_k = σ²_{k-1}/(σ²_{k-1}+σ²_ε) ✓
μ_k = μ_{k-1} + K_k(x_k - μ_{k-1}) ✓
σ²_k = (1-K_k)σ²_{k-1} ✓
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b)**

As k→∞: σ²_k → 0, K_k → 0, μ_k converges (becomes stationary).
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (b)**

The ∝ is crucial. The full update combines observation likelihood with predicted state (marginalized over previous state).
</details>
