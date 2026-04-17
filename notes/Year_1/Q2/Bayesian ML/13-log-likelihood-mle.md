# Exercise Type 13: Log-Likelihood & MLE for Generative Classifiers

> **What the exam asks:** Given a generative classifier model, write down the log-likelihood function and/or derive the Maximum Likelihood Estimate (MLE) for parameters like the mean and covariance of each class.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $D$ | Capital D | The **dataset** — all our training data |
| $\theta$ | Greek letter theta | The collection of ALL model parameters (means, covariances, mixing coefficients) |
| $\log$ | Logarithm (natural log, base e) | The inverse of exponentiation — turns products into sums |
| $\log p(D\|\theta)$ | "log probability of data given parameters" | The **log-likelihood** — how well do these parameters explain the data? |
| $\hat{\mu}_k$ | "mu hat sub k" | The MLE estimate for the mean of class k |
| $\hat{\Sigma}_k$ | "Sigma hat sub k" | The MLE estimate for the covariance of class k |
| $y_{nk}$ | "y sub n k" | Is data point n in class k? (1 if yes, 0 if no — one-hot encoding) |
| $\pi_k$ | "pi sub k" | The mixing coefficient — what fraction of data comes from class k |
| $(x-\mu)(x-\mu)^T$ | "outer product" | Matrix multiplication that gives a covariance-like matrix |
| $(x-\mu)^T(x-\mu)$ | "inner product" | Matrix multiplication that gives a scalar (single number) |

### What Is a Log-Likelihood? (Plain English)

The **likelihood** $p(D|\theta)$ answers: "If these were the true parameters, how likely would our data be?"

The **log-likelihood** $\log p(D|\theta)$ is the same thing but with a logarithm applied. We do this because:

1. **Products become sums** — much easier to work with
2. **Very small numbers become manageable** — likelihoods can be tiny (like $10^{-100}$), but their logs are reasonable (like $-230$)
3. **Maximizing the log gives the same answer as maximizing the original** — so we can use the log without changing the result

### What Is MLE? (Plain English)

**Maximum Likelihood Estimation** asks: "What parameter values make the data MOST likely?"

$$\hat{\theta}_{MLE} = \arg\max_\theta \log p(D|\theta)$$

**In plain English:** "Find the parameter values that maximize the log-likelihood."

---

## Part 1: The Generative Classifier Model

### The Joint Distribution

For a two-class classifier with one-hot encoding $y_{nk}$:

$$p(x_n, y_n) = \prod_{k=1}^2 \left(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)\right)^{y_{nk}}$$

### The Log-Likelihood

Taking the log of the product of all N data points:

$$\log p(D|\theta) = \sum_{n=1}^N \sum_{k=1}^2 y_{nk} \log \mathcal{N}(x_n|\mu_k, \Sigma_k) + \sum_{n=1}^N \sum_{k=1}^2 y_{nk} \log \pi_k$$

**How to read this:**

- **First term:** For each data point n and each class k, if $y_{nk} = 1$ (point n is in class k), add the log probability of that point under class k's Gaussian
- **Second term:** For each data point n and each class k, if $y_{nk} = 1$, add the log of the mixing coefficient

### The MLE for Gaussian Parameters

For class k:

$$\hat{\mu}_k = \frac{\sum_n y_{nk} x_n}{\sum_n y_{nk}} \quad \text{(average of points in class k)}$$

$$\hat{\Sigma}_k = \frac{1}{N_k} \sum_n y_{nk} (x_n - \hat{\mu}_k)(x_n - \hat{\mu}_k)^T$$

Where $N_k = \sum_n y_{nk}$ (number of points in class k).

**In plain English:** 
- The MLE mean is just the average of the data points assigned to that class
- The MLE covariance is the average outer product of deviations from the mean

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-B, Question 2c)

> The log-likelihood $\log p(D|\theta)$ is:
>
> Options:
> - (a) $\sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_k y_{nk} \log \pi_k$
> - (b) $\sum_n \sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_n \sum_k \log \pi_k$
> - (c) $\sum_n \sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_n \sum_k y_{nk} \log \pi_k$
> - (d) $\sum_k y_{nk} \log(\pi_k \mathcal{N}(x_n|\mu_k,\Sigma_k))$

### STEP-BY-STEP SOLUTION

**Step 1: Start with the joint distribution**

$$p(D|\theta) = \prod_{n=1}^N \prod_{k=1}^2 \left(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)\right)^{y_{nk}}$$

**Step 2: Take the logarithm**

Using the rule $\log(\prod a_i) = \sum \log(a_i)$:

$$\log p(D|\theta) = \sum_{n=1}^N \sum_{k=1}^2 y_{nk} \log\left(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)\right)$$

**Step 3: Use the rule $\log(ab) = \log(a) + \log(b)$**

$$\log p(D|\theta) = \sum_{n=1}^N \sum_{k=1}^2 y_{nk} \log \mathcal{N}(x_n|\mu_k, \Sigma_k) + \sum_{n=1}^N \sum_{k=1}^2 y_{nk} \log \pi_k$$

**Step 4: Match the answer**

(c) matches exactly.

Key features of the correct answer:
- **Sum over n** (all data points) AND **sum over k** (all classes)
- **$y_{nk}$** appears in BOTH terms (it selects the right class for each point)

**(a)** Missing the sum over n. Only sums over k. ELIMINATE.
**(b)** Missing $y_{nk}$ in the $\log \pi_k$ term. Every data point should only contribute to its assigned class, not all classes. ELIMINATE.
**(d)** Missing the sum over n. ELIMINATE.

**Answer: (c)** ✅

---

### EXAM QUESTION 2 (2021-Part-B, Question 2d)

> Let $\hat{\mu}_2$ be the MLE for $\mu_2$. The MLE for $\Sigma_2$ is:
>
> Options:
> - (a) $\hat{\Sigma}_2 = \frac{1}{N} \sum_n (x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$
> - (b) $\hat{\Sigma}_2 = \frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$
> - (c) $\hat{\Sigma}_2 = \frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)^T (x_n - \hat{\mu}_2)$
> - (d) $\hat{\Sigma}_2 = \frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)^2$

### STEP-BY-STEP SOLUTION

**Step 1: For a single Gaussian, the MLE covariance is:**

$$\hat{\Sigma} = \frac{1}{N} \sum_{n=1}^N (x_n - \hat{\mu})(x_n - \hat{\mu})^T$$

**Step 2: For a GMM, we only use points assigned to class 2:**

$$\hat{\Sigma}_2 = \frac{1}{N_2} \sum_{n=1}^N y_{n2} (x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$$

Where $y_{n2}$ acts as a selector: it's 1 if point n is in class 2, 0 otherwise. So only points from class 2 contribute.

**Note:** The exam uses $1/N$ instead of $1/N_2$, but the key distinguishing feature is the structure of the formula.

**Step 3: Match the answer**

**(a)** No $y_{n2}$ selector — uses ALL data points, not just class 2. ELIMINATE.

**(b)** Has $y_{n2}$ selector AND the outer product $(x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$. This gives an $N \times N$ matrix (correct for covariance). ✓

**(c)** Has the INNER product $(x_n - \hat{\mu}_2)^T (x_n - \hat{\mu}_2)$ — this gives a single number (scalar), not a matrix. Covariance must be a matrix. ELIMINATE.

**(d)** Has $(x_n - \hat{\mu}_2)^2$ — this is for 1D case only. The problem states $x_n \in \mathbb{R}^{2 \times 1}$ (2D vectors), so we need the outer product. ELIMINATE.

**Answer: (b)** ✅

---

### EXAM QUESTION 3 (2021-Part-B, Question 2e)

> Aside from degenerate cases, the discrimination boundary between two Gaussian classes will be:
>
> Options:
> - (a) straight line
> - (b) parabola
> - (c) square
> - (d) triangle

### STEP-BY-STEP SOLUTION

**Step 1: Understand the decision boundary**

The boundary is where $p(C_1|x) = p(C_2|x)$, or equivalently:

$$\log p(x|C_1) + \log p(C_1) = \log p(x|C_2) + \log p(C_2)$$

**Step 2: What does $\log p(x|C_k)$ look like?**

For a Gaussian: $\log \mathcal{N}(x|\mu_k, \Sigma_k) = -\frac{1}{2}(x-\mu_k)^T \Sigma_k^{-1} (x-\mu_k) + \text{constants}$

This is a **quadratic** function of x (it has $x^2$ terms).

**Step 3: What happens when we set the two equal?**

If $\Sigma_1 \neq \Sigma_2$ (different covariances), the quadratic terms don't cancel, and the boundary is **quadratic** — a parabola in 2D.

If $\Sigma_1 = \Sigma_2$ (shared covariance), the quadratic terms cancel, and the boundary is **linear** — a straight line.

Since the problem doesn't assume shared covariance:

**Answer: (b) parabola** ✅

---

### EXAM QUESTION 4 (2021-Part-B, Question 2b)

> Posterior class probability $p(y_{n1}=1|x_n)$:
>
> Options:
> - (a) $\frac{\mathcal{N}(x_n|\mu_1,\Sigma_1)}{\mathcal{N}(x_n|\mu_1,\Sigma_1) + \mathcal{N}(x_n|\mu_2,\Sigma_2)}$
> - (b) $\frac{\pi_1}{\pi_1 + \pi_2}$
> - (c) $\frac{\pi_2 \cdot \mathcal{N}(x_n|\mu_2,\Sigma_2)}{\pi_1 \mathcal{N}(x_n|\mu_1,\Sigma_1) + \pi_2 \mathcal{N}(x_n|\mu_2,\Sigma_2)}$
> - (d) $\frac{\pi_1 \cdot \mathcal{N}(x_n|\mu_1,\Sigma_1)}{\pi_1 \mathcal{N}(x_n|\mu_1,\Sigma_1) + \pi_2 \cdot \mathcal{N}(x_n|\mu_2,\Sigma_2)}$

### STEP-BY-STEP SOLUTION

By Bayes' rule:

$$p(y_{n1}=1|x_n) = \frac{p(x_n|y_{n1}=1) \cdot p(y_{n1}=1)}{p(x_n)}$$

Where:
- $p(x_n|y_{n1}=1) = \mathcal{N}(x_n|\mu_1, \Sigma_1)$
- $p(y_{n1}=1) = \pi_1$
- $p(x_n) = \sum_{k=1}^2 \mathcal{N}(x_n|\mu_k, \Sigma_k) \cdot \pi_k$

So:

$$p(y_{n1}=1|x_n) = \frac{\pi_1 \cdot \mathcal{N}(x_n|\mu_1, \Sigma_1)}{\pi_1 \cdot \mathcal{N}(x_n|\mu_1, \Sigma_1) + \pi_2 \cdot \mathcal{N}(x_n|\mu_2, \Sigma_2)}$$

**Answer: (d)** ✅

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Log-Likelihood Pattern

$\sum_n \sum_k y_{nk} \log(\text{Gaussian}) + \sum_n \sum_k y_{nk} \log(\text{mixing coefficient})$

Both terms need $y_{nk}$ AND sums over both n and k.

### TRICK 2: MLE Covariance for GMM

- Must have $y_{nk}$ selector (only points from that class)
- Must have OUTER product: $(x-\mu)(x-\mu)^T$ (gives a matrix)
- NOT inner product $(x-\mu)^T(x-\mu)$ (gives a scalar)
- NOT $(x-\mu)^2$ (only for 1D)

### TRICK 3: Decision Boundary

- Different covariances → quadratic boundary (parabola)
- Same covariance → linear boundary (straight line)

### TRICK 4: Posterior Class

- Numerator = class likelihood × class prior
- Denominator = sum over ALL classes

---

## Part 4: Practice Exercises

### Exercise 1

> The log-likelihood $\log p(D|\theta)$ for a two-class GMM:
>
> Options:
> - (a) $\sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_k y_{nk} \log \pi_k$
> - (b) $\sum_n \sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_n \sum_k \log \pi_k$
> - (c) $\sum_n \sum_k y_{nk} \log \mathcal{N}(x_n|\mu_k,\Sigma_k) + \sum_n \sum_k y_{nk} \log \pi_k$
> - (d) $\sum_k y_{nk} \log(\pi_k \mathcal{N}(x_n|\mu_k,\Sigma_k))$

---

### Exercise 2

> MLE for $\Sigma_2$:
>
> Options:
> - (a) $\frac{1}{N} \sum_n (x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$
> - (b) $\frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)(x_n - \hat{\mu}_2)^T$
> - (c) $\frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)^T (x_n - \hat{\mu}_2)$
> - (d) $\frac{1}{N} \sum_n y_{n2} (x_n - \hat{\mu}_2)^2$

---

### Exercise 3

> Discrimination boundary between two Gaussian classes with different covariances:
>
> Options:
> - (a) straight line
> - (b) parabola
> - (c) square
> - (d) triangle

---

### Exercise 4

> Posterior $p(y_{n1}=1|x_n)$:
>
> Options:
> - (a) $\frac{\mathcal{N}(x_n|\mu_1,\Sigma_1)}{\mathcal{N}(x_n|\mu_1,\Sigma_1) + \mathcal{N}(x_n|\mu_2,\Sigma_2)}$
> - (b) $\frac{\pi_1}{\pi_1 + \pi_2}$
> - (c) $\frac{\pi_2 \cdot \mathcal{N}(x_n|\mu_2,\Sigma_2)}{\pi_1 \mathcal{N}(x_n|\mu_1,\Sigma_1) + \pi_2 \mathcal{N}(x_n|\mu_2,\Sigma_2)}$
> - (d) $\frac{\pi_1 \cdot \mathcal{N}(x_n|\mu_1,\Sigma_1)}{\pi_1 \mathcal{N}(x_n|\mu_1,\Sigma_1) + \pi_2 \cdot \mathcal{N}(x_n|\mu_2,\Sigma_2)}$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (c)**

Both terms sum over n AND k, both have y_{nk} selector.

(a) missing sum over n.
(b) missing y_{nk} in the log π term.
(d) missing sum over n.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (b)**

Outer product (x-μ)(x-μ)ᵀ with y_{n2} selector. Covariance is a matrix, needs outer product form.

(a) no selector — uses all points.
(c) inner product — gives scalar, not matrix.
(d) squared — only for 1D.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b) parabola**

Different covariances → quadratic (parabolic) decision boundary.
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (d)**

Numerator = class 1 joint probability (likelihood × prior).
Denominator = sum of both joint probabilities (the evidence).

(a) missing the priors (π).
(b) missing the likelihoods (Gaussians).
(c) has class 2 in the numerator, not class 1.
</details>
