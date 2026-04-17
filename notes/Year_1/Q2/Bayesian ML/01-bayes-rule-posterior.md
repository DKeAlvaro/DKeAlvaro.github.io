# Exercise Type 1: Bayes' Rule & Posterior Computation

> **What the exam asks:** You are given a mathematical model with an unknown parameter θ, a formula for how data is generated (the likelihood), and a formula for what you believed before seeing data (the prior). You must compute the updated belief after seeing data (the posterior).

---

## Part 0: What Do All These Symbols Mean?

Before we do ANYTHING, let's learn to read the math.

### The Basic Symbols

| Symbol | What It Looks Like | What It Means |
|--------|--------------------|---------------|
| $p(\cdot)$ | lowercase p with parentheses | "probability of..." — a function that tells you how likely something is |
| $\theta$ | Greek letter "theta" (looks like a circle with a line through it) | The **unknown parameter** we're trying to figure out. Think of it as "the truth we don't know" |
| $x$ | lowercase x | The **data** we observed. A number we actually saw |
| $|$ | vertical bar | "GIVEN" — it means we already know what's on the right side |
| $m_1$ | letter m with subscript 1 | "Model 1" — a particular way the world might work |
| $\int$ | elongated S symbol | **Integral** — means "add up infinitely many tiny pieces" (like a continuous sum) |
| $d\theta$ | letter d with Greek theta | "with respect to θ" — tells the integral what variable we're adding over |
| $\leq$ | less-than-or-equal sign | "less than or equal to" |

### Reading Probability Expressions Out Loud

| Expression | How to Read It | What It Means |
|------------|---------------|---------------|
| $p(x)$ | "probability of x" | How likely is it that we'd observe this data? |
| $p(\theta)$ | "probability of theta" | How likely do we think each possible value of θ is? |
| $p(x\|\theta)$ | "probability of x GIVEN theta" | If we KNEW θ was the truth, how likely would this data be? |
| $p(\theta\|x)$ | "probability of theta GIVEN x" | Now that we've SEEN the data x, how likely is each value of θ? |
| $p(x,\theta)$ | "joint probability of x and theta" | How likely are BOTH x and θ together? |

### The Key Relationship (Product Rule)

$$p(x, \theta) = p(x|\theta) \cdot p(\theta)$$

**In words:** The joint probability (both happening) equals the conditional probability times the marginal probability.

**Analogy:** "The probability that it's raining AND you have an umbrella" = "The probability you have an umbrella GIVEN it's raining" × "The probability it's raining."

---

## Part 1: The Core Concepts — No Math

### What Is Bayesian Inference? (Plain English)

Imagine you're trying to figure out if a coin is fair or biased. You have:

1. **A prior belief** — before flipping, you think the coin is probably fair (maybe slightly biased)
2. **Some data** — you flip the coin 10 times and get 8 heads
3. **A posterior belief** — after seeing the data, you update your belief

**Bayesian inference is just the math of updating beliefs.** That's it.

### The Four Key Words

| Word | Symbol | Plain English |
|------|--------|---------------|
| **Prior** | $p(\theta)$ | What I believed BEFORE seeing any data |
| **Likelihood** | $p(x|\theta)$ | How well does each possible value of θ explain the data I actually saw? |
| **Posterior** | $p(\theta|x)$ | What I believe AFTER seeing the data |
| **Evidence** | $p(x)$ | How likely was this data overall? (just a normalization number) |

### Bayes' Rule — THE Most Important Formula

$$p(\theta|x) = \frac{p(x|\theta) \cdot p(\theta)}{p(x)}$$

**In plain English:**

> My updated belief = (how well θ explains the data) × (my original belief), divided by (a normalizing number)

### The "Proportional To" Shortcut (∝)

You'll see this everywhere:

$$p(\theta|x) \propto p(x|\theta) \cdot p(\theta)$$

The symbol $\propto$ means **"proportional to"**. It means: "the shape of the posterior is given by likelihood × prior, but the height might not add up to 1 yet."

**Why do we use this?** Because the denominator $p(x)$ is just a number that makes everything add up to 1. We can figure it out at the end.

**Analogy:** Imagine you're baking a cake and the recipe says "2 parts flour, 1 part sugar." The proportions matter. Then at the end you scale it up or down to feed the right number of people. That scaling is the denominator.

---

## Part 2: The Beta Function Trick (You NEED This)

### What Is an Integral?

An integral $\int_a^b f(\theta) \, d\theta$ means "add up the area under the curve of $f(\theta)$ from θ = a to θ = b."

In our case, we need to compute integrals like:

$$\int_0^1 \theta^3(1-\theta)^2 \, d\theta$$

This looks terrifying. But there's a **trick**.

### The Beta Function Formula (MEMORIZE THIS)

For ANY integral of this form:

$$\int_0^1 \theta^p (1-\theta)^q \, d\theta = \frac{p! \cdot q!}{(p+q+1)!}$$

Where $p$ and $q$ are the **powers** (exponents) of θ and $(1-\theta)$.

### What Is a Factorial?

The notation $n!$ (read "n factorial") means multiply all numbers from 1 to n:

| Factorial | Calculation | Value |
|-----------|-------------|-------|
| $1!$ | $1$ | $1$ |
| $2!$ | $2 \times 1$ | $2$ |
| $3!$ | $3 \times 2 \times 1$ | $6$ |
| $4!$ | $4 \times 3 \times 2 \times 1$ | $24$ |
| $5!$ | $5 \times 4 \times 3 \times 2 \times 1$ | $120$ |
| $6!$ | $720$ | $720$ |
| $7!$ | $5040$ | $5040$ |
| $8!$ | $40320$ | $40320$ |

### Worked Examples of the Beta Function

**Example 1:** $\int_0^1 \theta^2(1-\theta)^1 \, d\theta$

- $p = 2$ (power of θ), $q = 1$ (power of $1-\theta$)
- Answer: $\frac{2! \cdot 1!}{(2+1+1)!} = \frac{2 \cdot 1}{4!} = \frac{2}{24} = \frac{1}{12}$

**Example 2:** $\int_0^1 \theta^5(1-\theta)^2 \, d\theta$

- $p = 5$, $q = 2$
- Answer: $\frac{5! \cdot 2!}{(5+2+1)!} = \frac{120 \cdot 2}{8!} = \frac{240}{40320} = \frac{1}{168}$

**Example 3:** $\int_0^1 \theta^1(1-\theta)^1 \, d\theta$

- $p = 1$, $q = 1$
- Answer: $\frac{1! \cdot 1!}{(1+1+1)!} = \frac{1 \cdot 1}{3!} = \frac{1}{6}$

---

## Part 3: FULL Walkthrough of a Real Exam Question

### THE EXAM QUESTION (2021-Part-B, Question 2a)

> A model $m_1$ has a single parameter $\theta$ where $0 \leq \theta \leq 1$ (θ is a number between 0 and 1).
>
> The **sampling distribution** (also called likelihood) is:
> $$p(x|\theta, m_1) = (1-\theta)\theta^x$$
>
> The **prior** is:
> $$p(\theta|m_1) = 6\theta(1-\theta)$$
>
> We observe data $x = 4$.
>
> **Determine the posterior** $p(\theta|x=4, m_1)$.
>
> Options:
> - (a) $6\theta^4(1-\theta)^2$
> - (b) $\frac{\int_0^1 \theta^5(1-\theta)^2 \, d\theta}{\theta^5(1-\theta)^2}$
> - (c) $\frac{\theta^5(1-\theta)^2}{\int_0^1 \theta^5(1-\theta)^2 \, d\theta}$

---

### STEP 1: Understand What the Question Is Asking

We need to find $p(\theta|x=4, m_1)$ — our updated belief about θ after seeing $x = 4$.

By Bayes' rule:

$$p(\theta|x=4, m_1) = \frac{p(x=4|\theta, m_1) \cdot p(\theta|m_1)}{p(x=4|m_1)}$$

The numerator is **likelihood × prior**. The denominator is the **evidence** (a number that normalizes things).

---

### STEP 2: Evaluate the Likelihood at x = 4

The likelihood formula is: $p(x|\theta, m_1) = (1-\theta)\theta^x$

We replace $x$ with $4$:

$$p(x=4|\theta, m_1) = (1-\theta)\theta^4$$

**What this means:** For each possible value of θ, this formula tells us how well it explains the observation $x = 4$.

---

### STEP 3: Write Down the Prior

$$p(\theta|m_1) = 6\theta(1-\theta)$$

**What this means:** Before seeing any data, this is how plausible we think each value of θ is.

- When θ = 0: prior = $6 \times 0 \times 1 = 0$ (we don't believe θ = 0 at all)
- When θ = 0.5: prior = $6 \times 0.5 \times 0.5 = 1.5$ (quite plausible)
- When θ = 1: prior = $6 \times 1 \times 0 = 0$ (we don't believe θ = 1 at all)

So the prior says θ is most likely somewhere in the middle.

---

### STEP 4: Multiply Likelihood × Prior (The Numerator)

$$\text{Numerator} = (1-\theta)\theta^4 \times 6\theta(1-\theta)$$

Now let's carefully multiply these together:

1. The constant: $6$
2. Powers of θ: $\theta^4 \times \theta^1 = \theta^{4+1} = \theta^5$ (when you multiply, add exponents)
3. Powers of $(1-\theta)$: $(1-\theta)^1 \times (1-\theta)^1 = (1-\theta)^{1+1} = (1-\theta)^2$

$$\text{Numerator} = 6\theta^5(1-\theta)^2$$

---

### STEP 5: Compute the Evidence (The Denominator)

The evidence is the integral of the numerator over all possible values of θ:

$$p(x=4|m_1) = \int_0^1 6\theta^5(1-\theta)^2 \, d\theta = 6 \int_0^1 \theta^5(1-\theta)^2 \, d\theta$$

We pull the 6 outside the integral because constants can be moved out.

**IMPORTANT:** We don't need to evaluate this integral yet. We just need to write it down for now.

---

### STEP 6: Write the Full Posterior

$$p(\theta|x=4, m_1) = \frac{6\theta^5(1-\theta)^2}{6 \int_0^1 \theta^5(1-\theta)^2 \, d\theta}$$

The 6 cancels:

$$p(\theta|x=4, m_1) = \frac{\theta^5(1-\theta)^2}{\int_0^1 \theta^5(1-\theta)^2 \, d\theta}$$

---

### STEP 7: Match the Answer

- (a) $6\theta^4(1-\theta)^2$ — **Wrong.** Power of θ is 4, should be 5. Also not normalized.
- (b) $\frac{\int \cdots}{\theta^5(1-\theta)^2}$ — **Wrong.** Upside down! The integral is in the numerator.
- (c) $\frac{\theta^5(1-\theta)^2}{\int_0^1 \theta^5(1-\theta)^2 \, d\theta}$ — **Correct!** ✅

**Answer: (c)**

---

## Part 4: Tricks & Shortcuts

### TRICK 1: The Power-Adding Rule

When multiplying terms with the same base, ADD the exponents:

- $\theta^4 \times \theta^1 = \theta^5$
- $(1-\theta)^1 \times (1-\theta)^1 = (1-\theta)^2$

So if the prior has $\theta^a(1-\theta)^b$ and the likelihood has $\theta^c(1-\theta)^d$, the product has $\theta^{a+c}(1-\theta)^{b+d}$.

### TRICK 2: Spot the Correct Answer Instantly

The posterior **always** looks like:

$$\frac{\text{function}}{\int \text{same function} \, d\theta}$$

If the integral is in the numerator → wrong.
If the function in the numerator doesn't match the one in the integral → wrong.

### TRICK 3: The Constant Cancels

If both the numerator and denominator have the same constant (like 6), it cancels. The final answer won't have it.

### TRICK 4: Common Wrong Answers to Watch For

| What They Do Wrong | What It Looks Like | Why It's Wrong |
|--------------------|--------------------|----------------|
| Forget to multiply by the prior | $\theta^4(1-\theta)$ instead of $\theta^5(1-\theta)^2$ | They only used the likelihood |
| Wrong exponent arithmetic | $\theta^4$ instead of $\theta^5$ | They didn't add the exponents from prior |
| Upside down | integral on top, function on bottom | Bayes' rule is likelihood×prior / evidence, not the reverse |
| Missing normalization | Just $6\theta^5(1-\theta)^2$ | This doesn't integrate to 1, so it's not a valid probability |

---

## Part 5: Practice Exercises

### Exercise 1 (2021-Part-B, Question 2b)

> Same model: $p(x|\theta, m_1) = (1-\theta)\theta^x$, $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Determine the evidence** $p(x=4|m_1)$.
>
> Options:
> - (a) $\int_0^1 \frac{(1-\theta)\theta^4}{6\theta(1-\theta)} \, d\theta$
> - (b) $\int_0^1 (1-\theta)\theta^4 \, d\theta$
> - (c) $\int_0^1 6\theta^5(1-\theta)^2 \, d\theta$
> - (d) $\int_0^1 \frac{6\theta(1-\theta)}{(1-\theta)\theta^4} \, d\theta$

**Hint:** The evidence = ∫ likelihood × prior dθ. What did we compute in Step 5 above?

---

### Exercise 2 (2021-Part-B, Question 2c)

> Model $m_2$: likelihood $p(x|\theta, m_2) = (1-\theta)\theta^x$, prior $p(\theta|m_2) = 2\theta$
>
> **Determine** $p(x=4|m_2)$.
>
> Options:
> - (a) $\int_0^1 2(1-\theta)\theta^5 \, d\theta$
> - (b) $\frac{1}{\int_0^1 2(1-\theta)\theta^5} \, d\theta$
> - (c/d) $\int_0^1 \frac{(1-\theta)\theta^4}{2\theta} \, d\theta$

**Hint:** 
- Step 1: Likelihood at x=4 → $(1-\theta)\theta^4$
- Step 2: Multiply by prior → $(1-\theta)\theta^4 \times 2\theta$
- Step 3: Add exponents → $2\theta^5(1-\theta)$
- Step 4: Integrate

---

### Exercise 3 (2022, Question 4a)

> Model $m_1$: likelihood $p(x|\theta, m_1) = \theta^x(1-\theta)^{1-x}$, prior $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Determine** $p(x=1|m_1)$ (the evidence for x=1).
>
> Options:
> - (a) $2/3$
> - (b) $1/6$
> - (c) $1/3$
> - (d) $1/2$

**Hint:**
- Step 1: Plug x=1 into likelihood → $\theta^1(1-\theta)^0 = \theta$ (anything to the power 0 = 1)
- Step 2: Multiply by prior → $\theta \times 6\theta(1-\theta) = 6\theta^2(1-\theta)$
- Step 3: Integrate → use Beta function: p=2, q=1

---

### Exercise 4 (2022, Question 4b)

> Same model as Exercise 3. **Determine the posterior** $p(\theta|x=1, m_1)$.
>
> Options:
> - (a) $6\frac{\theta^2}{1-\theta}$
> - (b) $12\theta^2(1-\theta)$
> - (c) $6\theta^2(1-\theta)$
> - (d) $12\frac{\theta^2}{1-\theta}$

**Hint:**
- Numerator = likelihood × prior = $6\theta^2(1-\theta)$
- Evidence = $\int_0^1 6\theta^2(1-\theta) d\theta = 6 \times \frac{2! \cdot 1!}{4!} = 6 \times \frac{2}{24} = 1/2$
- Posterior = numerator / evidence = $6\theta^2(1-\theta) / (1/2)$

---

### Exercise 5 (2022, Question 4a)

> Model $m_1$: $p(x|\theta, m_1) = \theta^x(1-\theta)^{1-x}$, $p(\theta|m_1) = 6\theta(1-\theta)$
>
> **Work out** $p(x=1|m_1)$.
>
> Options:
> - (a) $1/4$
> - (b) $1/2$
> - (c) $\theta/(1+\theta)$
> - (d) $3/4$

**Hint:** This is the SAME model as Exercise 3. Same answer.

---

### Exercise 6 (2022, Question 4b)

> Same model. **Determine** $p(\theta|x=1, m_1)$.
>
> Options:
> - (a) $6\theta^2(1-\theta)$
> - (b) $12\theta(1-\theta)^2$
> - (c) $12\theta^2(1-\theta)$
> - (d) $6\theta(1-\theta)^2$

**Hint:** Same as Exercise 4.

---

### Exercise 7 (2022, Question 4c)

> Model $m_2$: $p(x|\theta, m_2) = (1-\theta)^x\theta^{1-x}$, $p(\theta|m_2) = 2\theta$
>
> **Determine** $p(x=1|m_2)$.
>
> Options:
> - (a) $2/3$
> - (b) $1/4$
> - (c) $1/2$
> - (d) $1/3$

**Hint:** 
- **WARNING:** The likelihood is $(1-\theta)^x\theta^{1-x}$, which is DIFFERENT from before!
- Step 1: Plug x=1 → $(1-\theta)^1\theta^0 = 1-\theta$
- Step 2: Multiply by prior → $(1-\theta) \times 2\theta = 2\theta(1-\theta)$
- Step 3: Integrate → p=1, q=1

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (c)** $\int_0^1 6\theta^5(1-\theta)^2 \, d\theta$

The evidence is always ∫ likelihood × prior dθ.

From our work above: likelihood × prior = $6\theta^5(1-\theta)^2$.

Option (a) divides likelihood by prior — wrong operation.
Option (b) is missing the prior entirely.
Option (d) divides prior by likelihood — wrong.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (a)** $\int_0^1 2(1-\theta)\theta^5 \, d\theta$

Step-by-step:
1. Likelihood at x=4: $(1-\theta)\theta^4$
2. Prior: $2\theta$
3. Product: $(1-\theta)\theta^4 \times 2\theta = 2\theta^5(1-\theta)$
4. Evidence = $\int_0^1 2\theta^5(1-\theta) d\theta$

Option (b) has the integral upside down.
Option (c/d) divides instead of multiplying.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (d) 1/2**

Step-by-step:
1. Likelihood at x=1: $\theta^1(1-\theta)^{1-1} = \theta^1(1-\theta)^0 = \theta \times 1 = \theta$
2. Prior: $6\theta(1-\theta)$
3. Product: $\theta \times 6\theta(1-\theta) = 6\theta^2(1-\theta)$
4. Integrate using Beta function: p=2, q=1
   $$\int_0^1 6\theta^2(1-\theta) d\theta = 6 \cdot \frac{2! \cdot 1!}{(2+1+1)!} = 6 \cdot \frac{2}{24} = 6 \cdot \frac{1}{12} = \frac{1}{2}$$
</details>

<details>
<summary>Exercise 4</summary>

**Answer: (b) $12\theta^2(1-\theta)$**

Step-by-step:
1. Numerator = $6\theta^2(1-\theta)$ (from Exercise 3, Step 3)
2. Evidence = $1/2$ (from Exercise 3, Step 4)
3. Posterior = $\frac{6\theta^2(1-\theta)}{1/2} = 6\theta^2(1-\theta) \times 2 = 12\theta^2(1-\theta)$

Option (a) has $(1-\theta)$ in the denominator — wrong.
Option (c) didn't divide by the evidence (forgot normalization).
Option (d) has the wrong powers.
</details>

<details>
<summary>Exercise 5</summary>

**Answer: (b) 1/2**

Same calculation as Exercise 3. Same model, same x=1.
</details>

<details>
<summary>Exercise 6</summary>

**Answer: (c) $12\theta^2(1-\theta)$**

Same calculation as Exercise 4.
</details>

<details>
<summary>Exercise 7</summary>

**Answer: (d) 1/3**

Step-by-step:
1. Likelihood at x=1: $(1-\theta)^1\theta^{1-1} = (1-\theta)\theta^0 = (1-\theta) \times 1 = 1-\theta$
2. Prior: $2\theta$
3. Product: $(1-\theta) \times 2\theta = 2\theta(1-\theta) = 2\theta^1(1-\theta)^1$
4. Integrate using Beta function: p=1, q=1
   $$\int_0^1 2\theta(1-\theta) d\theta = 2 \cdot \frac{1! \cdot 1!}{(1+1+1)!} = 2 \cdot \frac{1}{6} = \frac{1}{3}$$
</details>
