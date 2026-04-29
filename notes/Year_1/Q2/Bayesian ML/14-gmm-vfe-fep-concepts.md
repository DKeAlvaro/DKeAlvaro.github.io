# Exercise Type 14: GMM, VFE, FEP & Concept Questions

> **What the exam asks:** A mixed bag of questions testing your ability to spot the correct GMM form, understand VFE properties, reason about FEP conceptually, and distinguish true/false statements about Bayesian vs ML approaches, Gaussian properties, and overfitting.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $\pi_k$ | "pi sub k" | Mixing coefficient — how common is component k? |
| $z_{nk}$ | "z sub n k" | Is data point n in cluster k? (1 if yes, 0 if no) |
| $K$ | Capital K | Total number of clusters/components |
| $F[q]$ | "F of q" | The **VFE functional** — a function of the variational distribution q |
| $q(z)$ | "q of z" | The **variational distribution** — our approximation to the true posterior |
| $p(x,z)$ | "p of x comma z" | The **joint distribution** over observed and latent variables |
| $KL(q \,\|\, p)$ | "KL divergence of q from p" | How different q is from p — always ≥ 0 |
| $p(y_\bullet \mid x_\bullet, D)$ | "prob of y bullet given x bullet and data" | Predictive distribution for a new data point |
| $L(\theta)$ | "L of theta" | The **likelihood function** — a function of the parameters |

### The Core Ideas — Plain English

**GMM (Gaussian Mixture Model):** Data comes from multiple hidden clusters, each generating points from its own Gaussian. The joint distribution uses a **product** over components, raised to the power $z_{nk}$, which acts as a switch — only the active cluster's term survives.

**VFE (Variational Free Energy):** When the true posterior is too hard to compute, we approximate it with a simpler distribution $q(z)$. VFE measures how good our approximation is. **Minimizing VFE** simultaneously improves the approximation and gives an estimate of the model evidence.

**FEP (Free Energy Principle):** A theory of intelligent behavior. Agents have an internal model of the world. They **perceive** by updating beliefs to match observations (minimize free energy). They **act** by choosing actions that minimize expected future surprise. Goals are encoded as **target priors** — preferred future states built into the model.

**Bayesian vs MLE:** MLE maximizes fit only. Bayesian averages over uncertainty. As data grows, MLE ≈ MAP because the likelihood dominates the prior. Bayesian evidence automatically penalizes complexity — no separate test set needed.

---

## Part 1: The Key Formulas (MEMORIZE)

### GMM Joint Distribution

$$p(x_n, z_n) = \prod_{k=1}^K \left(\pi_k \cdot \mathcal{N}(x_n \mid \mu_k, \Sigma_k)\right)^{z_{nk}}$$

**Spotting trick:** Both $\pi_k$ AND $\mathcal{N}$ must be inside the parentheses raised to $z_{nk}$ (not $z_n$). Product ∏, not sum Σ.

### VFE Functional

$$F[q] = \int q(z) \log \frac{q(z)}{p(x,z)} \, dz$$

| Property | Expression |
|----------|------------|
| **Upper bound** | $F[q] \geq -\log p(x)$ for any $q(z)$ |
| **Equality** | $F[q] = -\log p(x)$ when $q(z) = p(z \mid x)$ |
| **Minimization** | Minimizes $KL(q(z) \,\|\, p(z \mid x))$ AND gives evidence estimate |

### FEP Core Principles

| Concept | What It Means |
|---------|---------------|
| **Perception** | Minimize free energy (update beliefs to match observations) |
| **Action** | Minimize **expected free energy** of future states |
| **Goals** | Encoded as **target priors** in the generative model |
| **Decision making** | Minimization of a functional of **beliefs** (not costs) |

### Concept Facts

| Statement | True/False | Why |
|-----------|-----------|-----|
| Likelihood = function of parameters | True | $L(\theta) = p(D \mid \theta)$ |
| Linear combination of Gaussians = Gaussian | True | $Z = aX + bY$ preserves Gaussianity |
| Product of Gaussians = Gaussian | False | $Z = XY$ is NOT Gaussian |
| MLE = MAP always | False | Only when prior is uniform |
| Bayesian evidence = fit − complexity | True | Built-in overfitting protection |
| Discriminative classification ≈ regression | True | Predicts label, not full density |

---

## Part 2: Tricks & Shortcuts

### TRICK 1: GMM Joint — Both Must Be in the Power

The correct answer ALWAYS has both $\pi_k$ and $\mathcal{N}$ inside the parentheses raised to $z_{nk}$.

If only $\mathcal{N}$ has the exponent → wrong.
If only $\pi_k$ has the exponent → wrong.
If it uses a sum (Σ) instead of product (∏) → that's the marginal, not the joint.

### TRICK 2: VFE — Always ≥ Negative Log Evidence

Think: "Variational Free Energy is an **Upper** bound" → VFEU.

- If an option says ≤ → wrong direction.
- If it says equality at $q(z) = p(z)$ (prior) → wrong, it's the **posterior** $p(z \mid x)$.
- If it says equality at $q(z) = 0$ → nonsense, not a valid distribution.

### TRICK 3: FEP — Always MINIMIZE, Never Maximize

FEP is about MINIMIZING free energy (or expected free energy).

- "Maximize free energy" → wrong direction.
- "Cost function" → wrong framework (traditional engineering, not FEP).
- "Desired" vs "actual" future → it's **desired** (target priors), not actual.
- "Generative model" → if a statement says agents hold one, it's true.

### TRICK 4: Gaussian Properties

- **Linear combination** ($aX + bY$) → Gaussian ✅
- **Product** ($XY$) → NOT Gaussian ❌
- **Sum of distributions** (mixture) → NOT Gaussian in general ❌
- **Ratio** ($X/Y$) → NOT Gaussian ❌

### TRICK 5: Bayesian vs MLE

- More data → likelihood gets **narrower** (more certain), prior stays fixed.
- MLE ≈ MAP eventually because likelihood dominates.
- Bayesian methods are NOT faster — often more expensive (integration).
- No train/test split needed — complexity penalty handles overfitting.

---

## Part 3: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-B, Question 1e — GMM Form)

> Which is a correct GMM specification for $p(x_n, z_n)$ with one-hot $z_n$?
>
> Options:
> - (a) $p(x_n,z_n) = \prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k))^{z_n}$
> - (b) $p(x_n,z_n) = \prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k)^{z_{nk}}$
> - (c) $p(x_n,z_n) = \sum_{k=1}^K \pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k)$
> - (d) $p(x_n,z_n) = \prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k))^{z_{nk}}$

### STEP-BY-STEP SOLUTION

**Step 1: Check the exponent**

We need $z_{nk}$ (the k-th element), not $z_n$ (the whole vector).

(a) uses $z_n$ → ELIMINATE.

**Step 2: Check what's raised to the power**

Both $\pi_k$ AND $\mathcal{N}$ must be inside the exponentiation — the power selects the right cluster entirely.

(b) only $\mathcal{N}$ has the exponent, $\pi_k$ is outside → ELIMINATE.

**Step 3: Check product vs sum**

The joint uses a product (∏) — we're selecting one component per data point.
The marginal uses a sum (Σ) — we've summed out the hidden variable.

(c) uses a sum → this is the marginal, not the joint → ELIMINATE.

**Step 4: Verify (d)**

(d) has: product over k ✓, both $\pi_k$ and $\mathcal{N}$ inside ✓, raised to $z_{nk}$ ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 2 (2021-Resit, Question 4e — VFE Property)

> $F[q] = \int q(z) \log \frac{q(z)}{p(x,z)} \, dz$. Which statement is true?
>
> Options:
> - (a) $F[q] = -\log p(x)$ if $q(z) = 0$
> - (b) $F[q] \leq -\log p(x)$ for any $q(z)$
> - (c) $F[q] \geq -\log p(x)$ for any $q(z)$
> - (d) $F[q] = -\log p(x)$ if $q(z) = p(z)$

### STEP-BY-STEP SOLUTION

**Step 1: Recall the fundamental VFE property**

$F[q] \geq -\log p(x)$ for any $q(z)$. It's an **upper bound** on the negative log evidence.

This immediately gives us (c).

**Step 2: Eliminate the rest**

(a) $q(z) = 0$ is not a valid probability distribution (doesn't integrate to 1) → ELIMINATE.

(b) Wrong direction — it's ≥ not ≤ → ELIMINATE.

(d) Equality is at $q(z) = p(z \mid x)$ (the true posterior), not $q(z) = p(z)$ (the prior) → ELIMINATE.

**Answer: (c)** ✅

---

### EXAM QUESTION 3 (2023, Question 4f — VFE & Bayesian Inference)

> Why can VFE minimization approximate Bayesian inference?
>
> Options:
> - (a) VFE is Bayesian inference plus Gaussian noise
> - (b) VFE minimizes KL-divergence to evidence, and VFE is upper bound on posterior
> - (c) VFE minimizes evidence by optimizing variational posterior
> - (d) VFE minimizes KL-divergence between variational and true posterior, and VFE is upper bound on negative log evidence

### STEP-BY-STEP SOLUTION

**Step 1: Two key facts about VFE**

1. $F[q] = KL(q(z) \,\|\, p(z \mid x)) - \log p(x)$. Since $-\log p(x)$ doesn't depend on $q$, minimizing $F[q]$ minimizes the KL divergence to the true posterior.
2. $F[q] \geq -\log p(x)$ (upper bound on negative log evidence).

**Step 2: Match the options**

(a) "Plus Gaussian noise" — nonsense → ELIMINATE.

(b) "KL to evidence" — wrong, it's KL to the posterior. "Upper bound on posterior" — wrong, it's on negative log evidence → ELIMINATE.

(c) "Minimizes evidence" — wrong, it minimizes KL to the posterior → ELIMINATE.

(d) Both parts are correct → ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 4 (2021-Part-B, Question 1b — VB Properties)

> Which is NOT a property of the Variational Bayesian approach?
>
> Options:
> - (a) Transfers Bayesian ML to optimization problem
> - (b) VB finds posteriors by maximizing Bayesian evidence
> - (c) VFE minimization gives posterior AND evidence
> - (d) Global VFE minimization realizes Bayes rule

### STEP-BY-STEP SOLUTION

(a) True — VB turns integration into optimization → NOT the answer.

(b) VB finds posteriors by **minimizing** VFE (upper bound on negative log evidence), not "maximizing evidence" → **This is wrong** → ELIMINATE as the answer.

(c) True — VFE gives both $q(z)$ (approximate posterior) and a lower bound on log evidence → NOT the answer.

(d) True — at the global minimum, $q(z) = p(z \mid x)$ (exact Bayes rule) → NOT the answer.

**Answer: (b)** ✅

---

### EXAM QUESTION 5 (2022, Question 4a — FEP Comprehension)

> Which statement is most consistent with FEP?
>
> Options:
> - (a) Actions aim to minimize free energy of future states
> - (b) Actions aim to minimize complexity of future states
> - (c) Intelligent decision making requires minimization of a functional of beliefs about future states
> - (d) Intelligent decision making requires minimization of a cost function of future states

### STEP-BY-STEP SOLUTION

(a) Close, but imprecise — it's about minimizing a functional of **beliefs**, not directly "free energy of future states."

(b) "Minimize complexity" — not the core idea of FEP → ELIMINATE.

(c) Yes — expected free energy is a **functional** of probability distributions (beliefs) about future states → ✓

(d) "Cost function" — that's traditional control theory, not FEP → ELIMINATE.

**Answer: (c)** ✅

---

### EXAM QUESTION 6 (2021-Part-B, Question 1d — FEP Goal-Driven Behavior)

> How to equip an agent with goal-driven behavior in FEP?
>
> Options:
> - (a) Specify cost function, minimize costs
> - (b) Extend generative model with target priors for future observations. Minimize Free Energy.
> - (c) Specify cost function of actions, minimize
> - (d) Extend with posterior for actions, maximize posterior

### STEP-BY-STEP SOLUTION

In FEP, goals are encoded as **target priors** — preferred future states built into the generative model. The agent then minimizes expected free energy, which naturally achieves these goals.

(a), (c) "Cost function" — wrong framework → ELIMINATE.
(d) Doesn't explain how goals are encoded → ELIMINATE.

**Answer: (b)** ✅

---

### EXAM QUESTION 7 (2021-Part-B, Question 5b — FEP Consistent Statements)

> Which statements are consistent with FEP?
> - (a) Active inference agent holds generative model for sensory inputs
> - (b) Actions inferred from differences between predicted and desired future observations
> - (c) Actions inferred from differences between predicted and actual future observations
> - (d) Agent focuses on explorative behavior only
>
> Options:
> - (a) (a) and (b)
> - (b) (a)
> - (c) (b) and (d)
> - (d) (c) and (d)

### STEP-BY-STEP SOLUTION

(a) True — generative model is fundamental to FEP → ✓
(b) True — actions bridge predicted vs. **desired** (target prior) states → ✓
(c) False — it's about desired, not "actual" future → ✗
(d) False — agents balance exploration AND exploitation → ✗

(a) and (b) are true.

**Answer: (a) — (a) and (b)** ✅

---

### EXAM QUESTION 8 (2021-Part-A, Question 1a — Likelihood Terminology)

> "The likelihood of the parameters" is more appropriate than "the likelihood of the data".
>
> Options: (a) true, (b) false

### STEP-BY-STEP SOLUTION

The likelihood IS a function of the parameters given the data: $L(\theta) = p(D \mid \theta)$. So "likelihood of the parameters" is correct usage.

**Answer: (a) true** ✅

---

### EXAM QUESTION 9 (2021-Part-A, Question 1b — Gaussian Properties)

> If X and Y are independent Gaussian distributed variables, then $Z = 3X - XY$ is also Gaussian.
>
> Options: (a) true, (b) false

### STEP-BY-STEP SOLUTION

The product $XY$ of two Gaussians is NOT Gaussian in general. Linear combinations like $3X - Y$ are Gaussian, but $3X - XY$ involves a product term.

**Answer: (b) false** ✅

---

### EXAM QUESTION 10 (2021-Part-A, Question 1d — MLE vs MAP)

> MLE always selects the parameter where the Bayesian posterior distribution is maximal.
>
> Options: (a) true, (b) false

### STEP-BY-STEP SOLUTION

MLE maximizes $p(D \mid \theta)$. MAP maximizes $p(D \mid \theta)p(\theta)$. They're only equal when the prior $p(\theta)$ is uniform. MLE ≠ MAP in general.

**Answer: (b) false** ✅

---

### EXAM QUESTION 11 (2021-Resit, Question 4b — Bayesian vs MLE)

> Which statement is most accurate?
>
> Options:
> - (a) ML becomes better approximation as data grows, since prior becomes wider
> - (b) ML becomes worse as data grows, since both likelihood and prior become wider
> - (c) ML becomes better as data grows, since likelihood becomes wider while prior doesn't depend on data
> - (d) ML becomes better as data grows, since likelihood becomes narrower while prior doesn't depend on data

### STEP-BY-STEP SOLUTION

With more data:
- Likelihood becomes **narrower** (more certain about the true parameter)
- Prior stays the same (doesn't depend on data)
- The likelihood eventually dominates → MLE ≈ MAP

(a) Prior doesn't become wider → ELIMINATE.
(b) Both don't become wider → ELIMINATE.
(c) Likelihood becomes narrower, not wider → ELIMINATE.

**Answer: (d)** ✅

---

### EXAM QUESTION 12 (2021-Part-B, Question 1a — Bayesian Approach)

> Which statement is FALSE about the Bayesian approach?
>
> Options:
> - (a) No need to split data into train/test. All data used for training.
> - (b) Fundamentally sound, based on probability theory.
> - (c) Requires explicit model assumptions upfront.
> - (d) Fast alternative to maximum likelihood.

### STEP-BY-STEP SOLUTION

Bayesian methods are NOT generally faster — they're often more computationally expensive due to integration over parameters.

**Answer: (d) false** ✅

---

### EXAM QUESTION 13 (2021-Part-B, Question 5d — Discriminative Classification)

> Which statements are true?
> - (a) Product of independent Gaussians is Gaussian
> - (b) Linear combination $Z = 3X - Y$ of independent Gaussians is Gaussian
> - (c) Sum of two Gaussians is Gaussian
> - (d) Discriminative classification is more similar to regression than density estimation
>
> Options:
> - (a) (b) and (c)
> - (b) (a) and (d)
> - (c) (b) and (d)
> - (d) (b) and (c)

### STEP-BY-STEP SOLUTION

(a) False — the product random variable $Z = XY$ is NOT Gaussian → ✗
(b) True — linear combinations of Gaussians are Gaussian → ✓
(c) True — sum of Gaussians is Gaussian → ✓
(d) True — discriminative classification predicts a label value (like regression), not a full density → ✓

Options with (a) → ELIMINATE. (b), (c), and (d) are all true.

Best match: **(c) — (b) and (d)**.

**Answer: (c)** ✅

---

### EXAM QUESTION 14 (2023, Question 4b — Overfitting)

> Why is a "Bayesian engineer" not concerned about overfitting?
>
> Options:
> - (a) Model evidence decomposes as "fit minus complexity". Complexity prevents overfitting.
> - (b) Uses separate test set
> - (c) Minimizes probability of overfitting
> - (d) Evidence decomposes as "fit minus entropy"

### STEP-BY-STEP SOLUTION

Bayesian model evidence naturally penalizes complexity (the "Occam factor"):

$$\log p(D \mid m) = \text{fit} - \text{complexity}$$

This is built-in overfitting protection — no separate test set needed.

(b) That's the frequentist approach → ELIMINATE.
(c) Vague, not the reason → ELIMINATE.
(d) "Entropy" — wrong term, it's complexity → ELIMINATE.

**Answer: (a)** ✅

---

### EXAM QUESTION 15 (2021-Part-B, Question 1c — Bayesian Model Comparison)

> Posterior model probability $p(m_k \mid D)$:
>
> Options:
> - (a) $p(m_k \mid D) = p(m_k) \int p(\theta \mid D,m_k) \, p(D \mid m_k) \, d\theta$
> - (b) $p(m_k \mid D) = p(m_k) \int p(D \mid \theta,m_k) \, p(\theta \mid m_k) \, d\theta$
> - (c) $p(m_k \mid D) = \sum_n p(m_k) \, p(D \mid m_k)$
> - (d) $p(m_k \mid D) = \int p(D \mid \theta,m_k) \, p(\theta \mid m_k) \, d\theta$

### STEP-BY-STEP SOLUTION

$$p(m_k \mid D) = \frac{p(D \mid m_k) \cdot p(m_k)}{p(D)}$$

Where the evidence is:

$$p(D \mid m_k) = \int p(D \mid \theta,m_k) \, p(\theta \mid m_k) \, d\theta$$

So without the normalizing constant $p(D)$:

$$p(m_k \mid D) \propto p(m_k) \int p(D \mid \theta,m_k) \, p(\theta \mid m_k) \, d\theta$$

(a) Integrates $p(\theta \mid D,m_k) \cdot p(D \mid m_k)$ — wrong terms → ELIMINATE.
(c) Sums over data points — nonsense → ELIMINATE.
(d) Missing the prior $p(m_k)$ — that's just the evidence, not the posterior → ELIMINATE.

**Answer: (b)** ✅

---

## Part 4: Practice Exercises

### Exercise 1 (GMM Form)

> Which is a correct GMM for $p(x_n, z_n)$ with one-hot $z_n$?
>
> Options:
> - (a) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k))^{z_n}$
> - (b) $\prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k)^{z_{nk}}$
> - (c) $\sum_{k=1}^K \pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k)$
> - (d) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n \mid \mu_k,\Sigma_k))^{z_{nk}}$

---

### Exercise 2 (VFE Property)

> $F[q] = \int q(z) \log \frac{q(z)}{p(x,z)} \, dz$. Which is true?
>
> Options:
> - (a) $F[q] = -\log p(x)$ if $q(z) = 0$
> - (b) $F[q] \leq -\log p(x)$ for any $q(z)$
> - (c) $F[q] \geq -\log p(x)$ for any $q(z)$
> - (d) $F[q] = -\log p(x)$ if $q(z) = p(z)$

---

### Exercise 3 (FEP Action)

> In FEP, how does an agent choose actions?
>
> Options:
> - (a) Minimize cost function of future states
> - (b) Minimize expected free energy in future states
> - (c) Maximize free energy in future states
> - (d) Maximize expected accuracy of future states

---

### Exercise 4 (Gaussian Property)

> Which is true?
>
> Options:
> - (a) Product of independent Gaussians is Gaussian
> - (b) Linear combination of independent Gaussians is Gaussian
> - (c) Ratio of Gaussians is Gaussian
> - (d) Product $Z = XY$ of Gaussians is Gaussian

---

### Exercise 5 (Bayesian vs MLE)

> As data size grows:
>
> Options:
> - (a) ML becomes worse, prior becomes wider
> - (b) ML becomes better, likelihood becomes narrower, prior unchanged
> - (c) ML becomes worse, both become wider
> - (d) ML becomes better, prior becomes narrower

---

### Exercise 6 (Discriminative Classification)

> Discriminative approach to classification for new input $x_\bullet$:
>
> Options:
> - (a) $p(y_\bullet \mid x_\bullet,D) = \int p(y_\bullet \mid x_\bullet,\theta,D) \, d\theta$
> - (b) $p(y_\bullet \mid x_\bullet) = \int p(y_\bullet \mid x_\bullet,\theta) \, p(\theta) \, d\theta$
> - (c) $p(y_\bullet \mid x_\bullet,D) = \int p(y_\bullet \mid x_\bullet,\theta) \, p(\theta \mid D) \, d\theta$
> - (d) $p(y_\bullet \mid x_\bullet) = \int p(y_\bullet \mid x_\bullet,\theta) \, d\theta$

---

### Exercise 7 (Overfitting)

> Why are Bayesian engineers not concerned about overfitting?
>
> Options:
> - (a) Evidence = fit − complexity
> - (b) Use separate test set
> - (c) Minimize overfitting probability
> - (d) Evidence = fit − entropy

---

### Exercise 8 (Generative Model for Signal Recovery)

> Bayesian records signal $x$, wants to recover speech $s$. How?
>
> Options:
> - (a) Model $p(x,s,z) = p(s \mid x,z)p(x,z)$, compute $p(s \mid x) \propto \int p(s \mid x,z) \, dz$
> - (b) Model $p(x,s,z) = p(s \mid x,z)p(x,z)$, compute $p(s \mid x) \propto \int p(s \mid x,z)p(x,z) \, dz$
> - (c) Model $p(x,s,z) = p(x \mid s,z)p(s,z)$, compute $p(s \mid x,z) = \frac{p(x \mid s,z)p(s,z)}{p(x,z)}$
> - (d) Model $p(x,s,z) = p(x \mid s,z)p(s,z)$, compute $p(s \mid x) \propto \int p(x \mid s,z)p(s,z) \, dz$

---

## Part 5: Answers

<details>
<summary>Exercise 1</summary>

**Answer: (d)**

(a) uses $z_n$ instead of $z_{nk}$.
(b) only $\mathcal{N}$ has the exponent.
(c) is a sum (that's the marginal, not the joint).
(d) is correct: both inside, power $z_{nk}$, product.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (c)**

VFE is always ≥ negative log evidence (upper bound).
(a) $q(z)=0$ is not a valid distribution.
(b) wrong direction.
(d) equality at posterior, not prior.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b)**

Actions minimize expected free energy, not maximize. Not cost functions.
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (b)**

Linear combinations of Gaussians are Gaussian. Products and ratios are not.
</details>

<details>
<summary>Exercise 5</summary>

**Answer: (b)**

With more data, likelihood narrows (more certain), prior stays fixed. ML ≈ MAP eventually.
</details>

<details>
<summary>Exercise 6</summary>

**Answer: (c)**

Bayesian predictive: average the likelihood $p(y \mid x,\theta)$ over the posterior $p(\theta \mid D)$.
(a) has wrong conditioning. (b), (d) don't use the data $D$.
</details>

<details>
<summary>Exercise 7</summary>

**Answer: (a)**

Evidence = training fit − complexity. The complexity term prevents overfitting.
(b) is the frequentist approach. (d) says "entropy" — wrong.
</details>

<details>
<summary>Exercise 8</summary>

**Answer: (d)**

Joint model $p(x,s,z) = p(x \mid s,z)p(s,z)$. Marginalize $z$: $p(s \mid x) \propto \int p(x \mid s,z)p(s,z) \, dz$.
(a), (b) use wrong factorization. (c) conditions on $z$ which is unobserved.
</details>
