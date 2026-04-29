# Bayesian ML Exam — Formula Cheatsheet

> Organized by exercise type number. Every formula you need, nothing you don't.

---

## Type 1: Bayes' Rule & Posterior Computation

| Formula | Expression |
|---------|------------|
| **Bayes' Rule** | $p(\theta \mid x) = \dfrac{p(x \mid \theta) \cdot p(\theta)}{p(x)}$ |
| **Proportional form** | $p(\theta \mid x) \propto p(x \mid \theta) \cdot p(\theta)$ |
| **Evidence** | $p(x \mid m) = \int p(x \mid \theta, m) \cdot p(\theta \mid m) \, d\theta$ |
| **Joint** | $p(x, \theta) = p(x \mid \theta) \cdot p(\theta)$ |

### Beta Function Trick (for integrals over $\theta \in [0,1]$)

$$\int_0^1 \theta^p (1-\theta)^q \, d\theta = \frac{p! \cdot q!}{(p+q+1)!}$$

**How to use:** Multiply likelihood × prior → read off powers $p$ and $q$ → plug into formula → multiply by any constant outside the integral.

---

## Type 2: Beta-Bernoulli Coin Toss

| Formula | Expression |
|---------|------------|
| **Bernoulli likelihood** | $p(D \mid \mu) = \mu^{N_1}(1-\mu)^{N_0}$ |
| **Beta prior** | $p(\mu) = \text{Beta}(\mu \mid \alpha, \beta) = \dfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \mu^{\alpha-1}(1-\mu)^{\beta-1}$ |
| **Posterior** | $p(\mu \mid D) = \text{Beta}(\mu \mid \alpha + N_1,\; \beta + N_0)$ |
| **Evidence** | $p(D) = \dfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \cdot \dfrac{\Gamma(\alpha+N_1)\Gamma(\beta+N_0)}{\Gamma(\alpha+\beta+N)}$ |
| **Predictive** | $p(x_{\text{next}}=1 \mid D) = \dfrac{\alpha + N_1}{\alpha + \beta + N}$ |
| **Beta mean** | $\mathbb{E}[\mu] = \dfrac{\alpha}{\alpha + \beta}$ |
| **Gamma (integers)** | $\Gamma(n) = (n-1)!$ |

**Key:** $N_1$ = count of ones, $N_0$ = count of zeros, $N = N_1 + N_0$. **No binomial coefficient in the likelihood!**

---

## Type 3: Gaussian Posterior & Evidence

**Setup:** Likelihood $\mathcal{N}(x \mid \mu, \sigma^2)$, Prior $\mathcal{N}(\mu \mid \mu_0, \sigma_0^2)$

| Formula | Expression |
|---------|------------|
| **Posterior variance** | $\dfrac{1}{\sigma^2_{\text{post}}} = \dfrac{1}{\sigma^2_0} + \dfrac{1}{\sigma^2}$ |
| **Posterior mean** | $\mu_{\text{post}} = \sigma^2_{\text{post}} \left( \dfrac{\mu_0}{\sigma^2_0} + \dfrac{x}{\sigma^2} \right)$ |
| **Evidence** | $p(x) = \mathcal{N}(x \mid \mu_0,\; \sigma^2_0 + \sigma^2)$ |

**Shortcut:** Posterior precision = sum of precisions. Posterior mean = precision-weighted average. Evidence variance = prior variance + likelihood variance.

**When both variances = 1:** $\sigma^2_{\text{post}} = 0.5$, $\mu_{\text{post}} = (\mu_0 + x)/2$.

---

## Type 4: Model Evidence & Bayesian Model Averaging

| Formula | Expression |
|---------|------------|
| **Evidence** | $p(x \mid m_k) = \int p(x \mid \theta, m_k) \cdot p(\theta \mid m_k) \, d\theta$ |
| **Model averaging** | $p(x) = \sum_k p(x \mid m_k) \cdot p(m_k)$ |
| **Gaussian evidence** | $p(x \mid m) = \mathcal{N}(x \mid \mu_0,\; \sigma^2_0 + \sigma^2)$ |

---

## Type 5: Model Comparison & Bayes Factor

| Formula | Expression |
|---------|------------|
| **Bayes Factor** | $B_{12} = \dfrac{p(D \mid m_1)}{p(D \mid m_2)}$ |
| **Posterior ratio** | $\dfrac{p(m_1 \mid D)}{p(m_2 \mid D)} = \dfrac{p(D \mid m_1)}{p(D \mid m_2)} \cdot \dfrac{p(m_1)}{p(m_2)} = B_{12} \cdot \dfrac{p(m_1)}{p(m_2)}$ |
| **BF from posteriors** | $B_{12} = \dfrac{p(D \mid m_1)}{p(D \mid m_2)} = \dfrac{p(m_1 \mid D)}{p(m_2 \mid D)} \cdot \dfrac{p(m_2)}{p(m_1)}$ |
| **Posterior model prob** | $p(m_k \mid D) = \dfrac{p(D \mid m_k) \cdot p(m_k)}{p(D)}$ |

**Interpretation:** Posterior ratio > 1 → model 1 wins. Evidence = ∫ likelihood × prior dθ.

---

## Type 6: Bayesian Classifier

| Formula | Expression |
|---------|------------|
| **Posterior** | $p(C_k \mid x) = \dfrac{p(x \mid C_k) \cdot p(C_k)}{p(x)}$ |
| **Evidence** | $p(x) = p(x \mid C_1) \cdot p(C_1) + p(x \mid C_2) \cdot p(C_2)$ |
| **Decision boundary** | $\dfrac{p(x \mid C_1) \cdot p(C_1)}{p(x \mid C_2) \cdot p(C_2)} = 1$ |
| **Error probability** | $P(\text{error}) = \int_{\text{decide }C_2} p(x \mid C_1)p(C_1)dx + \int_{\text{decide }C_1} p(x \mid C_2)p(C_2)dx$ |

**Boundary shortcuts:**
- Different covariances → **quadratic** (parabola)
- Shared covariance → **linear** (straight line)

**Learned class prior (Beta):** $p(C_1 \mid x_\bullet, D) \propto \int p(x_\bullet \mid C_1)\, p(C_1 \mid \theta)\, p(\theta \mid D)\, d\theta$

---

## Type 7: Ball/Box Conditional Probability

| Formula | Expression |
|---------|------------|
| **Product Rule** | $P(A, B) = P(A \mid B) \cdot P(B)$ |
| **Total Probability** | $P(A) = \sum_i P(A \mid B_i) \cdot P(B_i)$ |
| **Bayes' Rule** | $P(B_i \mid A) = \dfrac{P(A \mid B_i) \cdot P(B_i)}{P(A)}$ |

**Without replacement:** Update counts after each draw (decrease both the drawn type and total by 1).

---

## Type 8: Gaussian Mixture Model (GMM) Form

| Formula | Expression |
|---------|------------|
| **Joint** (one-hot $z_n$) | $p(x_n, z_n) = \prod_{k=1}^K \left(\pi_k \cdot \mathcal{N}(x_n \mid \mu_k, \Sigma_k)\right)^{z_{nk}}$ |
| **Marginal** | $p(x_n) = \sum_{k=1}^K \pi_k \, \mathcal{N}(x_n \mid \mu_k, \Sigma_k)$ |
| **Mixing constraint** | $\sum_{k=1}^K \pi_k = 1$ |

**Spotting trick:** Both $\pi_k$ AND $\mathcal{N}$ must be inside the parentheses raised to $z_{nk}$ (not $z_n$). Joint uses product ∏, marginal uses sum Σ.

---

## Type 9: Variational Free Energy (VFE)

| Formula | Expression |
|---------|------------|
| **VFE functional** | $F[q] = \int q(z) \log \dfrac{q(z)}{p(x,z)} \, dz$ |
| **Upper bound** | $F[q] \geq -\log p(x)$ for any $q(z)$ |
| **Equality** | $F[q] = -\log p(x)$ when $q(z) = p(z \mid x)$ |

**Key:** VFE minimizes $KL(q(z) \,\|\, p(z \mid x))$ and gives an upper bound on negative log evidence.

---

## Type 10: Free Energy Principle (FEP) — Concepts

| Principle | Statement |
|-----------|-----------|
| **Generative model** | Agents MUST have an internal model of how sensory data is generated |
| **Perception** | Minimizes free energy (update beliefs to match observations) |
| **Action** | Minimizes **expected free energy** of future states |
| **Goals** | Encoded as **target priors** in the generative model |
| **Decision making** | Minimization of a functional of beliefs about future states |

**Rules of thumb:** Always MINIMIZE (never maximize) free energy. Beliefs, not cost functions. Desired (target priors), not actual future.

---

## Type 11: Factor Analysis & Marginal Gaussian

| Formula | Expression |
|---------|------------|
| **Model** | $x = Wz + \epsilon$, $z \sim \mathcal{N}(0, I)$, $\epsilon \sim \mathcal{N}(0, \Psi)$ |
| **Conditional** | $p(x \mid z) = \mathcal{N}(x \mid Wz, \Psi)$ |
| **Joint** | $p(x, z) = \mathcal{N}(x \mid Wz, \Psi) \cdot \mathcal{N}(z \mid 0, I)$ |
| **Marginal** | $p(x) = \mathcal{N}(x \mid 0,\; WW^T + \Psi)$ |

**Note:** $WW^T$ (not $W^TW$) — must give $N \times N$ covariance for $x$.

---

## Type 12: Recursive Filtering / Kalman

| Formula | Expression |
|---------|------------|
| **Observation model** | $x_t = \theta + \epsilon_t$, $\epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$ |
| **Likelihood** | $p(x_k \mid \theta) = \mathcal{N}(x_k \mid \theta, \sigma_\epsilon^2)$ |
| **Recursive update** | $p(\theta \mid D_k) \propto p(x_k \mid \theta) \cdot p(\theta \mid D_{k-1})$ |
| **Kalman gain** | $K_k = \dfrac{\sigma_{k-1}^2}{\sigma_{k-1}^2 + \sigma_\epsilon^2}$ |
| **Mean update** | $\mu_k = \mu_{k-1} + K_k \, (x_k - \mu_{k-1})$ |
| **Variance update** | $\sigma_k^2 = (1 - K_k) \, \sigma_{k-1}^2$ |

**State-space update:** $p(z_t \mid x_{1:t}) \propto p(x_t \mid z_t) \sum_{z_{t-1}} p(z_t \mid z_{t-1})\, p(z_{t-1} \mid x_{1:t-1})$

**As $k \to \infty$:** $\sigma_k^2 \to 0$, $K_k \to 0$, $\mu_k \to$ true value (stationary).

---

## Type 13: Log-Likelihood & MLE

| Formula | Expression |
|---------|------------|
| **Log-likelihood** | $\log p(D \mid \theta) = \sum_n \sum_k y_{nk} \log \mathcal{N}(x_n \mid \mu_k, \Sigma_k) + \sum_n \sum_k y_{nk} \log \pi_k$ |
| **MLE mean** | $\hat{\mu}_k = \dfrac{\sum_n y_{nk} x_n}{N_k}$ where $N_k = \sum_n y_{nk}$ |
| **MLE covariance** | $\hat{\Sigma}_k = \dfrac{1}{N_k} \sum_n y_{nk} (x_n - \hat{\mu}_k)(x_n - \hat{\mu}_k)^T$ |
| **Log-Gaussian** | $\log \mathcal{N}(x \mid \mu, \Sigma) = -\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu) + \text{const}$ |

**Covariance trick:** Must use **outer product** $(x-\mu)(x-\mu)^T$ (gives matrix), NOT inner product $(x-\mu)^T(x-\mu)$ (gives scalar).

**Decision boundary:** Different covariances → **quadratic** (parabola). Shared covariance → **linear** (straight line).

---

## Type 14: GMM, VFE, FEP & Concept Questions

### VFE Properties
- $F[q] \geq -\log p(x)$ — upper bound on negative log evidence
- Equality at $q(z) = p(z \mid x)$ (true posterior, NOT the prior)
- Minimizing VFE = minimizing KL divergence to true posterior

### Bayesian vs MLE
- **Likelihood** is a function of parameters: $L(\theta) = p(D \mid \theta)$
- **MLE** maximizes $p(D \mid \theta)$; **MAP** maximizes $p(D \mid \theta)p(\theta)$ — equal only with uniform prior
- As data grows: likelihood narrows, prior stays fixed → MLE ≈ MAP
- **Bayesian evidence** = fit minus complexity (built-in overfitting protection)

### Gaussian Properties
- **Linear combination** of Gaussians → Gaussian
- **Products/ratios** of Gaussians → NOT Gaussian

### Discriminative Predictive
$$p(y_\bullet \mid x_\bullet, D) = \int p(y_\bullet \mid x_\bullet, \theta)\, p(\theta \mid D)\, d\theta$$

### Generative Model for Signal Recovery
$$p(s \mid x) \propto \int p(x \mid s,z)\, p(s,z) \, dz$$

---

## Quick-Reference Concept Facts

- **Bayesian methods** are NOT faster than MLE — often more computationally expensive
- **No train/test split needed** in Bayesian approach — all data used for inference
- **Beta** is the conjugate prior for Bernoulli (not Gaussian)
- MLE covariance uses $1/N_k$ (not $1/N$), and requires $y_{nk}$ selector

---

## Gamma Factorial Quick Values

| $n$ | $\Gamma(n) = (n-1)!$ |
|-----|---------------------|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 6 |
| 5 | 24 |
| 6 | 120 |
| 7 | 720 |
| 8 | 5040 |
| 10 | 362880 |
