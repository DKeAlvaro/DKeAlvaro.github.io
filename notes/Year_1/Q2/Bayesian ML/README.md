# Bayesian ML Exam Survival Guide

> Based on past papers: 2021 Part A/B, 2021 Resit, 2022, 2023

---

## How to Use These Notes

Each file covers **one exam question type**. Every file has the same structure:

1. **Part 0** — What all the symbols mean (read this first)
2. **Part 1** — Core concepts in plain English
3. **Part 2** — Full step-by-step walkthrough of real exam questions
4. **Part 3** — Tricks & shortcuts (how to spot the right answer fast)
5. **Part 4** — Practice exercises (try these without looking at the answers)
6. **Answers** — Hidden behind `<details>` tags — click to reveal

### Recommended Study Order

Study them **in numerical order** — each builds on the previous:

| # | File | Topic | Prerequisites |
|---|------|-------|---------------|
| 1 | [01-bayes-rule-posterior](pdf/01-bayes-rule-posterior.pdf) | Bayes' Rule & Posterior Computation | None — start here |
| 2 | [02-beta-bernoulli-coin-toss](pdf/02-beta-bernoulli-coin-toss.pdf) | Beta-Bernoulli Coin Toss | Type 1 (Beta integral trick) |
| 3 | [03-gaussian-posterior-evidence](pdf/03-gaussian-posterior-evidence.pdf) | Gaussian Posterior & Evidence | Type 1 (Bayes' rule) |
| 4 | [04-model-evidence-averaging](pdf/04-model-evidence-averaging.pdf) | Model Evidence & Averaging | Types 1–3 |
| 5 | [05-model-comparison-bayes-factor](pdf/05-model-comparison-bayes-factor.pdf) | Model Comparison & Bayes Factor | Types 1, 4 |
| 6 | [06-bayesian-classifier](pdf/06-bayesian-classifier.pdf) | Bayesian Classifier | Type 1, Type 3 |
| 7 | [07-ball-box-conditional](pdf/07-ball-box-conditional.pdf) | Ball/Box Conditional Probability | Type 1 (Bayes' rule practice) |
| 8 | [08-gmm-form](pdf/08-gmm-form.pdf) | GMM Form (one-hot encoding) | None — pattern recognition |
| 9 | [09-vfe](pdf/09-vfe.pdf) | Variational Free Energy | Types 1, 4 (evidence + posteriors) |
| 10 | [10-fep](pdf/10-fep.pdf) | Free Energy Principle | None — conceptual |
| 11 | [11-factor-analysis](pdf/11-factor-analysis.pdf) | Factor Analysis & Marginal | Type 3 (Gaussian marginals) |
| 12 | [12-recursive-filtering](pdf/12-recursive-filtering.pdf) | Kalman / Recursive Filtering | Type 3 (Gaussian updates) |
| 13 | [13-log-likelihood-mle](pdf/13-log-likelihood-mle.pdf) | Log-Likelihood & MLE | Type 8 (GMM form) |
| 14 | [14-gmm-vfe-fep-concepts](pdf/14-gmm-vfe-fep-concepts.pdf) | Mixed Concepts | Types 8, 9, 10 |

### Difficulty & Surprise Factor

| # | Type | Difficulty | Surprise | Why |
|---|------|-----------|----------|-----|
| 8 | GMM Form | **10/100** | **5/100** | Pure pattern spotting. Literally same question across all exams |
| 1 | Bayes' Rule & Posterior | **15/100** | **20/100** | Fixed pipeline: multiply → normalize. Only the function changes |
| 2 | Beta-Bernoulli Coin | **20/100** | **30/100** | Count → add → formula. Watch: which outcome = 1 flips between exams |
| 3 | Gaussian Posterior | **20/100** | **25/100** | Plug numbers into 2 formulas. Different numbers, same skeleton |
| 11 | Factor Analysis | **20/100** | **20/100** | Joint and marginal are one-liners. Only W vs Λ notation changes |
| 9 | VFE | **25/100** | **20/100** | Same 3-4 questions recycled (upper bound, equality, KL). No variation |
| 5 | Bayes Factor | **25/100** | **20/100** | Evidence ratio × prior ratio. Same structure every time |
| 4 | Model Evidence | **25/100** | **25/100** | Two patterns only: Beta integral or Gaussian averaging. Predictable |
| 12 | Kalman / Filtering | **30/100** | **25/100** | 3-4 fixed questions. Formulas don't change |
| 7 | Ball/Box Conditional | **30/100** | **40/100** | Standard Bayes' rule, but two-draw/two-box variants add a wrinkle |
| 10 | FEP Concepts | **35/100** | **55/100** | No computation, but phrasing changes significantly each exam |
| 13 | Log-Likelihood & MLE | **40/100** | **35/100** | Same core questions. Inner vs outer product trap requires attention |
| 6 | Bayesian Classifier | **45/100** | **45/100** | Densities change each exam. Algebra for boundary shifts. Error limits need care |
| 14 | Mixed Concepts | **40/100** | **55/100** | True/false statements vary the most. Signal recovery appeared once, could return |

**Free points (80+ score guaranteed):** Types 8, 9, 11, 12 — pure pattern recognition.
**Where marks are lost:** Types 6, 14 — densities change, concept questions test understanding, not recognition.
**Watch for traps:** Type 2 (outcome=1 flips), Type 7 (two-draw variant differs), Type 10 (wrong answers get creatively reworded).

### Quick Reference

- [**exam-cheatsheet.md**](exam-cheatsheet.md) — All formulas in one page, organized by type
- This file (`README.md`) — Index and roadmap

### Other Files in This Folder

| File | Description |
|------|-------------|
| `crash-course.md` / `.pdf` | Course crash course |
| `2021-part-a.md` | 2021 Part A past paper |
| `2021-part-b.md` | 2021 Part B past paper |
| `2021-resit.md` | 2021 Resit past paper |
| `2022.md` | 2022 past paper |
| `2023.md` | 2023 past paper |

### Study Strategy

```
Session 1-2:  Types 1, 2, 3   → Foundation
Session 3-4:  Types 4, 5, 6   → Gaussian algebra + model comparison
Session 5-6:  Types 7, 8, 13  → Classification + GMM + MLE
Session 7-8:  Types 11, 12    → Latent variables + Kalman
Session 9:    Types 9, 10, 14 → VFE, FEP, concepts
Session 10:   Full past paper under timed conditions
```

**Per session:** Read → Cover solution → Try yourself → Check → Redo wrong ones next day.
