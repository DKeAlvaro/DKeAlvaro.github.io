# Exercise Type 2: Beta-Bernoulli Coin Toss

> **What the exam asks:** You observe coin tosses. You have a prior belief about the coin's bias. You must compute the likelihood, posterior, evidence, and/or predictive probability.

---

## Part 0: What Do All These Symbols Mean?

### New Symbols for This Exercise Type

| Symbol | What It Looks Like | What It Means |
|--------|--------------------|---------------|
| $\mu$ | Greek letter "mu" (looks like a u) | The **bias** of the coin. $\mu = 0.7$ means 70% chance of "1" |
| $x_n$ | x with subscript n | The n-th coin toss outcome |
| $D$ | Capital D | The **dataset** — all the toss results we've seen |
| $\text{Beta}(\cdot)$ | "Beta" with parentheses | The **Beta distribution** — a specific probability formula |
| $\alpha$ | Greek letter "alpha" (looks like a fish) | A parameter of the Beta distribution — "pseudo-count" of ones |
| $\beta$ | Greek letter "beta" | A parameter of the Beta distribution — "pseudo-count" of zeros |
| $\Gamma$ | Capital Greek letter Gamma | The **Gamma function** — generalizes factorial to non-integers |
| $N_1$ | Capital N with subscript 1 | The number of ones observed in the data |
| $N_0$ | Capital N with subscript 0 | The number of zeros observed in the data |
| $\mathbb{E}[\cdot]$ | E with square brackets | "Expected value" — the average you'd expect |

### The Bernoulli Distribution

The Bernoulli distribution describes a single coin toss:

$$p(x_n|\mu) = \mu^{x_n}(1-\mu)^{1-x_n}$$

**How to read this:** "The probability of outcome $x_n$ given coin bias $\mu$ equals $\mu$ raised to the power $x_n$, times $(1-\mu)$ raised to the power $1-x_n$."

**The clever trick:** This formula "selects" the right probability:
- When $x_n = 1$: $p(1|\mu) = \mu^1(1-\mu)^0 = \mu \times 1 = \mu$
- When $x_n = 0$: $p(0|\mu) = \mu^0(1-\mu)^1 = 1 \times (1-\mu) = 1-\mu$

**Why write it this fancy way?** So we can write the probability of ALL tosses in one compact formula.

### The Beta Distribution

The Beta distribution is a formula for our belief about μ:

$$p(\mu) = \text{Beta}(\mu|\alpha, \beta) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \mu^{\alpha-1}(1-\mu)^{\beta-1}$$

**How to read this:** "The probability density of μ given parameters α and β equals a normalization constant (the Gamma fraction) times $\mu^{\alpha-1}(1-\mu)^{\beta-1}$."

**Don't panic about the Gamma function.** For integers, $\Gamma(n) = (n-1)!$. So:
- $\Gamma(5) = 4! = 24$
- $\Gamma(3) = 2! = 2$
- $\Gamma(1) = 0! = 1$

**The intuitive meaning of α and β:**
- $\alpha$ = "number of pseudo-ones" (imaginary tosses that came up 1)
- $\beta$ = "number of pseudo-zeros" (imaginary tosses that came up 0)
- $\alpha + \beta$ = total pseudo-observations

**Example:** Beta(μ|3, 2) means "before seeing real data, it's as if I'd already seen 3 ones and 2 zeros."

### The Mean of the Beta Distribution

$$\mathbb{E}[\mu] = \frac{\alpha}{\alpha + \beta}$$

**In plain English:** "The average value of μ under my Beta belief is α divided by the total."

**Example:** If α=3, β=2: mean = 3/(3+2) = 3/5 = 0.6

---

## Part 1: The Core Concepts — No Math

### What's Going On?

1. You have a coin. You don't know its bias μ.
2. Before tossing, you have a prior belief: "I think the coin is probably somewhat fair, maybe slightly biased." This is your **Beta prior**.
3. You toss the coin several times and record results. This is your **data D**.
4. After seeing the data, you update your belief about μ. This is your **posterior**.

### The Magic Rule: Conjugacy

**When the prior is Beta and the likelihood is Bernoulli, the posterior is ALSO Beta.**

And updating is incredibly simple:

$$\text{Beta}(\alpha, \beta) + \text{data } (N_1 \text{ ones}, N_0 \text{ zeros}) \rightarrow \text{Beta}(\alpha + N_1, \beta + N_0)$$

**In plain English:** Just add the real counts to the pseudo-counts. That's it!

**Example:**
- Prior: Beta(3, 2) — as if 3 ones and 2 zeros
- Data: {0, 1, 0, 0, 1, 0, 0} — that's 2 ones and 5 zeros
- Posterior: Beta(3+2, 2+5) = Beta(5, 7)

### The Four Things You Might Be Asked

| What | Symbol | How to Compute |
| :--- | :--- | :--- |
| **Likelihood** | $p(D \mid \mu)$ | $\mu^{N_1}(1-\mu)^{N_0}$ |
| **Posterior** | $p(\mu \mid D)$ | $\text{Beta}(\alpha + N_1, \beta + N_0)$ |
| **Evidence** | $p(D)$ | $B(\alpha+N_1, \beta+N_0) \, / \, B(\alpha, \beta)$ |
| **Predictive** | $p(x=1 \mid D)$ | $(\alpha+N_1) \, / \, (\alpha+\beta+N)$ |

---

## Part 2: The Key Formulas (MEMORIZE)

### Formula 1: Likelihood

$$p(D|\mu) = \mu^{N_1}(1-\mu)^{N_0}$$

**IMPORTANT:** There is NO binomial coefficient $\binom{N}{k}$ in the likelihood. The likelihood is just the product of individual probabilities.

### Formula 2: Posterior

$$p(\mu|D) = \text{Beta}(\mu|\alpha + N_1, \beta + N_0)$$

### Formula 3: Evidence

$$p(D) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \cdot \frac{\Gamma(\alpha+N_1)\Gamma(\beta+N_0)}{\Gamma(\alpha+\beta+N)}$$

Where $N = N_1 + N_0$ (total number of tosses).

### Formula 4: Predictive Probability

$$p(x_{next}=1|D) = \frac{\alpha + N_1}{\alpha + \beta + N}$$

This is just the posterior mean.

---

## Part 3: FULL Walkthrough of Real Exam Questions

### THE EXAM QUESTION (2022, Question 3 — Complete)

> Consider a biased coin with outcomes:
> $$x_n = \begin{cases} 0 & \text{(heads)} \\ 1 & \text{(tails)} \end{cases}$$
>
> Bernoulli: $p(x_n|\mu) = \mu^{x_n}(1-\mu)^{1-x_n}$
> Beta prior: $p(\mu) = \text{Beta}(\mu|\alpha=3, \beta=2)$
>
> We throw 7 times and observe: $D = \{0, 1, 0, 0, 1, 0, 0\}$

---

### Question 3a: Interpretation of α=3, β=2

> Which interpretation is most valid?
> - (a) 5 pseudo tosses, 2 tails and 1 heads
> - (b) 3 pseudo tosses, 2 tails and 1 heads
> - (c) P(tails) = 2/3 × P(heads)
> - (d) 5 pseudo tosses, 3 tails and 2 heads

### STEP-BY-STEP SOLUTION

**Step 1: Understand what α and β represent**

The problem says:
- $x_n = 1$ means **tails**
- $x_n = 0$ means **heads**

So:
- $\alpha$ = pseudo-count of ones = pseudo-count of **tails**
- $\beta$ = pseudo-count of zeros = pseudo-count of **heads**

**Step 2: Read off the values**

- $\alpha = 3$ → 3 pseudo-tails
- $\beta = 2$ → 2 pseudo-heads
- Total = $3 + 2 = 5$ pseudo-tosses

**Step 3: Match the answer**

(d) says "5 pseudo tosses, 3 tails and 2 heads" — this matches exactly.

**Answer: (d)** ✅

---

### Question 3b: The Likelihood $p(D|\mu)$

> Options:
> - (a) $\binom{5}{2} \cdot \mu^5(1-\mu)^2$
> - (b) $\mu^5(1-\mu)^2$
> - (c) $\mu^2(1-\mu)^5$
> - (d) $\mu^1(1-\mu)^4$

### STEP-BY-STEP SOLUTION

**Step 1: Count ones and zeros in the data**

$D = \{0, 1, 0, 0, 1, 0, 0\}$

Let me go through each element:
- Position 1: 0
- Position 2: 1
- Position 3: 0
- Position 4: 0
- Position 5: 1
- Position 6: 0
- Position 7: 0

Count:
- Number of zeros ($N_0$) = 5 (positions 1, 3, 4, 6, 7)
- Number of ones ($N_1$) = 2 (positions 2, 5)

**Step 2: Write the likelihood formula**

$$p(D|\mu) = \prod_{n=1}^{7} p(x_n|\mu) = \mu^{N_1}(1-\mu)^{N_0} = \mu^2(1-\mu)^5$$

**Step 3: Match the answer**

(c) says $\mu^2(1-\mu)^5$ — matches.

**Answer: (c)** ✅

### WHY (a) AND (b) ARE WRONG

**(a)** has $\binom{5}{2}$ — a binomial coefficient. The likelihood does NOT include this. The binomial coefficient appears in the Binomial distribution (which asks "what's the probability of exactly k heads in N tosses?"), not in the likelihood for μ.

**(b)** has the powers reversed: $\mu^5(1-\mu)^2$. This would mean 5 ones and 2 zeros, but we have 2 ones and 5 zeros.

---

### Question 3c: The Posterior $p(\mu|D)$

> Options:
> - (a) $\text{Beta}(\mu|4, 6)$
> - (b) $\mu^4(1-\mu)^6$
> - (c) $\mu^5(1-\mu)^7$
> - (d) $\text{Beta}(\mu|5, 7)$

### STEP-BY-STEP SOLUTION

**Step 1: Apply the conjugacy rule**

Prior: Beta(α=3, β=2)
Data: $N_1 = 2$ ones, $N_0 = 5$ zeros

$$\text{Posterior} = \text{Beta}(\alpha + N_1, \beta + N_0) = \text{Beta}(3+2, 2+5) = \text{Beta}(5, 7)$$

**Step 2: Match the answer**

(d) says Beta(μ|5, 7) — matches.

**Answer: (d)** ✅

### WHY (a) IS WRONG

(a) says Beta(4, 6). That would come from adding 1 to each parameter, which makes no sense. You add the DATA counts, not 1.

### WHY (b) AND (c) ARE WRONG

These are just the kernel $\mu^{\alpha-1}(1-\mu)^{\beta-1}$ without the normalization constant. The posterior is a PROPER Beta distribution, not just the kernel.

---

### Question 3d: Predictive Probability

> Compute the probability of throwing tails after absorbing the data.
>
> Options:
> - (a) $4/11$
> - (b) $3/5$
> - (c) $1/2$
> - (d) $5/12$

### STEP-BY-STEP SOLUTION

**Step 1: What are we computing?**

$p(x_{next}=1|D)$ = probability the next toss is tails (=1), given all the data we've seen.

**Step 2: This equals the posterior mean**

$$p(x_{next}=1|D) = \mathbb{E}[\mu|D] = \frac{\alpha_{post}}{\alpha_{post} + \beta_{post}}$$

**Step 3: Plug in posterior parameters**

Posterior = Beta(5, 7), so:

$$p(x_{next}=1|D) = \frac{5}{5+7} = \frac{5}{12}$$

**Answer: (d)** ✅

---

### SECOND EXAM WALKTHROUGH (2023, Question 3)

> Coin: $x_n = 0$ (tails), $x_n = 1$ (heads)
> **NOTE:** This is FLIPPED from the previous exam!
> Bernoulli: $p(x_n|\mu) = \mu^{x_n}(1-\mu)^{1-x_n}$
> Beta prior: $p(\mu) = \text{Beta}(\mu|\alpha=3, \beta=2)$
> Data: $D = \{0, 1, 1, 0, 1\}$ (5 throws)

---

### Question 3a: Likelihood

> Options:
> - (a) $\mu^3(1-\mu)^2$
> - (b) $\binom{5}{3} \cdot \mu^2(1-\mu)^3$
> - (c) $\binom{5}{2} \cdot \mu^3(1-\mu)^2$
> - (d) $\binom{3}{2} \cdot \mu^3(1-\mu)^2$

### STEP-BY-STEP SOLUTION

**Step 1: Count ones and zeros**

$D = \{0, 1, 1, 0, 1\}$
- $N_0$ = 2 (positions 1, 4)
- $N_1$ = 3 (positions 2, 3, 5)

**Step 2: Write likelihood**

$$p(D|\mu) = \mu^{N_1}(1-\mu)^{N_0} = \mu^3(1-\mu)^2$$

**Answer: (a)** ✅ (No binomial coefficient!)

---

### Question 3b: Posterior

> Options:
> - (a) $\binom{5}{2} \cdot \mu^3(1-\mu)^2$
> - (b) $\text{Beta}(\mu|6, 4)$
> - (c) $\text{Beta}(\mu|5, 5)$
> - (d) $\mu^3(1-\mu)^2 \cdot \text{Beta}(\mu|\alpha=3, \beta=2)$

### STEP-BY-STEP SOLUTION

Prior: Beta(3, 2)
Data: $N_1 = 3$ ones, $N_0 = 2$ zeros

Posterior: Beta(3+3, 2+2) = Beta(6, 4)

**Answer: (b)** ✅

---

### Question 3c: Evidence

> Options:
> - (a) $\frac{\Gamma(4)\Gamma(6)}{\Gamma(10)}$
> - (b) $\frac{\Gamma(4)\Gamma(5)\Gamma(6)}{\Gamma(2)\Gamma(3)\Gamma(10)}$
> - (c) $\frac{\Gamma(5)}{\Gamma(2)\Gamma(3)}$
> - (d) $\frac{\Gamma(5)\Gamma(10)}{\Gamma(2)\Gamma(3)\Gamma(4)\Gamma(6)}$

### STEP-BY-STEP SOLUTION

**Step 1: Write the evidence formula**

$$p(D) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \cdot \frac{\Gamma(\alpha+N_1)\Gamma(\beta+N_0)}{\Gamma(\alpha+\beta+N)}$$

**Step 2: Plug in the numbers**

- $\alpha = 3$, $\beta = 2$
- $N_1 = 3$, $N_0 = 2$
- $N = 3 + 2 = 5$
- $\alpha + \beta = 5$
- $\alpha + N_1 = 3 + 3 = 6$
- $\beta + N_0 = 2 + 2 = 4$
- $\alpha + \beta + N = 5 + 5 = 10$

$$p(D) = \frac{\Gamma(5)}{\Gamma(3)\Gamma(2)} \cdot \frac{\Gamma(6)\Gamma(4)}{\Gamma(10)}$$

**Step 3: Match the answer**

(b) says $\frac{\Gamma(4)\Gamma(5)\Gamma(6)}{\Gamma(2)\Gamma(3)\Gamma(10)}$

Let me check: rearranging my result:
$$\frac{\Gamma(5)}{\Gamma(3)\Gamma(2)} \cdot \frac{\Gamma(6)\Gamma(4)}{\Gamma(10)} = \frac{\Gamma(5)\Gamma(6)\Gamma(4)}{\Gamma(3)\Gamma(2)\Gamma(10)} = \frac{\Gamma(4)\Gamma(5)\Gamma(6)}{\Gamma(2)\Gamma(3)\Gamma(10)}$$

Yes, matches (b).

**Answer: (b)** ✅

---

### Question 3d: Predictive Probability

> Options:
> - (a) $\text{Beta}(0.6|6, 4)$
> - (b) $0.6$
> - (c) $0.7$
> - (d) $0.4$

### STEP-BY-STEP SOLUTION

Posterior = Beta(6, 4)

Predictive = posterior mean = $\frac{6}{6+4} = \frac{6}{10} = 0.6$

**Answer: (b) 0.6** ✅

---

## Part 4: Tricks & Shortcuts

### TRICK 1: ALWAYS Check Which Outcome = 1

Different exams define it differently:
- 2022: 1 = tails, 0 = heads
- 2023: 1 = heads, 0 = tails

This changes which count goes to α and which to β.

### TRICK 2: Likelihood Has NO Binomial Coefficient

If an option has $\binom{N}{k}$, it's wrong. The likelihood is simply $\mu^{N_1}(1-\mu)^{N_0}$.

### TRICK 3: Posterior Is Always a Proper Beta Distribution

The answer should say "Beta(μ|..., ...)" not just "$\mu^a(1-\mu)^b$".

### TRICK 4: Predictive = Posterior Mean = α/(α+β)

Just read off the posterior parameters and divide α by their sum.

### TRICK 5: Evidence = Gamma Function Pattern

$$p(D) = \frac{\Gamma(\alpha+\beta) \cdot \Gamma(\alpha+N_1) \cdot \Gamma(\beta+N_0)}{\Gamma(\alpha) \cdot \Gamma(\beta) \cdot \Gamma(\alpha+\beta+N)}$$

Look for this exact pattern in the options.

### TRICK 6: Counting Ones and Zeros

Write the data out and count manually. Don't rush this step.

---

## Part 5: Practice Exercises

### Exercise 1

> Coin: $x_n = 0$ (heads), $x_n = 1$ (tails)
> Beta prior: Beta(μ|α=3, β=2)
> Data: $D = \{0, 1, 0, 0, 1, 0, 0\}$
>
> **How many ones and zeros are in the data?**

---

### Exercise 2

> Same data and prior as Exercise 1.
>
> **Write the likelihood** $p(D|\mu)$.

---

### Exercise 3

> Same setup.
>
> **Compute the posterior** $p(\mu|D)$.

---

### Exercise 4

> Same setup.
>
> **Compute the predictive probability** $p(x_{next}=1|D)$ (probability of tails).

---

### Exercise 5

> Coin: $x_n = 0$ (tails), $x_n = 1$ (heads)
> Beta prior: Beta(μ|α=3, β=2)
> Data: $D = \{0, 1, 1, 0, 1\}$
>
> **Write the likelihood** $p(D|\mu)$.

---

### Exercise 6

> Same setup as Exercise 5.
>
> **Compute the posterior** $p(\mu|D)$.

---

### Exercise 7

> Same setup as Exercise 5.
>
> **Compute the evidence** $p(D)$.

---

### Exercise 8

> Same setup as Exercise 5.
>
> **Compute** $p(x_{next}=1|D)$ (probability of heads).

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**N₁ = 2 ones** (tails), **N₀ = 5 zeros** (heads)

Data: {0, 1, 0, 0, 1, 0, 0}
Zeros at positions: 1, 3, 4, 6, 7 → 5 zeros
Ones at positions: 2, 5 → 2 ones
</details>

<details>
<summary>Exercise 2</summary>

**p(D|μ) = μ²(1-μ)⁵**

N₁ = 2, N₀ = 5. Likelihood = μ²(1-μ)⁵. No binomial coefficient!
</details>

<details>
<summary>Exercise 3</summary>

**p(μ|D) = Beta(μ|5, 7)**

Prior: Beta(3, 2). Data: N₁=2, N₀=5.
Posterior: Beta(3+2, 2+5) = Beta(5, 7)
</details>

<details>
<summary>Exercise 4</summary>

**p(x_next=1|D) = 5/12**

Posterior mean = 5/(5+7) = 5/12
</details>

<details>
<summary>Exercise 5</summary>

**p(D|μ) = μ³(1-μ)²**

N₁ = 3 (heads), N₀ = 2 (tails). Likelihood = μ³(1-μ)²
</details>

<details>
<summary>Exercise 6</summary>

**p(μ|D) = Beta(μ|6, 4)**

Prior: Beta(3, 2). Data: N₁=3, N₀=2.
Posterior: Beta(3+3, 2+2) = Beta(6, 4)
</details>

<details>
<summary>Exercise 7</summary>

**p(D) = Γ(5)Γ(6)Γ(4) / [Γ(3)Γ(2)Γ(10)] = Γ(4)Γ(5)Γ(6) / [Γ(2)Γ(3)Γ(10)]**

α=3, β=2, N₁=3, N₀=2, N=5.
p(D) = Γ(3+2)/(Γ(3)Γ(2)) × Γ(3+3)Γ(2+2)/Γ(3+2+5) = Γ(5)/(Γ(3)Γ(2)) × Γ(6)Γ(4)/Γ(10)
</details>

<details>
<summary>Exercise 8</summary>

**p(x_next=1|D) = 0.6**

Posterior mean = 6/(6+4) = 6/10 = 0.6
</details>
