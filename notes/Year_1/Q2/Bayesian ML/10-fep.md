# Exercise Type 10: Free Energy Principle (FEP) Comprehension

> **What the exam asks:** You are given statements about the Free Energy Principle and Active Inference, and must identify which ones are consistent with the theory.

---

## Part 0: What Is the Free Energy Principle? (Plain English)

### The Core Idea

The Free Energy Principle (FEP) is a theory about how living things (especially brains) work. It says:

**Living things try to minimize "surprise" — the difference between what they expect to sense and what they actually sense.**

They do this in TWO ways:
1. **Perception:** Update your beliefs about the world to better match your sensations
2. **Action:** Change your sensations by acting on the world

### Key Vocabulary

| Term | Plain English Meaning |
|------|----------------------|
| **Generative model** | Your internal model of how the world works — it predicts what you should sense |
| **Sensory inputs** | What you actually see, hear, feel, etc. |
| **Free Energy** | A measure of how wrong your predictions are (like "surprise") |
| **Perception** | Updating your beliefs to minimize Free Energy |
| **Action (Active Inference)** | Choosing actions that make your predictions come true |
| **Expected Free Energy** | How much surprise you EXPECT to have in the future if you take a certain action |
| **Target priors** | Your preferred/desired future states — what you WANT to happen |

### The Key Principles

1. **Agents have a generative model** — an internal model of how sensory data is generated
2. **Perception minimizes Free Energy** — you update beliefs to match observations
3. **Actions minimize Expected Free Energy** — you choose actions that reduce expected future surprise
4. **Goals are encoded as target priors** — you specify what future states you want, then act to make predictions match those targets

---

## Part 1: FULL Walkthrough of Real Exam Questions

### EXAM QUESTION 1 (2021-Part-B, Question 1a)

> The Free Energy Principle is about biological self-organization. Which statement is most consistent with FEP?
>
> Options:
> - (a) Our actions aim to reduce the complexity of our model of the environment
> - (b) Learning maximizes variational free energy
> - (c) Perception aims to reduce the complexity of our model of the environment
> - (d) We act to fulfil our predictions about future sensory inputs

### STEP-BY-STEP SOLUTION

**(a)** "Reduce complexity of model" — FEP is about minimizing surprise/free energy, not specifically about model complexity. ELIMINATE.

**(b)** "Maximizes variational free energy" — WRONG direction. We MINIMIZE free energy, not maximize. ELIMINATE.

**(c)** "Reduce complexity" — again, not the core idea. Perception minimizes free energy by updating beliefs, not specifically "complexity." ELIMINATE.

**(d)** "We act to fulfil our predictions" — YES! In Active Inference, we act to make our sensory predictions match what we want. Our predictions become self-fulfilling prophecies through action. ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 2 (2021-Part-B, Question 1d)

> How to equip an agent with goal-driven behavior in FEP?
>
> Options:
> - (a) Specify a cost function and minimize costs
> - (b) Extend the generative model with target priors for future observations. Then minimize Free Energy.
> - (c) Specify a cost function of actions and minimize
> - (d) Extend with a posterior distribution for actions and maximize posterior

### STEP-BY-STEP SOLUTION

**(a)** "Cost function" — this is the traditional engineering approach, NOT the FEP way. FEP doesn't use external cost functions. ELIMINATE.

**(b)** "Target priors in the generative model + minimize Free Energy" — YES! In FEP, goals are encoded as preferred future states (target priors) built into your model. Then you act to minimize expected free energy, which naturally achieves those goals. ✓

**(c)** "Cost function of actions" — again, not the FEP approach. ELIMINATE.

**(d)** "Maximize posterior for actions" — this describes action selection but doesn't explain how GOALS are encoded. ELIMINATE.

**Answer: (b)** ✅

---

### EXAM QUESTION 3 (2021-Part-B, Question 5b)

> Which statements are consistent with FEP?
> - (a) An active inference agent holds a generative model for its sensory inputs
> - (b) Actions are inferred from differences between predicted and desired future observations
> - (c) Actions are inferred from differences between predicted and actual future observations
> - (d) An active inference agent focuses on explorative behavior only
>
> Options:
> - (a) (a) and (b)
> - (b) (a)
> - (c) (b) and (d)
> - (d) (c) and (d)

### STEP-BY-STEP SOLUTION

**(a) True.** Agents MUST have a generative model — that's the foundation of FEP.

**(b) True.** Actions bridge the gap between what you PREDICT and what you DESIRE (target prior). This is the essence of Active Inference.

**(c) False.** It's about "desired" future observations (target priors), not "actual" future observations. You can't know actual future observations.

**(d) False.** Agents balance exploration AND exploitation — they don't ONLY explore.

So (a) and (b) are true.

**Answer: (a) — (a) and (b)** ✅

---

### EXAM QUESTION 4 (2023, Question 4a)

> Active Inference agent:
>
> Options:
> - (a) Perception minimizes the complexity of the states
> - (b) Agent infers actions by maximizing free energy in future states
> - (c) Agent infers actions by maximizing expected accuracy in future states
> - (d) Agent infers actions by minimizing expected free energy in future states

### STEP-BY-STEP SOLUTION

**(a)** "Complexity of states" — not the core idea. Perception minimizes free energy, not "complexity." ELIMINATE.

**(b)** "Maximizing free energy" — WRONG direction. We MINIMIZE free energy. ELIMINATE.

**(c)** "Maximizing expected accuracy" — this sounds plausible but isn't the standard FEP formulation. ELIMINATE.

**(d)** "Minimizing expected free energy in future states" — YES! Actions minimize Expected Free Energy (EFE). ✓

**Answer: (d)** ✅

---

### EXAM QUESTION 5 (2022, Question 4a)

> Which statement most consistently describes FEP?
>
> Options:
> - (a) Actions aim to minimize the free energy of future states of the world
> - (b) Actions aim to minimize the complexity of future states of the world
> - (c) Intelligent decision making requires minimization of a functional of beliefs about future states
> - (d) Intelligent decision making requires minimization of a cost function of future states

### STEP-BY-STEP SOLUTION

**(a)** "Minimize free energy of future states of the world" — close, but FEP is about minimizing expected free energy of your BELIEFS, not directly of the world.

**(b)** "Minimize complexity" — not the core idea. ELIMINATE.

**(c)** "Minimization of a functional of beliefs about future states" — YES! Expected Free Energy is a functional (a function of functions) of your probability distributions (beliefs) about future states. This is the most accurate description. ✓

**(d)** "Cost function" — this is the traditional approach, not FEP. ELIMINATE.

**Answer: (c)** ✅

---

## Part 2: Tricks & Shortcuts

### TRICK 1: Always MINIMIZE, Never Maximize

FEP is about MINIMIZING free energy (or expected free energy).

If an option says "maximize free energy" → wrong.

### TRICK 2: Beliefs, Not Cost Functions

FEP uses probability distributions (beliefs), not external cost functions.

If an option mentions "cost function" → wrong (usually).

### TRICK 3: Desired, Not Actual

Actions bridge predicted vs. DESIRED future states (target priors).

If an option says "predicted vs. actual future" → wrong.

### TRICK 4: Generative Model Is Fundamental

Agents MUST have a generative model.

If a statement says agents hold a generative model → true.

---

## Part 3: Practice Exercises

### Exercise 1

> In FEP, how does an agent choose actions?
>
> Options:
> - (a) Minimize a cost function
> - (b) Minimize expected free energy in future states
> - (c) Maximize free energy in future states
> - (d) Maximize expected accuracy

---

### Exercise 2

> Which statement is consistent with FEP?
>
> Options:
> - (a) Agents hold a generative model for sensory inputs
> - (b) Actions maximize free energy
> - (c) Agents only explore
> - (d) Goals are specified as external cost functions

---

### Exercise 3

> How are goals encoded in FEP?
>
> Options:
> - (a) As a cost function to minimize
> - (b) As target priors in the generative model
> - (c) As a posterior distribution to maximize
> - (d) As constraints on actions

---

---

## Answers

<details>
<summary>Exercise 1</summary>

**Answer: (b)**

Actions minimize expected free energy, not maximize. Not cost functions.
</details>

<details>
<summary>Exercise 2</summary>

**Answer: (a)**

Generative model is fundamental to FEP.
(b) is wrong direction (minimize, not maximize).
(c) is false (balance exploration/exploitation).
(d) is wrong (target priors, not cost functions).
</details>

<details>
<summary>Exercise 3</summary>

**Answer: (b)**

Goals = target priors in the generative model. The agent then acts to make predictions match these priors.
</details>
