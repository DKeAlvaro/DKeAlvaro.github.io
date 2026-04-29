# Exercise Type 8: Gaussian Mixture Model (GMM) Form

> **What the exam asks:** You are given several mathematical expressions and must identify which one correctly specifies a Gaussian Mixture Model with one-hot encoded cluster assignments.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $x_n$ | "x sub n" | The n-th data point (observation) |
| $z_n$ | "z sub n" | The hidden cluster assignment for data point n |
| $z_{nk}$ | "z sub n k" | The k-th element of the vector $z_n$ — is data point n in cluster k? |
| $K$ | Capital K | Total number of clusters (mixture components) |
| $\pi_k$ | "pi sub k" | The mixing coefficient — how common is cluster k? |
| $\mathcal{N}$ | Capital N (script) | The **Gaussian** (Normal) distribution |
| $\mathcal{N}(x\|\mu, \Sigma)$ | "Gaussian of x given mu and Sigma" | A Gaussian distribution for x, with mean μ and covariance Σ |
| $\prod$ | Capital Pi (product) | "Multiply together" — like sum (Σ) but for multiplication |
| $\sum$ | Capital Sigma (sum) | "Add up" |
| $^{z_{nk}}$ | "to the power z sub n k" | Exponentiation — since $z_{nk}$ is 0 or 1, this acts as a "switch" |

### What Is a Gaussian Mixture Model?

Imagine you have data that comes from several different "clusters" or "groups." Each cluster has its own Gaussian distribution (bell curve). But you don't know which cluster each data point belongs to — that's hidden.

**The GMM says:**
1. First, pick a cluster: cluster k is chosen with probability $\pi_k$
2. Then, generate a data point from that cluster's Gaussian distribution

### One-Hot Encoding

The cluster assignment $z_n$ is a vector of length $K$ where exactly ONE element is 1 and the rest are 0.

**Example with K=3 clusters:**
- If data point n belongs to cluster 1: $z_n = (1, 0, 0)$ → $z_{n1} = 1, z_{n2} = 0, z_{n3} = 0$
- If data point n belongs to cluster 2: $z_n = (0, 1, 0)$ → $z_{n1} = 0, z_{n2} = 1, z_{n3} = 0$
- If data point n belongs to cluster 3: $z_n = (0, 0, 1)$ → $z_{n1} = 0, z_{n2} = 0, z_{n3} = 1$

**Why use one-hot encoding?** It lets us write the mixture model as a compact product:

$$\prod_{k=1}^K f_k^{z_{nk}} = f_1^{z_{n1}} \cdot f_2^{z_{n2}} \cdot ... \cdot f_K^{z_{nK}}$$

Since exactly one $z_{nk} = 1$ and all others are 0, and anything to the power 0 = 1, all terms become 1 except the one where $z_{nk} = 1$. So this product equals exactly the active component.

**Example:** If $z_n = (0, 1, 0)$:
$$f_1^0 \cdot f_2^1 \cdot f_3^0 = 1 \cdot f_2 \cdot 1 = f_2$$

---

## Part 1: The Correct GMM Joint Distribution

### The Formula

$$p(x_n, z_n) = \prod_{k=1}^K \left(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)\right)^{z_{nk}}$$

### Why This Works

- The product runs over all clusters k = 1, 2, ..., K
- For each cluster, we have $\pi_k$ (mixing coefficient) times the Gaussian for that cluster
- The whole thing is raised to the power $z_{nk}$
- Since $z_n$ is one-hot, only ONE term survives
- That surviving term is $\pi_j \cdot \mathcal{N}(x_n|\mu_j, \Sigma_j)$ where $z_{nj} = 1$

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-B, Question 1e)

> Which is a correct GMM specification?
>
> Options:
> - (a) $p(x_n,z_n) = \prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_n}$
> - (b) $p(x_n,z_n) = \prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)^{z_{nk}}$
> - (c) $p(x_n,z_n) = \sum_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)$
> - (d) $p(x_n,z_n) = \prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_{nk}}$

### STEP-BY-STEP SOLUTION

**Step 1: What should the correct answer look like?**

The joint $p(x_n, z_n)$ must:
1. Use a **product** (∏) over k (not a sum Σ) — because we're selecting ONE component
2. Have the exponent $z_{nk}$ (not $z_n$) — we need the k-th element of the vector
3. Have **both** $\pi_k$ AND $\mathcal{N}$ inside the parentheses, raised to the power $z_{nk}$

**Step 2: Eliminate wrong answers**

**(c)** uses a sum (Σ) instead of a product (∏). This is actually the **marginal** $p(x_n)$ (after summing out $z_n$), not the joint. ELIMINATE.

**(a)** uses $z_n$ as the exponent, not $z_{nk}$. $z_n$ is the whole vector — you can't raise a number to the power of a vector. ELIMINATE.

**(b)** Only $\mathcal{N}$ is raised to $z_{nk}$, but $\pi_k$ is outside the exponent. This means every $\pi_k$ appears in the product, not just the one for the active cluster. ELIMINATE.

**(d)** Has everything correct:
- Product over k ✓
- Both $\pi_k$ and $\mathcal{N}$ inside the parentheses ✓
- Raised to the power $z_{nk}$ ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 2 (2023, Question 4c)

> Same question, different exam:
>
> Options:
> - (a) $\prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)$
> - (b) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_{nk}}$
> - (c) $\prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)^{z_{nk}}$
> - (d) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_n}$

### STEP-BY-STEP SOLUTION

**(a)** Missing the $z_{nk}$ exponent entirely. This is just the product of all mixing coefficients times all Gaussians. ELIMINATE.

**(d)** Uses $z_n$ instead of $z_{nk}$. ELIMINATE.

**(c)** Only $\mathcal{N}$ is raised to $z_{nk}$. The $\pi_k$ is outside and appears for ALL k, not just the active one. ELIMINATE.

**(b)** Correct: both $\pi_k$ and $\mathcal{N}$ inside the power $z_{nk}$.

**Answer: (b)** ✅

---

### EXAM QUESTION 3 (2021-Part-B, Question 2a — Generative Classifier)

> Generative model $p(x_n, y_n)$ for two-class classification with one-hot $y_n$:
>
> Options:
> - (a) $\prod_{k=1}^2 \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)^{y_{nk}}$
> - (b) $\prod_{k=1}^2 (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{y_{nk}}$
> - (c) $\prod_{k=1}^2 \pi_k^{y_{nk}} \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)$
> - (d) $\sum_{k=1}^2 y_{nk} \log(\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))$

### STEP-BY-STEP SOLUTION

Same pattern — this is just K=2 (two classes instead of K clusters).

**(a)** Only $\mathcal{N}$ has the exponent. ELIMINATE.

**(c)** Only $\pi_k$ has the exponent. ELIMINATE.

**(d)** This is a sum of logs — that's a log-likelihood form, not the joint distribution. ELIMINATE.

**(b)** Correct: both inside the power.

**Answer: (b)** ✅

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Both Must Be Inside the Power

The correct answer ALWAYS has **both** $\pi_k$ and $\mathcal{N}$ inside the parentheses, raised to $z_{nk}$.

If only one of them has the exponent → wrong.

### TRICK 2: It Must Be $z_{nk}$ Not $z_n$

$z_{nk}$ = the k-th element (a single 0 or 1).
$z_n$ = the whole vector.

### TRICK 3: Product, Not Sum

The joint uses ∏ (product). The marginal (after summing out z) uses Σ (sum).

If the question asks for the **joint** $p(x_n, z_n)$ → product.
If the question asks for the **marginal** $p(x_n)$ → sum.

---

## Part 4: Practice Exercises

### Exercise 1

> Which is a correct GMM for $p(x_n, z_n)$?
>
> Options:
> - (a) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_n}$
> - (b) $\prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)^{z_{nk}}$
> - (c) $\sum_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)$
> - (d) $\prod_{k=1}^K (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{z_{nk}}$

---

### Exercise 2

> Generative model $p(x_n, y_n)$ for two-class classification:
>
> Options:
> - (a) $\prod_{k=1}^2 \pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)^{y_{nk}}$
> - (b) $\prod_{k=1}^2 (\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))^{y_{nk}}$
> - (c) $\prod_{k=1}^2 \pi_k^{y_{nk}} \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k)$
> - (d) $\sum_{k=1}^2 y_{nk} \log(\pi_k \cdot \mathcal{N}(x_n|\mu_k,\Sigma_k))$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (d)**

(a) uses z_n instead of z_{nk}.
(b) only 𝒩 has the exponent.
(c) is a sum (that's the marginal, not the joint).
(d) is correct: both inside, power z_{nk}, product.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (b)**

(a) only 𝒩 has the exponent.
(c) only π has the exponent.
(d) is a log-likelihood form, not the joint.
(b) is correct: both inside the power y_{nk}.
</details>
