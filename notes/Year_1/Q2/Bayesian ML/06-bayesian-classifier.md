# Exercise Type 6: Bayesian Classifier (Discrimination Boundary & Error)

> **What the exam asks:** You have a machine that measures some property of a liquid/object. You want to classify it into one of two categories. Given the mathematical formulas for how each category behaves and how common each is, find the decision boundary, compute posterior class probabilities, and calculate error rates.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $C_1$ | "Class one" | One category (e.g., "Fanta") |
| $C_2$ | "Class two" | The other category (e.g., "Orangina") |
| $x$ | lowercase x | The measurement you made (e.g., "orangeness" = 1.3) |
| $p(x\|C_1)$ | "probability of x given class C₁" | If the drink IS Fanta, how likely is it to have measurement x? |
| $p(C_1)$ | "probability of class C₁" | Before measuring, how likely is it to be Fanta? (the prior) |
| $p(C_1\|x)$ | "probability of class C₁ given x" | After measuring x, how likely is it to be Fanta? (the posterior) |

### The Core Idea

You have two types of drinks. Each type produces measurements according to a different mathematical pattern. You see a measurement and want to know: "Which type of drink is this?"

Bayes' rule for classification:

$$p(C_1|x) = \frac{p(x|C_1) \cdot p(C_1)}{p(x)}$$

**In plain English:** "The probability this is Fanta given the measurement = (how likely Fanta produces this measurement) × (how common Fanta is), divided by (overall probability of this measurement)."

### The Evidence $p(x)$

$$p(x) = p(x|C_1) \cdot p(C_1) + p(x|C_2) \cdot p(C_2)$$

**In plain English:** "The overall probability of seeing measurement x = (how likely C₁ produces x × how common C₁ is) + (how likely C₂ produces x × how common C₂ is)."

---

## Part 1: The Three Things You Might Be Asked

### Thing 1: The Discrimination Boundary

This is the measurement value where you're equally unsure about both classes. At this point:

$$p(C_1|x) = p(C_2|x)$$

Which is equivalent to:

$$\frac{p(C_1|x)}{p(C_2|x)} = 1$$

Using Bayes' rule:

$$\frac{p(x|C_1) \cdot p(C_1)}{p(x|C_2) \cdot p(C_2)} = 1$$

**This is the equation you solve to find the boundary.**

### Thing 2: Posterior Class Probability

Given a specific measurement (e.g., $x = 0.5$), compute $p(C_1|x)$:

$$p(C_1|x) = \frac{p(x|C_1) \cdot p(C_1)}{p(x|C_1) \cdot p(C_1) + p(x|C_2) \cdot p(C_2)}$$

### Thing 3: Error Probability

If your decision boundary is at $x = a$, the probability of making a wrong classification is:

$$P(\text{error}) = \int_{\text{decide } C_2} p(x|C_1)p(C_1)dx + \int_{\text{decide } C_1} p(x|C_2)p(C_2)dx$$

**In plain English:** "Error = (probability it's C₁ but we decide C₂) + (probability it's C₂ but we decide C₁)"

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Resit, Question 5 — Orange-ness)

> $p(x|C_1) = 6x(1-x)$ for $0 \leq x \leq 1$
> $p(x|C_2) = 2x$ for $0 \leq x \leq 1$
> $p(C_1) = 0.6$, $p(C_2) = 0.4$

---

### Question 5a: The Discrimination Boundary

> Options:
> - (a) $1 = \frac{p(x|C_1)}{p(x|C_2)} = \frac{6x(1-x)}{2x} \Rightarrow x = 2/3$
> - (b) $\frac{1}{2} = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 8/9$
> - (c) $1 = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 7/9$

### STEP-BY-STEP SOLUTION

**Step 1: Set up the boundary equation**

At the boundary, the two posterior probabilities are equal:

$$\frac{p(C_1|x)}{p(C_2|x)} = 1$$

Using Bayes' rule:

$$\frac{p(x|C_1) \cdot p(C_1)}{p(x|C_2) \cdot p(C_2)} = 1$$

**Step 2: Plug in the formulas**

$$\frac{6x(1-x) \cdot 0.6}{2x \cdot 0.4} = 1$$

**Step 3: Simplify the left side**

First, let's handle the constants:
- Numerator constant: $6 \times 0.6 = 3.6$
- Denominator constant: $2 \times 0.4 = 0.8$

$$\frac{3.6x(1-x)}{0.8x} = 1$$

Cancel the $x$ (assuming $x \neq 0$):

$$\frac{3.6(1-x)}{0.8} = 1$$

Simplify the fraction: $3.6/0.8 = 36/8 = 9/2 = 4.5$

$$\frac{9(1-x)}{2} = 1$$

**Step 4: Solve for x**

$$9(1-x) = 2$$
$$9 - 9x = 2$$
$$-9x = 2 - 9 = -7$$
$$x = \frac{7}{9}$$

**Step 5: Match the answer**

(c) has the correct setup (with "1 =" and the full Bayes' rule) AND gets $x = 7/9$.

(a) is missing the prior probabilities — it only uses the likelihood ratio.
(b) has "1/2 =" which is wrong — the boundary is at ratio = 1.

**Answer: (c)** ✅

---

### Question 5b: Compute $p(C_1|x=0.5)$

> Options:
> - (a) $\frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5|C_2)p(C_2)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{1\cdot\frac{4}{10}}$
> - (b) $\frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{\frac{6}{4}\cdot\frac{6}{10}+1\cdot\frac{4}{10}}$
> - (c) $p(x=0.5|C_1)p(C_1) = \frac{6}{4}\cdot\frac{6}{10}$

### STEP-BY-STEP SOLUTION

**Step 1: Evaluate class-conditionals at x = 0.5**

For $C_1$: $p(x=0.5|C_1) = 6 \times 0.5 \times (1-0.5) = 6 \times 0.5 \times 0.5 = 6/4 = 1.5$

For $C_2$: $p(x=0.5|C_2) = 2 \times 0.5 = 1$

**Step 2: Write Bayes' rule**

$$p(C_1|x=0.5) = \frac{p(x=0.5|C_1) \cdot p(C_1)}{p(x=0.5)}$$

Where:
$$p(x=0.5) = p(x=0.5|C_1) \cdot p(C_1) + p(x=0.5|C_2) \cdot p(C_2)$$

**Step 3: Plug in**

$$p(C_1|x=0.5) = \frac{\frac{6}{4} \cdot \frac{6}{10}}{\frac{6}{4} \cdot \frac{6}{10} + 1 \cdot \frac{4}{10}}$$

**Step 4: Match the answer**

(b) matches exactly — it has the proper evidence in the denominator.

(a) divides one joint by the other — that's a ratio, not a posterior.
(c) is just the joint probability $p(x, C_1)$, not the posterior.

**Answer: (b)** ✅

---

### Question 5c: Learning Class Priors from Data

> Options:
> - (a) Gaussian prior on θ, classify by $\int p(x_\bullet|C_1,\theta)p(\theta|D)d\theta$
> - (b) Assume $p(C_1)=p(C_2)=0.5$ and use Bayes rule
> - (c) Beta prior on θ, classify by $\int p(x_\bullet|C_1)p(C_1|\theta)p(\theta|D)d\theta$

### STEP-BY-STEP SOLUTION

If we don't know the prior probabilities $p(C_1)$ and $p(C_2)$, we need to learn them from labeled data.

We model: $p(C_1|\theta) = \theta$ and $p(C_2|\theta) = 1-\theta$, where $0 \leq \theta \leq 1$.

Since θ is between 0 and 1, the conjugate prior is **Beta** (not Gaussian).

The predictive probability for a new sample $x_\bullet$:

$$p(C_1|x_\bullet, D) \propto \int p(x_\bullet|C_1) \cdot p(C_1|\theta) \cdot p(\theta|D) \, d\theta$$

**Answer: (c)** ✅

---

### EXAM QUESTION 2 (2023, Question 2c — Error Probability)

> Let the discrimination boundary be $x = a$. Work out the probability of wrong classification.
>
> Options:
> - (a) $0.4\int_a^2(4-2x)dx + 0.6\int_1^a 6(1-x)(x-2)dx$
> - (b) $0.6\int_a^2(4-2x)dx + 0.4\int_1^a 6(1-x)(x-2)dx$
> - (c) $a/2$
> - (d) $\int_a^2(4-2x)dx + \int_1^a 6(1-x)(x-2)dx$

> **Context:** $p(x|C_1) = -6(x-1)(x-2) = 6(1-x)(x-2)$ for $1 \leq x \leq 2$
> $p(x|C_2) = 4-2x$ for $1 \leq x \leq 2$
> $p(C_1) = 0.4$, $p(C_2) = 0.6$
> We decide $C_1$ if $x > a$, and $C_2$ if $x < a$.

### STEP-BY-STEP SOLUTION

**Step 1: Understand the decision rule**

- If $x < a$: we decide $C_2$
- If $x > a$: we decide $C_1$

**Step 2: When do we make an error?**

Error occurs in two scenarios:
1. **False $C_2$**: It's actually $C_1$ but we decided $C_2$ (i.e., $x < a$)
2. **False $C_1$**: It's actually $C_2$ but we decided $C_1$ (i.e., $x > a$)

**Step 3: Write the error probability**

$$P(\text{error}) = P(\text{true } C_1, \text{ decide } C_2) + P(\text{true } C_2, \text{ decide } C_1)$$

For the first term (true $C_1$, decide $C_2$ = $x < a$):
$$\int_1^a p(x|C_1) \cdot p(C_1) \, dx = p(C_1) \int_1^a p(x|C_1) \, dx = 0.4 \int_1^a 6(1-x)(x-2) \, dx$$

For the second term (true $C_2$, decide $C_1$ = $x > a$):
$$\int_a^2 p(x|C_2) \cdot p(C_2) \, dx = p(C_2) \int_a^2 p(x|C_2) \, dx = 0.6 \int_a^2 (4-2x) \, dx$$

**Step 4: Combine**

$$P(\text{error}) = 0.4 \int_1^a 6(1-x)(x-2) \, dx + 0.6 \int_a^2 (4-2x) \, dx$$

**Step 5: Match the answer**

(a) matches exactly.

(b) has the priors swapped (0.6 with the first integral, 0.4 with the second).
(c) is way too simple.
(d) is missing the prior probabilities.

**Answer: (a)** ✅

---

## Part 3: Tricks & Shortcuts

### TRICK 1: Boundary Equation Pattern

The correct answer ALWAYS has "1 =" on the left side, not "1/2 =" or anything else.

The correct answer ALWAYS includes BOTH the likelihoods AND the priors.

If an option only has likelihoods (no priors) → wrong.

### TRICK 2: Posterior Always Has Evidence in Denominator

$$p(C_1|x) = \frac{p(x|C_1)p(C_1)}{p(x|C_1)p(C_1) + p(x|C_2)p(C_2)}$$

If the denominator is just one term → wrong.
If there's no denominator → wrong.

### TRICK 3: Error Integral Structure

Each term must have:
- A prior probability ($p(C_1)$ or $p(C_2)$)
- An integral of the class-conditional density
- Integration limits matching the wrong decision region

If an option is missing the priors → wrong.

---

## Part 4: Practice Exercises

### Exercise 1

> $p(x|C_1) = 6x(1-x)$ for $0 \leq x \leq 1$
> $p(x|C_2) = 2x$ for $0 \leq x \leq 1$
> $p(C_1) = 0.6$, $p(C_2) = 0.4$
>
> **Find the discrimination boundary.**
>
> Options:
> - (a) $1 = \frac{p(x|C_1)}{p(x|C_2)} = \frac{6x(1-x)}{2x} \Rightarrow x = 2/3$
> - (b) $\frac{1}{2} = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 8/9$
> - (c) $1 = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 7/9$

---

### Exercise 2

> Same setup. Compute $p(C_1|x=0.5)$.
>
> Options:
> - (a) $\frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5|C_2)p(C_2)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{1\cdot\frac{4}{10}}$
> - (b) $\frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{\frac{6}{4}\cdot\frac{6}{10}+1\cdot\frac{4}{10}}$
> - (c) $p(x=0.5|C_1)p(C_1) = \frac{6}{4}\cdot\frac{6}{10}$

---

### Exercise 3

> Prior probabilities not known, have labeled data $D$. How to classify $x_\bullet$?
>
> Options:
> - (a) Gaussian prior on θ, classify by $\int p(x_\bullet|C_1,\theta)p(\theta|D)d\theta$
> - (b) Assume $p(C_1)=p(C_2)=0.5$
> - (c) Beta prior on θ, classify by $\int p(x_\bullet|C_1)p(C_1|\theta)p(\theta|D)d\theta$

---

### Exercise 4

> $p(x|C_1) = -6(x-1)(x-2)$ for $1 \leq x \leq 2$
> $p(x|C_2) = 4-2x$ for $1 \leq x \leq 2$
> $p(C_1) = 0.4$, $p(C_2) = 0.6$
> Boundary at $x = a$.
>
> **Error probability:**
>
> Options:
> - (a) $0.4\int_{a}^{2}(4-2x)dx + 0.6\int_{1}^{a}6(1-x)(x-2)dx$
> - (b) $0.6\int_{a}^{2}(4-2x)dx + 0.4\int_{1}^{a}6(1-x)(x-2)dx$
> - (c) $a/2$
> - (d) $\int_{a}^{2}(4-2x)dx + \int_{1}^{a}6(1-x)(x-2)dx$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (c) x = 7/9**

Set up: 6x(1-x)·0.6 / (2x·0.4) = 1
Simplify: 3.6x(1-x) / 0.8x = 1
Cancel x: 3.6(1-x)/0.8 = 1
Simplify: 9(1-x)/2 = 1
Solve: 1-x = 2/9, x = 7/9

(a) is wrong because it doesn't include the priors.
(b) is wrong because it has "1/2 =" instead of "1 =".
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (b)**

Full Bayes' rule with proper evidence in denominator:
p(C₁|x) = p(x|C₁)p(C₁) / [p(x|C₁)p(C₁) + p(x|C₂)p(C₂)]

(a) is a ratio of joints, not a posterior.
(c) is just the joint probability, missing the denominator.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (c)**

Class prior θ ∈ [0,1] → Beta is the conjugate prior (not Gaussian).
Predictive: ∫ p(x|C₁)p(C₁|θ)p(θ|D)dθ
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (a)**

Error = p(C₁) × ∫₁ᵃ p(x|C₁)dx + p(C₂) × ∫ₐ² p(x|C₂)dx

Below boundary (x < a): decide C₂, error if true class is C₁
Above boundary (x > a): decide C₁, error if true class is C₂

(b) has the priors swapped.
(d) is missing the priors.
</details>
