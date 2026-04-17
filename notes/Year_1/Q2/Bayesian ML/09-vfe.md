# Exercise Type 9: Variational Free Energy (VFE)

> **What the exam asks:** You are given the VFE functional formula and must identify its key properties: whether it's an upper or lower bound on the evidence, when equality holds, and why VFE minimization approximates Bayesian inference.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $F[q]$ | "Free Energy of q" | A number that depends on our choice of the distribution q — we want to minimize this |
| $q(z)$ | "q of z" | Our **approximate** distribution for the hidden variables z — we get to choose this |
| $p(x, z)$ | "p of x and z" | The **true** joint distribution of data x and hidden variables z (our model) |
| $p(z\|x)$ | "p of z given x" | The **true posterior** — what we'd ideally want to compute but can't |
| $-\log p(x)$ | "negative log evidence" | How surprised we are by the data (lower = better model) |
| $\int$ | Integral sign | "Add up continuously" — integrate over all values of z |
| $\log$ | Logarithm (natural log) | The inverse of exponentiation — turns products into sums |
| $\geq$ | Greater than or equal | "At least as big as" |

### What Is Variational Free Energy? (Plain English)

Imagine you want to compute the posterior $p(z|x)$ — your belief about hidden things z after seeing data x. But the math is too hard (the integral in the denominator is impossible to compute).

**The variational approach says:** "Instead of computing the exact posterior, let me find a simple distribution $q(z)$ that's CLOSE to the true posterior."

The VFE $F[q]$ measures how good our choice of $q(z)$ is. We want to minimize it.

### The VFE Formula

$$F[q] = \int q(z) \log \frac{q(z)}{p(x, z)} \, dz$$

**In plain English:** "For each possible value of z, compute how much q(z) differs from p(x,z), weight by q(z), and add them all up."

---

## Part 1: The Three Key Properties (MEMORIZE)

### Property 1: VFE Is an UPPER BOUND

$$F[q] \geq -\log p(x) \quad \text{for ANY choice of } q(z)$$

**In plain English:** "The Free Energy is ALWAYS at least as big as the negative log evidence. No matter what q you pick, F[q] will be ≥ $-\log p(x)$."

**Think of it like this:** $-\log p(x)$ is the ground floor. F[q] is always at or above it. You can never go below.

### Property 2: Equality at the True Posterior

$$F[q] = -\log p(x) \quad \text{when } q(z) = p(z|x)$$

**In plain English:** "If you happen to choose q(z) equal to the TRUE posterior, then F[q] equals the negative log evidence exactly."

**This is the BEST you can do.** At this point, your approximation is perfect.

### Property 3: Minimizing VFE Does Two Things

When you minimize F[q]:
1. It makes q(z) closer to the true posterior $p(z|x)$
2. It gives you a better estimate of the evidence $p(x)$

**This is why VFE approximates Bayesian inference.**

---

## Part 2: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Resit, Question 4e)

> $F[q] = \int q(z) \log \frac{q(z)}{p(x,z)} dz$
>
> Which statement is true?
>
> Options:
> - (a) $F[q] = -\log p(x)$ if $q(z) = 0$
> - (b) $F[q] \leq -\log p(x)$ for any choice of $q(z)$
> - (c) $F[q] \geq -\log p(x)$ for any choice of $q(z)$
> - (d) $F[q] = -\log p(x)$ if $q(z) = p(z)$

### STEP-BY-STEP SOLUTION

**Step 1: Recall the key properties**

- VFE is always ≥ negative log evidence (upper bound)
- Equality holds when q(z) = p(z|x) (the true posterior)

**Step 2: Evaluate each option**

**(a)** $q(z) = 0$ is NOT a valid probability distribution (it must integrate to 1). ELIMINATE.

**(b)** Says F[q] ≤ $-\log p(x)$ — this is the WRONG direction. VFE is an UPPER bound, not lower. ELIMINATE.

**(c)** Says F[q] ≥ $-\log p(x)$ for any q(z). This is correct — VFE is always an upper bound. ✓

**(d)** Says equality when q(z) = p(z) (the PRIOR). This is wrong — equality is when q(z) = p(z|x) (the POSTERIOR). ELIMINATE.

**Answer: (c)** ✅

---

### EXAM QUESTION 2 (2023, Question 4f)

> Why can VFE minimization be interpreted as an approximation to Bayesian inference?
>
> Options:
> - (a) VFE minimization is a model for Bayesian inference plus Gaussian noise
> - (b) VFE minimizes KL-divergence to evidence, and VFE is upper bound on posterior
> - (c) VFE minimizes evidence by optimizing the variational posterior
> - (d) VFE minimizes KL-divergence between variational and true posterior, and VFE is upper bound on negative log evidence

### STEP-BY-STEP SOLUTION

**Step 1: Recall what VFE does**

Minimizing F[q] is equivalent to minimizing $KL(q(z) || p(z|x))$ — the KL divergence (a measure of difference) between our approximation and the true posterior.

And F[q] ≥ $-\log p(x)$ always.

**Step 2: Evaluate each option**

**(a)** "Gaussian noise" — this is nonsense in this context. ELIMINATE.

**(b)** "KL-divergence to evidence" — we minimize KL to the POSTERIOR, not the evidence. "Upper bound on posterior" — wrong, it's an upper bound on NEGATIVE LOG EVIDENCE. ELIMINATE.

**(c)** "VFE minimizes evidence" — no, we don't want to minimize evidence. We want to approximate the posterior. ELIMINATE.

**(d)** "KL-divergence between variational and true posterior" — correct. "Upper bound to negative log evidence" — correct. ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 3 (2021-Part-B, Question 1b)

> Which is NOT a property of the Variational Bayesian approach?
>
> Options:
> - (a) Transfers Bayesian ML to an optimization problem
> - (b) VB finds posteriors by maximizing Bayesian evidence
> - (c) VFE minimization gives posterior AND evidence
> - (d) Global VFE minimization realizes Bayes rule

### STEP-BY-STEP SOLUTION

**Step 1: Evaluate each option**

**(a)** True — VB turns Bayesian inference (which requires hard integrals) into an optimization problem (find the q that minimizes F[q]). This IS a property.

**(b)** "Maximizing Bayesian evidence" — this is NOT quite right. VB MINIMIZES the VFE (which is an upper bound on NEGATIVE log evidence). It doesn't directly "maximize evidence." This is the FALSE statement.

**(c)** True — minimizing VFE gives you both an approximate posterior q(z) and an estimate of the evidence through F[q].

**(d)** True — if you could globally minimize F[q], you'd find q(z) = p(z|x), which is exactly Bayes' rule.

**Answer: (b)** ✅ (this is NOT a property)

---

## Part 3: Tricks & Shortcuts

### TRICK 1: VFE Is Always ≥ Negative Log Evidence

Think: "VFE is an Upper bound" → remember the letter U → Upper.

If an option says ≤ → wrong.

### TRICK 2: Equality at the Posterior, Not the Prior

$F[q] = -\log p(x)$ when q(z) = p(z|x), NOT when q(z) = p(z).

If an option says "equality when q = prior" → wrong.

### TRICK 3: VFE Minimizes KL to the Posterior

Not to the evidence, not to the prior — to the TRUE POSTERIOR.

---

## Part 4: Practice Exercises

### Exercise 1

> $F[q] = \int q(z) \log \frac{q(z)}{p(x,z)} dz$. Which is true?
>
> Options:
> - (a) $F[q] = -\log p(x)$ if $q(z) = 0$
> - (b) $F[q] \leq -\log p(x)$ for any $q(z)$
> - (c) $F[q] \geq -\log p(x)$ for any $q(z)$
> - (d) $F[q] = -\log p(x)$ if $q(z) = p(z)$

---

### Exercise 2

> Why does VFE minimization approximate Bayesian inference?
>
> Options:
> - (a) It's Bayesian inference plus Gaussian noise
> - (b) It minimizes KL-divergence to evidence
> - (c) It minimizes evidence
> - (d) It minimizes KL-divergence between q(z) and p(z|x), and F[q] is upper bound on negative log evidence

---

### Exercise 3

> Which is NOT a property of VB?
>
> Options:
> - (a) Transfers Bayesian ML to optimization
> - (b) VB finds posteriors by maximizing evidence
> - (c) VFE gives posterior and evidence
> - (d) Global VFE minimization realizes Bayes rule

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (c)**

VFE is always ≥ negative log evidence (upper bound).

(a) q(z)=0 is not valid.
(b) Wrong direction (≤ should be ≥).
(d) Equality is at q(z)=p(z|x), not p(z).
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (d)**

VFE minimization = minimize KL(q||p(z|x)) + F[q] ≥ -log p(x).

(a) is nonsense.
(b) KL is to posterior, not evidence.
(c) We don't minimize evidence.
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b)**

VB MINIMIZES VFE (upper bound on negative log evidence), it doesn't "maximize evidence" directly. This statement is imprecise/false.
</details>
