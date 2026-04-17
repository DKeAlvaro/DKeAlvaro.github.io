# Exercise Type 7: Ball/Box Conditional Probability

> **What the exam asks:** You have boxes/bags with different objects (apples, oranges, red balls, green balls). You pick a box, draw an object, and must compute probabilities. Sometimes objects are NOT returned (without replacement), which changes the counts.

---

## Part 0: What Do All These Symbols Mean?

### The Key Notation

| Symbol | How to Read It | What It Means |
|--------|---------------|---------------|
| $P(A)$ | "probability of A" | How likely event A is |
| $P(A\|B)$ | "probability of A given B" | How likely A is IF we know B already happened |
| $P(A, B)$ | "probability of A and B" | How likely both A and B happen together |
| $P(B_1)$ | "probability of box 1" | How likely we pick box 1 |
| $P(\text{apple}\|B_1)$ | "probability of apple given box 1" | If we picked box 1, what's the chance we draw an apple? |
| $P(B_1\|\text{apple})$ | "probability of box 1 given apple" | We drew an apple — what's the chance it came from box 1? |

### The Core Concepts

**1. The Product Rule:**

$$P(A, B) = P(A|B) \cdot P(B)$$

**In plain English:** "Probability of both A and B happening = (probability of A if B happened) × (probability of B)"

**Example:** "Probability of picking box 1 AND drawing an apple = (probability of apple if box 1) × (probability of box 1)"

**2. Law of Total Probability:**

$$P(A) = P(A|B_1) \cdot P(B_1) + P(A|B_2) \cdot P(B_2)$$

**In plain English:** "Total probability of A = (probability of A in scenario 1 × probability of scenario 1) + (probability of A in scenario 2 × probability of scenario 2)"

**3. Bayes' Rule:**

$$P(B_1|A) = \frac{P(A|B_1) \cdot P(B_1)}{P(A)}$$

**In plain English:** "Probability that scenario 1 was the cause, given we saw A = (how likely scenario 1 produces A × how likely scenario 1 is) ÷ (total probability of A)"

---

## Part 1: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Resit, Questions 1a-1b)

> Box 1: 4 apples, 8 oranges (12 total)
> Box 2: 10 apples, 2 oranges (12 total)
> Boxes chosen with equal probability (50/50)
> One draw.

---

### Question 1a: What is the probability of choosing an apple?

### STEP-BY-STEP SOLUTION

**Step 1: Understand what we're computing**

We want $P(\text{apple})$. We don't know which box we'll pick, so we need to consider both possibilities.

**Step 2: Use the Law of Total Probability**

$$P(\text{apple}) = P(\text{apple}|B_1) \cdot P(B_1) + P(\text{apple}|B_2) \cdot P(B_2)$$

**Step 3: Fill in each piece**

- $P(B_1) = 1/2$ (equal probability)
- $P(B_2) = 1/2$ (equal probability)
- $P(\text{apple}|B_1) = 4/12$ (4 apples out of 12 total in box 1)
- $P(\text{apple}|B_2) = 10/12$ (10 apples out of 12 total in box 2)

**Step 4: Compute**

$$P(\text{apple}) = \frac{4}{12} \cdot \frac{1}{2} + \frac{10}{12} \cdot \frac{1}{2} = \frac{4}{24} + \frac{10}{24} = \frac{14}{24} = \frac{7}{12}$$

**Answer: 7/12** ✅

---

### Question 1b: If an apple is chosen, what is the probability it came from Box 1?

### STEP-BY-STEP SOLUTION

**Step 1: Understand what we're computing**

We want $P(B_1|\text{apple})$. This is the REVERSE of what we computed before — now we KNOW we got an apple, and we want to know which box it likely came from.

This is Bayes' rule!

**Step 2: Write Bayes' rule**

$$P(B_1|\text{apple}) = \frac{P(\text{apple}|B_1) \cdot P(B_1)}{P(\text{apple})}$$

**Step 3: Plug in the numbers**

- $P(\text{apple}|B_1) = 4/12$
- $P(B_1) = 1/2$
- $P(\text{apple}) = 7/12$ (from part a)

$$P(B_1|\text{apple}) = \frac{\frac{4}{12} \cdot \frac{1}{2}}{\frac{7}{12}} = \frac{4/24}{7/12}$$

**Step 4: Simplify the fraction**

$$\frac{4/24}{7/12} = \frac{4}{24} \cdot \frac{12}{7} = \frac{4 \cdot 12}{24 \cdot 7} = \frac{48}{168} = \frac{4}{14} = \frac{2}{7}$$

**Note:** The exam listed 1/3 as an option, but the correct answer depends on the exact numbers. The method is what matters.

---

### EXAM QUESTION 2 (2023, Question 4d — Without Replacement)

> A dark bag contains 5 red balls and 7 green balls (12 total).
> Balls are NOT returned after each draw.
> You know that on the LAST draw, the ball was green.
> What is the probability of drawing a red ball on the FIRST draw?
>
> Options: (a) $4/11$, (b) $5/11$, (c) $5/12$, (d) $6/11$

### STEP-BY-STEP SOLUTION

**Step 1: Understand the scenario**

We draw balls one at a time without putting them back. We're told the LAST ball was green. Given this information, what's the probability the FIRST ball was red?

We want: $P(R_1 | G_{\text{last}})$

**Step 2: Write Bayes' rule**

$$P(R_1 | G_{\text{last}}) = \frac{P(G_{\text{last}} | R_1) \cdot P(R_1)}{P(G_{\text{last}})}$$

**Step 3: Compute $P(R_1)$**

Before any draws, the bag has 5 red and 7 green:

$$P(R_1) = \frac{5}{12}$$

**Step 4: Compute $P(G_{\text{last}} | R_1)$**

If the first ball was RED, the remaining balls are:
- 4 red, 7 green (11 total)

So the probability the last ball is green (from the remaining 11):

$$P(G_{\text{last}} | R_1) = \frac{7}{11}$$

**Step 5: Compute $P(G_{\text{last}})$**

Using the Law of Total Probability:

$$P(G_{\text{last}}) = P(G_{\text{last}} | R_1) \cdot P(R_1) + P(G_{\text{last}} | G_1) \cdot P(G_1)$$

- $P(R_1) = 5/12$
- $P(G_1) = 7/12$
- $P(G_{\text{last}} | R_1) = 7/11$ (if first was red: 4 red, 7 green remain)
- $P(G_{\text{last}} | G_1) = 6/11$ (if first was green: 5 red, 6 green remain)

$$P(G_{\text{last}}) = \frac{7}{11} \cdot \frac{5}{12} + \frac{6}{11} \cdot \frac{7}{12} = \frac{35}{132} + \frac{42}{132} = \frac{77}{132} = \frac{7}{12}$$

**Important insight:** By symmetry, $P(G_{\text{last}}) = P(G_1) = 7/12$. The marginal probability of green is the same regardless of position!

**Step 6: Apply Bayes' rule**

$$P(R_1 | G_{\text{last}}) = \frac{\frac{7}{11} \cdot \frac{5}{12}}{\frac{7}{12}} = \frac{7}{11} \cdot \frac{5}{12} \cdot \frac{12}{7} = \frac{5}{11}$$

The $7/12$ cancels with $12/7$, and the 7s cancel.

**Answer: (b) 5/11** ✅

---

## Part 2: Tricks & Shortcuts

### TRICK 1: Symmetry for Marginal Probabilities

$P(G_{\text{last}}) = P(G_1)$ when you don't know intermediate draws. The marginal probability doesn't depend on position.

### TRICK 2: "Without Replacement" Means Update Counts

After drawing a red ball:
- Red count decreases by 1
- Total count decreases by 1

### TRICK 3: Future Conditions Past

$P(\text{first} | \text{last})$ uses Bayes' rule with the future as "evidence."

### TRICK 4: Tree Diagram Helps

Draw all possible sequences as branches. Multiply along branches, add across paths.

---

## Part 3: Practice Exercises

### Exercise 1

> Box 1: 4 apples, 8 oranges. Box 2: 10 apples, 2 oranges. Boxes chosen with equal probability. One draw.
>
> **What is the probability of choosing an apple?**

---

### Exercise 2

> Same setup. **If an apple is chosen, what is the probability it came from Box 1?**

---

### Exercise 3

> A dark bag contains 5 red balls and 7 green ones. Balls are not returned. If you know that on the last draw the ball was green, what is the probability of drawing a red ball on the first draw?
>
> Options:
> - (a) $4/11$
> - (b) $5/11$
> - (c) $5/12$
> - (d) $6/11$

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: 7/12**

P(apple) = P(apple|B₁)P(B₁) + P(apple|B₂)P(B₂)
= (4/12)(1/2) + (10/12)(1/2)
= 4/24 + 10/24
= 14/24
= 7/12
</details>

<details>
<summary>Exercise 2</summary>

**Answer: 2/7**

P(B₁|apple) = P(apple|B₁)P(B₁) / P(apple)
= (4/12 × 1/2) / (7/12)
= (4/24) / (7/12)
= 4/24 × 12/7
= 48/168
= 2/7
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b) 5/11**

P(R₁|G_last) = P(G_last|R₁)P(R₁) / P(G_last)
= (7/11 × 5/12) / (7/12)
= 5/11
</details>
