# Exercise Type 5: Model Comparison & Bayes Factor

> **What the exam asks:** You have two competing models. After observing data, which model is more plausible? Compute the Bayes Factor and/or the ratio of posterior model probabilities.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $p(D\|m_1)$ | "probability of data given model 1" | The **evidence** for model 1 — how well model 1 predicted the data |
| $B_{12}$ | "Bayes Factor one-two" | Ratio of evidences: $B_{12} = p(D\|m_1) / p(D\|m_2)$ |
| $p(m_1\|D)$ | "probability of model 1 given data" | How plausible model 1 is AFTER seeing the data |
| $p(m_1)$ | "probability of model 1" | How plausible model 1 was BEFORE seeing the data (prior) |
| $\frac{p(m_1\|D)}{p(m_2\|D)}$ | "ratio of posterior probabilities" | After seeing data, how many times more likely is model 1 vs model 2? |

### The Key Concept: Bayes Factor

The Bayes Factor tells you which model explained the data better:

$$B_{12} = \frac{p(D|m_1)}{p(D|m_2)}$$

**In plain English:** "How many times better did model 1 explain the data compared to model 2?"

- If $B_{12} = 3$: Model 1 explained the data 3 times better than model 2
- If $B_{12} = 0.5$: Model 2 explained the data 2 times better than model 1
- If $B_{12} = 1$: Both models explained the data equally well

### The Key Concept: Posterior Model Probability

After seeing data, how plausible is each model?

$$p(m_k|D) = \frac{p(D|m_k) \cdot p(m_k)}{p(D)}$$

**In plain English:** "Model plausibility = (how well it explained the data) × (how plausible it was to begin with), divided by a normalizing number."

### The Key Concept: Ratio of Posterior Probabilities

This is the MOST useful formula:

$$\frac{p(m_1|D)}{p(m_2|D)} = \frac{p(D|m_1)}{p(D|m_2)} \cdot \frac{p(m_1)}{p(m_2)} = B_{12} \cdot \frac{p(m_1)}{p(m_2)}$$

**In plain English:** "The ratio of posterior probabilities = (ratio of evidences) × (ratio of prior probabilities)"

**Why this is useful:** You don't need to compute $p(D)$ (the overall evidence). It cancels out!

---

## Part 1: Key Formulas (MEMORIZE)

### Formula 1: Evidence for a Model

$$p(D|m) = \int p(D|\theta, m) \cdot p(\theta|m) \, d\theta$$

### Formula 2: Bayes Factor

$$B_{12} = \frac{p(D|m_1)}{p(D|m_2)}$$

### Formula 3: Posterior Probability Ratio

$$\frac{p(m_1|D)}{p(m_2|D)} = B_{12} \cdot \frac{p(m_1)}{p(m_2)}$$

### Formula 4: Bayes Factor in Terms of Posteriors

$$B_{12} = \frac{p(m_1|D)}{p(m_2|D)} \cdot \frac{p(m_2)}{p(m_1)}$$

This is just a rearrangement of Formula 3.

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-B, Questions 2d-2e)

> Model $m_1$: $p(x|\theta, m_1) = (1-\theta)\theta^x$, $p(\theta|m_1) = 6\theta(1-\theta)$
> Model $m_2$: $p(x|\theta, m_2) = (1-\theta)\theta^x$, $p(\theta|m_2) = 2\theta$
> Model priors: $p(m_1) = 2/3$, $p(m_2) = 1/3$
>
> We observe $x = 4$.

### Question 2d: Which model has the largest evidence?

### STEP-BY-STEP SOLUTION

**Step 1: Compute evidence for $m_1$**

$$p(x=4|m_1) = \int_0^1 p(x=4|\theta, m_1) \cdot p(\theta|m_1) \, d\theta$$

Likelihood at x=4: $(1-\theta)\theta^4$
Prior: $6\theta(1-\theta)$
Product: $6\theta^5(1-\theta)^2$

$$p(x=4|m_1) = 6 \int_0^1 \theta^5(1-\theta)^2 \, d\theta$$

Using Beta function (p=5, q=2):

$$\int_0^1 \theta^5(1-\theta)^2 d\theta = \frac{5! \cdot 2!}{(5+2+1)!} = \frac{120 \cdot 2}{8!} = \frac{240}{40320} = \frac{1}{168}$$

$$p(x=4|m_1) = 6 \times \frac{1}{168} = \frac{6}{168} = \frac{1}{28}$$

**Step 2: Compute evidence for $m_2$**

Likelihood at x=4: $(1-\theta)\theta^4$
Prior: $2\theta$
Product: $2\theta^5(1-\theta)$

$$p(x=4|m_2) = 2 \int_0^1 \theta^5(1-\theta)^1 \, d\theta$$

Using Beta function (p=5, q=1):

$$\int_0^1 \theta^5(1-\theta)^1 d\theta = \frac{5! \cdot 1!}{(5+1+1)!} = \frac{120}{7!} = \frac{120}{5040} = \frac{1}{42}$$

$$p(x=4|m_2) = 2 \times \frac{1}{42} = \frac{2}{42} = \frac{1}{21}$$

**Step 3: Compare**

$p(x=4|m_1) = 1/28 \approx 0.0357$
$p(x=4|m_2) = 1/21 \approx 0.0476$

$1/21 > 1/28$, so model 2 has larger evidence.

**Answer: (b) $m_2$** ✅

---

### Question 2e: Which model has the largest posterior probability?

### STEP-BY-STEP SOLUTION

**Step 1: Write the posterior probability ratio formula**

$$\frac{p(m_1|x=4)}{p(m_2|x=4)} = \frac{p(x=4|m_1)}{p(x=4|m_2)} \cdot \frac{p(m_1)}{p(m_2)}$$

**Step 2: Plug in the numbers**

$$\frac{p(m_1|x=4)}{p(m_2|x=4)} = \frac{1/28}{1/21} \cdot \frac{2/3}{1/3}$$

**Step 3: Compute the evidence ratio**

$$\frac{1/28}{1/21} = \frac{21}{28} = \frac{3}{4}$$

**Step 4: Compute the prior ratio**

$$\frac{2/3}{1/3} = \frac{2}{3} \times \frac{3}{1} = 2$$

**Step 5: Multiply**

$$\frac{p(m_1|x=4)}{p(m_2|x=4)} = \frac{3}{4} \times 2 = \frac{3}{2} = 1.5$$

**Step 6: Interpret**

Since the ratio is > 1, $p(m_1|x=4) > p(m_2|x=4)$. Model 1 has higher posterior probability.

**Answer: (a) $m_1$** ✅

### IMPORTANT INSIGHT

Model 2 had higher evidence, but model 1 has higher posterior! Why? Because model 1 had a much higher prior (2/3 vs 1/3), and this prior advantage outweighed the evidence disadvantage.

---

### EXAM QUESTION 2 (2022, Question 1c — Bayes Factor Formula)

> Which expression correctly gives the Bayes Factor $B_{12}$?
>
> Options:
> - (a) $B_{12} = \frac{p(D|m_1)}{p(D|m_2)} = \frac{p(m_1|D)}{p(m_2|D)} \cdot \frac{p(m_1)}{p(m_2)}$
> - (b) $B_{12} = \frac{p(D|m_1)}{p(D|m_2)} = \frac{p(m_1|D)}{p(m_2|D)} \cdot \frac{p(m_2)}{p(m_1)}$
> - (c) $B_{12} = \frac{p(m_1|D)}{p(m_2|D)} = \frac{p(D|m_1)}{p(D|m_2)} \cdot \frac{p(m_2)}{p(m_1)}$
> - (d) $B_{12} = \frac{p(m_1|D)}{p(m_2|D)} = \frac{p(D|m_1)}{p(D|m_2)} \cdot \frac{p(m_1)}{p(m_2)}$

### STEP-BY-STEP SOLUTION

**Step 1: The definition of Bayes Factor**

$$B_{12} = \frac{p(D|m_1)}{p(D|m_2)}$$

This eliminates (c) and (d) because they define $B_{12}$ as the posterior ratio.

**Step 2: The relationship between posterior ratio and Bayes Factor**

$$\frac{p(m_1|D)}{p(m_2|D)} = B_{12} \cdot \frac{p(m_1)}{p(m_2)}$$

Rearranging:
$$B_{12} = \frac{p(m_1|D)}{p(m_2|D)} \cdot \frac{p(m_2)}{p(m_1)}$$

**Step 3: Match the answer**

(b) says $B_{12} = \frac{p(D|m_1)}{p(D|m_2)} = \frac{p(m_1|D)}{p(m_2|D)} \cdot \frac{p(m_2)}{p(m_1)}$ — correct!

**Answer: (b)** ✅

---

### EXAM QUESTION 3 (2022, Question 4e)

> $p(x=1|m_1) = 1/2$, $p(x=1|m_2) = 1/3$
> $p(m_1) = 1/3$, $p(m_2) = 2/3$
>
> **Compute** $\frac{p(m_1|x=1)}{p(m_2|x=1)}$.
>
> Options: (a) $3/4$, (b) $4/9$, (c) $5/9$, (d) $2/3$

### STEP-BY-STEP SOLUTION

$$\frac{p(m_1|x=1)}{p(m_2|x=1)} = \frac{p(x=1|m_1)}{p(x=1|m_2)} \cdot \frac{p(m_1)}{p(m_2)} = \frac{1/2}{1/3} \cdot \frac{1/3}{2/3}$$

$$= \frac{1/2}{1/3} \times \frac{1/3}{2/3} = \frac{3}{2} \times \frac{1}{2} = \frac{3}{4}$$

**Answer: (a) 3/4** ✅

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Bayes Factor Is Just a Ratio of Evidences

Compute each evidence using the Beta function. Divide them.

### TRICK 2: Posterior Ratio = Bayes Factor × Prior Ratio

Don't compute each posterior separately. Just multiply.

### TRICK 3: Which Model Wins?

- If posterior ratio > 1: model 1 wins
- If posterior ratio < 1: model 2 wins

### TRICK 4: The Bayes Factor Formula Pattern

$B_{12}$ = evidence ratio × (prior of model 2 / prior of model 1)

Watch for which prior goes on top — it's the OPPOSITE of what you might expect!

---

## Part 4: Practice Exercises

### Exercise 1

> Model $m_1$: $p(x|\theta) = (1-\theta)\theta^x$, $p(\theta) = 6\theta(1-\theta)$
> Model $m_2$: $p(x|\theta) = (1-\theta)\theta^x$, $p(\theta) = 2\theta$
>
> After observing $x=4$, which model has larger evidence?
>
> Options:
> - (a) $m_1$
> - (b) $m_2$
> - (c) Same evidence

---

### Exercise 2

> Same models. Priors: $p(m_1) = 2/3$, $p(m_2) = 1/3$.
>
> After observing $x=4$, which model has larger posterior probability?
>
> Options:
> - (a) $m_1$
> - (b) $m_2$
> - (c) Equal

---

### Exercise 3

> Model $m_1$: $p(x|\theta) = \theta^x(1-\theta)^{1-x}$, $p(\theta) = 6\theta(1-\theta)$
> Model $m_2$: $p(x|\theta) = (1-\theta)^x\theta^{1-x}$, $p(\theta) = 1$ (uniform)
> $p(m_1) = 2/3$, $p(m_2) = 1/3$
>
> Compute $\frac{p(m_1|x=1)}{p(m_2|x=1)}$.
>
> Options:
> - (a) $1/3$
> - (b) $1/2$
> - (c) $2/3$
> - (d) $2$

---

### Exercise 4

> $p(x=1|m_1) = 1/2$, $p(x=1|m_2) = 1/3$
> $p(m_1) = 1/3$, $p(m_2) = 2/3$
>
> Compute $\frac{p(m_1|x=1)}{p(m_2|x=1)}$.
>
> Options:
> - (a) $3/4$
> - (b) $4/9$
> - (c) $5/9$
> - (d) $2/3$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (b) m₂**

p(x=4|m₁) = 1/28, p(x=4|m₂) = 1/21.
Since 1/21 > 1/28, model 2 has larger evidence.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (a) m₁**

Posterior ratio = (1/28)/(1/21) × (2/3)/(1/3) = (21/28) × 2 = 3/4 × 2 = 3/2 = 1.5 > 1.
So model 1 has higher posterior.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (d) 2**

p(x=1|m₁) = ∫ θ·6θ(1-θ)dθ = 6∫θ²(1-θ)dθ = 6×(2!×1!)/4! = 1/2
p(x=1|m₂) = ∫(1-θ)·1 dθ = ∫(1-θ)dθ = 1 - 1/2 = 1/2

Posterior ratio = (1/2)/(1/2) × (2/3)/(1/3) = 1 × 2 = 2
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (a) 3/4**

Posterior ratio = (1/2)/(1/3) × (1/3)/(2/3) = (3/2) × (1/2) = 3/4
</details>
