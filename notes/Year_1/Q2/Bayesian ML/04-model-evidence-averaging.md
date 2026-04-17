# Exercise Type 4: Model Evidence & Bayesian Model Averaging

> **What the exam asks:** Compute how likely the data is under a model (evidence), and/or combine predictions from multiple models using Bayesian model averaging.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $p(x|m_1)$ | "probability of x given model m₁" | How likely is the data under model m₁, averaging over ALL possible θ values? (Model Evidence) |
| $p(x|m_k)$ | "probability of x given model m_k" | Same thing, but for model k |
| $p(m_k)$ | "probability of model m_k" | How plausible do we think model k is BEFORE seeing data? (Prior over models) |
| $p(m_k|x)$ | "probability of model m_k given x" | How plausible is model k AFTER seeing the data? (Posterior over models) |
| $p(x)$ | "probability of x" | Overall probability of the data, combining ALL models |
| $\sum$ | Capital Sigma (sum) | "Add up" — used when combining multiple models |
| $\int$ | Integral | "Continuous sum" — used to average over all possible parameter values |

---

## Part 1: The Core Concepts — No Math

### What Is "Model Evidence"? (Plain English)

Imagine you have a coin (Model $m_1$) and you don't know its bias $\theta$ (probability of heads). You want to know how well this coin model explains a sequence of flips.

You can't just plug in one number for $\theta$ because you don't know it. Instead, you **average over ALL possible $\theta$ values**, weighting each by how plausible it was to begin with (your prior belief about $\theta$).

The **model evidence** $p(x|m)$ answers the question: "If I randomly picked a parameter $\theta$ from my prior, how likely is it that I would generate the exact data $x$ that I observed?" It automatically penalizes models that are too complex or overly vague.

### What Is "Bayesian Model Averaging"? (Plain English)

When you have multiple competing models (e.g., $m_1$ is a biased coin, $m_2$ is a fair coin), you don't have to just pick one and discard the rest. Instead, you **combine their predictions**, weighted by how much you believe in each model.

Think of it like asking two different weather forecasters:
- Forecaster 1 ($m_1$) predicts rain with 80% confidence, and you trust them 75% of the time.
- Forecaster 2 ($m_2$) predicts rain with 40% confidence, and you trust them 25% of the time.
Your overall prediction is a weighted average of their forecasts. In Bayesian terms, you weight each model's prediction by its probability $p(m_k)$.

---

## Part 2: The Key Formulas (MEMORIZE)

### 1. Model Evidence (Continuous Parameters)

To compute the evidence for a model with a continuous parameter $\theta$, you integrate the likelihood multiplied by the prior over all possible values of $\theta$:

$$p(x|m) = \int p(x|\theta, m) \cdot p(\theta|m) \, d\theta$$

**How to remember:** Evidence = Integral of (Likelihood $\times$ Prior).

### 2. Bayesian Model Averaging

To find the overall probability of the data across multiple models, sum the evidence of each model weighted by its prior probability:

$$p(x) = \sum_k p(x|m_k) \cdot p(m_k)$$

**How to remember:** Total probability = Sum of (Model Evidence $\times$ Model Prior).

### 3. The Beta Function Trick (CRITICAL FOR INTEGRALS)

You will frequently need to solve integrals of the form $\theta^p(1-\theta)^q$. Use this exact formula:

$$\int_0^1 \theta^p (1-\theta)^q \, d\theta = \frac{p! \cdot q!}{(p+q+1)!}$$

**How to use it:**
1. Multiply your likelihood and prior together to get an expression like $C \cdot \theta^p(1-\theta)^q$.
2. Identify the powers $p$ and $q$.
3. Plug $p$ and $q$ into the factorial formula.
4. Don't forget to multiply the result by any constant $C$ that was pulled out of the integral!

#### Quick Example of the Beta Trick
Compute $\int_0^1 6\theta^2(1-\theta) \, d\theta$:
1. The integrand is $6\theta^2(1-\theta)^1$, so $p=2$, $q=1$. Constant $C=6$.
2. $\int_0^1 \theta^2(1-\theta)^1 d\theta = \frac{2! \cdot 1!}{(2+1+1)!} = \frac{2}{24} = \frac{1}{12}$
3. Multiply by the constant 6: $6 \times \frac{1}{12} = \frac{1}{2}$

---

## Part 3: Tricks & Shortcuts

### TRICK 1: The Evidence Calculation Pattern
Almost every exam question asking for $p(x|m_1)$ follows this exact pattern:
1. Multiply the given likelihood and prior: $p(x|\theta, m_1) \times p(\theta|m_1)$
2. Simplify into the form $C \cdot \theta^p(1-\theta)^q$
3. Use the Beta function trick to evaluate the integral.
4. The answer is $C \times \frac{p! \cdot q!}{(p+q+1)!}$

### TRICK 2: Model Averaging Is Just a Weighted Sum
Don't overcomplicate it. Multiply each model's evidence by its prior probability, then add them up. 

### TRICK 3: Any Number to the Power of 0 is 1
When evaluating a likelihood like $\theta^x(1-\theta)^{1-x}$ at $x=1$, you get $\theta^1(1-\theta)^0$. Remember that $(1-\theta)^0 = 1$, so it simplifies to just $\theta$.

### TRICK 4: Gaussian Evidence = Gaussian with Summed Variances
If a question gives you Gaussian likelihoods instead of Beta/Binomial ones (e.g., Question 1c from 2023), the evidence for model $m$ with likelihood $\mathcal{N}(x|\mu, \sigma^2)$ and prior $\mathcal{N}(\mu|\mu_0, \sigma_0^2)$ is:

$$p(x|m) = \mathcal{N}(x|\mu_0, \sigma_0^2 + \sigma^2)$$

Mean = prior mean, variance = prior variance + likelihood variance.

---

## Part 4: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2022, Question 4a)

> Model $m_1$: $p(x|\theta, m_1) = \theta^x(1-\theta)^{1-x}$, $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Work out** $p(x=1|m_1)$.
>
> Options: (a) $2/3$, (b) $1/6$, (c) $1/3$, (d) $1/2$

### STEP-BY-STEP SOLUTION

**Step 1: Write the evidence formula**

$$p(x=1|m_1) = \int_0^1 p(x=1|\theta, m_1) \cdot p(\theta|m_1) \, d\theta$$

**Step 2: Evaluate the likelihood at x=1**

The likelihood is: $p(x|\theta, m_1) = \theta^x(1-\theta)^{1-x}$

Plug in x=1:
$$p(x=1|\theta, m_1) = \theta^1(1-\theta)^{1-1} = \theta^1(1-\theta)^0 = \theta \times 1 = \theta$$

**Why $(1-\theta)^0 = 1$?** Any number to the power of 0 equals 1.

**Step 3: Write the prior**

$$p(\theta|m_1) = 6\theta(1-\theta)$$

**Step 4: Multiply likelihood × prior**

$$\theta \times 6\theta(1-\theta) = 6\theta^2(1-\theta)$$

**How:** $\theta \times \theta = \theta^2$. The constant 6 stays. The $(1-\theta)$ stays.

**Step 5: Set up the integral**

$$p(x=1|m_1) = \int_0^1 6\theta^2(1-\theta) \, d\theta = 6 \int_0^1 \theta^2(1-\theta)^1 \, d\theta$$

**Step 6: Apply the Beta function**

p=2, q=1:

$$\int_0^1 \theta^2(1-\theta)^1 d\theta = \frac{2! \cdot 1!}{(2+1+1)!} = \frac{2}{24} = \frac{1}{12}$$

**Step 7: Multiply by the constant**

$$p(x=1|m_1) = 6 \times \frac{1}{12} = \frac{6}{12} = \frac{1}{2}$$

**Answer: (d) 1/2** ✅

---

### EXAM QUESTION 2 (2022, Question 4d)

> Model $m_1$: $p(x=1|m_1) = 1/2$ (from previous calculation)
> Model $m_2$: $p(x=1|m_2) = 1/3$ (from previous calculation)
> Model priors: $p(m_1) = 1/3$, $p(m_2) = 2/3$
>
> **Compute** $p(x=1)$ by Bayesian model averaging.
>
> Options: (a) $7/18$, (b) $1/2$, (c) $4/9$, (d) $8/18$

### STEP-BY-STEP SOLUTION

**Step 1: Write the model averaging formula**

$$p(x=1) = p(x=1|m_1) \cdot p(m_1) + p(x=1|m_2) \cdot p(m_2)$$

**Step 2: Plug in the numbers**

$$p(x=1) = \frac{1}{2} \cdot \frac{1}{3} + \frac{1}{3} \cdot \frac{2}{3}$$

**Step 3: Compute each term**

- First term: $\frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$
- Second term: $\frac{1}{3} \times \frac{2}{3} = \frac{2}{9}$

**Step 4: Add them (find common denominator)**

$$\frac{1}{6} + \frac{2}{9} = \frac{1 \times 3}{6 \times 3} + \frac{2 \times 2}{9 \times 2} = \frac{3}{18} + \frac{4}{18} = \frac{7}{18}$$

**Answer: (a) 7/18** ✅

---

### EXAM QUESTION 3 (2023, Question 1c — Gaussian Model Averaging)

> Model $m_1$: $p(x|\mu, m_1) = \mathcal{N}(x|\mu, 1)$, $p(\mu|m_1) = \mathcal{N}(\mu|0, 1)$
> Model $m_2$: $p(x|m_2) = \mathcal{N}(x|1, 1)$
> Model priors: $p(m_1) = 2/3$, $p(m_2) = 1/3$
>
> **Determine** $p(x=2)$ by Bayesian model averaging.
>
> Options:
> - (a) $\frac{2}{3\sqrt{2\pi}} + \frac{1}{3}\mathcal{N}(2|0, 1)$
> - (b) $\frac{1}{3}\mathcal{N}(2|1, 2) + \frac{1}{3\sqrt{2\pi}}$
> - (c) $\frac{2}{3}\mathcal{N}(2|0, 2) + \frac{1}{3}\mathcal{N}(2|1, 1)$
> - (d) $\frac{1}{3\sqrt{2\pi}} + \frac{1}{3}\mathcal{N}(2|1, 1)$

### STEP-BY-STEP SOLUTION

**Step 1: Write the model averaging formula**

$$p(x=2) = p(x=2|m_1) \cdot p(m_1) + p(x=2|m_2) \cdot p(m_2)$$

**Step 2: Compute $p(x=2|m_1)$ (evidence for model 1)**

For a Gaussian likelihood with Gaussian prior, the evidence is:

$$p(x|m_1) = \mathcal{N}(x|\mu_0, \sigma_0^2 + \sigma^2)$$

Where:
- $\mu_0 = 0$ (prior mean)
- $\sigma_0^2 = 1$ (prior variance)
- $\sigma^2 = 1$ (likelihood variance)

So:
$$p(x=2|m_1) = \mathcal{N}(2|0, 1+1) = \mathcal{N}(2|0, 2)$$

**Step 3: Read off $p(x=2|m_2)$**

Model 2 directly gives: $p(x|m_2) = \mathcal{N}(x|1, 1)$

So: $p(x=2|m_2) = \mathcal{N}(2|1, 1)$

**Step 4: Combine with model averaging**

$$p(x=2) = \frac{2}{3} \cdot \mathcal{N}(2|0, 2) + \frac{1}{3} \cdot \mathcal{N}(2|1, 1)$$

**Step 5: Match the answer**

(c) says $\frac{2}{3}\mathcal{N}(2|0, 2) + \frac{1}{3}\mathcal{N}(2|1, 1)$ — matches exactly.

**Answer: (c)** ✅

---

## Part 5: Practice Exercises

### Exercise 1

> Model $m_1$: $p(x|\theta, m_1) = (1-\theta)\theta^x$, $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Determine the evidence** $p(x=4|m_1)$.
>
> Options:
> - (a) $\int_0^1 \frac{(1-\theta)\theta^4}{6\theta(1-\theta)} d\theta$
> - (b) $\int_0^1 (1-\theta)\theta^4 d\theta$
> - (c) $\int_0^1 6\theta^5(1-\theta)^2 d\theta$
> - (d) $\int_0^1 \frac{6\theta(1-\theta)}{(1-\theta)\theta^4} d\theta$

---

### Exercise 2

> Model $m_2$: $p(x|\theta, m_2) = (1-\theta)\theta^x$, $p(\theta|m_2) = 2\theta$
>
> **Determine** $p(x=4|m_2)$.
>
> Options:
> - (a) $\int_0^1 2(1-\theta)\theta^5 d\theta$
> - (b) $\frac{1}{\int_0^1 2(1-\theta)\theta^5} d\theta$
> - (c) $\int_0^1 \frac{(1-\theta)\theta^4}{2\theta} d\theta$

---

### Exercise 3

> Model $m_1$: $p(x|\theta, m_1) = \theta^x(1-\theta)^{1-x}$, $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Work out** $p(x=1|m_1)$.
>
> Options:
> - (a) $1/4$
> - (b) $1/2$
> - (c) $\theta/(1+\theta)$
> - (d) $3/4$

---

### Exercise 4

> Model $m_2$: $p(x|\theta, m_2) = (1-\theta)^x\theta^{1-x}$, $p(\theta|m_2) = 2\theta$
>
> **Determine** $p(x=1|m_2)$.
>
> Options:
> - (a) $2/3$
> - (b) $1/4$
> - (c) $1/2$
> - (d) $1/3$

---

### Exercise 5

> $p(m_1) = 1/3$, $p(m_2) = 2/3$
> $p(x=1|m_1) = 1/2$, $p(x=1|m_2) = 1/3$
>
> **Compute** $p(x=1)$ by Bayesian model averaging.
>
> Options:
> - (a) $7/18$
> - (b) $1/2$
> - (c) $4/9$
> - (d) $8/18$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (c)** ∫₀¹ 6θ⁵(1-θ)² dθ

Evidence = ∫ likelihood × prior dθ.

Likelihood at x=4: (1-θ)θ⁴
Prior: 6θ(1-θ)
Product: 6θ⁵(1-θ)²
Integral: ∫₀¹ 6θ⁵(1-θ)² dθ
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (a)** ∫₀¹ 2(1-θ)θ⁵ dθ

Likelihood at x=4: (1-θ)θ⁴
Prior: 2θ
Product: 2θ⁵(1-θ)
Integral: ∫₀¹ 2θ⁵(1-θ) dθ
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b) 1/2**

Likelihood at x=1: θ¹(1-θ)⁰ = θ
Prior: 6θ(1-θ)
Product: 6θ²(1-θ)
Integral: 6 × (2!×1!)/4! = 6 × 2/24 = 1/2
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (d) 1/3**

Likelihood at x=1: (1-θ)¹θ⁰ = 1-θ
Prior: 2θ
Product: 2θ(1-θ) = 2θ¹(1-θ)¹
Integral: 2 × (1!×1!)/3! = 2 × 1/6 = 1/3
</details>

<details>
<summary>Exercise 5</summary>

**Answer: (a) 7/18**

p(x=1) = (1/2)(1/3) + (1/3)(2/3) = 1/6 + 2/9 = 3/18 + 4/18 = 7/18
</details>
